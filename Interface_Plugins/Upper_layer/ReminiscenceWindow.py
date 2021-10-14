import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import ctypes
from time import strftime
import os
import time

class ReminiscenceWindow(QtGui.QMainWindow):

	#Signals

	onPhoto = QtCore.pyqtSignal()
	onAvatar = QtCore.pyqtSignal()


	def __init__(self):
		super(ReminiscenceWindow, self).__init__()

		#Setting tools
		self.gxlabels = {}

		self.path = "C:/Users/natha/Desktop/Reminiscence_Interface/Interface_Plugins/Lower_layer/Workspace_Understanding/Images"

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


		self.gxlabels["photo1"] = QtGui.QLabel(self)
		self.gxlabels["photo1"].setGeometry(QtCore.QRect(self.winsize_h*0.5,self.winsize_v*0.25,self.winsize_h*0.3 ,self.winsize_v*0.27))
		icon = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/photo_rem.png")
		icon = icon.scaled(self.winsize_h*0.3,self.winsize_v*0.27,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["photo1"].setPixmap(icon)


		self.gxlabels["photo2"] = QtGui.QLabel(self)
		self.gxlabels["photo2"].setGeometry(QtCore.QRect(self.winsize_h*0.75,self.winsize_v*0.25,self.winsize_h*0.3 ,self.winsize_v*0.27))
		icon = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/photo_rem.png")
		icon = icon.scaled(self.winsize_h*0.3,self.winsize_v*0.27,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["photo2"].setPixmap(icon)


		self.gxlabels["photo3"] = QtGui.QLabel(self)
		self.gxlabels["photo3"].setGeometry(QtCore.QRect(self.winsize_h*0.5,self.winsize_v*0.55,self.winsize_h*0.3 ,self.winsize_v*0.27))
		icon = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/photo_rem.png")
		icon = icon.scaled(self.winsize_h*0.3,self.winsize_v*0.27,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["photo3"].setPixmap(icon)


		self.gxlabels["photo4"] = QtGui.QLabel(self)
		self.gxlabels["photo4"].setGeometry(QtCore.QRect(self.winsize_h*0.75,self.winsize_v*0.55,self.winsize_h*0.3 ,self.winsize_v*0.27))
		icon = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/photo_rem.png")
		icon = icon.scaled(self.winsize_h*0.3,self.winsize_v*0.27,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["photo4"].setPixmap(icon)



		self.gxlabels["Agent"] = QtGui.QLabel(self)
		self.gxlabels["Agent"].setGeometry(QtCore.QRect(self.winsize_h*0.15,self.winsize_v*0.2,self.winsize_h*0.6 ,self.winsize_v*0.6))
		Agent = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/VA_3.jpeg")
		Agent = Agent.scaled(self.winsize_h*0.6,self.winsize_v*0.6,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["Agent"].setPixmap(Agent)


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
		self.controlButtons['photo1'].setGeometry(QtCore.QRect(self.winsize_h*0.49,self.winsize_v*0.25,self.winsize_h*0.15 ,self.winsize_v*0.27))
		self.controlButtons['photo1'].hide()

		self.controlButtons["photo2"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['photo2'].setIconSize(QSize(0,0))
		self.controlButtons['photo2'].setGeometry(QtCore.QRect(self.winsize_h*0.74,self.winsize_v*0.25,self.winsize_h*0.15 ,self.winsize_v*0.27))
		self.controlButtons['photo2'].hide()


		self.controlButtons["photo3"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['photo3'].setIconSize(QSize(0,0))
		self.controlButtons['photo3'].setGeometry(QtCore.QRect(self.winsize_h*0.49,self.winsize_v*0.55,self.winsize_h*0.15 ,self.winsize_v*0.27))
		self.controlButtons['photo3'].hide()

		self.controlButtons["photo4"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['photo4'].setIconSize(QSize(0,0))
		self.controlButtons['photo4'].setGeometry(QtCore.QRect(self.winsize_h*0.74,self.winsize_v*0.55,self.winsize_h*0.15 ,self.winsize_v*0.27))
		self.controlButtons['photo4'].hide()



		self.closeButton(self.confirm_close)
		self.hideButton()
		self.set_date()
		self.set_time()

		self.set_internalsignals()
		#self.upload_images()
		#self.photo_buttons()

		#self.show()


	


		
		
	def set_internalsignals(self):

		self.validate_images()
		self.onAvatar.connect(self.virtualAgent_talking)
	

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

		self.controlButtons["upload"].clicked.connect(f)


	def playButton(self,f):

		self.uploadButton()

		self.controlButtons["play"].clicked.connect(f)
		


	def validate_images(self):

		print('Validating_images')

		self.photos = os.listdir(self.path)

		self.icon = QtGui.QPixmap(self.path + "/" + self.photos[2])
		self.icon = self.icon.scaled(self.winsize_h*0.25,self.winsize_v*0.25,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		
		self.icon1 = QtGui.QPixmap(self.path + "/" + self.photos[3])
		self.icon1 = self.icon1.scaled(self.winsize_h*0.25,self.winsize_v*0.25,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		

		self.icon2 = QtGui.QPixmap(self.path + "/" + self.photos[4])
		self.icon2 = self.icon2.scaled(self.winsize_h*0.25,self.winsize_v*0.25,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		

		
		self.icon3 = QtGui.QPixmap(self.path + "/" + self.photos[5])
		#print(icon3.isNull())
		self.icon3 = self.icon3.scaled(self.winsize_h*0.25,self.winsize_v*0.25,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		



		if (self.icon.isNull() or self.icon1.isNull() or self.icon2.isNull() or self.icon3.isNull()) == True:

			self.imageNull = True

			print('Missing Image')

		else:
			print('All images correct')
			self.imageNull = False




	def show_images(self):

		print('In show Images')

		
		self.gxlabels["photo1"].setPixmap(self.icon)
		self.gxlabels["photo2"].setPixmap(self.icon1)
		self.gxlabels["photo3"].setPixmap(self.icon2)
		self.gxlabels["photo4"].setPixmap(self.icon3)

		self.photo_buttons()




	def get_imageNull(self):

		return(self.imageNull) 


	def  photo_buttons(self):

		self.controlButtons['photo1'].show()
		self.controlButtons['photo2'].show()
		self.controlButtons['photo3'].show()
		self.controlButtons['photo4'].show()


		self.controlButtons["photo1"].clicked.connect(lambda: self.hide_images(m=1))
		self.controlButtons["photo2"].clicked.connect(lambda: self.hide_images(m=2))
		self.controlButtons["photo3"].clicked.connect(lambda: self.hide_images(m=3))
		self.controlButtons["photo4"].clicked.connect(lambda: self.hide_images(m=4))

	def set_pathPhoto1(self,f):

		self.controlButtons["photo1"].clicked.connect(f)

	def set_pathPhoto2(self,f):

		self.controlButtons["photo2"].clicked.connect(f)

	def set_pathPhoto3(self,f):

		self.controlButtons["photo3"].clicked.connect(f)

	def set_pathPhoto4(self,f):

		self.controlButtons["photo4"].clicked.connect(f)
		



	def hide_images(self,m):



		self.controlButtons["upload"].hide()
		self.controlButtons["photo1"].hide()
		self.controlButtons["photo2"].hide()
		self.controlButtons["photo3"].hide()
		self.controlButtons["photo4"].hide()
		self.gxlabels["photo1"].hide()
		self.gxlabels["photo2"].hide()
		self.gxlabels["photo3"].hide()
		self.gxlabels["photo4"].hide()

		icon_stop = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/stop_rem.png")
		icon_stop = icon_stop.scaled(self.winsize_h*0.08,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["play"].setPixmap(icon_stop)
	


		if m == 1:
			self.reminiscenceImage = self.path + "/" + self.photos[2]

		elif m == 2:
			self.reminiscenceImage = self.path + "/" + self.photos[3]

		elif m ==3:
			self.reminiscenceImage = self.path + "/" + self.photos[4]

		elif m == 4:
			self.reminiscenceImage = self.path + "/" + self.photos[5]



		self.set_recognImage()

		'''
		self.gxlabels["photomain"] = QtGui.QLabel(self)
		self.gxlabels["photomain"].setGeometry(QtCore.QRect(self.winsize_h*0.52,self.winsize_v*0.17,self.winsize_h*0.6 ,self.winsize_v*0.6))
		#print('aqui', self.reminiscenceImage)
		icon = QtGui.QPixmap(self.reminiscenceImage)
		icon = icon.scaled(self.winsize_h*0.6,self.winsize_v*0.6,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["photomain"].setPixmap(icon)
		self.gxlabels["photomain"].show()
		'''





	def get_path(self):

		#print('GET PAAAAAAAAAAAAAAAATH')

		data = self.reminiscenceImage
		#self.update_data()
		print(data)

	def update_data(self):
		i = self.reminiscenceImage

		return(i)


	def set_recognImage(self):
		self.gxlabels["photomain"] = QtGui.QLabel(self)
		self.gxlabels["photomain"].setGeometry(QtCore.QRect(self.winsize_h*0.52,self.winsize_v*0.17,self.winsize_h*0.6 ,self.winsize_v*0.6))
		#print('aqui', self.reminiscenceImage)
		icon = QtGui.QPixmap('C:/Users/natha/Desktop/Reminiscence_Interface/imagenew.jpg')
		icon = icon.scaled(self.winsize_h*0.6,self.winsize_v*0.6,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["photomain"].setPixmap(icon)
		self.gxlabels["photomain"].show()



	def update_sound(self):

		#self.sound = data

		self.onAvatar.emit()


	def virtualAgent_talking(self):

		

		avatar_speaking = ["Interface_Plugins/Upper_layer/ImgGui/VA.jpeg","Interface_Plugins/Upper_layer/ImgGui/VA_1.jpeg","Interface_Plugins/Upper_layer/ImgGui/VA_2.jpeg",
						   "Interface_Plugins/Upper_layer/ImgGui/VA_3.jpeg","Interface_Plugins/Upper_layer/ImgGui/VA_4.jpeg","Interface_Plugins/Upper_layer/ImgGui/VA_5.jpeg",
						   "Interface_Plugins/Upper_layer/ImgGui/VA_6.jpeg","Interface_Plugins/Upper_layer/ImgGui/VA_1.jpeg","Interface_Plugins/Upper_layer/ImgGui/VA_4.jpeg",
						   "Interface_Plugins/Upper_layer/ImgGui/VA_3.jpeg","Interface_Plugins/Upper_layer/ImgGui/VA_1.jpeg","Interface_Plugins/Upper_layer/ImgGui/VA_2.jpeg"]

		#print('Sound from graphics', self.sound)

		
		if self.contTalking < 100:

			self.contTalking = self.contTalking +1

			if self.cont < 12 :

			
				avatar =  QtGui.QPixmap(avatar_speaking[self.cont])
				avatar = avatar.scaled(self.winsize_h*0.6,self.winsize_v*0.6,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
				self.gxlabels["Agent"].setPixmap(avatar)
				self.gxlabels["Agent"].show()
				self.cont = self.cont +1 

		#elif self.cont == 8:
			#avatar =  QtGui.QPixmap("Upper_layer/ImgGui/VA.jpeg")
			#avatar = avatar.scaled(self.winsize_h*0.6,self.winsize_v*0.6,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
			#self.gxlabels["Agent"].setPixmap(avatar)
			#self.gxlabels["Agent"].show()
			

			else:
				avatar =  QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/VA.jpeg")
				avatar = avatar.scaled(self.winsize_h*0.6,self.winsize_v*0.6,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
				self.gxlabels["Agent"].setPixmap(avatar)
				self.gxlabels["Agent"].show()
				self.cont = 0
		else:

			avatar =  QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/VA_6.jpeg")
			avatar = avatar.scaled(self.winsize_h*0.6,self.winsize_v*0.6,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
			self.gxlabels["Agent"].setPixmap(avatar)
			self.gxlabels["Agent"].show()
			self.cont = 0
			self.contTalking  = 0
			time.sleep(4)

















'''

def main():
    app=QtGui.QApplication(sys.argv)
    GUI=ReminiscenceWindow()
    sys.exit(app.exec_())
A=main()
'''

