#!/usr/bin/python2.7
# -*- encoding: UTF-8 -*-

"""Example: Use say Method"""
import qi
import argparse
import sys
from naoqi  import ALProxy
import time
import threading

class SpeechRecognizer(object):

    def __init__(self):
        """
        Initialisation of qi framework and event detection.
        """
        # Get the memory service
        self.session = qi.Session()
        self.ip = "10.34.58.142"
        self.port = 9559
        try:
            self.session.connect("tcp://" + self.ip + ":" + str(self.port))
        
        except RuntimeError:
                logging.debug("Can't connect to Naoqi at ip \"" + self.ip + "\" on port " + str(self.port) +".\n"
                              "Please check your script arguments. Run with -h option for help.")
                sys.exit(1)

        # Get the service ALMemory.
        self.memory = self.session.service("ALMemory")
        self.subscriber = self.memory.subscriber("WordRecognized")
        self.subscriber.signal.connect(self.on_words_tracked)
        # Get the services ALTextToSpeech
        self.asr = self.session.service("ALSpeechRecognition")
        self.asr.setLanguage("English")
        self.tts = self.session.service("ALTextToSpeech")

        #Adding vocabulary
        self.vocabulary = ["yes", "no", "nao", "please","Pepper", "yeah"]
        self.asr.pause(True)
        self.asr.setVocabulary(self.vocabulary, False)
        time.sleep(5)
        self.asr.pause(False)
        self.asr.subscribe("SpeechRecognizer")
        self.else_word = 0
        self.word = None



    def on_words_tracked(self, value):

        #print('on_words_tracked P_SpeechRecog', value)

        if((value[0] == 'no' or value[0] == 'nao')  and (value[1] > 0.5)):
                
            self.word = 'no'

            #self.tts.say('You say no')
        elif((value[0] == 'no' or value[0] == 'nao')  and (value[1] < 0.5)):

            self.word = 'no_dcatch'

        elif((value[0] == 'yes' or value[0] == 'yeah') and (value[1] > 0.5)):
            
            self.word ='yes'
            #self.tts.say('You say yes')

        elif((value[0] == 'yes' or value[0] == 'yeah') and (value[1] < 0.5)):

            self.word ='yes_dcatch'
        

        elif(value[0] == 'Pepper' and value[1] > 0.5):
            self.word = 'Pepper'
            #self.tts.say('Pepper')

        else:

            self.word = None


        #print('value in 1', value[0])
        #print('value in 2', value[1])




    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print "Starting Speech Recognized"

        while self.go_on:

            time.sleep(1)
        '''
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print "Interrupted by user, stopping SpeechRecognizer"
            self.asr.pause(False)
            self.asr.unsubscribe("SpeechRecognizer")
            #stop
            sys.exit(0)
        '''


    def start(self):

        self.go_on = True

    def pause(self):

        self.go_on = False
        self.asr.pause(False)
        self.asr.unsubscribe("SpeechRecognizer")

    def launch_thread(self):

        self.t = threading.Thread(target = self.run)
        self.t.start()

    def getData(self):
        # return the word of this function
        return(self.word)

    def setData(self):

        self.word = None





'''
def main():

    sr = SpeechRecognizer()
    sr.start()
    sr.launch_thread()
    time.sleep(2)
    for i in range(100):
        time.sleep(0.25)
        m = sr.getData()
        print('m from main', m)

A= main()
'''