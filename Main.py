
import os, sys
ab_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Reminiscence_Interface_Robot'))
#print(ab_path)
sys.path.append(ab_path)
import threading 
#import GUI elements
import Interface_Plugins.Upper_layer.MenuWindow as MenuWindow
import Interface_Plugins.Upper_layer.RegisterWindow as RegisterWindow
import Interface_Plugins.Upper_layer.ReminiscenceWindow as ReminiscenceWindow
import Interface_Plugins.Upper_layer.CalibrationWindow as CalibrationWindow
# import Plugins
import Interface_Plugins.TherapyPlugin as TherapyPlugin
import Interface_Plugins.MenuPlugin as MenuPlugin
import Interface_Plugins.RegisterPlugin as RegisterPlugin
import Interface_Plugins.CalibrationPlugin as CalibrationPlugin


from PyQt4 import QtCore, QtGui

import db.database as database

import time
import sys
import os

class MainController(object):

	def __init__(self):


		#Running file path
		self.dir = os.getcwd()
		print(self.dir)
		# Reminiscence Images Path
		self.imgDir = self.dir + '/'+'Interface_Plugins' +'/'+ 'Lower_layer' + '/'+'Workspace_Understanding' + '/'+ 'Images'
		self.database_path = self.dir + '/'+'db'+'/'+'general'

		db = database.database(self.database_path)

		# loading interface windows 

		self.MenuWindow = MenuWindow.MenuWindow()

		self.ReminiscenceWindow = ReminiscenceWindow.ReminiscenceWindow(settings = self.imgDir)

		self.RegisterWindow = RegisterWindow.RegisterWindow()

		self.CalibrationWindow = CalibrationWindow.CalibrationWindow()


		#loading interface plugins



		self.MenuPlugin = MenuPlugin.MenuPlugin()

		self.RegisterPlugin = RegisterPlugin.RegisterPlugin(DataHandler = db) 

		self.TherapyPlugin = TherapyPlugin.TherapyPlugin(settings = self.imgDir, DataHandler = db, path = ab_path)


		self.CalibrationPlugin = CalibrationPlugin.CalibrationPlugin(DataHandler = db)

		self.set_signals()



	def set_signals(self):

		self.TherapyPlugin.image_processing()

		self.MenuWindow.show()

		#Register Logics

		self.MenuWindow.registerButton(self.RegisterWindow.show)

		self.RegisterWindow.registerReminiscence(self.onLaunch_Therapy)

		self.RegisterWindow.registerReminiscence(self.MenuWindow.hideButton)

		self.RegisterWindow.registerButton(self.register_User)

		self.RegisterWindow.statisticsButton(self.CalibrationWindow.show)

		



		#MainMenu Logics

		self.MenuWindow.reminiscenceButton(self.onLaunch_Therapy)

		self.MenuWindow.reminiscenceButton(self.MenuWindow.hideButton)


		# Calibration Logics


		self.CalibrationWindow.reminiscenceButton(self.onLaunch_Therapy)
		self.CalibrationWindow.calibration(self.calibration)
		self.CalibrationWindow.onCalibration_end.connect(self.CalibrationWindow.calibration_charging)




	def calibration(self):

		self.CalibrationPlugin.calibration()
		self.CalibrationWindow.onCalibration_end.emit()



	def register_User(self):

		m = self.RegisterWindow.get_patient_data()

		self.RegisterPlugin.onDataReceived(m)

		self.TherapyPlugin.user_data(m)


	def onLaunch_Therapy(self):

		print('onLaunch_Therapy')

		self.TherapyPlugin.launch_view()

		pass


def main():

	app = QtGui.QApplication(sys.argv)
	menu = MainController()
	sys.exit(app.exec_())


A = main()