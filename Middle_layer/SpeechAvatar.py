#Speech engine for the Avatar 
#Class to create the voice of the avatar 

import pyttsx3
import time 
import threading
import os 

class Avatar_Speech(object):

	def __init__(self):

		self.engine = pyttsx3.init()

		self.set_properties()

		self.get_properties()



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


		self.engine.say("Hello, my name is Ava")
		time.sleep(0.1)
		self.engine.say("It's great to know you. Today we will talk about you and some of your photos")
		time.sleep(0.1)
		self.engine.say("Please push the upload images button, To see what we've got")

		self.engine.runAndWait()
		self.engine.stop()



	def image_validation(self, m):


		if m == True:
			self.engine.say("It seems that your photos are not complete")
			time.sleep(0.1)
			self.engine.say("You want to continue?, or, You want to upload a new image?")
			self.engine.runAndWait()
			self.engine.stop()
		else:
			self.engine.say("Cool !, your photos are great!")
			time.sleep(0.1)
			self.engine.say("Let's continue with the reminiscence")
			time.sleep(0.1)
			self.engine.say("Please choose a photo")
			self.engine.runAndWait()
			self.engine.stop()







	def create_speech(self, phrase):



		self.engine.say(phrase)
		self.engine.say("My current speaking rate is:"+ str(self.rate))
		self.engine.runAndWait()
		self.engine.stop()


'''
def main():

    Speech = Avatar_Speech()
    Speech.set_properties()
    Speech.get_properties()
    Speech.create_speech("Hello world")


A = main()
'''







