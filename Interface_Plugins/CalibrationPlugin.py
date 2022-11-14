#!/usr/bin/python2.7
import threading
import os
import sys
from PyQt4 import QtCore, QtGui
ab_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Interface_Plugins'))
sys.path.append(ab_path)
from statistics import mean
#import Middle_layer.robotController as Robot
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
		#Setting go_on to true
		self.VE.start()
		self.CameraCaptureThread = CameraCaptureThread(interface = self)


		
		self.calibration_data = 0

		self.gaze_cal = []
		self.headpose_cal = []
		self.data_calibrated = None


		self.average_gaze = 0
		self.average_headpose = 0


	def calibration(self):
		print('In calibration')
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
		self.CameraCaptureThread.shutdown()
		#self.CalibrationWindow.onCalibration_end.emit()

		self.get_data()


	def get_data(self):


		m = self.data()
		self.average_gaze = mean(m['gaze'])
		self.average_gaze = "{:.10f}".format(self.average_gaze)
		self.average_headpose = mean(m['head_pose'])
		print(str(self.average_gaze)+","+str(self.average_headpose))
		self.DB.General.SM.loadCalibration(ag = self.average_gaze, hp = self.average_headpose)



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