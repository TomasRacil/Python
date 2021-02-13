from Source.parser import *
from Source.downloadyt import *

def main():

	video = vlajky()

	try:
		downloader(video.o, video.r, video.t)
	except:
		print("Stahování selhalo")


if __name__ == '__main__':
    main()