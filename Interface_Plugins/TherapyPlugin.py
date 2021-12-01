import os, sys
ab_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Interface_Plugins'))
sys.path.append(ab_path)



from PyQt4 import QtCore, QtGui
import time
import threading
import Middle_layer.SpeechAvatar as Avatar
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

		self.useAvatar = True

		#Load database manager

		self.DB = DataHandler

		self.date = datetime.datetime.now()

		

		#Loading libraries for TherapyPlugin

		self.Lowerlevel = Lowerlevel.LowerLevel(Datahandler = self.DB)
		self.Avatar = Avatar.Avatar_Speech(Datahandler = self.DB)
		self.ReminiscenceWindow = ReminiscenceWindow.ReminiscenceWindow(settings = self.settings)

		self.launch_sensors()
		self.launch_avatar()
	
	def launch_view(self):

		#self.image_processing()

		self.ReminiscenceWindow.show()
		
		self.set_signals()

	def set_signals(self):

		#self.image_validation()

		#  Avatar Interaction signals
		self.ReminiscenceWindow.playButton(self.Avatar.welcome_sentence)
		self.ReminiscenceWindow.playButton(self.SensorCaptureThread.start)
		self.ReminiscenceWindow.playButton(self.AvatarGraphicsThread.start)
		self.ReminiscenceWindow.closeButton(self.onShutdown)


		# Internal Signals
		self.ReminiscenceWindow.onUpload(self.image_validation)
		#self.ReminiscenceWindow.onUpload(self.onStart)
		
		# Lower level signals
		self.ReminiscenceWindow.set_pathPhoto1(self.onStart)
		self.ReminiscenceWindow.set_pathPhoto2(self.onStart)
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
		self.Lowerlevel.set_path(self.settings +'/' + photo1)
		self.Lowerlevel.set_modules(work = True, sound = True)
		self.Lowerlevel.launch_wsmodule()

	def launch_sensors(self):

		self.SensorCaptureThread = SensorCaptureThread(interface = self)

	def launch_avatar(self):

		self.AvatarCaptureThread = AvatarCaptureThread(interface = self)
		self.AvatarGraphicsThread = AvatarGraphicsThread(f = self.update_AvatarGraphics, sample = 0.1)

	def image_validation(self):

		m = self.ReminiscenceWindow.get_imageNull()
		if m == True:
			self.Avatar.image_validation(m)
		else:
			self.Avatar.image_validation(m)

	def onStart(self):

		# Setting lower layer modules:

		#self.ReminiscenceWindow.set_recognImage()

		#self.AvatarGraphicsThread.start()

		self.Avatar.commenting_photos()





		self.ReminiscenceWindow.set_recognImage()

		m = self.Lowerlevel.get_data()

		self.DB.General.SM.loadSensor(recog_obj = m)


		time.sleep(5)

		self.Avatar.conversation_topics(m)
		self.Avatar.coversation_beginning()



		self.AvatarCaptureThread.start()


	def update_AvatarGraphics(self):

		#data = self.Lowerlevel.update_sounddata()

		self.ReminiscenceWindow.update_sound()



	def onShutdown(self):
		print('Here shutdown')

		path = 'C:/Users/natha/Desktop/Reminiscence_Interface/db/general'+'/'+ self.user['id'] + '/'+ str(self.date.year) +"-"+ str(self.date.month)+"-"+ str(self.date.day)
		
		self.Lowerlevel.write_audio(path)
		
		self.AvatarCaptureThread.shutdown()
		self.SensorCaptureThread.shutdown()
		self.AvatarGraphicsThread.shutdown()


		














class AvatarCaptureThread(QtCore.QThread):
    def __init__(self, parent = None, sample = 0.5, interface = None):
        super(AvatarCaptureThread,self).__init__()
        self.Ts = sample
        self.ON = True
        self.interface = interface
        self.c = 0 
         
    def run(self):
        #self.interface.robotController.posture.goToPosture("StandZero", 1.0)
        while self.ON:


        	if self.c == 0:

        		n = self.interface.Avatar.sr_beginning()
        		print('Speech recognition from avatar', n)

        		if n == "yes":

        			self.c = 1

        		if n =='no':

        			self.c = 2

        		else:
        			pass

        	if self.c == 1:

        		if (n == 'yes'):
        			
        			d = self.interface.Lowerlevel.update_sounddata()
        			#loading sound data in the interface
        			self.interface.DB.General.SM.loadSensor(voice = d)
        			#print('data from thread',d)
        			self.interface.Avatar.set_Dialog(d)
        			time.sleep(self.Ts)

        	if self. c == 2:


        		self.interface.Avatar.no_beginning()

        		self.ON = False

        		time.sleep(10)

        		self.interface.onShutdown()



        	else:

        		pass
           

            
            
                
    def shutdown(self):
        self.ON = False




class SensorCaptureThread(QtCore.QThread):

     def __init__(self, parent = None, sample = 0.5, interface = None):
        super(SensorCaptureThread,self).__init__()
        self.on = False
        self.interface = interface
        
     def run(self):

        self.interface.Lowerlevel.launch_sensors()

     def shutdown(self):
        self.on = False
        self.interface.Lowerlevel.close_sensors()




class AvatarGraphicsThread(QtCore.QThread):

	def __init__(self, parent = None, f = None, sample = 0.5):
		super(AvatarGraphicsThread,self).__init__()
		self.f = f
		self.Ts = sample
		self.ON = True

	def run(self):

		if self.f:

			while self.ON:

				self.f()
				time.sleep(self.Ts)

	def shutdown(self):

		self.ON = False



		

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










