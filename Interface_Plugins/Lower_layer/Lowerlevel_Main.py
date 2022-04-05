#!/usr/bin/python2.7
import os, sys
ab_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Lower_layer'))
sys.path.append(ab_path)

from Speech_Understanding import Speech as speech
import Workspace_Understanding.WorkspaceManager as workspace
import threading
import time
import random

class LowerLevel(object):

	def __init__(self, Datahandler = None):


		# Modules setting configuration

		self.DB = Datahandler


		

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
			self.speech = speech.Sound_Detection(Datahandler = self.DB)

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


	def write_audio(self,path):

		self.speech.write_audio(path)




	def print_data(self):

		# Function to print data acquire from sensors
		print("Data from LowerLevel Main:" + str(self.data))

	def image_data(self):

		if self.WS:
			self.img_data = self.workspace.data_extraction()

		return(self.img_data)

	def update_sounddata(self):
		#print('	Updating data from main')

		if self.SND:
			self.sound_data = self.speech.getData()
			#print(self.data)

		return(self.sound_data)

	def storaging(self):
		pass


	def get_data(self, n):


		data = self.workspace.data_extraction()

		persons = data['Objects'].count('person')
		dog = data['Objects'].count('dog')
		cat = data['Objects'].count('cat')
		bird = data['Objects'].count('bird')
		wine_glass = data['Objects'].count('wine glass')
		cup = data['Objects'].count('cup')
		car = data['Objects'].count('car')
		bus = data['Objects'].count('bus')
		book = data['Objects'].count('book')
		fork = data['Objects'].count('fork')
		spoon = data['Objects'].count('spoon')
		knife = data['Objects'].count('knife')
		traffic_light = data['Objects'].count('traffic light')
		stop_sign = data['Objects'].count('stop sign')


		persons1 = data['Objects1'].count('person')
		dog1 = data['Objects1'].count('dog')
		cat1 = data['Objects1'].count('cat')
		bird1 = data['Objects1'].count('bird')
		wine_glass1 = data['Objects1'].count('wine glass')
		cup1 = data['Objects1'].count('cup')
		car1 = data['Objects1'].count('car')
		bus1 = data['Objects1'].count('bus')
		book1 = data['Objects1'].count('book')
		fork1 = data['Objects1'].count('fork')
		spoon1 = data['Objects1'].count('spoon')
		knife1 = data['Objects1'].count('knife')
		traffic_light1 = data['Objects1'].count('traffic light')
		stop_sign1 = data['Objects1'].count('stop sign')



		

		count_data =  {'person': persons,'cat': cat ,'dog': dog,'bird': bird, 'wine glass':wine_glass, 'cup': cup, "car": car, "bus": bus, "book": book,
						'fork': fork, 'spoon': spoon, 'knife': knife, 'traffic light': traffic_light, 'stop sign': stop_sign}


		count_data1 = {'person': persons1,'cat': cat1 ,'dog': dog1,'bird': bird1, 'wine glass':wine_glass1, 'cup': cup1, "car": car1, "bus": bus1, "book": book1,
						'fork': fork1, 'spoon': spoon1, 'knife': knife1, 'traffic light': traffic_light, 'stop sign': stop_sign}

		if n == 1:
			return(count_data)

		elif n == 2:
			return(count_data1)


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



