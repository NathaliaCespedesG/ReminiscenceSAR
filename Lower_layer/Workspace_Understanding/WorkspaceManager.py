#Importing the workspace understanding 
#libraries 
from . import Color_Detection as Color
from . import Object_Detection as Object
#import Color_Detection as Color
#import Object_Detection as Object

import threading
import time 

class WorkspaceManager(object):

	def __init__(self, imgpath ='None'):


		# Extract Image path to pass both objects

		self.impath = imgpath
		print('WorkspaceManager')
		print(self.impath)

		# Initialize Color_Detection
		self.color = Color.Color_Detection(path = self.impath)

		# Initialize Object Detection
		self.object = Object.Object_Detection(path = self.impath)

		


	def launch_workspace(self):

		#Function to launching the workspace understanding
		#using 

		self.color.process()
		self.color.color_main()
		self.object.loading_model()
		self.object.detection()


	def data_extraction(self):
 
		self.color_data = self.color.getData()
		self.object_data = self.object.getData()
		self.data = {'Color':self.color_data, 'Objects':self.object_data}

		return(self.data)

'''
def main():
	
	Workspace_manager = WorkspaceManager(imgpath = 'Images/Photo_1.jpeg')
	Workspace_manager.launch_workspace()
	Workspace_manager.data_extraction()

a = main()
'''






