import os.path

import ffmpeg
import PySimpleGUI as sg
from pytube import YouTube

sg.theme('DarkAmber')

layout = [
    [sg.Text("Zadejte YouTube odkaz"), sg.InputText(key='url')],
    [sg.Radio("Video", "RADIO1", key="VID", default=True), sg.Radio("Zvuk", "RADIO1", key="AUD")],
    [sg.Text("Zadejte složku"), sg.InputText(key='path'), sg.FolderBrowse()],
    [sg.Button('Potvrdit vše')]
]

window = sg.Window("Hello Word", layout)

win2_active = False

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if values['url'] == "":
        sg.popup_error("Zadejte url!")
    elif values['path'] == "":
        sg.popup_error('Zadejte cestu!')
    elif values["VID"] and not win2_active:

        vid_url = values['url']
        path = values['path']
        try:
            yt = YouTube(vid_url)

            captions_en = ''
            captions_cs = ''

            try:
                captions_en = yt.captions.get_by_language_code('en')
            except:
                pass
            try:
                captions_cs = yt.captions.get_by_language_code('cs')
            except:
                pass

            win2_active = True
            window.hide()

        except:
            values['url'] = ""
            sg.popup_error("Zadejte url!")
            continue

        #GUI pro titulky ještě nemám vyřešené, ale vím jak na to, jde si jen o to najít čas to udělat
        if not captions_en and not captions_cs:
            layout2 = [
                [sg.Text("Zadejte rozlišení videa (720p,480p,etc)"), sg.Combo(key='RES',
                                                              values=(
                                                                  '1080p', '720p', '480p', '360p', '240p', '144p'))],
                [sg.Text("Titulky nejsou k dispozici")],
                [sg.Button('Potvrdit vše', key='BTN')]
            ]
            win2 = sg.Window('Select res and sub', layout2)

        elif not captions_cs:
            layout2 = [
                [sg.Text("Zadejte rozlišení videa"), sg.Combo(key='RES',
                                                              values=(
                                                                  '1080p', '720p', '480p', '360p', '240p', '144p'))],
                [sg.Text("Titulky: ")],
                [sg.Listbox(values=('Ne', captions_en), size=(30, 6), key='List')],
                [sg.Button('Potvrdit vše', key='BTN')]
            ]
            win2 = sg.Window('Druhe okno', layout2)
        elif not captions_en:
            layout2 = [
                [sg.Text("Zadejte rozlišení videa (720p,480p,etc)"), sg.Combo(key='RES',
                                                              values=(
                                                                  '1080p', '720p', '480p', '360p', '240p', '144p'))],
                [sg.Text("Titulky: ")],
                [sg.Listbox(values=('Ne', captions_cs), size=(30, 6), key='List')],
                [sg.Button('Potvrdit vše', key='BTN')]
            ]
            win2 = sg.Window('Druhe okno', layout2)
        else:
            layout2 = [
                [sg.Text("Zadejte rozlišení videa (720p,480p,etc)"), sg.Combo(key='RES',
                                                              values=(
                                                                  '1080p', '720p', '480p', '360p', '240p', '144p'))],
                [sg.Text("Titulky: ")],
                [sg.Listbox(values=('Ne', captions_en, captions_cs), size=(30, 6), key='List')],
                [sg.Button('Potvrdit vše', key='BTN')]
            ]
            win2 = sg.Window('Druhe okno', layout2)

        while True:
            ev2, vals2 = win2.read()
            if ev2 == sg.WIN_CLOSED:
                win2.close()
                win2_active = False
                window.UnHide()
                break
            if ev2 == 'BTN':

                res = vals2['RES']
                video = yt.streams.filter(res=res).first()

                #video = yt.streams.filter(mime_type="video/webm").filter(res=res).order_by(
                #   'resolution').desc().first()

                if video is None:
                    sg.popup_error('Zadaná kvalita není k dispozici')
                elif res == '':
                    sg.popup_error('Zadejte kvalitu!')
                else:
                    sub = ''

                    try:
                        sub = vals2['List']
                    except:
                        pass

                    try:
                        if "en" in str(sub[0]):
                            code = 'en'
                        elif "cs" in str(sub[0]):
                            code = 'cs'
                        else:
                            code = 'ne'
                    except:
                        code = 'ne'

                    #Nefungující titulky
                    ###########################################################
                    if 'ne' not in code:
                        caption = yt.captions.get_by_language_code(code)
                        caption.xml_captions
                        tit = caption.generate_srt_captions()
                        tit.download()
                    ###########################################################

                    video.download(output_path=path, filename=yt.title + ".mp4")


                    ###############################################################
                    # audio = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
                    #
                    # if not os.path.exists(os.getcwd() + "/tmp"):
                    #      os.makedirs(os.getcwd() + "/tmp")

                    # try:
                    #     print('Stahovani')
                    #     video.download(filename='video.webm')
                    #     audio.download(filename='audio.webm')
                    #
                    #     source_audio = ffmpeg.input("audio.webm")
                    #     source_video = ffmpeg.input("video.webm")
                    #
                    #     ffmpeg.concat(source_video, source_audio, v=1, a=1).output(yt.title + ".mp4").run(
                    #         cmd=os.getcwd() + "\\Source\\binaries\\ffmpeg")
                    #
                    # except:
                    #     print("Bad data")


                    ##################################################################

    elif values['AUD']:

        vid_url = values['url']
        path = values['path']

        yt = YouTube(vid_url)

        ys = yt.streams.get_audio_only()
        soubor = ys.download(path)

        base, ext = os.path.splitext(soubor)
        new_soubor = base + '.mp3'
        os.rename(soubor, new_soubor)

        print("Hotovo")

window.close()
