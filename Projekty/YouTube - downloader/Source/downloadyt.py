from pytube import YouTube

def downloader(odkaz, rozliseni, titulky):

	yt = YouTube(odkaz) 	 #najde video

	print("Název: ",yt.title)			#vypíše paramtery videa
	print("Délka videa: ",yt.length)
	print("Počet shlédnutí: ",yt.views)


	try:
		if titulky == 'ano':
			caption = yt.captions.get_by_language_code('en')
			caption.xml_captions
			tit = caption.generate_srt_captions()
			tit.download()
	except:
		print("Žádné titulky  k dispozici")

	if rozliseni == 'nezadano':													#pokud uživatel nezadá rozlišení, stáhne se video v nejlepší kvalitě
		video_file = yt.streams.order_by('resolution').desc().first()		
	else:
		video_file = yt.streams.order_by('resolution').desc().filter(res=rozliseni)

	audio_file = yt.streams.filter(only_audio=True).order_by('abr').desc().first()		

	try: 
		print("Stahování")
		video_file.download()    						 	#zahájí stahování videa a zvukobé stopy
		audio_file.download(filename_prefix="audio_") 		


		source_audio = ffmpeg.input(audio_file)			#zpracování videa a stopy
		source_video = ffmpeg.input(video_file)

		ffmpeg.concat(source_video, source_audio, v=1, a=1).output("Stažené_video.mp4").run()
		print("Staženo")
	except:
		print("Špatně zadaná data")