#!/usr/bin/python2.7
import threading
import os
import sys
from PyQt4 import QtCore, QtGui
ab_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Interface_Plugins'))
sys.path.append(ab_path)
from statistics import mean
import Upper_layer.CalibrationWindow as CalibrationWindow
import Lower_layer.User_Understanding.Visual_Engagement as VE
import time


class CalibrationPlugin(object):

	def __init__(self, DataHandler = None):

		# load inf from the database manager

		self.DB = DataHandler

		#loading GUI
		self.CalibrationWindow = CalibrationWindow.CalibrationWindow()
		#self.launchView()

		#loading VE module for calibration
		self.VE = VE.Visual_EngagementTracker(DataHandler = self.DB)
		self.VE.start()

		
		self.calibration_data = 0

		self.gaze_cal = []
		self.headpose_cal = []
		self.data_calibrated = None

		self.set_signals()



	def set_signals(self):
		self.CalibrationWindow.onCalibration_run.connect(self.calibration)
		self.CalibrationWindow.mini_rem(self.get_data)
		#self.CalibrationWindow.calibration(self.CalibrationWindow.onCalibration_run.emit())



	def launchView(self):
		print('Here')

		self.CalibrationWindow.show()
		self.CameraCaptureThread = CameraCaptureThread(interface = self)




	def charging_colour(self):
		self.CalibrationWindow.onCalibration_run.emit()


	def calibration(self):
		print('In calibration')
		#elf.CalibrationWindow.onCalibration_run.emit()

		#self.CalibrationWindow.calibration_charging()
		time.sleep(2)

		self.CameraCaptureThread.start()
		time.sleep(2)

		for x in range(100):
			self.calibration_data = self.VE.get_calibration()
			print('data', self.calibration_data)
			self.gaze_cal.append(self.calibration_data[0])
			self.headpose_cal.append(self.calibration_data[1])

			time.sleep(0.1)


		self.data_calibrated = {'gaze': self.gaze_cal, 'head_pose': self.headpose_cal}

		self.VE.pause()


	def get_data(self):

		m = self.data()
		average_gaze = mean(m['gaze'])
		average_headpose = mean(m['head_pose'])
		print(str(average_gaze)+","+str(average_headpose))



	def data(self):

		return(self.data_calibrated)


	def shutdown(self):

		self.CalibrationWindow.close()



class CameraCaptureThread(QtCore.QThread):

	def __init__(self, parent = None, sample = 0.01, interface = None):
		super(CameraCaptureThread, self).__init__()
		self.on = False
		self.interface = interface

	def run(self):


		self.interface.VE.launch_thread()

	def shutdown(self):

		self.on = False



'''

def main():

	app = QtGui.QApplication(sys.argv)
	a = CalibrationPlugin()
	sys.exit(app.exec_())
	#a.calibration()
	#a.launchView()

A = main()	
'''