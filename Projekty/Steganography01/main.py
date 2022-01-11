from alive_progress import alive_bar
from moviepy import editor
from math import ceil
import numpy as np
from os import remove
import lzma
import cv2
import skvideo.io

from PIL import Image
from subprocess import Popen, PIPE
import imageio
import subprocess

class Stego_encode:

    # rotation = None
    # x_pos = 0
    # y_pos = 0
    original_video_name : str
    encoded_video_name : str
    binary_string : str
    frame_height : int
    frame_width : int
    total_frames : int
    fps : float
    video = None

    def __init__(self, video_name):
        self.original_video_name = video_name
        self.encoded_video_name = video_name.split('.')[0] + '_secret.' + video_name.split('.')[1]
        self.encrypt()
        pass


    def file_to_binary(self):
        filename = 'file.txt'

        with open(filename, 'rb') as f:
            byte_array = f.read()
        f.close()
        # print(binascii.hexlify(byte_array).decode())
        # print(bytes.hex(byte_array))
        # test = bytes.hex(content)

        #compressed_data = lzma.compress(byte_array)
        #compressed_data = byte_array.encode()

        self.binary_string = bin(int.from_bytes(byte_array, "big"))
        print(f"{self.binary_string}")
        #back = int.to_bytes(int(self.binary_string, 2), int(len(self.binary_string) / 8), "big") #na zacatku stringu musí byt 0b
        # with open("new.png", 'wb') as f:
        #     f.write(back)
        # f.close()

        # print(back.decode())

    def space_to_hide(self):
        file_extension = ".txt"
        size_of_header = 400
        space_for_data = self.frame_height * self.frame_width * 3 #number of bits in frame
        size_of_data = len(self.binary_string)+size_of_header-4 #delete 0b from strings
        needed_frames = ceil(size_of_data/space_for_data)

        header = str(needed_frames) + str(self.frame_height) + str(self.frame_width) + "3" + file_extension
        header = "{:<50}".format(header).encode()
        header_binary = bin(int.from_bytes(header, "big"))

        self.binary_string = header_binary[2:] + self.binary_string[2:] #delete 0b from strings

        return size_of_data, needed_frames #for lower size_of_data than space_for_data returns always 1

    def encode_to_frame(self):

        index = 0
        size_of_data, needed_frames = self.space_to_hide()
        image = self.video_to_frames(self.total_frames)
        print("\nEncoding Data to Video\n")

        with alive_bar(size_of_data, stats = True) as bar:
            for idx, x in np.ndenumerate(image):

                if(index < size_of_data):
                    binary_to_encode = int(self.binary_string[index])
                else:
                    break
                if image[idx] % 2 == 0:
                    if binary_to_encode == 0:
                        pass
                    else:
                        image[idx] += 1
                else:
                    if binary_to_encode == 1:
                        pass
                    else:
                        image[idx] -= 1
                bar()
                index += 1

        return image

    def load_video_parameters(self):

        self.video = cv2.VideoCapture(self.original_video_name)

        self.frame_width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.total_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = self.video.get(cv2.CAP_PROP_FPS)

        print(f"Resolution: {self.frame_width}x{self.frame_height} fps: {self.fps:.2f} Total frames: {self.total_frames}")

    def video_to_frames(self, needed_frames):

        frames = np.empty((needed_frames, self.frame_height, self.frame_width, 3), dtype='uint8')

        # p = Popen(['ffmpeg', '-y', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-r', '24', '-i', '-', '-vcodec', 'h264','-qscale', '5', '-r', '24', 'videoccc.mp4'], stdin=PIPE)
        #p = Popen(['ffmpeg', '-y', '-f', 'image2pipe', '-vcodec', 'mjpeg', '-r', '24', '-i', '-', '-vcodec', 'mpeg4','-qscale', '5', '-r', '24', 'video.mp4'], stdin=PIPE)
        # fps, duration = 24, 46

        # frames = skvideo.io.vread(self.original_video_name)
        for i in range(needed_frames):
            state, image = self.video.read() # returns ndarray to image

            frames[i] = image #4D array (frame, pixel_x, pixel_y, color_position(RGB))

        #     frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #     im = Image.fromarray(frame)
        #     im.save(p.stdin, 'JPEG')
        # p.stdin.close()
        # p.wait()

            #SHOW FRAME - testing purposes
            # cv2.imshow("IMAGE", image)
            # cv2.waitKey(None)

        return frames

    def encoded_to_video(self, frames):

        # #fourcc = cv2.VideoWriter_fourcc(*'HFYU')
        # fourcc = cv2.VideoWriter_fourcc(*'DIB ')
        # # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        # # fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # # #out = cv2.VideoWriter(self.encoded_video_name, cv2.VideoWriter_fourcc(*'DIVX'), self.fps, (self.frame_width,self.frame_height))
        # # out = cv2.VideoWriter('new_stego.mp4', fourcc, 24, (self.frame_width, self.frame_height))
        # out = cv2.VideoWriter('new_stego.avi', fourcc, 25, (self.frame_width, self.frame_height))

        writer = skvideo.io.FFmpegWriter(self.encoded_video_name, outputdict={
            '-vcodec': 'libx264',   # use the h.264 codec
            '-crf': '0',            # set the constant rate factor to 0, which is lossless
            # '-qp': '0',  # set the constant rate factor to 0, which is lossless
            '-preset': 'veryslow'   # the slower the better compression, in princple, try
                                    # other options see https://trac.ffmpeg.org/wiki/Encode/H.264
        })

	#PROBLEM TO SOLVE
	#After saving back to video few values change -> not possible to extract information
        for image in frames:
            # writing to a image array
            writer.writeFrame(image[:,:,::-1])
        #     out.write(image)
        # out.release()

        writer.close()

    def audio_splitter(self):
        print("\nMerging Audio and Video\n")
        clip = editor.VideoFileClip(self.original_video_name)
        video = editor.VideoFileClip(self.encoded_video_name)
        remove(self.encoded_video_name)
        encoded_video = video.set_audio(clip.audio) #takes audio from original video
        encoded_video.write_videofile(self.encoded_video_name)

    def encrypt(self):
        self.load_video_parameters()
        self.file_to_binary()
        frames = self.encode_to_frame()
        self.encoded_to_video(frames)
        #self.audio_splitter()


class Stego_decode(Stego_encode):

    secret_file_name : str

    def __init__(self, video_name):
        self.original_video_name = video_name
        self.secret_file_name = video_name.split('.')[0] + '_secret'
        self.decrypt()
        pass


    def extract_header(self):

        frames = np.empty((10, self.frame_height, self.frame_width, 3), dtype='uint8')

        index = 0
        counter = 0
        needed_frames = 1

        for i in range(needed_frames):
            state, image = self.video.read()  # returns ndarray to image
            frames[i] = image
            header_binary = "0b"

            for x in np.nditer(frames):
                if(counter < 400):
                    if(x % 2 == 0):
                        header_binary += "0"
                    else:
                        header_binary += "1"
                    print(x)
                else:
                    break
                counter += 1

        print(header_binary)
            # cv2.imshow("IMAGE", image)
            # cv2.waitKey(None)


    def decrypt(self):
        self.load_video_parameters()
        self.extract_header()
        pass


filename = 'original.mp4'


MySecretVideo = Stego_encode(filename)
#MyVideoToDecode = Stego_decode('video_secret.mp4')


