from pytube import YouTube
import ffmpeg
import os

def downloader(odkaz, rozliseni, titulky):

	yt = YouTube(odkaz) 	 #najde video

	print("Název: ",yt.title)			#vypíše paramtery videa
	print("Délka videa: ",yt.length)
	print("Počet shlédnutí: ",yt.views)


	try:
		if titulky == 'ano': #stahování tutulků
			caption = yt.captions.get_by_language_code('en')  #zvolení jazyka, zatím nevolitelné => vždy angličtina
			caption.xml_captions
			tit = caption.generate_srt_captions()
			tit.download()
	except:
		print("Žádné titulky  k dispozici")

	if rozliseni == 'nezadano':	#pokud uživatel nezadá rozlišení, stáhne se první nabízené video
		video_file = yt.streams.filter(mime_type="video/webm").order_by('resolution').desc().first()		
	else: 				#zvlášť se seáhne video a zvuková stopa
		video_file = yt.streams.filter(mime_type="video/webm").filter(res=rozliseni).order_by('resolution').desc().first()    
		#zvuková stopa je jen jedna pro všechan videa stejná
	audio_file = yt.streams.filter(only_audio=True).order_by('abr').desc().first()		


	if not os.path.exists(os.getcwd()+"/tmp"):  #pokud nejsou, vytvoří potřebné složky
			os.makedirs(os.getcwd()+"/tmp")

	if not os.path.exists(os.getcwd()+"/downloaded_videos"):
			os.makedirs(os.getcwd()+"/downloaded_videos")

	try: 
		print("Stahování")  #zahájí stahování videa a zvukové stopy
		video_file.download(output_path=os.getcwd()+"/tmp",filename="video")  
		audio_file.download(output_path=os.getcwd()+"/tmp",filename="audio") 		

		print(os.getcwd()+"/tmp/audio.webm")  #uloží ve formátu webm
		source_audio = ffmpeg.input(os.getcwd()+"\\tmp\\audio.webm")			
		source_video = ffmpeg.input(os.getcwd()+"\\tmp\\video.webm")

		#zpracování videa a stopy do mp4

		ffmpeg.concat(source_video, source_audio, v=1, a=1).output("downloaded_videos/"+yt.title+".mp4").run(cmd=os.getcwd()+"\\Source\\binaries\\ffmpeg")

		print("Staženo")

	except:
		print("Špatně zadaná data")

		#postupně odstraní nepotřebné složky
	if os.path.exists(os.getcwd()+"/tmp/video.webm")		
			os.remove(os.getcwd()+"/tmp/video.webm")

	if os.path.exists(os.getcwd()+"/tmp/audio.webm"):
		os.remove(os.getcwd()+"/tmp/audio.webm")

	if os.path.exists(os.getcwd()+"/tmp"):
		os.rmdir(os.getcwd()+"/tmp")
