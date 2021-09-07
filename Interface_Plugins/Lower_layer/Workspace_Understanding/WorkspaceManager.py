
#Importing the workspace understanding 
#libraries 

import os, sys
ab_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Workspace_Understanding'))
sys.path.append(ab_path)

import Color_Detection as Color
import Object_Detection as Object


import threading
import time 

class WorkspaceManager(object):

	def __init__(self, imgpath ='None'):


		# Extract Image path to pass both objects

		self.impath = imgpath

		#print('WorkspaceManager')
		#print(self.impath)

		# Initialize Color_Detection
		self.color = Color.Color_Detection(path = self.impath)

		# Initialize Object Detection
		self.object = Object.Object_Detection(path = self.impath)

		self.go_On = None

		


	def launch_workspace(self):


		print('Hereee')
		self.color.process()
		self.color.color_main()
		self.object.loading_model()
		self.object.detection()


	def data_extraction(self):

		
		self.object_data = self.object.getData()
		self.color_data = self.color.getData()
		self.data = {'Color':self.color_data, 'Objects':self.object_data}


		return(self.data)


	def start(self):

		self.go_On = True



	def pause(self):
		self.go_On = False



'''

def main():
	
	Workspace_manager = WorkspaceManager(imgpath = 'Images/dogs.jpg')
	Workspace_manager.launch_workspace()
	m = Workspace_manager.data_extraction()
	print(m)

a = main()

'''





