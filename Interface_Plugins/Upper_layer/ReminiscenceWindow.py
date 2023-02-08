import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import ctypes
from time import strftime
import os
import time
import cv2

class ReminiscenceWindow(QtGui.QMainWindow):

	#Signals

	onPhoto = QtCore.pyqtSignal()
	onAvatar = QtCore.pyqtSignal()
	onPhoto2 = QtCore.pyqtSignal()


	def __init__(self, settings = None):
		super(ReminiscenceWindow, self).__init__()

		#Setting tools
		self.gxlabels = {}


		print('Hereeeeeeeeeeeeeee settings')
		print(settings)
		self.path = settings



		self.fontlabels = {}

		self.controlButtons = {}

		self.reminiscenceImage = None

		self.imageNull = None

		self.rem_path=None

		self.cont = 0

		self.contTalking = 0


		# Setting the grpahics modules
		self.init_ui()


		# Setting the signales of the GUI
		#self.set_signals()

	def init_ui(self):

		#Set window title 
		self.setWindowTitle("Reminisicence Window")
		#Set window size
		self.user32 = ctypes.windll.user32
		self.screensize = self.user32.GetSystemMetrics(0), self.user32.GetSystemMetrics(1)
		# Resize window
		self.winsize_h = int(self.screensize [0])
		self.winsize_v = int(self.screensize[1])
		self.resize(self.winsize_h,self.winsize_v)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		# Setting background image
		self.background = QtGui.QLabel(self)
		self.background.setGeometry(QtCore.QRect(0,0,self.winsize_h,self.winsize_v))
		self.background.setPixmap(QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/black_menu.png"))
		self.background.setScaledContents(True)


		# Graphics Labels

			# Label
		self.gxlabels["date"] = QtGui.QLabel(self)
		self.gxlabels["date"].setGeometry(QtCore.QRect(self.winsize_h*0.03,self.winsize_v*0.08,self.winsize_h*0.5 ,self.winsize_v*0.08))
		icon_date = QtGui.QPixmap("Upper_layer/ImgGui/date_main.png")
		icon_date = icon_date.scaled(self.winsize_h*0.5,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["date"].setPixmap(icon_date)

		self.currdate = QtGui.QLabel(self)
		self.currdate.setGeometry(QtCore.QRect(self.winsize_h*0.05,self.winsize_v*0.07,self.winsize_h*0.15 ,self.winsize_v*0.1))
		self.currdate.setStyleSheet("color:white;font:bold;font-size:14px; Sans Serif")

		# Reniniscence Title

		self.gxlabels["WinName"] = QtGui.QLabel(self)
		self.gxlabels["WinName"].setText("Reminisicence Interface")
		self.gxlabels["WinName"].setStyleSheet("color:white;font:bold;font-size:18px; Sans Serif")
		self.gxlabels["WinName"].setGeometry(QtCore.QRect(self.winsize_h*0.4,self.winsize_v*0.04,self.winsize_h*0.3 ,self.winsize_h*0.05))

			# Hide 

		self.gxlabels["hide"] = QtGui.QLabel(self)
		self.gxlabels["hide"].setGeometry(QtCore.QRect(self.winsize_h*0.9,self.winsize_v*0.04,self.winsize_h*0.04 ,self.winsize_v*0.04))
		icon_hide = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/hide_main.png")
		icon_hide = icon_hide.scaled(self.winsize_h*0.04,self.winsize_v*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["hide"].setPixmap(icon_hide)

			# Close

		self.gxlabels["close"] = QtGui.QLabel(self)
		self.gxlabels["close"].setGeometry(QtCore.QRect(self.winsize_h*0.95,self.winsize_v*0.04,self.winsize_h*0.04 ,self.winsize_v*0.04))
		icon_close = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/close_main.png")
		icon_close = icon_close.scaled(self.winsize_h*0.04,self.winsize_v*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["close"].setPixmap(icon_close)


			#Upload Images

		self.gxlabels["upload"] = QtGui.QLabel(self)
		self.gxlabels["upload"].setGeometry(QtCore.QRect(self.winsize_h*0.07,self.winsize_v*0.89,self.winsize_h*0.15 ,self.winsize_v*0.06))
		icon_upload = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/Upload_rem.png")
		icon_upload = icon_upload.scaled(self.winsize_h*0.15,self.winsize_v*0.06,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["upload"].setPixmap(icon_upload)


			#Play

		self.gxlabels["play"] = QtGui.QLabel(self)
		self.gxlabels["play"].setGeometry(QtCore.QRect(self.winsize_h*0.5,self.winsize_v*0.88,self.winsize_h*0.08 ,self.winsize_v*0.08))
		icon_play = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/Play_rem.png")
		icon_play = icon_play.scaled(self.winsize_h*0.08,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["play"].setPixmap(icon_play)


			#Photos Display 


		self.gxlabels["photo1_b"] = QtGui.QLabel(self)
		self.gxlabels["photo1_b"].setGeometry(QtCore.QRect(self.winsize_h*0.205,self.winsize_v*0.28,self.winsize_h*0.3 ,self.winsize_v*0.45))
		icon = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/photo_rem.png")
		icon = icon.scaled(self.winsize_h*0.3,self.winsize_v*0.45,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["photo1_b"].setPixmap(icon)


		self.gxlabels["photo2_b"] = QtGui.QLabel(self)
		self.gxlabels["photo2_b"].setGeometry(QtCore.QRect(self.winsize_h*0.583,self.winsize_v*0.28,self.winsize_h*0.3 ,self.winsize_v*0.45))
		icon = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/photo_rem.png")
		icon = icon.scaled(self.winsize_h*0.3,self.winsize_v*0.45,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["photo2_b"].setPixmap(icon)



		self.gxlabels["photo1"] = QtGui.QLabel(self)
		self.gxlabels["photo1"].setGeometry(QtCore.QRect(self.winsize_h*0.215,self.winsize_v*0.11,self.winsize_h*0.8 ,self.winsize_v*0.8))
		


		self.gxlabels["photo2"] = QtGui.QLabel(self)
		self.gxlabels["photo2"].setGeometry(QtCore.QRect(self.winsize_h*0.5895,self.winsize_v*0.11,self.winsize_h*0.8 ,self.winsize_v*0.8))



		#self.gxlabels["Agent"] = QtGui.QLabel(self)
		#self.gxlabels["Agent"].setGeometry(QtCore.QRect(self.winsize_h*0.15,self.winsize_v*0.2,self.winsize_h*0.6 ,self.winsize_v*0.6))
		#Agent = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/VA_3.jpeg")
		#Agent = Agent.scaled(self.winsize_h*0.6,self.winsize_v*0.6,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		#self.gxlabels["Agent"].setPixmap(Agent)


			#Time
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.set_time)
		self.timer.start(1000)

		self.lcd = QtGui.QLCDNumber(self)
		self.lcd.setGeometry(QtCore.QRect(self.winsize_h*0.9,self.winsize_v*0.9,self.winsize_h*0.055,self.winsize_v*0.055))
		self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))
		self.lcd.setDigitCount(8)

		self.gxlabels["mini_sun"] = QtGui.QLabel(self)
		self.gxlabels["mini_sun"].setGeometry(QtCore.QRect(self.winsize_h*0.875,self.winsize_v*0.905,self.winsize_h*0.04,self.winsize_v*0.04))
		icon_sun = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/sun_main.png")
		icon_sun = icon_sun.scaled(self.winsize_h*0.04,self.winsize_v*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["mini_sun"].setPixmap(icon_sun)





			#Buttons

		self.controlButtons["close"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['close'].setIconSize(QSize(0,0))
		self.controlButtons['close'].setGeometry(QtCore.QRect(self.winsize_h*0.945,self.winsize_v*0.04,self.winsize_h*0.035 ,self.winsize_v*0.045))  

		self.controlButtons["hide"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['hide'].setIconSize(QSize(0,0))
		self.controlButtons['hide'].setGeometry(QtCore.QRect(self.winsize_h*0.895,self.winsize_v*0.04,self.winsize_h*0.035 ,self.winsize_v*0.045))



		self.controlButtons["play"] = QtGui.QCommandLinkButton(self)
		self.controlButtons['play'].setIconSize(QSize(0,0))
		self.controlButtons['play'].setGeometry(QtCore.QRect(self.winsize_h*0.49,self.winsize_v*0.88,self.winsize_h*0.07 ,self.winsize_v*0.08))




		self.controlButtons["upload"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['upload'].setIconSize(QSize(0,0))
		self.controlButtons['upload'].setGeometry(QtCore.QRect(self.winsize_h*0.065,self.winsize_v*0.88,self.winsize_h*0.12 ,self.winsize_v*0.08))

		self.controlButtons["photo1"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['photo1'].setIconSize(QSize(0,0))
		self.controlButtons['photo1'].setGeometry(QtCore.QRect(self.winsize_h*0.203,self.winsize_v*0.26,self.winsize_h*0.255 ,self.winsize_v*0.48))
		self.controlButtons['photo1'].hide()

		self.controlButtons["photo2"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['photo2'].setIconSize(QSize(0,0))
		self.controlButtons['photo2'].setGeometry(QtCore.QRect(self.winsize_h*0.580,self.winsize_v*0.26,self.winsize_h*0.255 ,self.winsize_v*0.48))
		self.controlButtons['photo2'].hide()



		self.hideButton()
		self.set_date()
		self.set_time()
		self.uploadButton()
		self.set_signals()
		self.validate_images()


	def set_signals(self):

		self.onPhoto2.connect(self.second_time)



	def closeButton(self,f):

		self.controlButtons["close"].clicked.connect(f)

	def confirm_close(self):

		choice = QtGui.QMessageBox.question(self, 'Close?',
                                            "Are you sure you want to close",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
		
		if choice == QtGui.QMessageBox.Yes:
			sys.exit()
		else:
			pass

	
	def hideButton(self):

		self.controlButtons["hide"].clicked.connect(self.showMinimized)

	def set_date(self):

		today = QtCore.QDate.currentDate()
		self.currdate.setText(today.toString())

	def set_time(self):

		self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))


	def uploadButton(self):

		self.controlButtons["upload"].clicked.connect(self.show_images)



	def onUpload(self,f):

		#self.uploadButton()

		self.controlButtons["upload"].clicked.connect(f)


	def playButton(self,f):

		

		self.controlButtons["play"].clicked.connect(f)
		


	def validate_images(self):

		print('Validating_images ---------------')

		self.photos = os.listdir(self.path)
		size = (1280,962)

		img = cv2.imread(self.path + "/" + self.photos[0])
		img = cv2.resize(img, size, interpolation = cv2.INTER_AREA )

		img1 = cv2.imread(self.path + "/" + self.photos[1])
		img1 = cv2.resize(img1, size, interpolation = cv2.INTER_AREA )

		rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		h, w, ch = rgb_image.shape
		bytes_per_line = ch * w

		rgb_image1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
		h1, w1, ch1 = rgb_image1.shape
		bytes_per_line1 = ch1 * w1

		self.icon = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
		self.icon = self.icon.scaled(self.winsize_h*0.78,self.winsize_v*0.3, Qt.KeepAspectRatio)
		self.icon1 = QtGui.QImage(rgb_image1.data, w1, h1, bytes_per_line1, QtGui.QImage.Format_RGB888)
		self.icon1 = self.icon1.scaled(self.winsize_h*0.78,self.winsize_v*0.3, Qt.KeepAspectRatio )



		if (self.icon.isNull() or self.icon1.isNull()) == True:

			self.imageNull = True

			print('Missing Image')

		else:
			print('All images correct')
			self.imageNull = False


		return(self.imageNull)

	def show_images(self):

		print('In show Images')

		
		self.gxlabels["photo1"].setPixmap(QPixmap.fromImage(self.icon))
		self.gxlabels["photo2"].setPixmap(QPixmap.fromImage(self.icon1))

		print('Showiiiiiiing')
		
		self.photo_buttons()

	def  photo_buttons(self):

		self.controlButtons['photo1'].show()
		self.controlButtons['photo2'].show()
	
		self.controlButtons["photo1"].clicked.connect(self.hide_images)
		self.controlButtons["photo2"].clicked.connect(self.hide_images)


	def set_pathPhoto1(self,f):

		self.controlButtons["photo1"].clicked.connect(f)

	def set_pathPhoto2(self,f):

		self.controlButtons["photo2"].clicked.connect(f)


	def hide_images(self):



		self.controlButtons["upload"].hide()

		self.controlButtons["photo1"].hide()
		self.controlButtons["photo2"].hide()
		#self.controlButtons["photo3"].hide()
		#self.controlButtons["photo4"].hide()
		self.gxlabels["photo1_b"].hide()
		self.gxlabels["photo2_b"].hide()
		self.gxlabels["photo1"].hide()
		self.gxlabels["photo2"].hide()

		#self.gxlabels["photo3"].hide()
		#self.gxlabels["photo4"].hide()

		icon_stop = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/stop_rem.png")
		icon_stop = icon_stop.scaled(self.winsize_h*0.08,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["play"].setPixmap(icon_stop)
	

		'''
		if m == 1:
			print('Here 1')
			self.reminiscenceImage = self.path + "/" + self.photos[2]

		elif m == 2:
			print('Here 2')
			self.reminiscenceImage = self.path + "/" + self.photos[3]


		self.set_recognImage()

		self.gxlabels["photomain"] = QtGui.QLabel(self)
		self.gxlabels["photomain"].setGeometry(QtCore.QRect(self.winsize_h*0.52,self.winsize_v*0.17,self.winsize_h*0.6 ,self.winsize_v*0.6))
		#print('aqui', self.reminiscenceImage)
		icon = QtGui.QPixmap(self.reminiscenceImage)
		icon = icon.scaled(self.winsize_h*0.6,self.winsize_v*0.6,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["photomain"].setPixmap(icon)
		self.gxlabels["photomain"].show()
		'''



	def second_time(self):

		#print('Here Second Time')
		self.gxlabels["photomain"].hide()

		self.gxlabels["photo1_b"].show()
		self.gxlabels["photo2_b"].show()
		self.gxlabels["photo1"].show()
		self.gxlabels["photo2"].show()
		self.show_images()




	def get_path(self):

		data = self.reminiscenceImage
		print(data)

	def update_data(self):
		i = self.reminiscenceImage

		return(i)


	def set_recognImage(self, n):


		self.gxlabels["photomain"] = QtGui.QLabel(self)
		self.gxlabels["photomain"].setGeometry(QtCore.QRect(self.winsize_h*0.32,self.winsize_v*0.17,self.winsize_h*0.6 ,self.winsize_v*0.6))
		#print('aqui', self.reminiscenceImage)
		#icon = "None"
		print('Printing N from icon option', n)

		if n == 1:
			icon = QtGui.QPixmap('C:/Users/natha/Desktop/ReminiscenceSAR/output1.jpg')
		elif n ==2:
			icon = QtGui.QPixmap('C:/Users/natha/Desktop/ReminiscenceSAR/output2.jpg')

		icon = icon.scaled(self.winsize_h*0.6,self.winsize_v*0.6,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["photomain"].setPixmap(icon)
		self.gxlabels["photomain"].show()





	

'''

def main():
    app=QtGui.QApplication(sys.argv)
    GUI=ReminiscenceWindow()
    sys.exit(app.exec_())
A=main()
'''

