import threading 
#import GUI elements
import Interface_Plugins.Upper_layer.MenuWindow as MenuWindow
import Interface_Plugins.Upper_layer.RegisterWindow as RegisterWindow
import Interface_Plugins.Upper_layer.ReminiscenceWindow as ReminiscenceWindow
# import Plugins
import Interface_Plugins.TherapyPlugin as TherapyPlugin
import Interface_Plugins.MenuPlugin as MenuPlugin

from PyQt4 import QtCore, QtGui

import time
import sys

class MainController(object):

	def __init__(self):

		self.ImgPath = 'Workspace_Understanding/Images/Photo_1.jpeg'

		self.MenuWindow = MenuWindow.MenuWindow()

		self.ReminiscenceWindow = ReminiscenceWindow.ReminiscenceWindow()


		self.MenuPlugin = MenuPlugin.MenuPlugin()

		self.TherapyPlugin = TherapyPlugin.TherapyPlugin(settings = self.ImgPath)

		self.set_signals()



	def set_signals(self):

		self.TherapyPlugin.image_processing()

		self.MenuWindow.show()

		self.MenuWindow.reminiscenceButton(self.onLaunch_Therapy)

		self.MenuWindow.reminiscenceButton(self.MenuWindow.hideButton)




	def onLaunch_Therapy(self):

		self.TherapyPlugin.launch_view()


def main():

	app = QtGui.QApplication(sys.argv)
	menu = MainController()
	sys.exit(app.exec_())


A = main()