from os.path import dirname, abspath, exists, join
from os import makedirs, remove, rmdir, rename

import os
import PySimpleGUI as sg
from pytube import YouTube
import ffmpeg

#ffmpeg-python
#kompilovany ffmpeg tools
#zmena knihovny titulku

#################################################################################################

def zmeneni_title():
    title = yt.title.replace('/', '')
    title = title.replace('\\', '')
    title = title + '.mp4'
    return title


#################################################################################################

def stazeni_titulku():
    caption = yt.captions.get_by_language_code(
        captions[sub])
    print(caption.xml_captions)
    tit = caption.generate_srt_captions()
    with open(target_path + '/titulky.srt', 'w') as f:
        f.writelines(tit)


#################################################################################################

def vytvoreni_tmp():
    script_path = dirname(abspath(__file__))
    if not exists(join(script_path, 'tmp')):
        makedirs(join(script_path, 'tmp'))
    return script_path


#################################################################################################

def videoaudio():
    #Download
    video.download(output_path=join(script_path, 'tmp'),
                   filename="video.webm")
    audio.download(output_path=join(script_path, 'tmp'),
                   filename="audio.webm")

#######################################################
    #Spojeni
    source_audio = ffmpeg.input(
        join(script_path, 'tmp', 'audio.webm'))
    source_video = ffmpeg.input(
        join(script_path, 'tmp', 'video.webm'))

    title = zmeneni_title()

    ffmpeg.concat(source_video, source_audio, v=1, a=1).output(
        join(target_path, title)).run(
        cmd=join(script_path, 'tools', 'ffmpeg'),
        overwrite_output=True)


#################################################################################################

def odstraneni_tmp():
    try:
        remove(join(script_path, 'tmp', 'audio.webm'))
        remove(join(script_path, 'tmp', 'video.webm'))
        rmdir(join(script_path, 'tmp'))
    except Exception as e:
        print(e)


#################################################################################################

def stazeni_audia():
    vid_url = values['url']
    target_path = values['path']

    yt = YouTube(vid_url)

    ys = yt.streams.get_audio_only()
    soubor = ys.download(target_path)

    base, ext = os.path.splitext(soubor)
    new_soubor = base + '.mp3'
    rename(soubor, new_soubor)


#################################################################################################

sg.theme('DarkAmber')

layout = [
    [sg.Text("Zadejte YouTube odkaz"), sg.InputText(key='url')],
    [sg.Radio("Video", "RADIO1", key="VID", default=True),
     sg.Radio("Zvuk", "RADIO1", key="AUD")],
    [sg.Text("Zadejte složku"), sg.InputText(key='path'), sg.FolderBrowse()],
    [sg.Button('Potvrdit vše')]
]

window = sg.Window("Hello Word", layout)

win2_active = False

#################################################################################################

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
        target_path = values['path']

        try:
            yt = YouTube(vid_url)
            resolutions = set(
                map(lambda x: x.resolution,
                    yt.streams.filter(mime_type="video/webm")
                    )
            )
            captions = {x.name: x.code for x in yt.captions.all()}
            captions_name = list(captions.keys())

            win2_active = True
            window.hide()

        except Exception as e:
            print(e)
            values['url'] = ""
            sg.popup_error("Zadejte url!")
            continue

        #################################################################################################

        layout2 = [
            [sg.Text("Zadejte rozlišení videa: "),
             sg.Combo(key='RES',
                      values=list(resolutions)
                      )
             ],
            [sg.Text("Titulky: ")],
            [sg.Listbox(values=['ne'] + captions_name,
                        size=(30, 6), key='List')],
            [sg.Button('Potvrdit vše', key='BTN')]
        ]
        win2 = sg.Window('Druhe okno', layout2)

        #################################################################################################

        while True:
            ev2, vals2 = win2.read()
            if ev2 == sg.WIN_CLOSED:
                win2.close()
                win2_active = False
                window.UnHide()
                break
            if ev2 == 'BTN':

                res = vals2['RES']
                try:
                    sub = vals2['List'][0]
                except:
                    sub = ''

                video = yt.streams.filter(res=res).filter(
                    mime_type="video/webm").first()
                audio = yt.streams.filter(
                    only_audio=True).order_by('abr').desc().first()

                if res == '':
                    sg.popup_error('Zadejte kvalitu!')
                elif sub == '':
                    sg.popup_error('Zadejte titulky!')
                else:

                    if sub != 'ne':
                        stazeni_titulku()

                    script_path = vytvoreni_tmp()

                    videoaudio()

                    odstraneni_tmp()

    elif values['AUD']:

        stazeni_audia()

window.close()
