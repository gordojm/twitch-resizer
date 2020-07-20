# badges 18 x 18 pixels, 36 x 36 pixels, and 72 x 72 pixels
# emotes 28 x 28 pixels, 56 x 56 pixels, and 112 x 112 pixels
# A:\\Desktop\\emotes\\

from PIL import Image
import os
import sys

path = ('C:\\Users\\Juan\\Desktop\\emote_test\\')
dirs = os.listdir(path)

emote_big = (112, 112)
emote_medium = (56, 56)
emote_small = (28, 28)

badge_big = (72, 72)
badge_medium = (36, 36)
badge_small = (18, 18)


'''
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((200, 200), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)
'''

##### EMOTES #####


def emote_resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)

            imResize = im.resize(emote_big, Image.ANTIALIAS)
            imResize.save(f + '112.png', 'PNG', quality=100)

            imResize = im.resize(emote_medium, Image.ANTIALIAS)
            imResize.save(f + '56.png', 'PNG', quality=100)

            imResize = im.resize(emote_small, Image.ANTIALIAS)
            imResize.save(f + '28.png', 'PNG', quality=100)


def badge_resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)

            imResize = im.resize(badge_big, Image.ANTIALIAS)
            imResize.save(f + '72.png', 'PNG', quality=100)

            imResize = im.resize(badge_medium, Image.ANTIALIAS)
            imResize.save(f + '36.png', 'PNG', quality=100)

            imResize = im.resize(badge_small, Image.ANTIALIAS)
            imResize.save(f + '18.png', 'PNG', quality=100)


def main():
    print('1: Emotes')
    print('2: Badges')
    print('3: Ayudame no entiendo')
    opcion = input('Modo elegido: ')
    if opcion == '3':
        print('\n \nEste programa cambia el tamaño de imágenes de lienzo cuadrado para usarlas en Twitch')
        print('Los tamaños de emotes son 28 x 28 pixels, 56 x 56 pixels y 112 x 112 pixels')
        print('Los tamaños de badges son 18 x 18 pixels, 36 x 36 pixels y 72 x 72 pixels')
        print('El programa funciona con una ruta predeterminada')
        print('Hay que poner las imágenes en la carpeta determinada en la ruta y el proceso se realizará automáticamente')
        print('La ruta actual es ' + str(path) + '\n\n')
        main()
    elif opcion == '1':
        emote_resize()
    elif opcion == '2':
        badge_resize()
    else:
        print('No es muy complicado papu, hay 3 opciones nomas\n\n')
        main()
    input('Finalizado! Apretá ENTER para salir')
    sys.exit()


print('Bienvenido/a al retamañador mágico para cosas de Twitch v1.0')
print('Elegí el modo para continuar \n')
main()
