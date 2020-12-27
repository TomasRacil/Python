from pytube import YouTube

odkaz = input("Zadejte link z youtube:  ")
yt = YouTube(odkaz)


print("Název: ",yt.title)
print("Délka videa: ",yt.length)

ys = yt.streams.get_highest_resolution()


print("Stahování")
ys.download()
print("Úspěšně staženo")