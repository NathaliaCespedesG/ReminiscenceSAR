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
#import Queue
import speech_recognition as sr 

class Avatar_Speech(object):

	def __init__(self, Datahandler = None):


		#Configuring talk engine 

		self.engine = pyttsx3.init()

		self.dialogs = dialogs.Dialogs()

		self.cont = 1

		self.cont1 = 0

		self.who = 0

		self.last_value = False

		self.onVoice = False

		self.change = 0

		self.person_topic = 0

		self.sound_data = []

		self.flag_topic = "Who"

		#self.q = queue.Queue()

		#self.tts_thread = TTSThread(self.q, interface = self)

		# Initializing recognizer

		self.r = sr.Recognizer()

		self.word_recognized = None

		self.cc = 0


		# Loading DB details

		self.DB = Datahandler

		self.flag = 2

		self.y = 0

		self.voice_act = 0

		self.voice_deac = 0


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




	def Talk(self, phrase):


		print('Talkiiiiiiiing')
		self.onVoice = True
		self.engine.say(phrase)
		self.engine.runAndWait()



	def getVoice(self):

		return(self.onVoice)


	def TalkingInit(self, phrase):

		self.engine.say(phrase)
		self.engine.runAndWait()





	def welcome_sentence(self):

		s = self.dialogs.welcome_sentence
		self.Talk(s)
		time.sleep(0.1)

		s = self.dialogs.welcome_sentence2
		self.Talk(s)
		time.sleep(0.1)

		s = self.dialogs.welcome_sentence3
		self.Talk(s)
		time.sleep(0.1)

		self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "WelcomingSentence", v ="True")

		#self.engine.stop()

		self.onVoice = False



	def image_validation(self, m):


		if m == True:
			s = self.dialogs.image_validationbad
			self.Talk(s)
			time.sleep(0.1)
			s = self.dialogs.image_validationbad1
			self.Talk("You want to continue?, or, You want to upload a new image?")
			

		else:
			s = self.dialogs.image_validationgreat
			self.Talk(s)
			time.sleep(0.1)
			s = self.dialogs.image_validationgreat1
			self.Talk(s)
			time.sleep(0.1)
			self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "ImageValidation", v ="True")
			s = self.dialogs.choose_photo
			self.Talk(s)
			self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "ImageSelection", v ="True")



		self.onVoice = False




	def set_petrecognized(self, num_dog, num_cat):

		print('dog', num_dog)
		print('cat', num_cat)


		if ((num_dog > 0) and (num_cat > 0)):

			s = self.dialogs.get_petWho()
			s = s.replace('XX', str(num_dog))
			s = s.replace('SS', str(num_cat))
			self.Talk(s)

			time.sleep(0.5)

		elif num_dog == 1 and num_cat ==0:

			s = self.dialogs.get_dogWho()
			self.Talk(s)


		elif num_dog > 1 and num_cat == 0:
			s = self.dialogs.dog_whos
			self.Talk(s)

		elif num_dog == 0 and num_cat ==1:

			s = self.dialogs.cat_who
			self.Talk(s)

		elif num_dog == 0 and num_cat > 1:

			s = self.dialogs.cat_whos
			self.Talk(s)
		



	def questions_pet(self, num_dog, num_cat, cont):


		if ((num_dog > 0) and (num_cat > 0)):

			if cont == 1 :
				s = self.dialogs.petQ1
				self.Talk(s)
				time.sleep(0.5)

			if cont == 2 :
				s = self.dialogs.petQ1
				self.Talk(s)
				time.sleep(0.5)

			elif cont == 3:

				s = self.dialogs.petQ2
				self.Talk(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.petQ3
				self.Talk(s)
				time.sleep(0.5)
				

			elif cont ==5:
				s = self.dialogs.petQ4
				self.Talk(s)
				time.sleep(0.5)
				self.whoVal.remove('dog')
				self.whoVal.remove('cat')




		elif num_dog == 1 and num_cat ==0:

			if cont == 1 :
				s = self.dialogs.dogQ1
				self.Talk(s)
				time.sleep(0.5)

			if cont == 2:

				s = self.dialogs.dogQ1
				self.Talk(s)
				time.sleep(0.5)

			elif cont == 3:

				s = self.dialogs.dogQ2
				self.Talk(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.dogQ3
				self.Talk(s)
				time.sleep(0.5)

			elif cont == 5:
				s = self.dialogs.dogQ4
				self.Talk(s)
				time.sleep(0.5)
				self.whoVal.remove('dog')

				

		elif num_dog > 1 and num_cat == 0:

			if cont == 1 :
				s = self.dialogs.petQ1
				self.Talk(s)
				time.sleep(0.5)

			if cont == 2:

				s = self.dialogs.dogsQ1
				self.Talk(s)
				time.sleep(0.5)

			elif cont == 3:

				s = self.dialogs.dogsQ2
				self.Talk(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.dogsQ3
				self.Talk(s)
				time.sleep(0.5)

			elif cont ==5:
				s = self.dialogs.dogsQ4
				self.Talk(s)
				time.sleep(0.5)
				self.whoVal.remove('dog')
	



		elif num_dog == 0 and num_cat ==1:

			if cont == 2:
				s = self.dialogs.catQ1
				self.Talk(s)
				time.sleep(0.5)

			elif cont == 3:

				s = self.dialogs.catQ2
				self.Talk(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.catQ3
				self.Talk(s)
				time.sleep(0.5)
		

			elif cont ==5:
				s = self.dialogs.catQ4
				self.Talk(s)
				time.sleep(0.5)
				self.whoVal.remove('cat')



		elif num_dog == 0 and num_cat > 1:


			if cont == 2:

				s = self.dialogs.catsQ1
				self.Talk(s)
				time.sleep(0.5)

			elif cont == 3:

				s = self.dialogs.catQ2
				self.Talk(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.catsQ3
				self.Talk(s)
				time.sleep(0.5)
	
			elif cont == 5:
				s = self.dialogs.catsQ4
				self.Talk(s)
				time.sleep(0.5)
				self.whoVal.remove('cat')

	def questions_where(self, num_wineglass, num_cup, num_fork, num_spoon, num_car, num_bus, num_trlig, num_stopsig, cont):

		print('where_function')


		if num_wineglass>0 and num_cup >0 and num_fork>0 and num_spoon>0:

			if cont == 1:
				s = self.dialogs.whereq1
				self.Talk(s)
				time.sleep(2)
				self.whereVal.remove('wine_glass')
				self.whereVal.remove('cup')
				self.whereVal.remove('fork')
				self.whereVal.remove('spoon')
				self.whereVal.remove('knife')


		elif num_wineglass>0 or num_cup >0 or num_fork>0 or num_spoon>0:

			print('num_cup', num_cup)

			#print('This option')

			if cont == 1:
				#print('This option 1')
				s = self.dialogs.whereq11
				print(s)
				self.Talk(s)
				time.sleep(2)
				if num_wineglass > 0:
					self.whereVal.remove('wine_glass')
				if num_cup > 0:
					self.whereVal.remove('cup')
				if num_fork > 0:
					self.whereVal.remove('fork')
				if num_spoon > 0:
					self.whereVal.remove('spoon')



		elif num_car>0 and num_bus>0 and num_trlig>0 and num_stopsig>0:
			# Is there a  street or a crowded place

			if cont == 1:
				pass


		










	def set_personrecognized(self, num):

		if num == 1:

			s = self.dialogs.get_person_sentence()
			s = s.replace('XX', str(num))
			self.Talk(s)


			time.sleep(0.5)

			s = self.dialogs.get_whoquestion()
			self.Talk(s)



		else:

			s = self.dialogs.get_numpersons_sentence()
			s = s.replace('XX', str(num))
			self.Talk(s)

			time.sleep(0.5)

			s = self.dialogs.get_whoquestions()
			self.Talk(s)


	def commenting_photos(self):

		print('Commenting the photos')

		s = self.dialogs.commenting_photo
		self.Talk(s)
		time.sleep(0.1)

		s = self.dialogs.analizing_photo
		self.Talk(s)
		time.sleep(0.1)

		self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Commenting Photos", v ="True")

		self.onVoice = False
		



	def conversation_topics(self, m):


		print(m)
		persons = int(m['person'])
		dog = int(m['dog'])
		cat = int(m['cat'])

		self.who = {"persons": persons, "dog": dog, "cat": cat}

		self.whoVal = [word for word, occurrences in self.who.items() if occurrences > 0]

		
		#print(self.whoVal)
		#print(len(self.whoVal))



		#Food Places
		whine_glass = int(m['wine glass'])
		cup = int(m['cup'])
		fork = int(m['fork'])
		spoon = int(m['spoon'])
		knife = int(m['knife'])


		# Transport - Street Places
		car = int(m['car'])
		bus = int(m['bus'])
		traffic_light = int(m['traffic light'])
		stop_sign = int(m['stop sign'])




		self.where = {"wine_glass": whine_glass, "cup": cup, "fork": fork, "spoon": spoon, "knife": knife, "car": car, "bus": bus, "traffic_light": traffic_light, "stop_sign": stop_sign}

		self.whereVal = [word for word, occurrences in self.where.items() if occurrences > 0]

		print(self.whereVal)
		#print(len(self.whereVal))

		book = int(m['book'])
		self.otherTopics = {"book":book}

		self.otherTopics = [word for word, occurrences in self.otherTopics.items() if occurrences > 0]



		#self.validation_dataWho()


	def coversation_beginning(self):

		#print('In coversation_beginning')

		self.Talk("Please say yes if you want to continue, if you don't please say no")
		self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "StartingSentence", v ="True")
		self.onVoice = False


	def no_understanding(self):

		self.Talk('Im sorry I dont understand, can you say it in a different way?')
		self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "StartingSentence", v ="Other-word")
		self.onVoice = False




	def sr_beginning(self):

		# Speech recognition implementation
		while(self.word_recognized == None):

			try:
				with sr.Microphone() as source2:
					print('here, heariiiing')
					self.r.adjust_for_ambient_noise(source2)
					self.audio2 = self.r.listen(source2)
					self.word_recognized = self.r.recognize_google(self.audio2)
					self.word_recognized = self.word_recognized.lower()
					#print(self.word_recognized)


			except sr.RequestError as e:

				print("Could not request results")

			except sr.UnknownValueError:

				self.cc = self.cc+1
				
				if self.cc == 2:
					self.Talk('I cannot understand you, could you repeat please?')
					self.onVoice = False
					time.sleep(0.1)
					self.cc = 0


		return(self.word_recognized)



	def no_beginning(self):

		s = self.dialogs.no_begin()
		print(s)
		self.Talk(s)
		time.sleep(0.1)



	def set_Dialog(self, data):

		
		print('-----------Not Talkiiiiiiing--------')
		self.onVoice = False
		self.y = self.y + 1

		[change, voice_act, voice_deac] = self.test(data)

		self.flag = change
		print('flag', self.flag)


		if self.y == 1:

			if (len(self.whoVal)>0):

				if ("persons" in self.whoVal):

					self.set_personrecognized(self.who['persons'])
					time.sleep(1)


				elif ("dog" in self.whoVal) or ("cat" in self.whoVal):

					self.set_petrecognized(self.who['dog'], self.who['cat'])
					self.questions_pet(self.who['dog'], self.who['cat'], self.cont)
					time.sleep(1)

			elif (len(self.whereVal)>0):

				if ("wine_glass" in self.whereVal) and ("cup" in self.whereVal) and ("fork" in self.whereVal) and ("spoon" in self.whereVal):

					s = self.dialogs.get_whereq1()
					self.Talk(s)
					time.sleep(1)

				if ("wine_glass" in self.whereVal) or ("cup" in self.whereVal) or ("fork" in self.whereVal) or ("spoon" in self.whereVal):

					s = self.dialogs.get_whereq11()
					self.Talk(s)
					time.sleep(1)

			else:

				self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="When")
				s = self.dialogs.get_When1()
				print(s)
				self.Talk(s)
				pass





		
		#print('CONTADOR', self.cont)


		#self.sr_beginning()


		if self.flag == 2 and self.y > 1:

		
			#print(data)

			self.cont = self.cont + 1
			self.cont1 = 0
			time.sleep(0.5)

			print('CONTADOR.......', self.cont)


			if self.flag_topic == "Who":

				if (len(self.whoVal)>0):

					if ("persons" in self.whoVal):



						#Questions regarding WHO

						
						if self.cont == 2:

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Persons-q2")

							time.sleep(1)


							if self.who['persons'] ==1:
								s = self.dialogs.get_connectiveWho1()
								self.Talk(s)
							else:
								s = self.dialogs.get_connectiveWhos1()
								self.Talk(s)
								print('plural1')


						elif self.cont == 3:

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Persons-q3")

							if self.who['persons']==1:
								s = self.dialogs.get_connectiveWho2()
								self.Talk(s)
							else:
								s = self.dialogs.get_connectiveWhos2()
								self.Talk(s)

						

						elif self.cont == 4:


							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Persons-q4")

							if self.who['persons']==1:
								s = self.dialogs.get_connectiveWho3()
								self.Talk(s)
								s = "Oh! It seem very interesting."
								self.whoVal.remove('persons')
								self.cont = 0
							else:
								s = self.dialogs.get_connectiveWhos3()
								self.Talk(s)
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
							self.cont = 1
							self.flag_topic = "When"


				else:

					# Cannot see people in the photos, let me ask another question

					self.flag_topic = "When"
					#self.cont = 1

				
			if self.flag_topic == "When":

				if self.cont == 1:

					self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="When-q1")
					s = self.dialogs.get_When1()
					self.Talk(s)
					#time.sleep(4)

				if self.cont == 2:

					self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="When-q2")
					s = self.dialogs.get_When2()
					self.Talk(s)
					self.flag_topic = "Where"
					self.cont = 0
					#time.sleep(4)				
					


			if self.flag_topic == "Where":

				time.sleep(1)

				if (len(self.whereVal)>0):


					if self.cont == 1:

						print('HERE Where 1')

						self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="where-q1")
						#Put the dialogs here for the first question depends on the data acquire from the images
						self.questions_where(self.where['wine_glass'], self.where['cup'],self.where['fork'], self.where['spoon'], self.where['car'], self.where['bus'], self.where['traffic_light'], self.where['stop_sign'], self.cont)
						print(self.whereVal)
						print(len(self.whereVal))
				else:	

					if self.cont == 1:

						self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Where-q1n")

						s = 'Oh, I cannot tell where the photo was taken. Where was it?'
						print(s)
						self.Talk(s)
						#time.sleep(4)
						

					if self.cont == 2:

						self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Where-q2")
						s = self.dialogs.get_whereq()
						self.Talk(s)
						time.sleep(0.5)



					if self.cont == 3:
						
						self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Where-q3")
						s = self.dialogs.get_where1q()
						self.Talk(s)
						time.sleep(0.5)
						self.flag_topic = "Other"
						self.cont = 0




			if self.flag_topic == "Other":


				if (len(self.otherTopics)>0):

					pass

				else:

					if self.cont == 1:
						s = 'One last question. Can you talk about other things about this photo?'
						print(s)
						self.Talk(s)
						#time.sleep(4)
						

					if self.cont == 2:

						s = 'Ahhh that is interesting.'
						print(s)
						self.Talk(s)
						self.flag_topic = "End"


		elif self.flag == 0:

			self.cont1 = self.cont1 +1


			if self.cont1 == 30:

				self.Talk("Sorry, I couldn't  hear that")
				self.cont1 = 0




	def end_phrase(self):

		self.Talk("Was nice to talk with you. Hope we can talk togheter soon")
		time.sleep(1)
		self.Talk("See ya")




	def topic_Status(self):

		return(self.flag_topic)

	
	def test(self,m):

		new_value = m


		if new_value is not None and new_value is not self.last_value:

			if new_value:

				self.change = 1

				#print('False to True')
				self.voice_act = self.voice_act + 1
				print('Voice active:', self.voice_act)

			else:

				self.change = 2
				#print('True to False')
				self.voice_deac = self.voice_deac + 1
				print('Voice deactive:', self.voice_deac)

		else:

			self.change = 0


		self.last_value = new_value


		#print('change from testing', self.change)

		return [self.change, self.voice_act, self.voice_deac]




'''

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









'''
def main():

    Speech = Avatar_Speech()
    Speech.set_properties()
    Speech.get_properties()
    Speech.welcome_sentence()
    Speech.image_validation(False)
    Speech.set_personrecognized(2)

    time.sleep(2)

    for x in range(100):

    	voice = Speech




A = main()


'''




