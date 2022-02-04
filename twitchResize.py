import PIL.Image
import os
import sys
from tkinter import filedialog
from tkinter import *

path = filedialog.askdirectory(
    initialdir='/', title='Seleccioná la carpeta contenedora') + '/'

path = path.replace('/', '\\')

dirs = os.listdir(path)
root = Tk()
root.withdraw()
print(path)
os.chdir(path)

emote_values = [28, 56, 112]
badge_values = [18, 36, 72]


def img_resize(type_values):
    for item in dirs:
        if os.path.isfile(path+item):
            im = PIL.Image.open(path+item)
            f, e = os.path.splitext(path+item)

            for value in type_values:
                imResize = im.resize((value, value), PIL.Image.ANTIALIAS)
                imResize.save(f + f'{str(value)}.png', 'PNG', quality=100)


def main():
    print('1: Emotes')
    print('2: Badges')
    print('3: Help')
    print('4: Exit')
    option = input('')
    if option == '4':
        sys.exit()
    if option == '3':
        print('\n \nThis script resizes square images to use them as Twitch icons\n'
              'Emote and custon Points rewards icon sizes are 28x28 px, 56x56 px and 112x112 px\n'
              'Badge sizes are 18x18 px, 36x36 px and 72x72 px\n'
              'This script works with a previously selected folder path\n'
              'Place the images to be resized inside the selected folder\n'
              'Current path is ' + str(path) + '\n\n')
        main()
    elif option == '1':
        img_resize(emote_values)
    elif option == '2':
        img_resize(badge_values)
    else:
        print('Not a valid option\n\n')
        main()
    input('Done! Press ENTER to exit')
    sys.exit()


if __name__ == '__main__':
    print('twitch-resizer v1.1\n')
    print('Pick an option to continue\n')
    main()
