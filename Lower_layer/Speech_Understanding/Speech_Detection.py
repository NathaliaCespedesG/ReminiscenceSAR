#Adapted from Steve Cox code


# Sound detection module

import pyaudio
import wave
import time
import threading
import webrtcvad
import sys
import collections
import pandas as pd
import xlsxwriter as xlsw
from array import array
from struct import pack
import numpy as np

class Sound_Detection(object):

    def __init__(self):


        # File to save the recorded audio
        self.filename = "Voice_record.wav"
        self.vad_excel = "Voice_activity.csv"


        # Sample format config
        self.FORMAT = pyaudio.paInt16
        # Channels config
        self.channels = 1
        # Sampling frequency configuration
        self.freq = 16000

        # Chunk duration in ms
        self.chunk_duration_ms = 30
        #chunk to read
        self.chunk_size = int(self.freq * self.chunk_duration_ms/1000)
        #chunk bytes
        self.chunk_bytes = self.chunk_size*2
        # Padding configuration in ms
        self.padding_duration_ms = 1500 #1 sec jugement 
        self.num_padding_chunks = int(self.padding_duration_ms/self.chunk_duration_ms)

        #Window chunks
        self.num_window_chunks = int(240/ self.chunk_duration_ms)
        self.num_window_chunks_end = self.num_window_chunks*2
        self.start_offset = int(self.num_window_chunks*self.chunk_duration_ms*0.5*self.freq)



        #VAD Config

        self.vad = webrtcvad.Vad(3)

        # Duration  config
        self.duration = 5

        # PyAudio object initialization
        self.p = pyaudio.PyAudio()
        self.streaming_object()

        # raw data variable
        self.data = []
        #  silce, no silence variable
        self.voice_activity = []

    def streaming_object(self):

        # Function to set the voice recorder and open the 
        # input channel

        self.stream = self.p.open(format=self.FORMAT,
                channels=self.channels,
                rate=self.freq,
                input=True,
                output=True,
                frames_per_buffer=self.chunk_size)
        self.frames = []
        self.frames_duration = 10 #ms

        self.got_a_sentence = False


    def normalize(snd):

        self.maximum= 32767
        self.times = float(self.maximum)/max(abs(i) for i in snd)
        self.r = array('h')
        for i in snd:
            self.r.append(int(i * self.times))
        return self.r


    def start(self):


        self.go_on = True

    def process(self):

        while self.go_on:

            ring_buffer = collections.deque(maxlen = self.num_padding_chunks)
            triggered = False
            self.voiced_frames = []
            ring_buffer_flags = [0]*self.num_window_chunks
            ring_buffer_index = 0

            ring_buffer_flags_end = [0] * self.num_window_chunks_end
            ring_buffer_index_end = 0
            buffer_in = ''

            self.raw_data = array('h')
            index = 0
            start_point = 0
            StartTime = time.time()
            print("* recording: ")
            self.stream.start_stream()

            while not self.got_a_sentence:
                self.chunk = self.stream.read(self.chunk_size)
                self.data.append(self.chunk)
                self.raw_data.extend(array('h',self.chunk))
                index += self.chunk_size
                TimeUse = time.time() - StartTime

                self.active = self.vad.is_speech(self.chunk,self.freq)
                self.voice_activity.append(1 if self.active else 0)
                #print(self.active)
                #sys.stdout.write('1' if self.active else '_')

                ring_buffer_flags[ring_buffer_index] = 1 if self.active else 0
                ring_buffer_index_end += 1
                ring_buffer_index_end %= self.num_window_chunks_end

                #start point detection

                if not triggered:
                    ring_buffer.append(self.chunk)
                    self.num_voiced = sum(ring_buffer_flags)
                    if self.num_voiced > 0.8 * self.num_window_chunks:
                        sys.stdout.write(' Open ')
                        triggered = True
                        start_point = index - self.chunk_size*20
                        ring.buffer.clear()

                # end point detection

                else:

                    ring_buffer.append(self.chunk)
                    self.num_unvoiced = self.num_window_chunks_end -sum(ring_buffer_flags_end)

                    if num_unvoiced > 0.90 * self.num_window_chunks_end or TimeUse> 10 :

                        sys.stdout.write(' Close ')
                        triggered = False
                        self.got_a_sentence = True

                #sys.stdout.flush()
                #sys.stdout.write('\n')


    def pause(self):

        self.go_on = False

    def close(self):

        print("Finished recording.")
        # stop and close stream
        self.stream.stop_stream()
        self.stream.close()
        # terminate pyaudio object
        self.p.terminate()

    def write_audio(self):
        # open the file in 'write bytes' mode
        self.wf = wave.open(self.filename, "wb")
        # set the channels
        self.wf.setnchannels(self.channels)
        # set the sample format
        self.wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        # set the sample rate
        self.wf.setframerate(self.freq)
        # write the frames as bytes
        self.wf.writeframes(b"".join(self.data))
        # close the file
        self.wf.close()

        # Write voice activity to an excel file
        self.voice_acd= np.array(self.voice_activity)
        print(self.voice_acd)
        pd.DataFrame(self.voice_acd).to_csv(self.vad_excel)

    def getData(self):

        return(self.active)

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
        data = sound.getData()
        #print(data)
        time.sleep(0.1)

    print(sound.frames)
    sound.pause()
    sound.close()
    sound.write_audio()


A = main()
'''








