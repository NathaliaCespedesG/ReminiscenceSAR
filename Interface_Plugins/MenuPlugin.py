#import standart libs
import threading
import time
#import GUI library
from PyQt4 import QtGui, QtCore
import Upper_layer.MenuWindow as MenuWindow

import time
import sys 
import numpy as np 

class MenuPlugin(object):

	def __init__(self):

		self.MenuWindow = MenuWindow.MenuWindow()

		self.set_signals()


	def set_signals(self):

		self.MenuWindow.registerButton(self.onRegister)
		self.MenuWindow.reminiscenceButton(self.onReminiscence)

	def launch_gui(self):
		self.MenuWindow.show()



	def onRegister(self):
		pass


	def onReminiscence(self):

		pass











