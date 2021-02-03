from pytube import YouTube

def downloader(odkaz, rozliseni, titulky):

	yt = YouTube(odkaz) 	 #najde video

	print("Název: ",yt.title)			#vypíše paramtery videa
	print("Délka videa: ",yt.length)
	print("Počet shlédnutí: ",yt.views)

	if rozliseni == 'nezadano':					#pokud uživatel nezadá rozlišení, stáhne se video v nejlepší kvalitě
		ys = yt.streams.get_highest_resolution()
	else:
		ys = yt.streams.filter(res=rozliseni)


	try:
		if titulky == 'ano':
			caption = yt.captions.get_by_language_code('en')
			caption.xml_captions
			tit = caption.generate_srt_captions()
			tit.download()
	except:
		print("Žádné titulky  k dispozici")

	try: 
		ys.download()     #zahájí stahování videa
		print("Stahování")
	except:
		print("Špatně zadaná data")