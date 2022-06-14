import ffmpeg
import numpy as np
import hashlib
from os import environ, path, getenv

ffmpeg_path=path.join(path.dirname(path.realpath(__file__)),'ffmpeg.exe')
ffprobe_path=path.join(path.dirname(path.realpath(__file__)),'ffprobe.exe')

#original = path.join(path.dirname(path.realpath(__file__)),'original.mp4')
original_avi=path.join(path.dirname(path.realpath(__file__)),'original.mkv')
copy_avi = path.join(path.dirname(path.realpath(__file__)),'original_copy.avi')

#change video file to avi
3#ffmpeg.input(original).output(original_avi, qscale=0, loglevel="quiet").overwrite_output().run(cmd=ffmpeg_path)

# Get video dimensions and framerate
probe = ffmpeg.probe(original_avi, cmd=ffprobe_path)
video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
width = int(video_stream['width'])
height = int(video_stream['height'])
frame_rate = video_stream['avg_frame_rate']

# Read video into buffer
out, error = (
    ffmpeg
        .input(original_avi, threads=120)
        .output("pipe:", format='rawvideo', pix_fmt='bgr24')  # Select bgr24 instead of rgb24 (becasue raw AVI requires bgr24).
        .run(capture_stdout=True, cmd=ffmpeg_path)
)

# Convert video buffer to array
video = (
    np
        .frombuffer(out, np.uint8)
        .reshape([-1, height, width, 3])
)

# Convert array to buffer
video_buffer = (
    np.ndarray
        .flatten(video)
        .tobytes()
)

# Write buffer back into a video
process = (
    ffmpeg
        .input('pipe:', format='rawvideo', s='{}x{}'.format(width, height), pixel_format='bgr24', r=frame_rate)  # Set input pixel format.
        .output(copy_avi, vcodec='rawvideo')  # Select video code "rawvideo"
        .overwrite_output()
        .run_async(pipe_stdin=True, cmd=ffmpeg_path)
)
# if not isinstance(video, np.ndarray):
#         images = np.asarray(video)
# for frame in video:
#         process.stdin.write(
#             frame
#                 .astype(np.uint8)
#                 .tobytes()
#         )

process.communicate(input=video_buffer)

# Read the newly written video
out_2, error = (
    ffmpeg
        .input(copy_avi, threads=40)
        .output("pipe:", format='rawvideo', pix_fmt='bgr24')
        .run(capture_stdout=True, cmd=ffmpeg_path)
)

# Convert new video into array
video_2 = (
    np
        .frombuffer(out_2, np.uint8)
        .reshape([-1, height, width, 3])
)

# Video dimesions change
print(f'{video.shape} vs {video_2.shape}') # (844, 1080, 608, 3) vs (844, 1080, 608, 3)
print(f'{np.array_equal(video, video_2)}') # True

# Hashes do match
print(hashlib.sha256(bytes(video_2)).digest())
print(hashlib.sha256(bytes(video)).digest())