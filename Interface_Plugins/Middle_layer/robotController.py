#!/usr/bin/python2.7
import qi
import sys
import time
import functools
import resources.dialogs as Dialogs
import threading
import resources.P_SpeechRecog as p_sr
import resources.P_SoundDetect as p_sd
import logging

class Robot(object):

	def __init__(self, settings = { 'IpRobot': "10.34.58.142",
                                    'port'   : 9559,
                                    'name'   : 'Aba',
                                    'MotivationTime':5,
                                    'BorgTime': 3,
                                    'useMemory': False
                                    },
                        db = None,
                        controller = None,
                 ):

		#loading settings
		self.settings = settings
		#loading event handler
		self.DB = db
		#loading resources as dialogs
		self.dialogs = Dialogs.Dialogs()
		self.word_recognized = None
		

		self.cc = 0
		self.flag = 2
		self.y = 0
		self.cont = 1

		self.cont1 = 0

		self.who = 0

		self.last_value = False

		self.onVoice = False

		self.change = 0

		self.person_topic = 0

		self.sound_data = []

		self.flag_topic = "Who"

		self.voice_act = 0

		self.voice_deac = 0

		self.flag_0 = False




		self.launch_robot()



	


	def launch_robot(self):


		#load dialogs
		self.dialogs.load_dialogs()
		print('Creating session from Robot Model Source')
		self.session = qi.Session()
		self.connect_session()

		#launching robot services
		self.get_services()
		#self.getBehaviors()
		#launching face tracking service for the robot
		self.face_tracking()

	def connect_session(self):

		print self.settings['IpRobot']

		print "tcp://" + self.settings['IpRobot'] + ":" + str(self.settings['port'])

		self.robotIp = self.settings['IpRobot']
		self.port = str(self.settings['port'])

		try:
			self.session.connect("tcp://" + self.robotIp + ":" + str(self.port))

		except RuntimeError:

			print "Can't connect to Naoqi at ip"

	def get_services(self):

		#Get the service ALMemory
		self.memory = self.session.service("ALMemory")
		self.subscriber = self.memory.subscriber("WordRecognized")
		#Get the service TexttoSpeech
		self.tts = self.session.service("ALTextToSpeech")
		#Get the robot's preprogrammed dialogues durind Autonomus Life

		self.autonomus = self.session.service("ALAutonomousLife")
		#print('AL dialogs', self.AlDialog.getLoadedTopics("English"))
		self.blinking = self.session.service("ALAutonomousBlinking")

		#Get the service SpeechRecognition
		self.asr = self.session.service("ALSpeechRecognition")
		# Get the service Motion
		self.motion = self.session.service("ALMotion")
		# Get the service Tracking
		self.tracker = self.session.service("ALTracker")
		# Get the service Animated Speech
		self.animated = self.session.service("ALAnimatedSpeech")
		self.animatedconfig = {"bodyLanguageMode":"contextual"}
		# Get service Behaviors
		self.behaviors = self.session.service("ALBehaviorManager")
		self.autonomuslife_off() # Turning off
		self.blinking_behaviour()
		#Loading Pepper SpeechRecognizer
		self.r = p_sr.SpeechRecognizer()
		self.r.start()
		self.r.launch_thread()
		# Loading Pepper SoundDetector
		self.d = p_sd.Sound_Detector()

	def getBehaviors(self):

		#print 'Aqui11'

		names = self.behaviors.getRunningBehaviors()
		print "Running Behaviors"

		if len(names) > 0:

			if (self.behaviors.isBehaviorRunning(names[0])):
				self.behaviors.stopBehavior(names[0])
				time.sleep(0.1)
			else:
				print 'Behaviors already stopped'

		else:
			print 'Not running behaviors'


		names_default = self.behaviors.getDefaultBehaviors()
		#print "Default behaviors:"
		#print names_default


		names_bha = self.behaviors.getInstalledBehaviors()
		#print "Behaviors on the robot:"
		#print names_bha

	def autonomuslife_off(self):

		self.autoState = self.autonomus.getState()
		if self.autoState != "disabled":
			self.autonomus.setState("disabled")

		self.motion.wakeUp()
		self.motion.setBreathConfig([["Bpm", 6], ["Amplitude", 0.9]])
		self.motion.setBreathEnabled("Arms", True)


	def blinking_behaviour(self):

		self.blinking.setEnabled(True)


	def face_tracking(self):

		targetName = "Face"
		faceWidth = 0.1
		self.tracker.registerTarget(targetName, faceWidth)
		self.tracker.track(targetName)

		#To stop face tracking 
		#self.tracker.stopTracker()
		#self.tracker.unregisterAllTargets()

	def welcome_sentence(self):

		s = self.dialogs.welcome_sentence
		self.animated.say(s, self.animatedconfig)
		time.sleep(0.1)

		s = self.dialogs.welcome_sentence2
		self.animated.say(s, self.animatedconfig)
		time.sleep(0.1)

		s = self.dialogs.welcome_sentence3
		self.animated.say(s, self.animatedconfig)
		time.sleep(0.1)

	def image_validation(self, m):


		if m == True:
			s = self.dialogs.image_validationbad
			self.animated.say(s)
			time.sleep(0.1)
			s = self.dialogs.image_validationbad1
			self.animated.say(s)
			

		else:
			s = self.dialogs.image_validationgreat
			self.animated.say(s)
			time.sleep(0.1)
			s = self.dialogs.image_validationgreat1
			self.animated.say(s)
			time.sleep(0.1)
			self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "ImageValidation", v ="True")
			s = self.dialogs.choose_photo
			self.animated.say(s)
			#self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "ImageSelection", v ="True")

	def set_petrecognized(self, num_dog, num_cat):

		print('dog', num_dog)
		print('cat', num_cat)


		if ((num_dog > 0) and (num_cat > 0)):

			s = self.dialogs.get_petWho()
			s = s.replace('XX', str(num_dog))
			s = s.replace('SS', str(num_cat))
			self.animated.say(s)

			time.sleep(0.5)

		elif num_dog == 1 and num_cat ==0:

			s = self.dialogs.get_dogWho()
			self.animated.say(s)


		elif num_dog > 1 and num_cat == 0:
			s = self.dialogs.dog_whos
			self.animated.say(s)

		elif num_dog == 0 and num_cat ==1:

			s = self.dialogs.cat_who
			self.animated.say(s)

		elif num_dog == 0 and num_cat > 1:

			s = self.dialogs.cat_whos
			self.animated.say(s)



	def questions_pet(self, num_dog, num_cat, cont):


		if ((num_dog > 0) and (num_cat > 0)):

			if cont == 2 :
				s = self.dialogs.petQ1
				self.animated.say(s)
				time.sleep(0.5)

			if cont == 3 :
				s = self.dialogs.petQ1
				self.animated.say(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.petQ2
				self.animated.say(s)
				time.sleep(0.5)

			elif cont == 6:

				s = self.dialogs.petQ3
				self.animated.say(s)
				time.sleep(0.5)
				

			elif cont == 5:
				s = self.dialogs.petQ4
				self.animated.say(s)
				time.sleep(0.5)
				self.whoVal.remove('dog')
				self.whoVal.remove('cat')




		elif num_dog == 1 and num_cat ==0:

			if cont == 2 :
				s = self.dialogs.dogQ1
				self.animated.say(s)
				time.sleep(0.5)

			if cont == 3:

				s = self.dialogs.dogQ2
				self.animated.say(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.dogQ3
				self.animated.say(s)
				time.sleep(0.5)

			elif cont == 5:

				s = self.dialogs.dogQ4
				self.animated.say(s)
				time.sleep(0.5)
				self.whoVal.remove('dog')


				

		elif num_dog > 1 and num_cat == 0:

			if cont == 2 :
				s = self.dialogs.petQ1
				self.animated.say(s)
				time.sleep(0.5)

			if cont == 3:

				s = self.dialogs.dogsQ1
				self.animated.say(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.dogsQ2
				self.animated.say(s)
				time.sleep(0.5)

			elif cont == 6:

				s = self.dialogs.dogsQ3
				self.animated.say(s)
				time.sleep(0.5)

			elif cont == 5:
				s = self.dialogs.dogsQ4
				self.animated.say(s)
				time.sleep(0.5)
				self.whoVal.remove('dog')
	



		elif num_dog == 0 and num_cat ==1:

			if cont == 2:
				s = self.dialogs.catQ1
				self.animated.say(s)
				time.sleep(0.5)

			elif cont == 3:

				s = self.dialogs.catQ2
				self.animated.say(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.catQ3
				self.animated.say(s)
				time.sleep(0.5)
		

			elif cont == 5:
				s = self.dialogs.catQ4
				self.animated.say(s)
				time.sleep(0.5)
				self.whoVal.remove('cat')



		elif num_dog == 0 and num_cat > 1:


			if cont == 2:

				s = self.dialogs.catsQ1
				self.animated.say(s)
				time.sleep(0.5)

			elif cont == 3:

				s = self.dialogs.catQ2
				self.animated.say(s)
				time.sleep(0.5)

			elif cont == 4:

				s = self.dialogs.catsQ3
				self.animated.say(s)
				time.sleep(0.5)
	
			elif cont == 5:
				s = self.dialogs.catsQ4
				self.animated.say(s)
				time.sleep(0.5)
				self.whoVal.remove('cat')
		



	def questions_where(self, num_wineglass, num_cup, num_fork, num_spoon, num_car, num_bus, num_trlig, num_stopsig, cont):

		print('where_function')


		if num_wineglass>0 and num_cup >0 and num_fork>0 and num_spoon>0:

			if cont == 1:
				s = self.dialogs.whereq1
				self.animated.say(s)
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
				self.animated.say(s)
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
			self.animated.say(s)


			time.sleep(0.5)

			s = self.dialogs.get_whoquestion()
			self.animated.say(s)



		else:

			s = self.dialogs.get_numpersons_sentence()
			s = s.replace('XX', str(num))
			self.animated.say(s)

			time.sleep(0.5)

			s = self.dialogs.get_whoquestions()
			self.animated.say(s)

	def commenting_photos(self, n):

		print('Commenting the photos')

		self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Commenting-photos")

		if n == 1:
			s = self.dialogs.commenting_photo
			self.animated.say(s)
			time.sleep(0.1)

			s = self.dialogs.analizing_photo
			self.animated.say(s)
			time.sleep(0.1)

		elif n > 1:

			self.animated.say("This second photo also looks good. Let's talk!")



	def coversation_beginning(self):

		#print('In coversation_beginning')

		self.animated.say("Please say yes if you want to continue, if you don't please say no")
		#self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "StartingSentence", v ="True")

	
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


	def no_understanding(self):

		self.animated.say('Im sorry I dont understand, can you say it in a different way?')



	def sr_beginning(self):

		#print('Speech Recognizer beginning')
		

		#Speech recognition implementation
		while(self.word_recognized == None):

			self.word_recognized = self.r.getData()

		print('WordRecognized', self.word_recognized)
		return(self.word_recognized)


	def bad_catching(self, word):

		if word == 'yes':
			s = self.dialogs.yes_nocatch()
			self.animated.say(s)

		if word == 'no':
			s = self.dialogs.no_nocatch()
			self.animated.say(s)


	def set_wordRecognized(self):

		print('Settings')

		self.word_recognized = None
		self.r.setData()






	def no_beginning(self):

		self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="No-beginning")

		s = self.dialogs.no_begin()
		print(s)
		self.animated.say(s)
		time.sleep(0.1)


	def yes_beginning(self):
		self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Yes-beginning")
		s = self.dialogs.yes_bsentence()
		print(s)
		self.animated.say(s)
		time.sleep(0.3)


	def second_Photo(self):

		self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Second-Photo")

		self.animated.say('Was interesting talk about this photo, how about if you chose the other one ?')



	def set_Dialog(self, data):

		#print('-----------Not Talkiiiiiiing--------')
		self.onVoice = False
		self.y = self.y + 1

		#self.getBehaviors()

		[change, voice_act, voice_deac] = self.test(data)
		#self.waiting(change,data)

		self.flag = change
		print('flag', self.flag)


		if self.y == 1:

			if (len(self.whoVal)>0):

				if ("persons" in self.whoVal):

					self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Persons-recognized")

					self.set_personrecognized(self.who['persons'])
					time.sleep(1)


				elif ("dog" in self.whoVal) or ("cat" in self.whoVal):

					self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Petsrecog-q4")

					self.set_petrecognized(self.who['dog'], self.who['cat'])
					self.questions_pet(self.who['dog'], self.who['cat'], self.cont)
					time.sleep(1)

			elif (len(self.whereVal)>0):

				self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="[Placerecog-q4")

				if ("wine_glass" in self.whereVal) and ("cup" in self.whereVal) and ("fork" in self.whereVal) and ("spoon" in self.whereVal):

					s = self.dialogs.get_whereq1()
					self.animated.say(s)
					time.sleep(1)

				if ("wine_glass" in self.whereVal) or ("cup" in self.whereVal) or ("fork" in self.whereVal) or ("spoon" in self.whereVal):

					s = self.dialogs.get_whereq11()
					self.animated.say(s)
					time.sleep(1)

			else:

				self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="When")
				s = self.dialogs.get_When1()
				#print(s)
				self.animated.say(s)
	



		if self.flag == 2 and self.y > 1:

		
			#print(data)

			self.cont = self.cont + 1
			self.cont1 = 0
			

			print('CONTADOR.......', self.cont)


			if self.flag_topic == "Who":

				if (len(self.whoVal)>0):

					if ("persons" in self.whoVal):



						#Questions regarding WHO

						
						if self.cont == 3:

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Persons-q2")

							


							if self.who['persons'] ==1:
								s = self.dialogs.get_connectiveWho1()
								self.animated.say(s)
							else:
								s = self.dialogs.get_connectiveWhos1()
								self.animated.say(s)
								print('plural1')



							time.sleep(2)



						elif self.cont == 4:

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Persons-q3")

							if self.who['persons']==1:
								s = self.dialogs.get_connectiveWho2()
								self.animated.say(s)
							else:
								s = self.dialogs.get_connectiveWhos2()
								self.animated.say(s)


							time.sleep(2)

						

						elif self.cont == 5:


							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Persons-q4")

							if self.who['persons']==1:
								s = self.dialogs.get_connectiveWho3()
								self.animated.say(s)
								s = "Oh! It seem very interesting."
								self.whoVal.remove('persons')
								self.cont = 0
							else:
								s = self.dialogs.get_connectiveWhos3()
								self.animated.say(s)
								self.whoVal.remove('persons')
								self.cont = 0

							time.sleep(2)
	

					elif ("dog" in self.whoVal) or ("cat" in self.whoVal):


						if self.cont == 2:

							print('Dog 1')

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Animals-q1")

							self.set_petrecognized(self.who['dog'], self.who['cat'])
							self.questions_pet(self.who['dog'], self.who['cat'], self.cont)

							time.sleep(2)

						if self.cont == 3:

							print('Dog 2')

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Animals-q2")

							self.questions_pet(self.who['dog'], self.who['cat'], self.cont)

							time.sleep(2)


						if self.cont == 4:

							print('Dog 3')

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Animals-q3")

							self.questions_pet(self.who['dog'], self.who['cat'], self.cont)

							time.sleep(2)


						if self.cont == 5:

							print('Dog 4')

							self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Animals-q4")

							self.questions_pet(self.who['dog'], self.who['cat'], self.cont)

							time.sleep(3)

							self.cont = 1

							self.flag_topic = 'When'



				else:

					# Cannot see people in the photos, let me ask another question

					self.flag_topic = "When"
					#self.cont = 1

				
			if self.flag_topic == "When":

				if self.cont == 1:

					self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="When-q1")
					s = self.dialogs.get_When1()
					self.animated.say(s)
					#time.sleep(4)

					time.sleep(2)

				if self.cont == 2:

					self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="When-q2")
					s = self.dialogs.get_When2()
					self.animated.say(s)
					self.flag_topic = "Where"
					self.cont = 1
					#time.sleep(4)
					time.sleep(2)				
					


			if self.flag_topic == "Where":

				#time.sleep(2)

				if (len(self.whereVal)>0):


					if self.cont == 2:

						print('HERE Where 1')

						self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="where-q1")
						#Put the dialogs here for the first question depends on the data acquire from the images
						self.questions_where(self.where['wine_glass'], self.where['cup'],self.where['fork'], self.where['spoon'], self.where['car'], self.where['bus'], self.where['traffic_light'], self.where['stop_sign'], self.cont)
						print(self.whereVal)
						print(len(self.whereVal))
						time.sleep(3)
				else:	

					if self.cont == 3:

						self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Where-q1n")

						s = 'Oh, I cannot tell where the photo was taken. Where was it?'
						print(s)
						self.animated.say(s)
						#time.sleep(4)
						time.sleep(2)
						

					if self.cont == 5:

						self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Where-q2")
						s = self.dialogs.get_whereq()
						self.animated.say(s)
						time.sleep(2)



					if self.cont == 6:
						
						self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Where-q3")
						s = self.dialogs.get_where1q()
						self.animated.say(s)
						time.sleep(2)
						self.flag_topic = "Other"
						self.cont = 1




			if self.flag_topic == "Other":


					if self.cont == 2:
						s = 'One last question. Can you talk about other things about this photo?'
						print(s)
						self.animated.say(s)
						time.sleep(2)
						

					if self.cont == 4:

						s = 'Ahhh I see.'
						print(s)
						self.animated.say(s)
						time.sleep(5)
						self.flag_topic = "End"
						self.cont = 1


		if self.flag == 0 and data == False:

			self.cont1 = self.cont1 +1


			if self.cont1 == 8:
				self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Not_User_Voice")
				self.animated.say("Sorry, I couldn't  hear that")
				self.cont1 = 0
				time.sleep(3)
				#self.cont = 0


	def end_phrase(self):

		self.DB.General.SM.loadEvent(t = "AvatarTalking", c = "Dialog", v ="Ending_Phrase")

		self.tts.say("Was nice to talk with you. Hope we can talk together soon")
		time.sleep(1)
		self.tts.say("Bye!")


	def set_topicStatus(self):

		self.flag_topic = "Who"


	def topic_Status(self):

		return(self.flag_topic)


	def waiting(self,m,n):

		#print('Change', m)
		#print('Voice', n)

		if m ==2:
			time.sleep(2)
			self.flag_0 = True

		if self.flag_0:

			if n == True:
				time.sleep(4)
				self.flag_0 = False

	
	def test(self,m):

		new_value = m


		if new_value is not None and new_value is not self.last_value:

			if new_value:

				self.change = 1

				#print('False to True')
				self.voice_act = self.voice_act + 1
				#print('Voice active:', self.voice_act)

			else:

				self.change = 2
				#print('True to False')
				self.voice_deac = self.voice_deac + 1
				#print('Voice deactive:', self.voice_deac)

		else:

			self.change = 0


		self.last_value = new_value


		#print('change from testing', self.change)

		return [self.change, self.voice_act, self.voice_deac]










		




    	
'''

#Testing function
def main():

	robot = Robot()
	#robot.launch_robot()
	time.sleep(6)
	robot.face_tracking()
	robot.welcome_sentence()
	robot.image_validation(m=True)
	robot.commenting_photos()
	robot.set_personrecognized(num = 5)

A = main()

'''


