import argparse
from pytube import YouTube

parser = argparse.ArgumentParser(description='Odkaz youtube videa')
parser.add_argument('-odkaz', metavar='odkaz', help='Zde zadejte odkaz')
args = parser.parse_args()

odkaz = (args.odkaz)
yt = YouTube(odkaz)  #najde video

print("Název: ",yt.title)		#vypíše paramtery videa
print("Délka videa: ",yt.length)
print("Počet shlédnutí: ",yt.views)

ys = yt.streams.get_highest_resolution() #vždy bude stahovat video v nejlepší kvalitě

print("Stahování")

ys.download()  			#zahájí stahování videa
print("Úspěšně staženo")