#Class to recognize people speech

import qi
import dialogs as dialogs
import time
import time 
import sys
#import argsparse
import threading

class SpeechRecognizer(object):

    def __init__(self):
        """
        Initialisation of qi framework and event detection.
        """
        #super(SpeechRecognizer, self).__init__()
        #app.start()
        #session = app.session

        self.launch_robot()


        # Get the memory service

        # Get the service ALMemory.
        self.memory = self.session.service("ALMemory")
        self.subscriber = self.memory.subscriber("WordRecognized")
        self.subscriber.signal.connect(self.on_words_tracked)
        # Get the services ALTextToSpeech
        self.asr = self.session.service("ALSpeechRecognition")
        self.asr.setLanguage("English")
        self.tts = self.session.service("ALTextToSpeech")
        self.asr.pause(True)
        time.sleep(2)

        #Adding vocabulary
        self.vocabulary = ["yes", "no", "yeah"]
        
        self.asr.setVocabulary(self.vocabulary, True)
        self.asr.subscribe("SpeechRecognizer")


        self.go_on = None
        self.data = False
        self.value = None


    def launch_robot(self):

    	self.session = qi.Session()

    	settings = "10.34.58.142"
    	port = 9559

    	print settings
    	print "tcp://" + settings + ":" + str(port)

    	try:
    		self.session.connect("tcp://" + settings + ":" + str(port))

    	except RuntimeError:
    		print "Can't connect to Naoqi at ip"

    
    def on_words_tracked(self, value):


    	#print('Real Value', value)

    	value_c = value[0].replace("<...>", "")

    	print('value from on words')
    	print(value_c)

    	print('..........')
    	print(value[-1])



        if(value[0] == 'no' and value[1] > 0.6):
        	self.value = 'no'
        	self.tts.say('You say no')
        elif(value[0] == 'yes' and value[1] > 0.6):
        	self.value = 'yes'
        	self.tts.say('You say yes')
        elif(value[0] == 'yeah' and value[1] > 0.6):
        	self.value = 'yes'
        	self.tts.say('You say yes')





        self.value = value[0]


        #print('value in 1', value[0])
        #print('value in 2', value[1])


    def get_data(self):

    	return(self.value)



    def on_Start(self):

    	self.go_on = True




    def run(self):
        """
        Loop on, wait for events until manual interruption.
        """
        print "Starting Speech Recognized"

        while self.go_on == True:
        	time.sleep(0.1)



    def launch_thread(self):

    	self.p = threading.Thread(target = self.run)
    	self.p.start()

    def shutdown(self):

    	print('Shutdown service')

    	self.go_on = False
    	self.asr.pause(False)
    	self.asr.unsubscribe("SpeechRecognizer")

#Testing function

def test():
	nao = SpeechRecognizer()
	nao.on_Start()
	nao.launch_thread()
	time.sleep(1)
	for i in range(100):
		time.sleep(0.5)
		m=nao.get_data()
		#print('Value from', m)

	nao.shutdown()

a = test()