import Speech_Understanding.Speech_Detection as speech
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
			self.workspace.data_extraction()

	def update_data(self):

		if self.SND:
			self.data = self.speech.getData()
			print(self.data)

	def storaging(self):
		pass


def main():

	ll = LowerLevel(path = 'Workspace_Understanding/Images/Photo_1.jpeg')
	ll.set_modules(work = True, sound = True)
	ll.launch_wsmodule()
	ll.image_data()
	time.sleep(1)
	ll.launch_sensors()
	time.sleep(2)
	for i in range(10):
		ll.update_data()
		time.sleep(0.1)
		#ll.print_data()
	ll.close_sensors()

A = main()


'''
if __name__ == '__main__':
    ll = LowerLevel(path = 'Images/Photo_1.jpeg')
    ll.set_modules(work = True, sound = True)
    ll.lauch_wsmodule()
    ll.launch_sensors()
    ll.image_data()
    for i in range(4):
    	ll.update_data()
    	ll.print_data()
    	time.sleep(2)
    sm.close_sensors()
    
'''





