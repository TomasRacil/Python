from Source.parser import *
from Source.downloadyt import *
import argparse
from pytube import YouTube

def main():

	

	video = vlajky()


	downloader(video.odkaz, video.rozliseni, video.titulky)

	print("Úspěšně staženo")


if __name__ == '__main__':
    main()	
