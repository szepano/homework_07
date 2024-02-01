from pathlib import Path
import shutil
import os
import re
import sys

'''funkcja normalize (nie rozumiem 2. podpunktu dotyczącego funkcji normalize 'Zamienia wszystkie litery, oprócz zwyczajnych znaków i cyfr, na znak '_'.')
Nie wiem czy o to chodziło, ale postanowiłem zamienić wszystkie ZNAKI oprócz liter i cyfr na '_' '''
def normalize(text):
    chr_pl = 'ĄąĆćĘęŁłŃńÓóŚśŹźŻż'
    chr_global = 'AaCcEeLlNnOoSsZzZz'
    switch = text.maketrans(chr_pl, chr_global)
    without_pl = text.translate(switch)
    final = re.sub(r'\[^a-zA-Z0-9_.]', '_', without_pl)
    return final



def sort():
    # końcówki rozszerzeń
    ext_arc = ('.zip', '.gz', '.tar')
    ext_audio = ('.mp3', '.ogg', '.wav', '.amr')
    ext_doc = ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx')
    ext_img = ('.jpeg', '.png', '.jpg', '.svg')
    ext_vid = ('.avi', '.mp4', '.mov', '.mkv')
    ext_unknown = []
    #folder rozszerzeń
    folders = ['archives', 'audio', 'documents', 'images', 'video']

    #ścieżki podancyh folderów
    p_arc = Path(sys.argv[1] + '/archives')
    p_audio = Path(sys.argv[1] + '/audio')
    p_doc = Path(sys.argv[1] + '/documents')
    p_img = Path(sys.argv[1] + '/images')
    p_vid = Path(sys.argv[1] + '/video')


    '''iterujemy po plikach/folderach w bałaganie i przenosimy,
    jeśli znajdziemy odpowiednie rozszerzenie'''
    os.chdir(Path(sys.argv[1]))

    # najpierw narmalizujemy nazwy
    for i in Path(sys.argv[1]).iterdir():
            new_name = normalize(i.name)
            old_name = i.name
            os.rename(old_name, new_name)
    
    # następnie sortujemy pliki już znormalizowane
    for i in Path(sys.argv[1]).iterdir():
        # archiva
        if i.name.endswith(ext_arc):
            shutil.unpack_archive(i, p_arc, i.name.removesuffix(ext_arc))
        #audio
        elif i.name.endswith(ext_audio):
            shutil.move(i, p_audio)
        #dokumenty
        elif i.name.endswith(ext_doc):
            shutil.move(i, p_doc)
        #obrazy
        elif i.name.endswith(ext_img):
            shutil.move(i, p_img)
        #video
        elif i.name.endswith(ext_vid):
            shutil.move(i, p_vid)
        #foldery główne
        elif i.name in folders:
            pass
        #pliki o innych rozszerzeniach
        elif i.is_file():
            new_ext = i.name.split('.') #dzielimy nazwe poprzez kropki
            ext_unknown.append('.' + new_ext[-1]) #dodajemy ostatnią część nazwy (razem z kropką) jeśli w nazwie pojawi się inna kropka
        #foldery
        elif i.is_dir():
            folder = os.listdir(i)
            if len(folder) == 0: #jeśli pusty folder
                os.rmdir(i)
            else:
                sort(i) #rekurencja
    print(ext_unknown)