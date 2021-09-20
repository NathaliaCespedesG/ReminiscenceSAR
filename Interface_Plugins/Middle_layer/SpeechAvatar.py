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

		self.cont = 0

		self.cont1 = 0

		self.who = 0

		self.last_value = False

		self.change = 0

		self.person_topic = 0

		self.sound_data = []

		self.flag_topic = "Who"



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

		if num == 1:
			s = self.dialogs.get_persons_sentence()
			s = s.replace('XX', str(num))
			self.engine.say(s)
			self.engine.runAndWait()

			time.sleep(0.5)

			s = self.dialogs.get_whoquestion()
			self.engine.say(s)
			self.engine.runAndWait()



		else:

			s = self.dialogs.get_numpersons_sentence()
			s = s.replace('XX', str(num))
			self.engine.say(s)
			self.engine.runAndWait()

			time.sleep(0.5)

			s = self.dialogs.get_whoquestions()
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



	def conversation_topics(self, m):


		print(m)
		persons = int(m['person'])
		dog = int(m['dog'])
		cat = int(m['cat'])

		self.who = {"persons": persons, "dog": dog, "cat": cat}

		self.whoVal = [word for word, occurrences in self.who.items() if occurrences > 0]

		
		#print(self.whoVal)
		#print(len(self.whoVal))



		bird = int(m['bird'])
		whine_glass = int(m['wine glass'])
		cup = int(m['cup'])
		car = int(m['car'])
		bus = int(m['bus'])

		self.where = {"bird": bird, "cup": cup, "car": car, "bus": bus}

		self.whereVal = [word for word, occurrences in self.where.items() if occurrences > 0]

		#print(self.whereVal)
		#print(len(self.whereVal))

		book = int(m['book'])
		self.otherTopics = {"book":book}

		self.otherTopics = [word for word, occurrences in self.otherTopics.items() if occurrences > 0]



		#self.validation_dataWho()


	def coversation_beginning(self):

		self.engine.say("Please say yes if you want to continue")
		self.engine.runAndWait()



	def set_Dialog(self, data):


		flag = self.test(data)
		print('flag', flag)



		if flag == 2:

			print(data)

			self.cont = self.cont + 1
			self.cont1 = 0
			time.sleep(5)


			if self.flag_topic == "Who":

				if (len(self.whoVal)>0):

					if ("persons" in self.whoVal):

						print('Who, persons')

						#Questions regarding WHO

						if self.cont == 1:
							#time.sleep(1)
							self.set_personrecognized(self.who['persons'])
							#time.sleep(4)

						elif self.cont == 2:
							#time.sleep(10)
							s = self.dialogs.connective_dialogueswho1
							print(s)
							self.engine.say(s)
							self.engine.runAndWait()
							#time.sleep(4)

						elif self.cont == 3:

							#time.sleep(1)
							s = self.dialogs.connective_dialogueswho2
							print(s)
							self.engine.say(s)
							self.engine.runAndWait()
							#time.sleep(4)

						elif self.cont == 4:

							s = self.dialogs.connective_dialogueswho2
							print(s)
							self.engine.say(s)
							self.engine.runAndWait()
							#time.sleep(4)
							self.flag_topic = "When"
							self.cont = 0

				else:

					# Cannot see people in the photos, let me ask another quesrion

					self.flag_topic = "When"
					self.cont = 0

				
			if self.flag_topic == "When":

				if self.cont == 1:

					#time.sleep(10)
					s = 'Can you tell me when this photo was taken?'
					print(s)
					self.engine.say(s)
					self.engine.runAndWait()
					#time.sleep(4)


				if self.cont == 2:

					#time.sleep(10)
					s = 'Can you tell me the time when this photo was taken?'
					print(s)
					self.engine.say(s)
					self.engine.runAndWait()
					#time.sleep(4)

				if self.cont == 3:

					#time.sleep(10)
					s = 'Can you tell me when this photo was taken?'
					print(s)
					self.engine.say(s)
					self.engine.runAndWait()
					#time.sleep(4)

				if self.cont == 4:

					#time.sleep(10)
					s = 'Can you tell me when this photo was taken?'
					print(s)
					self.engine.say(s)
					self.engine.runAndWait()
					#time.sleep(4)
					self.flag_topic = "Where"
					self.cont = 0

			if self.flag_topic == "Where":

				if (len(self.whereVal)>0):

					pass

				else:

					s = 'Oh, I cannot identify an specific place. Where this photo was taken?'
					print(s)
					self.engine.say(s)
					self.engine.runAndWait()
					#time.sleep(4)
					self.flag_topic = "Other"
					self.cont = 0

			if self.flag_topic == "Other":


				if (len(self.otherTopics)>0):

					pass

				else:

					s = 'Can you talk about other things about this photo?'
					print(s)
					self.engine.say(s)
					self.engine.runAndWait()
					#time.sleep(4)
					self.flag_topic = "Other"
					self.cont = 0








							

	
				





		elif flag == 0:

			self.cont1 = self.cont1 +1

			print('Here cont1', self.cont1)

			if self.cont1 == 12:

				self.engine.say("Sorry, I couldn't  hear that")
				self.engine.runAndWait()
				self.cont1 = 0



			pass


		'''
		if (len(self.whoVal)>0):

			if "persons" in self.whoVal:
				if self.cont == 0:
					time.sleep(1)
					self.set_personrecognized(self.who['persons'])

					self.cont =1000
				elif self.cont == 1:
					time.sleep(1)
					s = self.dialogs.connective_dialogueswho1
					print(s)
					self.engine.say(s)
					self.engine.runAndWait()
					time.sleep(5)

	'''



		#self.validation_dataWho()

		#self.engine



		'''
		if (self.change == 2):

			self.cont = self.cont + 1
			print(self.cont)


			if self.cont == 1:

				time.sleep(1)
				s = self.dialogs.connective_dialogueswho1
				print(s)
				self.engine.say(s)
				self.engine.runAndWait()
				time.sleep(5)

			if self.cont == 2:

				time.sleep(1)
				s = self.dialogs.connective_dialogueswho2
				print(s)
				self.engine.say(s)
				self.engine.runAndWait()
				ime.sleep(5)

		'''		





		#print('FLag', flag)

		'''
		if(flag == True):

			self.cont = self.cont + 1
			print(self.cont)

			if(self.cont == 1):
				print('AQUIIIII1')

				time.sleep(0.5)
				s = self.dialogs.connective_dialogueswho1
				print(s)
				self.engine.say(s)
				self.engine.runAndWait()

			


			if(self.cont == 2):

				time.sleep(0.5)
				s = self.dialogs.connective_dialogueswho2
				print(s)
				self.engine.say(s)
				self.engine.runAndWait()
			'''	
		


		


		

	def test(self,m):

		new_value = m


		if new_value is not None and new_value is not self.last_value:

			if new_value:

				self.change = 1

				print('False to True')

			else:

				self.change = 2
				print('True to False')

		else:

			self.change = 0


		self.last_value = new_value


		print('change from testing', self.change)

		return self.change


	def validation_dataWho(self):

		# Validation of who

		if(self.who['persons'] > 0 and self.person_topic == 0):

			self.set_personrecognized(self.who['persons'])



			self.Whotopic = 1


		elif self.who['dog'] > 0 :


			self.Whotopic = 2



		elif self.who['cat'] > 0:

			self.Whotopic = 3





	









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





