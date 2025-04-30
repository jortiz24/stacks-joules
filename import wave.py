import wave
from array import array
from pyaudio import *
wf = wave.open("C:/Users/jonsp/Desktop/S+J/One_-_Winged Angel (Final Fantasy VII).wav","r")
import time
import random
from qstation import *

connect('172.16.0.1')
light0_sn = 'MD1AC44200001773'
light1_sn = 'MD2AC44400002190'
light2_sn = 'MD1AC44200002979'
as_ints2 = []

data = wf.readframes(44100)



p = PyAudio()
def callback(in_data, frame_count, time_info, status):
        global as_ints2, data
        data = wf.readframes(frame_count)
        as_ints2 = array('h',data)
        # If len(data) is less than requested frame_count, PyAudio automatically
        # assumes the stream is finished, and the stream stops.
        return (data,paContinue)

#vals = {x*1000:[] for x in range(1,31)}

"""
as_ints = array('h',data)
print(len(as_ints))
total = 0
for x in as_ints:
      vals[abs(x//1000*1000)+1000].append(x)
      
      """

#print((as_ints[:331]))
color = []
color.append((256*random.random()//1,256*random.random()//1,256*random.random()//1))

stream = p.open(format =p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback,
                start=True)


#data = stream.read(2048)
time.sleep(2.5)
#color = random.random()



while stream.is_active():
    end = abs(as_ints2[-1])
    first = abs(as_ints2[1])
    spike = end-first
    #print(stream.get_time())
    currentlight = "1"
    lastlight = ""
    
        
        
     

    if 12000 > spike > 5000:
        lastlight = currentlight
        currentlight = "2"
        if lastlight != currentlight:
            color = []
            color.append((256*random.random()*(spike-5000)//7000//1,256*random.random()*(spike-5000)//7000//1,256*random.random()*(spike-5000)//7000//1))
        colors2 = tuple(map(lambda x: x*((spike-5000)/7000)//1,color[-1]))
        
        #print(colors2)
        #print(currentlight,colors1)
        set_color(colors2,light0_sn,0.05)
        """(abs(end)%256*spike//6250,abs(end)%256*spike//(6250),abs(end)%256*spike//6250)"""

        #print(currentlight+"\n"+ str(abs(as_ints2[-1]) - abs(as_ints2[1])) +"\nx")

    if 5000 > spike > 900:
        lastlight = currentlight
        currentlight = "1"
        if lastlight != currentlight:
            color = []
            color.append((spike*random.random()%256,spike*random.random()%256,spike*random.random()%256))

        colors1 = tuple(map(lambda x: x*((spike-900)/4100)//1,color[-1])) 

        #print(color,lastlight,currentlight,spike)

        set_color(colors1,light1_sn,0.05)
        """(abs(end)%256*spike//3750,abs(end)%256*spike//(3750),abs(end)%256*spike//3750)"""
        #print(currentlight+"\n",colors2,"\nx")

    if  spike > 12000:
        lastlight = currentlight
        currentlight="3"
        if lastlight != currentlight:
            color = []
            color.append((256*random.random()//1,256*random.random()//1,256*random.random()//1))

        colors3 = color[-1]
        #print(color[-1])

        set_color(colors3,light2_sn,0.05)
    
        """(abs(end)//29999*256,abs(end)//29999*256,abs(end)//29999*256)
        """
        """colors1 = (abs(as_ints[-1])%256,abs(as_ints[-1])%256,abs(as_ints[-1])%256)
        colors3 = (abs(as_ints[-1])%256,abs(as_ints[-1])%256,abs(as_ints[-1])%256)
        print(abs(as_ints2[-1])%256,abs(as_ints2[-1])%256,abs(as_ints2[-1])%256)"""
    #print(color[-1],currentlight)
    #print(as_ints2[:1248])
    
                 
          
    #time.sleep(1)
stream.close()