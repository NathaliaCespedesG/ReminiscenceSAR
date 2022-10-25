#!/usr/bin/python2.7
"""Example: A Simple class to get & read SoundDetected Events"""
import qi
#importing dialogs for the conversation with the robot
#import resources.dialogs as dialogs
import time
import sys
import argparse
import threading


class Sound_Detector(object):
    """
    A simple class to react to face detection events.
    """

    def __init__(self,settings = { 'name'           : "NAO",
                                   'ip'             : "10.34.59.28",
                                   'port'           : 9559,
                                   'UseSpanish'     : True,
                                   'MotivationTime' : 300000000,
                                   'HeartRate_Lim'  : 140,
                                   'Cerv_Lim'       : 0,
                                   'Thor_Lim'       : 0

                                 }):
        """
        Initialisation of qi framework and event detection.
        """
        self.settings = settings
        self.ip = self.settings['ip']
        self.port = self.settings['port']
        self.useSpanish = self.settings['UseSpanish']

        self.session = qi.Session()
        try:
            self.session.connect("tcp://" + self.ip + ":" + str(self.port))
        
        except RuntimeError:
                logging.debug("Can't connect to Naoqi at ip \"" + self.ip + "\" on port " + str(self.port) +".\n"
                              "Please check your script arguments. Run with -h option for help.")
                sys.exit(1)
        # Get the service ALMemory.
        self.memory = self.session.service("ALMemory")
        # Connect the event callback.
        self.subscriber = self.memory.subscriber("SoundDetected")
        self.subscriber.signal.connect(self.on_sound_tracked)
        # Get the services ALTextToSpeech and ALFaceDetection.
        self.tts = self.session.service("ALTextToSpeech")
        self.got_sound = False
        self.sound_detection = self.session.service("ALSoundDetection")
        self.sound_detection.subscribe("Sound_Detector")
        self.sound_detection.setParameter("Sensitivity", 0.8)
        
        self.go_on = None
        self.data = False

    def on_sound_tracked(self, value):

        #print("I hear something")

        if value[0][1] == 1:
            self.got_sound = True
            
        else:
            self.got_sound = False
            
        #print(self.got_sound)


    def update_sound(self):

        return(self.got_sound)



    def on_Start(self):
        self.go_on = True

    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print "Starting Sound Detector"

        while self.go_on == True:
            time.sleep(0.5)


    def launch_thread(self):

        self.p = threading.Thread(target = self.run)
        self.p.start()

    def shutdown(self):
        self.go_on = False
        self.sound_detection.unsubscribe("Sound_Detector")

#Testing function
'''
def test():
    nao = Sound_Detector()
    nao.on_Start()
    nao.launch_thread()
    time.sleep(2)
    for i in range (200):
        time.sleep(0.25)
        m=nao.got_sound
        print(m)

    
    nao.shutdown()

nao = test()

'''

#if __name__ == '__main__':
    #nao = test()

