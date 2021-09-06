#Speech engine for the Avatar 
#Class to create the voice of the avatar 
import os, sys
ab_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Middle_layer'))
sys.path.append(ab_path)

import sys
import pyttsx3
import time 
import threading
import os 
import resources.dialogs as dialogs


class Avatar_Speech(object):

	def __init__(self):


		#Configuring talk engine 

		self.engine = pyttsx3.init()

		self.dialogs = dialogs.Dialogs()



		#self.set_properties()

		#self.get_properties()



	def get_properties(self):

		# Avatar rate

		self.rate = self.engine.getProperty('rate')
		print(self.rate)

		# Avatar volume 

		self.volume = self.engine.getProperty('volume')

		




	def set_properties(self):

		# Set Avatar rate

		self.engine.setProperty('rate', 200)  

		# Set Avatar volume 

		self.engine.setProperty('volume', 1.0)


		# Avatar voice 

		self.voices = self.engine.getProperty('voices')

		self.engine.setProperty('voice', self.voices[1].id) 


	def welcome_sentence(self):

		s = self.dialogs.welcome_sentence
		self.engine.say(s)
		time.sleep(0.1)

		s = self.dialogs.welcome_sentence2
		self.engine.say(s)
		time.sleep(0.1)

		s = self.dialogs.welcome_sentence3
		self.engine.say(s)
		time.sleep(0.1)

		self.engine.runAndWait()
		#self.engine.stop()



	def image_validation(self, m):


		if m == True:
			s = self.dialogs.image_validationbad
			self.engine.say(s)
			time.sleep(0.1)
			s = self.dialogs.image_validationbad1
			self.engine.say("You want to continue?, or, You want to upload a new image?")
			self.engine.runAndWait()

		else:
			s = self.dialogs.image_validationgreat
			self.engine.say(s)
			time.sleep(0.1)
			s = self.dialogs.image_validationgreat1
			self.engine.say(s)
			time.sleep(0.1)
			s = self.dialogs.choose_photo
			self.engine.say(s)
			self.engine.runAndWait()





	def set_personrecognized(self, num):

		s = self.dialogs.get_numpersons_sentence()
		s = s.replace('XX', str(num))
		self.engine.say(s)
		self.engine.runAndWait()


	def commenting_photos(self):

		s = self.dialogs.commenting_photo
		self.engine.say(s)
		time.sleep(0.1)
		s = self.dialogs.analizing_photo
		self.engine.say(s)
		self.engine.runAndWait()
		self.engine.stop()



	def set_Whosentences(self, data):

		self.sound_data = data

		


		if self.sound_data == True: 
			s = self.get_connectivewho
			self.engine.say(s)
			self.engine.runAndWait()






def main():

    Speech = Avatar_Speech()
    Speech.set_properties()
    Speech.get_properties()
    Speech.welcome_sentence()
    Speech.image_validation(False)
    Speech.set_personrecognized(2)


A = main()







