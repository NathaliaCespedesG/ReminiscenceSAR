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

		self.counter = 0

		self.who = 0


		self.set_properties()

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


	def who_questions(self):

		s = self.dialogs.get_whoquestion()
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
		print('data from avatar', data)
		

		if self.sound_data == False: 

			print('First if')

			self.counter = self.counter +1
			print('counter', self.counter)

			if (self.counter == 8 and self.sound_data == False):

				print('Second if')

				s = self.dialogs.get_connectivewho()
				print(s)
				self.engine.say(s)
				self.engine.runAndWait()
				self.counter = 0
				self.who = self.who +1


				if self.who ==1:
					pass










'''

def main():

    Speech = Avatar_Speech()
    Speech.set_properties()
    Speech.get_properties()
    Speech.welcome_sentence()
    Speech.image_validation(False)
    Speech.set_personrecognized(2)


A = main()

'''





