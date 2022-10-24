#!/usr/bin/python2.7
import threading
import Upper_layer.CalibrationWindow as CalibrationWindow
import Lower_layer.User_Understanding.Visual_Engagement as VE
import os, sys

class CalibrationPlugin(object):

	def __init__(self, DataHandler):

		# load inf from the database manager

		self.DB = DataHandler

		#loading GUI
		self.CalibrationWindow = CalibrationWindow.CalibrationWindow()



	def set_signals(self):
		self.CalibrationWindow.calibration(self.calibration)


	def launchView(self):

		self.CalibrationWindow.show()


	def calibration(self):

		pass


	def shutdown(self):

		self.CalibrationWindow.close()


class CameraCaptureThread(QTCore.QThread):

	def __init__(self, parent = None, sample = 0.01, interface = None):
		super(CameraCaptureThread, self).__init__()
		self.on = False
		self.interface = interface

	def run(self):

		self.interface.VE.launch_thread()

	def shutdown(self):

		self.on = False

