from Source.parser import *
from Source.downloadyt import *

def main():

	video = vlajky()


	downloader(video.o, video.r, video.t)

	print("Úspěšně staženo")


if __name__ == '__main__':
    main()	
