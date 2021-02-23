from pytube import YouTube
import ffmpeg
import os

def downloader(odkaz, rozliseni, titulky):
	"""
	Funkce která najde pomocí odkazu youtube video a následně dle dalších poždavků stáhne a upraví:
	
	1) Najde video
	2) Stáhne titulky
	3) Zvlášť se stáhne video a zvuková stopa
	4) Pokud nejsou, vytvoří se potřebné složky pro manipulaci a uložení
	5) Zahájí se stahování videa a stopy
	6) Uloží se ve formátu "webm"
	7) Zpracuje video a zvuk do formátu "mp4"
	8) Odstraní složky pro manipulaci
	
	Následně bude ve složce "downloaded_videos" stažené video v požadované kvalitě	
	"""

	yt = YouTube(odkaz) 	 		# 1)

	print("Název: ",yt.title)			
	print("Délka videa: ",yt.length)
	print("Počet shlédnutí: ",yt.views)


	try:
		if titulky == 'ano': 					# 2) 
			caption = yt.captions.get_by_language_code('en') 
			caption.xml_captions
			tit = caption.generate_srt_captions()
			tit.download()
	except:
		print("Žádné titulky  k dispozici")

	if rozliseni == 'nezadano':  						# 3) 
		video_file = yt.streams.filter(mime_type="video/webm").order_by('resolution').desc().first()		
	else: 		
		video_file = yt.streams.filter(mime_type="video/webm").filter(res=rozliseni).order_by('resolution').desc().first()    
	audio_file = yt.streams.filter(only_audio=True).order_by('abr').desc().first()		


	if not os.path.exists(os.getcwd()+"/tmp"):                  # 4)
			os.makedirs(os.getcwd()+"/tmp")

	if not os.path.exists(os.getcwd()+"/downloaded_videos"):
			os.makedirs(os.getcwd()+"/downloaded_videos")

	try: 
		print("Stahování")  						# 5)
		video_file.download(output_path=os.getcwd()+"/tmp",filename="video")  
		audio_file.download(output_path=os.getcwd()+"/tmp",filename="audio") 		

		print(os.getcwd()+"/tmp/audio.webm")  				#6)
		source_audio = ffmpeg.input(os.getcwd()+"\\tmp\\audio.webm")			
		source_video = ffmpeg.input(os.getcwd()+"\\tmp\\video.webm")

		
							# 7)
		ffmpeg.concat(source_video, source_audio, v=1, a=1).output("downloaded_videos/"+yt.title+".mp4").run(cmd=os.getcwd()+"\\Source\\binaries\\ffmpeg")

		print("Staženo")

	except:
		print("Špatně zadaná data")

		#8) postupně odstraní nepotřebné složky
	if os.path.exists(os.getcwd()+"/tmp/video.webm")		
			os.remove(os.getcwd()+"/tmp/video.webm")

	if os.path.exists(os.getcwd()+"/tmp/audio.webm"):
		os.remove(os.getcwd()+"/tmp/audio.webm")

	if os.path.exists(os.getcwd()+"/tmp"):
		os.rmdir(os.getcwd()+"/tmp")
