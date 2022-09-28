
#!/usr/bin/python2.7
import threading
import os, sys
ab_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Interface_Plugins'))
sys.path.append(ab_path)
from PyQt4 import QtCore, QtGui
import time

#import Middle_layer.SpeechRobot as Robot
import Middle_layer.robotController as Robot
import Lower_layer.Lowerlevel_Main as Lowerlevel
import Upper_layer.ReminiscenceWindow as ReminiscenceWindow
import sys
from collections import Counter
import numpy as np
import datetime


class TherapyPlugin(object):

	def __init__(self, settings = 'Images/Photo_1.jpeg', DataHandler = None):

		#Loading interface settings
		self.settings = settings
		#print('Setting from TherapyPlugin', self.settings)

		self.useRobot = True

		#Load database manager

		self.DB = DataHandler

		self.date = datetime.datetime.now()

		self.validation = None

		self.onSart_count = 0

		

		#Loading libraries for TherapyPlugin

		self.Lowerlevel = Lowerlevel.LowerLevel(Datahandler = self.DB)
		self.Robot = Robot.Robot(db = self.DB)
		#self.Avatar = Avatar.Avatar_Speech(Datahandler = self.DB)
		self.ReminiscenceWindow = ReminiscenceWindow.ReminiscenceWindow(settings = self.settings)

		self.launch_sensors()
		self.launch_robot()
	
	def launch_view(self):

		#self.image_processing()

		self.ReminiscenceWindow.show()
		
		self.set_signals()

	def set_signals(self):

		#self.image_validation()

		#  Avatar Interaction signals
		self.ReminiscenceWindow.playButton(self.Robot.welcome_sentence)
		self.ReminiscenceWindow.playButton(self.SensorCaptureThread.start)
		#self.ReminiscenceWindow.playButton(self.AvatarGraphicsThread.start)
		self.ReminiscenceWindow.closeButton(self.onShutdown)


		# Internal Signals
		self.ReminiscenceWindow.onUpload(self.image_validation)
		self.ReminiscenceWindow.onPhoto.connect(self.comment_photos)

		#self.ReminiscenceWindow.onUpload(self.onStart)
		
		# Lower level signals
		self.ReminiscenceWindow.set_pathPhoto1(lambda:self.onStart(n=1))
		self.ReminiscenceWindow.set_pathPhoto2(lambda:self.onStart(n=2))
		#self.ReminiscenceWindow.set_pathPhoto3(self.onStart)
		#self.ReminiscenceWindow.set_pathPhoto4(self.onStart)


	def user_data(self, user):

		self.user = user



	def image_processing(self):


		# Available photos in Lower layer level
		self.photos = os.listdir(self.settings)
		# Photos name in the directory
		photo1 = self.photos[0]
		photo2 = self.photos[1]
		#Setting paths in the Lower level 
		self.Lowerlevel.set_path({'path1': self.settings +'/' + photo1, 'path2': self.settings +'/' + photo2})
		self.Lowerlevel.set_modules(work = True, sound = True)
		self.Lowerlevel.launch_wsmodule()

	def launch_sensors(self):

		self.SensorCaptureThread = SensorCaptureThread(interface = self)

	def launch_robot(self):

		#Launching the robot thread
		self.RobotCaptureThread = RobotCaptureThread(interface = self)

	def image_validation(self):
		print('image_validation')

		self.validation = self.ReminiscenceWindow.validate_images()

		print('Validatiooon', self.validation)

		if self.validation == False:
			self.comment_photos()
			#self.ReminiscenceWindow.onPhoto.emit()
		#time.sleep(10)


	def comment_photos(self):

		print('Robot commenting')

		self.Robot.image_validation(self.validation)



	def onStart(self, n):

		img_id = n
		self.onSart_count += 1

		#Launching Robot's SR module
		self.Robot.launch_RobotSR()
		
		# Setting lower layer modules


		self.ReminiscenceWindow.set_recognImage(img_id)

		self.Robot.commenting_photos(self.onSart_count)
		
		m = self.Lowerlevel.get_data(img_id)

		#print('Data from Lower Level Images', m)

		self.DB.General.SM.loadSensor(recog_obj = m)


		time.sleep(5)

		self.Robot.conversation_topics(m)
		self.Robot.coversation_beginning()

		self.RobotCaptureThread.start()


	def update_RobotGraphics(self):

		#data = self.Lowerlevel.update_sounddata()

		self.ReminiscenceWindow.update_sound()



	def second_Photo(self):

		self.ReminiscenceWindow.onPhoto2.emit()
		self.RobotCaptureThread.c = 0
		self.RobotCaptureThread.n = None
		self.RobotCaptureThread.shutdown()
		self.Robot.set_topicStatus()
	



	def onShutdown(self):
		print('Here shutdown')



		time.sleep(5)
		self.Robot.r.pause()
		self.RobotCaptureThread.shutdown()
		self.SensorCaptureThread.shutdown()

		path = 'C:/Users/Nathalia Cespedes/Desktop/Reminiscence_Interface_Robot/db/general'+'/'+ self.user['id'] + '/'+ str(self.date.year) +"-"+ str(self.date.month)+"-"+ str(self.date.day)
		self.Lowerlevel.write_audio(path)
		self.Lowerlevel.close_sensors()

		self.ReminiscenceWindow.close()

		time.sleep(1)

		sys.exit()
		


		














class RobotCaptureThread(QtCore.QThread):
    def __init__(self, parent = None, sample = 1, interface = None):
        super(RobotCaptureThread,self).__init__()
        self.Ts = sample
        self.ON = True
        self.interface = interface
        self.c = 0 
        self.n = None
        self.num_threads = 0
        self.cont_yesd = 0
        self.cont_nod = 0 

         
    def run(self):
        #self.cd dinterface.robotController.posture.goToPosture("StandZero", 1.0)
        self.ON = True
        d = 0
        #print('c variable', self.c)
        #print('n variable', self.n)
        #print('ON variable', self.ON)
        self.num_threads = self.num_threads + 1
        #print('Threads', self.num_threads)

        while self.ON:



        	if self.c == 0:


        		self.n = self.interface.Robot.sr_beginning()

        		print('word from recognized', self.n)


        		if self.n == "yes":
        			#print('Here, when says yes')
        			self.interface.Robot.yes_beginning()

        			self.c = 1


        		elif self.n =='no':
        			#print('Here')
        			self.c = 2

        		elif(self.n == "yes_dcatch"):

        			self.interface.Robot.set_wordRecognized()

        			if self.cont_yesd > 1:

        				#print('yes_dcatch 2222')
        				self.interface.Robot.bad_catching('yes')
        	
        			self.cont_yesd += 1
        			self.c = 0
        				

        		elif(self.n == "no_dcatch"):

        			self.interface.Robot.set_wordRecognized()

        			if self.cont_nod > 1:
        				#print('no_dcatch 2222')
        				self.interface.Robot.bad_catching('no')

        			self.cont_nod +=1
        			self.c = 0



        		elif(self.n != "yes" and self.n != "no"):

        			print('Different word')
        			self.interface.Robot.no_understanding()
        			self.interface.Robot.set_wordRecognized()
        			self.c = 0




        	if self.c == 1:

        		if (self.n == 'yes'):

        			#self.interface.Robot.r.pause()
        			#d = self.interface.Robot.d.update_sound()
        			d = self.interface.Lowerlevel.update_sounddata()
        			print('data from lower level sound', d)
        			#loading sound data in the interface
        			self.interface.DB.General.SM.loadSensor(voice = d)
        			#print('data from thread',d)
        			self.interface.Robot.set_Dialog(d)
        			
        			topic = self.interface.Robot.topic_Status()
        			print('Topic flag', topic)
        			if topic == "End":

        				if self.num_threads == 1:
        					self.n = None
        					self.c = 0
        					self.interface.Robot.set_wordRecognized()
        					self.interface.Robot.second_Photo()
        					self.interface.second_Photo()
        				elif self.num_threads ==2:
        					self.interface.Robot.end_phrase()
        					time.sleep(5)
        					self.interface.onShutdown()
        			time.sleep(self.Ts)

        	if self. c == 2:

        		#self.interface.Robot.r.pause()
        		self.interface.Robot.no_beginning()

        		self.ON = False

        		time.sleep(1)

        		self.interface.onShutdown()


           

            
            
                
    def shutdown(self):
    	print('shutdown')
        self.ON = False




class SensorCaptureThread(QtCore.QThread):

     def __init__(self, parent = None, sample = 0.5, interface = None):
        super(SensorCaptureThread,self).__init__()
        self.on = False
        self.interface = interface
        #self.interface.Robot.d.on_Start()
        
     def run(self):

     	#self.interface.Robot.d.launch_thread()
     	self.interface.Lowerlevel.launch_sensors()

     def shutdown(self):
        self.on = False
        
        







		

'''
def main():

	app = QtGui.QApplication(sys.argv)
	rem = TherapyPlugin()
	rem.launch_view()
	#rem.buttons_menu()
	#rem.reminisce_start()
	sys.exit(app.exec_())

A = main()
'''










