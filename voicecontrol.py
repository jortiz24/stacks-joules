# This is made for Mi Gente  (song file is provided)
# The lightshow fits first 60 seconds of the song
# This requires a microphone
# do 'pip install pygame' in Command Prompt or Terminal or PowerShell 
# (If you use Mac, and have problem installing pygame, please refer: http://www.pygame.org/wiki/GettingStarted#Mac installation )
# then run this code (no need to install pygame again if pygame is already installed)
# clap once to start the lightshow

import time
from array import array
from time import time
from random import *

import pyaudio
from pygame import mixer

from qstation import *

connect('172.16.0.1')
light0_sn = 'MD1AC44200001773'
light1_sn = 'MD2AC44400002190'
light2_sn = 'MD1AC44200002979'
set_group(light0_sn,1)
set_group(light1_sn,1)
set_group(light2_sn,1)
def start():
    ''' start the lightshow'''

    global endShow
    stream2 = p.open(format=FORMAT,
                channels=CHANNELS, 
                rate=RATE, 
                input=True,
                frames_per_buffer=CHUNK)



    turn_off(light0_sn)
    sleep(0.2)
    turn_off(light1_sn) 
    sleep(0.2)
    turn_off(light2_sn)
    sleep(0.7)

    
    mixer.init()
    mixer.music.load('One_-_Winged Angel (Final Fantasy VII).wav')
    mixer.music.play()

    print(mixer.find_channel(force=True))
    print(mixer.get_num_channels())
    # array that has tuples in the form of (timeCode, sn, color)
    info_array = [(0.1, light0_sn, (0, 0, 0)),                  

                  #la la la la la
    (1.1, light0_sn, (0, 0, 0)),
                  (1.2, light0_sn, (2, 20, 255)),
                  (2.2, light1_sn, (2, 20, 255)),
                  (3.3, light2_sn, (2, 20, 255)),
                  (4.3, light0_sn, (0, 0, 0)),
                  (4.4, light1_sn, (0, 0, 0)),
                  (4.5, light2_sn, (0, 0, 0)),

                  #after freeze 1
                  (5.8, light0_sn, (255, 12, 34)),
                  (6.8, light1_sn, (255, 12, 34)),
                  (7.9, light2_sn, (255, 12, 34)),
                  (8.7, light0_sn, (0, 0, 0)),
                  (8.8, light1_sn, (0, 0, 0)),
                  (8.9, light2_sn, (0, 0, 0)),

                  #after freeze 2
                  (10.5, light0_sn, (85, 107, 13)),
                  (11.5, light1_sn, (85, 107, 13)),
                  (12.5, light2_sn, (85, 107, 13)),
                  (13.5, light0_sn, (0, 0, 0)),
                  (13.6, light1_sn, (0, 0, 0)),
                  (13.7, light2_sn, (0, 0, 0)),

                  #after freeze 3
                  (14.9, light0_sn, (22, 100, 0)),
                  (16, light1_sn, (22, 100, 0)),
                  (17.1, light2_sn, (22, 100, 0)),
                  (18.2, light0_sn, (0, 0, 0)),
                  (18.3, light1_sn, (0, 0, 0)),
                  (18.4, light2_sn, (0, 0, 0)),

                  #y donde de estan mi gente
                  (19.4, light0_sn, (255, 128, 0)),
                  (19.9, light1_sn, (255, 128, 0)),
                  (20.4, light2_sn, (255, 128, 0)),
                  (20.9, light2_sn, (128, 0, 0)),
                  (20.95, light1_sn, (128, 0, 0)),
                  (21, light0_sn, (128, 0, 0)),

                  (21.6, light0_sn, (200, 250, 80)),
                  (22.1, light1_sn, (200, 250, 80)),
                  (22.6, light2_sn, (200, 250, 80)),
                  (23.2, light2_sn, (0, 0, 180)),
                  (23.3, light1_sn, (0, 0, 180)),
                  (23.4, light0_sn, (0, 0, 180)),

                  (24, light0_sn, (165, 42, 42)),
                  (24.6, light1_sn, (165, 42, 42)),
                  (25.2, light2_sn, (165, 42, 42)),
                  (25.8, light0_sn, (0, 0, 0)),
                  (25.9, light1_sn, (0, 0, 0)),
                  (26.0, light2_sn, (0, 0, 0)),

                  #1,2,3,4
                  (26.5, light0_sn, (255, 0, 0)),
                  (27.1, light1_sn, (0, 255, 0)),
                  (27.7, light2_sn, (0, 0, 255)),
                  (28.2, light0_sn, (200, 200, 0)),
                  (28.3, light1_sn, (200, 200, 0)),
                  (28.4, light2_sn, (200, 200, 0)),

                  #crazy part
                  (29, light0_sn, (0, 102, 255)),
                  (29.6, light1_sn, (103, 0, 255)),
                  (30.1, light2_sn, (10, 127, 255)),
                  (30.6, light0_sn, (0, 0, 0)),
                  (30.7, light1_sn, (0, 0, 0)),
                  (30.8, light2_sn, (0, 0, 0)),

                  (31.3, light0_sn, (165, 42, 42)),
                  (31.9, light1_sn, (165, 42, 42)),
                  (32.5, light2_sn, (165, 42, 42)),
                  (33.1, light0_sn, (0, 0, 0)),
                  (33.2, light1_sn, (0, 0, 0)),
                  (33.3, light2_sn, (0, 0, 0)),

                  (33.9, light0_sn, (0, 255, 0)),
                  (34.5, light1_sn, (0, 255, 0)),
                  (35.1, light2_sn, (0, 255, 0)),
                  (120.2, light0_sn, (0, 0, 0)),
                  (180.3, light1_sn, (0, 0, 0)),
                    (200.4, light2_sn, (0, 0, 0))]

                  

    length = len(info_array)
    next_color = (0, 0, 0)
    next_light = light0_sn
    next_time_code = 0.0
    start_time = time()
    next_index = 1
    sleep(0.6)

    # loop to find a match between the timecode and the current time
    # set the color accordingly
    while next_index < length:
        as_ints = array('h',stream.read(CHUNK))
        print(as_ints[-1])
        current_time = time() - start_time
        if current_time >= next_time_code:
            
            next_change = info_array[next_index]
            next_time_code = next_change[0]
            #next_light = next_change[1]
            #next_color = next_change[2]
            next_index = next_index + 1
        if as_ints[-1] > 200:
            
            colors1 = tuple(map(lambda x: x*(as_ints[-1]/2000)//1, (abs(as_ints[-1])%256*random(),abs(as_ints[-1])%256*random(),abs(as_ints[-1])%256*random())))
            colors2 = tuple(map(lambda x: x*(as_ints[-1]/2000)//1, (abs(as_ints[-1])%256*random(),abs(as_ints[-1])%256*random(),abs(as_ints[-1])%256*random())))
            colors3 = tuple(map(lambda x: x*(as_ints[-1]/2000)//1, (abs(as_ints[-1])%256*random(),abs(as_ints[-1])%256*random(),abs(as_ints[-1])%256*random())))

        
            set_color(colors1, light0_sn,0.001)
            set_color(colors2, light1_sn,0.001)
            set_color(((colors1[0]+colors2[0])%256,(colors1[0]+colors2[0])%256,(colors1[0]+colors2[0])%256), light2_sn,0.001)
        
    sleep(0.7)

    # turn off the lights
    turn_off(light1_sn)
    sleep(0.2)
    turn_off(light0_sn)
    sleep(0.2)
    turn_off(light2_sn)
    mixer.music.stop()
    global endShow
    endShow = True

# the following code is taken from https://github.com/nikhiljohn10/pi-clap
# with some small modifications


# main

# global variable
global endShow
endShow = False

CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
threshold = 1000
max_value = 0
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS, 
                rate=RATE, 
                input=True,
                frames_per_buffer=CHUNK)




print("Clap detection initialized")
while not endShow:
    data = stream.read(CHUNK)
    
    as_ints = array('h', data)
    max_value = max(as_ints)
    

    if max_value > threshold:
        print("Clapped")
        start()

stream.stop_stream()
stream.close()
p.terminate()
