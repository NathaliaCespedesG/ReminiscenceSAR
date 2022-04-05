#!/usr/bin/python2.7
'''
#--- Steve Cox --- 1/10/19
# Copyright (c) Stef van der Struijk
# License: GNU Lesser General Public License
# Modified code to play sound from buffer recording
# Added code to wait till sound is finished play so no echo occurs
# Modification of:
# https://github.com/wiseman/py-webrtcvad (MIT Copyright (c) 2016 John Wiseman)
# https://github.com/wangshub/python-vad (MIT Copyright (c) 2017 wangshub)
Requirements:
+ pyaudio - `pip install pyaudio`
+ py-webrtcvad - `pip install webrtcvad`
'''
import webrtcvad
import collections
import sys
import signal
import pyaudio
import threading
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


from array import array
from struct import pack
import wave
import time



#------ Steve Cox

#-------------------------- 


class Sound_Detection(object):


    def __init__(self, Datahandler = None):


        self.filename = "Voice_record.wav"
        self.vad_excel = "Voice_activity.cvs"
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 48000
        self.CHUNK_DURATION_MS = 30       # supports 10, 20 and 30 (ms)
        self.PADDING_DURATION_MS = 1500   # 1 sec jugement
        self.CHUNK_SIZE = int(self.RATE * self.CHUNK_DURATION_MS / 1000)  # chunk to read
        self.CHUNK_BYTES = self.CHUNK_SIZE * 2  # 16bit = 2 bytes, PCM
        self.NUM_PADDING_CHUNKS = int(self.PADDING_DURATION_MS / self.CHUNK_DURATION_MS)

        #--- Steve Cox
        self.NUM_WINDOW_CHUNKS = int(240 / self.CHUNK_DURATION_MS)
        self.NUM_WINDOW_CHUNKS = int(400 / self.CHUNK_DURATION_MS)  # 400 ms/ 30ms  ge

        self.NUM_WINDOW_CHUNKS_END = self.NUM_WINDOW_CHUNKS * 2
        self.START_OFFSET = int(self.NUM_WINDOW_CHUNKS * self.CHUNK_DURATION_MS * 0.5 * self.RATE)

        self.vad = webrtcvad.Vad(2)
        self.freq = 48000


        #raw data variable
        self.data = []
        #array to detect silence and no silence
        self.voice_activity = []
        self.chunk = []
        self.active = None


        self.pa = pyaudio.PyAudio()
        self.streaming_objects()


        self.got_a_sentence = False


    def streaming_objects(self):

        self.stream = self.pa.open(format=self.FORMAT,
                 channels=self.CHANNELS,
                 rate=self.RATE,
                 input=True,
                 start=False,
                 # input_device_index=2,
                 frames_per_buffer=self.CHUNK_SIZE)

    def normalize(snd_data):
        "Average the volume out"
        MAXIMUM = 32767  # 16384
        times = float(MAXIMUM) / max(abs(i) for i in snd_data)
        r = array('h')
        for i in snd_data:
            r.append(int(i * times))
        return r

    def process(self):

        while self.go_on:

            ring_buffer = collections.deque(maxlen = self.NUM_PADDING_CHUNKS)
            triggered = False
            voiced_frames = []
            ring_buffer_flags = [0] * self.NUM_WINDOW_CHUNKS
            ring_buffer_index = 0

            ring_buffer_flags_end = [0] * self.NUM_WINDOW_CHUNKS_END
            ring_buffer_index_end = 0
            buffer_in = ''
            # WangS
            self.raw_data = array('h')
            index = 0
            start_point = 0
            StartTime = time.time()
            #rint("* recording: ")
            self.stream.start_stream()

            while not self.got_a_sentence:

                self.chunk = self.stream.read(self.CHUNK_SIZE)
                # add WangS
                self.data.append(self.chunk)
                self.raw_data.extend(array('h', self.chunk))
                index += self.CHUNK_SIZE
                TimeUse = time.time() - StartTime

                self.active = self.vad.is_speech(self.chunk, self.RATE)

                #sys.stdout.write('1' if self.active else '_')

                ring_buffer_flags_end[ring_buffer_index_end] = 1 if self.active else 0
                ring_buffer_index_end += 1
                ring_buffer_index_end %= self.NUM_WINDOW_CHUNKS_END

                #print(triggered)

                if not triggered:
                    #print('Aqui')
                    ring_buffer.append(self.chunk)
                    self.num_voiced = sum(ring_buffer_flags)
                    if self.num_voiced > 0.8 * self.NUM_WINDOW_CHUNKS:
                        #print('Aqui2')
                        triggered = True
                        start_point = index - self.CHUNK_SIZE * 20  # start point
                        ring_buffer.clear()
                    # end point detection

                else:
                    #print('Aqui3')
                    ring_buffer.append(self.chunk)
                    self.num_unvoiced = self.NUM_WINDOW_CHUNKS_END - sum(ring_buffer_flags_end)

                    if self.num_unvoiced > 0.90 * self.NUM_WINDOW_CHUNKS_END or TimeUse > 10:
                        #print('Aqui4')
                        triggered = False
                        self.got_a_sentence = True

    def start(self):

        self.go_on = True

    def pause(self):

        self.go_on = False

    def close(self):

        print("Finishing recording")
        self.stream.stop_stream()
        print('Hereeeee 1111')
        self.stream.close()

        print('Hereeeee2222')

        #time.sleep(5)

        #self.pa.terminate()
        print('Hereeeee3333')

    def write_audio(self,path):

        print('Writing Audio')

        self.wf = wave.open(path +'/'+ self.filename, "wb")
        # set the channels
        self.wf.setnchannels(self.CHANNELS)
        # set the sample format
        self.wf.setsampwidth(self.pa.get_sample_size(self.FORMAT))
        # set the sample rate
        self.wf.setframerate(self.freq)
        # write the frames as bytes
        self.wf.writeframes(b"".join(self.data))
        # close the file
        self.wf.close()

        #self.voice_acd = np.array(self.active)
        #pd.DataFrame(self.voice_acd).to_csv(path + '/'+ self.vad_excel)

    def getData(self):

        return(self.active)

    def getVoice(self):

        return(self.chunk)

    def launch_thread(self):

        self.t = threading.Thread(target = self.process)
        self.t.start()


'''
def main():

    sound = Sound_Detection()
    sound.start()
    sound.launch_thread()

    
    time.sleep(2)
    for x in range(100):

        voice = sound.getVoice()
        data = sound.getData()
        plt.scatter(x,data)
        #plt.scatter(x, voice)
        plt.pause(0.05)
        #print(data)
        time.sleep(0.05)

    #print(sound.frames)
    plt.show
    sound.pause()
    sound.close()
    print('Ending')
    sound.write_audio(path = 'C:/Users/Nathalia Cespedes/Desktop/Reminiscence_Interface_Robot/Interface_Plugins/Lower_layer/Speech_Understanding')


A = main()

'''

