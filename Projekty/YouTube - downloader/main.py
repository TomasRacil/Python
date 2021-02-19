from Source.parser import *
from Source.downloadyt import *

def main():

	video = vlajky()

<<<<<<< HEAD

	downloader(video.o, video.r, video.t)

	print("Úspěšně staženo")


if __name__ == '__main__':
    main()	
=======
	try:
		downloader(video.o, video.r, video.t)
	except:
		print("Stahování selhalo")


if __name__ == '__main__':
    main()
>>>>>>> 580955f5df2223cb1f7e8204e5b77bfd6b71739a
