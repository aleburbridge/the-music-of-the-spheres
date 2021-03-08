import tkinter as tk
from tkinter import *
from pygame import *
from datetime import date
import requests
import bs4
import re
from os import path

root = Tk()
mixer.init() 
icon_path = path.relpath('images/icon.io')
root.iconbitmap(icon_path)
root.title('Music of the Spheres')
APP_ID = 'your app ID here'

todays_date = date.today()

# webscraping for planet distance using wolfram alpha api
# http://api.wolframalpha.com/v1/result?appid=YOUR-APP-ID-HERE+current+distance+from+Earth%3f

sun = requests.get(f'http://api.wolframalpha.com/v1/result?appid={APP_ID}-772K4A7THW&i=Sun+current+distance+from+Earth%3f')
mercury = requests.get(f'http://api.wolframalpha.com/v1/result?appid={APP_ID}-772K4A7THW&i=Mercury+current+distance+from+Earth%3f')
venus = requests.get(f'http://api.wolframalpha.com/v1/result?appid={APP_ID}-772K4A7THW&i=Venus+current+distance+from+Earth%3f')
mars = requests.get(f'http://api.wolframalpha.com/v1/result?appid={APP_ID}-772K4A7THW&i=Mars+current+distance+from+Earth%3f')
jupiter = requests.get(f'http://api.wolframalpha.com/v1/result?appid={APP_ID}-772K4A7THW&i=Jupiter+current+distance+from+Earth%3f')
saturn = requests.get(f'http://api.wolframalpha.com/v1/result?appid={APP_ID}-772K4A7THW&i=Saturn+current+distance+from+Earth%3f')
uranus = requests.get(f'http://api.wolframalpha.com/v1/result?appid={APP_ID}-772K4A7THW&i=Uranus+current+distance+from+Earth%3f')
neptune = requests.get(f'http://api.wolframalpha.com/v1/result?appid={APP_ID}-772K4A7THW&i=Neptune+current+distance+from+Earth%3f')

requestsList = [sun, mercury, venus, mars, jupiter, saturn, uranus, neptune]
requestsDict = {}
def getDistance(planetDistance, planet):
    planetDistance = planet.text
    planetDistance = re.sub('[about rmcl unis]','', planetDistance)
    if '.' in planetDistance:
        planetDistance = float(planetDistance)
    else:
        planetDistance = int(planetDistance)

getDistance(sunDistance, sun)
getDistance(mercuryDistance, mercury)
getDistance(venusDistance, venus)
getDistance(marsDistance, mars)
getDistance(jupiterDistance, jupiter)
getDistance(saturnDistance, saturn)
getDistance(uranusDistance, uranus)
getDistance(neptuneDistance, neptune)

# assigns dictionary for each planet then creates a sorted list from that dictionary 
distanceDict = {
    'The Sun': sunDistance,
    'Mercury': mercuryDistance,
    'Venus': venusDistance,
    'Mars': marsDistance,
    'Jupiter': jupiterDistance,
    'Saturn': saturnDistance,
    'Uranus': uranusDistance,
    'Neptune': neptuneDistance
}
sortedDistanceDict = sorted(distanceDict.items(), key=lambda x: x[1])
print(sortedDistanceDict)


#functions for playing sounds (used as commands in the button arguments)
pygame.mixer.init()
def pause_playing():
    pygame.mixer.fadeout(2000)

def play_note_1():
    pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_1_d4.wav")
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_1_d4.wav"))
    Button1.config(text=sortedDistanceDict[0][0] + ' (on)')
    label1 = Label(frame2, bg='black', fg='white', text=sortedDistanceDict[0][0] + ' is currently ' + str(sortedDistanceDict[0][1]) + ' astronomical units from Earth')
    label1.grid(row=0, column=8, sticky=tk.N)

def play_note_2():
    pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_2_e4.wav")
    pygame.mixer.Channel(2).play(pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_2_e4.wav"))
    Button2.config(text=sortedDistanceDict[1][0] + ' (on)')
    label2 = Label(frame2, bg='black', fg='white', text= sortedDistanceDict[1][0] + ' is currently ' + str(sortedDistanceDict[1][1]) + ' astronomical units from Earth')
    label2.grid(row=1, column=8, sticky=tk.N)

def play_note_3():
    pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_3_g4.wav")
    pygame.mixer.Channel(3).play(pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_3_g4.wav"))
    Button3.config(text=sortedDistanceDict[2][0] + ' (on)')
    label3 = Label(frame2, bg='black', fg='white', text= sortedDistanceDict[2][0] + ' is currently ' + str(sortedDistanceDict[2][1]) + ' astronomical units from Earth')
    label3.grid(row=2, column=8, sticky=tk.N)

def play_note_4():
    pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_4_b4.wav")
    pygame.mixer.Channel(4).play(pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_4_b4.wav"))
    Button4.config(text=sortedDistanceDict[3][0] + ' (on)')
    label4 = Label(frame2, bg='black', fg='white', text= sortedDistanceDict[3][0] + ' is currently ' + str(sortedDistanceDict[3][1]) + ' astronomical units from Earth')
    label4.grid(row=3, column=8, sticky=tk.N)

def play_note_5():
    pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_5_d4.wav")
    pygame.mixer.Channel(5).play(pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_5_d4.wav"))
    Button5.config(text=sortedDistanceDict[4][0] + ' (on)')
    label5 = Label(frame2, bg='black', fg='white', text= sortedDistanceDict[4][0] + ' is currently ' + str(sortedDistanceDict[4][1]) + ' astronomical units from Earth')
    label5.grid(row=4, column=8, sticky=tk.N)

def play_note_6():
    pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_6_a3.wav")
    pygame.mixer.Channel(6).play(pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_6_a3.wav"))
    Button6.config(text=sortedDistanceDict[5][0] + ' (on)')
    label6 = Label(frame2, bg='black', fg='white', text= sortedDistanceDict[5][0] + ' is currently ' + str(sortedDistanceDict[5][1]) + ' astronomical units from Earth')
    label6.grid(row=5, column=8, sticky=tk.N)

def play_note_7():
    pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_7_a4.wav")
    pygame.mixer.Channel(7).play(pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_7_a4.wav"))
    Button7.config(text=sortedDistanceDict[6][0] + ' (on)')
    label7 = Label(frame2, bg='black', fg='white', text= sortedDistanceDict[6][0] + ' is currently ' + str(sortedDistanceDict[6][1]) + ' astronomical units from Earth')
    label7.grid(row=6, column=8, sticky=tk.N)

def play_note_8():
    pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_8_e5.wav")
    pygame.mixer.Channel(8).play(pygame.mixer.Sound("D:\\alebu\\My-Programming-stuff\\mots\\Note_8_e5.wav"))
    Button8.config(text=sortedDistanceDict[7][0] + ' (on)')
    label8 = Label(frame2, bg='black', fg='white', text= sortedDistanceDict[7][0] + ' is currently ' + str(sortedDistanceDict[7][1]) + ' astronomical units from Earth')
    label8.grid(row=7, column=8, sticky=tk.N)

#sound channels
pygame.mixer.set_num_channels(10)
#background music

# tkinter window stuff 
# sets up window and bg image
C = Canvas(root, bg="black", height=700, width=800)
filename = PhotoImage(file = "D:\\alebu\\My-Programming-stuff\\mots\\background.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

# sets up frames
frame = tk.Frame(root, bg='black')
frame.place(relwidth=0.3, relheight=0.3, relx=0.3, rely=0.1)
frame.pack(side=tk.BOTTOM)

frame2 = tk.Frame(root, bg='black')
frame2.place(relwidth=0.9, relheight=0.3, relx=0.3, rely=0.1)

# sets up buttons
Button1 = tk.Button(frame, text=sortedDistanceDict[0][0], padx=10, pady=5, fg='black', bg='white', command=play_note_1)
Button2 = tk.Button(frame, text=sortedDistanceDict[1][0], padx=10, pady=5, fg='black', bg='white', command=play_note_2)
Button3 = tk.Button(frame, text=sortedDistanceDict[2][0], padx=10, pady=5, fg='black', bg='white', command=play_note_3)
Button4 = tk.Button(frame, text=sortedDistanceDict[3][0], padx=10, pady=5, fg='black', bg='white', command=play_note_4)
Button5 = tk.Button(frame, text=sortedDistanceDict[4][0], padx=10, pady=5, fg='black', bg='white', command=play_note_5)
Button6 = tk.Button(frame, text=sortedDistanceDict[5][0], padx=10, pady=5, fg='black', bg='white', command=play_note_6)
Button7 = tk.Button(frame, text=sortedDistanceDict[6][0], padx=10, pady=5, fg='black', bg='white', command=play_note_7)
Button8 = tk.Button(frame, text=sortedDistanceDict[7][0], padx=10, pady=5, fg='black', bg='white', command=play_note_8)
stopPlayingSound = tk.Button(frame, text='Silence', padx=10, pady=5, fg='black', bg='white', command=pause_playing)

#configures the buttons' positions 
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
frame.columnconfigure(4, weight=1)
frame.columnconfigure(5, weight=1)

frame2.columnconfigure(8, weight=2)

Button1.grid(row=0, column=0, sticky=tk.W+tk.E)
Button2.grid(row=0, column=1, sticky=tk.W+tk.E)
Button3.grid(row=0, column=2, sticky=tk.W+tk.E)
Button4.grid(row=0, column=3, sticky=tk.W+tk.E)
Button5.grid(row=0, column=4, sticky=tk.W+tk.E)
Button6.grid(row=0, column=5, sticky=tk.W+tk.E)
Button7.grid(row=0, column=6, sticky=tk.W+tk.E)
Button8.grid(row=0, column=7, sticky=tk.W+tk.E)

stopPlayingSound.grid(row=0, column=8, sticky=tk.W+tk.E)


root.mainloop()
'''
major 7th chord
Note 1: C
Note 2: E
Note 3: G
Note 4: C
Note 5: E
''' 