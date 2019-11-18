#Importing the modules to interact with the operating system
import sys
import os
import signal
#Making sure the user has the correct version of Python installed
if sys.version_info[0] < 3:
    raise Exception('Python 3 or a more recent version is required.')

#Getting the module(Only works with Python3+)
import youtube_dl

#Declaring global variable to define the location of home
home = os.path.expanduser('~')

#Format and download destination just as specifying only title and extension to appear in name
y = {
    'format':'bestvideo+bestaudio/bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
    }],
    'outtmpl': os.path.join(home, 'Videos', '%(title)s.%(ext)s'),
    }

#Initiating infinite loop
while True:
#Define file path
    def f():
        d = os.path.join(home, 'Videos')
        return d

#Specifying where the video will be saved
    print('Hello! Your video will be saved inside: {}'.format(f()))

#Getting the link from users input and downloading
    l = input('\nPaste the URL of the YouTube video you want to download and press enter: \n')
    youtube_dl.YoutubeDL(y).download([l])

#Asking for action from user to continue or leave the app and act accordingly or continue if the user is afk anyways. Printing destination folder again idea from Oscar Herrera.
    print('\nYour video was saved inside: {}'.format(f()))
    f = input('\nVideo downloaded successfully. Well done! \n\nPress Y to continue or N to exit. Then press enter:\n')
    if f == 'N' or f == 'n':
        print('\nThanks, come back soon!')
        os.kill(os.getppid(), signal.SIGHUP)
    elif f == 'Y' or f == 'y':
        print('\nYou\'re amazing! The script will start again...')
        continue
    else:
        print('\nYou\'re distracted! The script started again...')
        continue
