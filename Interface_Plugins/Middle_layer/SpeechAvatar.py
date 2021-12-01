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
import queue
import speech_recognition as sr 

class Avatar_Speech(object):

	def __init__(self, Datahandler = None):


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

		self.q = queue.Queue()

		self.tts_thread = TTSThread(self.q, interface = self)

		# Initializing recognizer

		self.r = sr.Recognizer()

		self.word_recognized = None

		self.c = 0


		# Loading DB details

		self.DB = Datahandler

		self.flag = 2




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
		self.engine.connect('started-utterance', self.onStart) 
		self.engine.connect('finished-utterance', self.onEnd)


	def onStart(self):


		print('starting')


	def onEnd(name, completed):

   		print('finishing')




	def welcome_sentence(self):

		s = self.dialogs.welcome_sentence
		self.q.put(s)
		time.sleep(0.1)

		s = self.dialogs.welcome_sentence2
		self.q.put(s)
		time.sleep(0.1)

		s = self.dialogs.welcome_sentence3
		self.q.put(s)
		time.sleep(0.1)

		self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "WelcomingSentence", v ="True")

		#self.engine.stop()



	def image_validation(self, m):


		if m == True:
			s = self.dialogs.image_validationbad
			self.q.put(s)
			time.sleep(0.1)
			s = self.dialogs.image_validationbad1
			self.q.put("You want to continue?, or, You want to upload a new image?")
			

		else:
			s = self.dialogs.image_validationgreat
			self.q.put(s)
			time.sleep(0.1)
			s = self.dialogs.image_validationgreat1
			self.q.put(s)
			time.sleep(0.1)
			self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "ImageValidation", v ="True")
			s = self.dialogs.choose_photo
			self.q.put(s)
			self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "ImageSelection", v ="True")




	def set_petrecognized(self, num_dog, num_cat):

		print('dog', num_dog)
		print('cat', num_cat)


		if ((num_dog > 0) and (num_cat > 0)):

			s = self.dialogs.get_petWho()
			s = s.replace('XX', str(num_dog))
			s = s.replace('SS', str(num_cat))
			self.q.put(s)

			time.sleep(0.5)

		elif num_dog == 1 and num_cat ==0:

			s = self.dialogs.get_dogWho()
			self.q.put(s)


		elif num_dog > 1 and num_cat == 0:
			s = self.dialogs.dog_whos
			self.q.put(s)

		elif num_dog == 0 and num_cat ==1:

			s = self.dialogs.cat_who
			self.q.put(s)

		elif num_dog == 0 and num_cat > 1:

			s = self.dialogs.cat_whos
			self.q.put(s)
		



	def questions_pet(self, num_dog, num_cat, cont):


		if ((num_dog > 0) and (num_cat > 0)):

			if cont == 1 :
				s = self.dialogs.petQ1
				self.q.put(s)
				time.sleep(0.5)

			if cont == 2 :
				s = self.dialogs.petQ1
				self.q.put(s)
				time.sleep(0.5)

			elif cont == 3:

				s = self.dialogs.petQ2
				self.q.put(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.petQ3
				self.q.put(s)
				time.sleep(0.5)
				

			elif cont ==5:
				s = self.dialogs.petQ4
				self.q.put(s)
				time.sleep(0.5)
				self.whoVal.remove('dog')
				self.whoVal.remove('cat')




		elif num_dog == 1 and num_cat ==0:

			if cont == 1 :
				s = self.dialogs.dogQ1
				self.q.put(s)
				time.sleep(0.5)

			if cont == 2:

				s = self.dialogs.dogQ1
				self.q.put(s)
				time.sleep(0.5)

			elif cont == 3:

				s = self.dialogs.dogQ2
				self.q.put(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.dogQ3
				self.q.put(s)
				time.sleep(0.5)

			elif cont == 5:
				s = self.dialogs.dogQ4
				self.q.put(s)
				time.sleep(0.5)
				self.whoVal.remove('dog')

				

		elif num_dog > 1 and num_cat == 0:

			if cont == 1 :
				s = self.dialogs.petQ1
				self.q.put(s)
				time.sleep(0.5)

			if cont == 2:

				s = self.dialogs.dogsQ1
				self.q.put(s)
				time.sleep(0.5)

			elif cont == 3:

				s = self.dialogs.dogsQ2
				self.q.put(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.dogsQ3
				self.q.put(s)
				time.sleep(0.5)

			elif cont ==5:
				s = self.dialogs.dogsQ4
				self.q.put(s)
				time.sleep(0.5)
				self.whoVal.remove('dog')
	



		elif num_dog == 0 and num_cat ==1:

			if cont == 2:
				s = self.dialogs.catQ1
				self.q.put(s)
				time.sleep(0.5)

			elif cont == 3:

				s = self.dialogs.catQ2
				self.talk(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.catQ3
				self.talk(s)
				time.sleep(0.5)
		

			elif cont ==5:
				s = self.dialogs.catQ4
				self.talk(s)
				time.sleep(0.5)
				self.whoVal.remove('cat')



		elif num_dog == 0 and num_cat > 1:


			if cont == 2:

				s = self.dialogs.catsQ1
				self.talk(s)
				time.sleep(0.5)

			elif cont == 3:

				s = self.dialogs.catQ2
				self.talk(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.catsQ3
				self.talk(s)
				time.sleep(0.5)
	
			elif cont == 5:
				s = self.dialogs.catsQ4
				self.talk(s)
				time.sleep(0.5)
				self.whoVal.remove('cat')



	def set_personrecognized(self, num):

		if num == 1:

			s = self.dialogs.get_person_sentence()
			s = s.replace('XX', str(num))
			self.q.put(s)


			time.sleep(0.5)

			s = self.dialogs.get_whoquestion()
			self.q.put(s)



		else:

			s = self.dialogs.get_numpersons_sentence()
			s = s.replace('XX', str(num))
			self.q.put(s)

			time.sleep(0.5)

			s = self.dialogs.get_whoquestions()
			self.q.put(s)


	def commenting_photos(self):

		print('Commenting the photos')

		s = self.dialogs.commenting_photo
		self.q.put(s)
		time.sleep(0.1)

		s = self.dialogs.analizing_photo
		self.q.put(s)
		time.sleep(0.1)

		self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Commenting Photos", v ="True")
		



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

		print('In coversation_beginning')

		self.q.put("Please say yes if you want to continue")
		self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "StartingSentence", v ="True")



	def sr_beginning(self):



		# Speech recognition implementation
		while(self.word_recognized == None):

			try:
				with sr.Microphone() as source2:

					self.r.adjust_for_ambient_noise(source2, duration = 0.2)
					self.audio2 = self.r.listen(source2)
					self.word_recognized = self.r.recognize_google(self.audio2)
					self.word_recognized = self.word_recognized.lower()
					print(self.word_recognized)


			except sr.RequestError as e:

				print("Could not request results")

			except sr.UnknownValueError:

				self.c = self.c+1
				
				if self.c == 5:
					self.q.put('I cannot understan you, could you repeat please?')
					time.sleep(0.1)
					self.c = 0


		return(self.word_recognized)



	def no_beginning(self):

		s = self.dialogs.no_begin()
		print(s)
		self.q.put(s)
		time.sleep(0.1)



	def set_Dialog(self, data):


		#flag = self.test(data)
		#print('flag', flag)


		#self.sr_beginning()

		




		if self.flag == 2:

			self.flag = self.test(data)
			print('flag', flag)


			#print(data)

			self.cont = self.cont + 1
			self.cont1 = 0
			time.sleep(5)


			if self.flag_topic == "Who":

				if (len(self.whoVal)>0):

					if ("persons" in self.whoVal):



						#Questions regarding WHO
						if self.cont == 1:

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Persons-q1")

							time.sleep(1)
							self.set_personrecognized(self.who['persons'])
							#time.sleep(4)

						
						elif self.cont == 2:

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Persons-q2")

							time.sleep(1)


							if self.who['persons'] ==1:
								s = self.dialogs.get_connectiveWho1()
								self.q.put(s)
							else:
								s = self.dialogs.get_connectiveWhos1()
								self.q.put(s)
								print('plural1')


						elif self.cont == 3:

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Persons-q3")

							if self.who['persons']==1:
								s = self.dialogs.get_connectiveWho2()
								self.q.put(s)
							else:
								s = self.dialogs.get_connectiveWhos2()
								self.q.put(s)

						

						elif self.cont == 4:

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Persons-q4")

							if self.who['persons']==1:
								s = self.dialogs.get_connectiveWho3()
								self.q.put(s)
								s = "Oh! It seem very interesting."
								self.whoVal.remove('persons')
								self.cont = 0 
							else:
								s = self.dialogs.get_connectiveWhos3()
								self.q.put(s)
								self.whoVal.remove('persons')
								self.cont = 0 
	

					elif ("dog" in self.whoVal) or ("cat" in self.whoVal):


						if self.cont == 1:

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Animals-q1")

							self.set_petrecognized(self.who['dog'], self.who['cat'])
							self.questions_pet(self.who['dog'], self.who['cat'], self.cont)

							time.sleep(1)

						if self.cont == 2:

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Animals-q2")

							self.questions_pet(self.who['dog'], self.who['cat'], self.cont)


						if self.cont == 3:

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Animals-q3")

							print("dogs 2")

							self.questions_pet(self.who['dog'], self.who['cat'], self.cont)


						if self.cont == 4:

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Animals-q4")

							self.questions_pet(self.who['dog'], self.who['cat'], self.cont)

						if self.cont == 5:

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Animals-q5")
							
							self.questions_pet(self.who['dog'], self.who['cat'], self.cont)
							self.cont = 0
							self.flag_topic = "When"


				else:

					# Cannot see people in the photos, let me ask another quesrion

					self.flag_topic = "When"
					self.cont = 0

				
			if self.flag_topic == "When":

				if self.cont == 1:

					#time.sleep(10)

					s = self.dialogs.get_When1()
					print(s)
					self.q.put(s)
					#time.sleep(4)
					self.cont = 0
					self.flag_topic = "Where"


			if self.flag_topic == "Where":

				time.sleep(1)

				if (len(self.whereVal)>0):

					pass

				else:

					s = 'Oh, I cannot identify an specific place. Where this photo was taken?'
					print(s)
					self.q.put(s)
					#time.sleep(4)
					self.flag_topic = "Other"
					self.cont = 0

			if self.flag_topic == "Other":


				if (len(self.otherTopics)>0):

					pass

				else:

					s = 'Can you talk about other things about this photo?'
					print(s)
					self.q.put(s)
					#time.sleep(4)
					self.flag_topic = "Other"
					self.cont = 0

		elif self.flag == 0:

			self.cont1 = self.cont1 +1


			if self.cont1 == 50:

				self.q.put("Sorry, I couldn't  hear that")
				self.cont1 = 0



	
	def test(self,m):

		new_value = m


		if new_value is not None and new_value is not self.last_value:

			if new_value:

				self.change = 1

				#print('False to True')

			else:

				self.change = 2
				#print('True to False')

		else:

			self.change = 0


		self.last_value = new_value


		#print('change from testing', self.change)

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



class TTSThread(threading.Thread):

	def __init__(self, queue, interface = None):

		threading.Thread.__init__(self)

		print("TTSThread_crated")


		self.queue = queue
		self.daemon = True
		self.interface = interface
		self.start()

	def run(self):
		tts_engine = pyttsx3.init()
		tts_engine.startLoop(False)
		t_running = True
		print('AvatarThread')

		while t_running:

			#print(tts.engine.isBusy())

			if self.queue.empty():
				tts_engine.iterate()
			else:
				data = self.queue.get()

				if data == "exit":
					t_running = False
					self.interface.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Avatar_Speech", v ="False")
				else:
					tts_engine.say(data)
					self.interface.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Avatar_Speech", v ="True")



		tts_engine.endLoop()










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





