import os, sys
ab_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Lower_layer'))
sys.path.append(ab_path)

from Speech_Understanding import Speech_Detection as speech
import Workspace_Understanding.WorkspaceManager as workspace
import threading
import time
import random

class LowerLevel(object):

	def __init__(self, path = None):


		# Modules setting configuration
		self.settings_work = path 

		

		# Data variables

		self.data = None 


	def set_path(self, path):

		self.settings_work = path 

		print(self.settings_work)

	def set_modules(self, work = True, sound = True):

		self.WS = work
		self.SND = sound

		if self.WS:
			self.workspace = workspace.WorkspaceManager(imgpath = self.settings_work)
		if self.SND:
			self.speech = speech.Sound_Detection()

		# Function to activate interface Workspace Understanding

	def launch_wsmodule(self):

		if self.WS:
			self.workspace.launch_workspace()
		# Function to activate interface Speech Understanding

	def launch_sensors(self):

		if self.SND:
			self.speech.start()
			self.speech.launch_thread()

	def close_sensors(self):
		# Function to activate interface Speech Understanding
		if self.SND:
			self.speech.pause()
			self.speech.close()




	def print_data(self):

		# Function to print data acquire from sensors
		print("Data from LowerLevel Main:" + str(self.data))

	def image_data(self):

		if self.WS:
			self.img_data = self.workspace.data_extraction()

		return(self.img_data)

	def update_data(self):
		print('	Updating data from main')

		if self.SND:
			self.data = self.speech.getData()
			print(self.data)

	def storaging(self):
		pass


	def get_data(self):

		data = self.workspace.data_extraction()

		return(data)


'''
def main():

	ll = LowerLevel(path = 'Workspace_Understanding/Images/Photo_1.jpeg')
	ll.set_modules(work = True, sound = True)
	ll.launch_wsmodule()
	m = ll.image_data()
	print(m)
	#time.sleep(1)
	#ll.launch_sensors()
	#time.sleep(2)
	#for i in range(10):
		#ll.update_data()
		#time.sleep(0.1)
		#ll.print_data()
	#ll.close_sensors()

A = main()
'''



