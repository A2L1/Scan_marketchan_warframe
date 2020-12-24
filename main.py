import os
import pytesseract
import yaml
from PIL import ImageGrab
from PIL import Image


os.remove('d:/Travail/Programation/Lecteur_marché/screen.png')
screen=ImageGrab.grab(bbox = (0, 860, 450, 1050))
screen.save("d:/Travail/Programation/Lecteur_marché/screen.png","png")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string(Image.open('D:/Travail/Programation/Lecteur_marché/screen.png')))
liste_image  = pytesseract.image_to_string(Image.open('D:/Travail/Programation/Lecteur_marché/screen.png')).split()
ajout = ''
chat = []
first = True

with open('image.txt','w') as file:
    file.write(pytesseract.image_to_string(Image.open('D:/Travail/Programation/Lecteur_marché/screen.png')))

liste_message = []
with open('image.txt','r') as stream:
    for ligne in stream:
        if ligne[0].isalpha() or ligne[0].isalnum():
            if ':' in ligne.split()[0] and len(ligne.split()) > 1:
                if not first:
                    chat.append(" ".join(liste_message))
                liste_message = ligne.replace('\n', ' ').split()
                first = False
            elif not first:
                liste_message.append(ligne.replace('\n', ' '))
                first = False
    chat.append(" ".join(liste_message))

with open('image.txt','w') as file:
    for annonce in chat:
        if chat.index(annonce) == len(chat)-1:
            point = ''
        else:point = '\n'
        file.write(f'{annonce}{point}')

with open('image.txt','r') as file:
    for ligne in file:
        item = []
        ligne = ajout[:] + ligne
        #print (f'ligne: {ligne}')
        if (('[' in ligne and ']' in ligne) or (ligne.find(']') > ligne.find('['))):
            liste= ligne.split()
            if ':' in liste[0]:
                name = liste[0]
            nb_o = ligne.count('[')
            nb_c = ligne.count(']')
            for i in range (nb_o + 1):
                pos_c = ligne.find(']')
                if pos_c != -1:
                    item.append(ligne[ligne.find('[') + 1:ligne.find(']')])
                    ligne = ligne[pos_c + 1:]
        print (f'{name}{item}')