from PyQt4 import QtCore, QtGui
import time
import threading
import Middle_layer.SpeechAvatar as Avatar
import Lower_layer.Lowerlevel_Main as Lowerlevel
import Upper_layer.ReminiscenceWindow as ReminiscenceWindow
import sys
from collections import Counter
import numpy as np


class TherapyPlugin(object):

	def __init__(self, settings = 'Workspace_Understanding/Images/Photo_1.jpeg'):

		#Loading interface settings
		self.settings = settings

		self.useAvatar = True

		#Loading libraries for TherapyPlugin

		self.Lowerlevel = Lowerlevel.LowerLevel()
		self.Avatar = Avatar.Avatar_Speech()
		self.ReminiscenceWindow = ReminiscenceWindow.ReminiscenceWindow()

		self.launch_sensors()
		self.launch_avatar()
	
	def launch_view(self):

		self.image_processing()

		self.ReminiscenceWindow.show()
		
		self.set_signals()

	def set_signals(self):

		#self.image_validation()

		#  Avatar Interaction signals
		self.ReminiscenceWindow.playButton(self.Avatar.welcome_sentence)
		self.ReminiscenceWindow.playButton(self.SensorCaptureThread.start)


		# Internal Signals
		self.ReminiscenceWindow.onUpload(self.image_validation)
		#self.ReminiscenceWindow.onUpload(self.onStart)
		
		# Lower level signals
		#self.ReminiscenceWindow.set_pathPhoto1(lambda: self.Lowerlevel.set_path('C:/Users/natha/Desktop/Reminiscence_Interface/Interface_Plugins/Lower_layer/Workspace_Understanding/Images/Photo_1.jpeg'))
		#self.ReminiscenceWindow.set_pathPhoto2(lambda: self.Lowerlevel.set_path('Workspace_Understanding/Images/Photo_2.jpeg'))
		#self.ReminiscenceWindow.set_pathPhoto3(lambda: self.Lowerlevel.set_path('Workspace_Understanding/Images/Photo_3.jpeg'))
		#self.ReminiscenceWindow.set_pathPhoto4(lambda: self.Lowerlevel.set_path('Workspace_Understanding/Images/Photo_4.jpeg'))
		self.ReminiscenceWindow.set_pathPhoto1(self.onStart)
		self.ReminiscenceWindow.set_pathPhoto2(self.onStart)
		self.ReminiscenceWindow.set_pathPhoto3(self.onStart)
		self.ReminiscenceWindow.set_pathPhoto4(self.onStart)



	def image_processing(self):


		self.Lowerlevel.set_path('C:/Users/natha/Desktop/Reminiscence_Interface/Interface_Plugins/Lower_layer/Workspace_Understanding/Images/Photo_1.jpeg')
		self.Lowerlevel.set_modules(work = True, sound = True)
		self.Lowerlevel.launch_wsmodule()

	def launch_sensors(self):

		self.SensorCaptureThread = SensorCaptureThread(interface = self)

	def launch_avatar(self):

		self.AvatarCaptureThread = AvatarCaptureThread(interface = self)

	def image_validation(self):

		m = self.ReminiscenceWindow.get_imageNull()
		if m == True:
			self.Avatar.image_validation(m)
		else:
			self.Avatar.image_validation(m)

	def onStart(self):

		# Setting lower layer modules:
		

		#self.ReminiscenceWindow.set_recognImage()

		self.Avatar.commenting_photos()




		self.ReminiscenceWindow.set_recognImage()

		m = self.Lowerlevel.get_data()

		time.sleep(5)

		self.Avatar.conversation_topics(m)

		self.Avatar.coversation_beginning()



		self.AvatarCaptureThread.start()



	
		


		'''
		self.Lowerlevel.set_modules(work = True, sound = True)

		#Lauch WS module
		self.Lowerlevel.launch_wsmodule()
		#self.imageData = self.Lowerlevel.image_data()
		#print(self.imageData)
		'''

	def randomizing_topic(self):

		pass


	'''	

	def who_conversation(self, m):

		persons = int(m['person'])
		dog = int(m['dog'])
		cat = int(m['cat'])

		if persons > 0:

			flag_persons = 1

			self.




		who = {"persons": persons, "dog": dog, "cat": cat}

	'''





	









		



		




class AvatarCaptureThread(QtCore.QThread):
    def __init__(self, parent = None, sample = 0.5, interface = None):
        super(AvatarCaptureThread,self).__init__()
        self.Ts = sample
        self.ON = True
        self.interface = interface   
         
    def run(self):
        #self.interface.robotController.posture.goToPosture("StandZero", 1.0)
        while self.ON:
            d = self.interface.Lowerlevel.update_sounddata()
            #print('data from thread',d)
            self.interface.Avatar.set_Dialog(d)
            time.sleep(self.Ts)
            
                
    def shutdown(self):
        self.ON = False



class SensorCaptureThread(QtCore.QThread):

     def __init__(self, parent = None, sample = 1, interface = None):
        super(SensorCaptureThread,self).__init__()
        self.on = False
        self.interface = interface
        
     def run(self):

        self.interface.Lowerlevel.launch_sensors()

     def shutdown(self):
        self.on = False
        self.interface.Lowerlevel.close_sensors()






		


def main():

	app = QtGui.QApplication(sys.argv)
	rem = TherapyPlugin()
	rem.launch_view()
	#rem.buttons_menu()
	#rem.reminisce_start()
	sys.exit(app.exec_())

A = main()











