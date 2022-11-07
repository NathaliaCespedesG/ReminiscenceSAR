import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import ctypes
import time
from time import strftime


class CalibrationWindow(QtGui.QMainWindow):

	#Signals
	onCalibration_run = QtCore.pyqtSignal()
	onCalibration_end = QtCore.pyqtSignal()

	def __init__(self):
		super(CalibrationWindow, self).__init__()

		#Setting tools
		self.gxlabels = {}

		self.fontlabels = {}

		self.controlButtons = {}

		#Settings the graphics modules
		self.init_ui()



	def init_ui(self):

		#Set window title 
		self.setWindowTitle("Calibration Window")
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
		#"Interface_Plugins/Upper_layer/ImgGui/date_main

		# Label
		self.gxlabels["date"] = QtGui.QLabel(self)
		self.gxlabels["date"].setGeometry(QtCore.QRect(self.winsize_h*0.03,self.winsize_v*0.08,self.winsize_h*0.5 ,self.winsize_v*0.08))
		icon_date = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/date_main.png")
		icon_date = icon_date.scaled(self.winsize_h*0.5,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["date"].setPixmap(icon_date)

		self.currdate = QtGui.QLabel(self)
		self.currdate.setGeometry(QtCore.QRect(self.winsize_h*0.05,self.winsize_v*0.07,self.winsize_h*0.15 ,self.winsize_v*0.1))
		self.currdate.setStyleSheet("color:white;font:bold;font-size:14px; Sans Serif")

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



		# Minimenu

		self.gxlabels["mini_re"] = QtGui.QLabel(self)
		self.gxlabels["mini_re"].setGeometry(QtCore.QRect(self.winsize_h*0.1,self.winsize_v*0.88,self.winsize_h*0.08 ,self.winsize_v*0.08))
		icon_register = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/save_re.png")
		icon_register = icon_register.scaled(self.winsize_h*0.08,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["mini_re"].setPixmap(icon_register)

		self.gxlabels["mini_sta"] = QtGui.QLabel(self)
		self.gxlabels["mini_sta"].setGeometry(QtCore.QRect(self.winsize_h*0.25,self.winsize_v*0.88,self.winsize_h*0.08 ,self.winsize_v*0.08))
		icon_statis = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/stati_menu.png")
		icon_statis = icon_statis.scaled(self.winsize_h*0.08,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["mini_sta"].setPixmap(icon_statis)

		self.gxlabels["mini_rem"] = QtGui.QLabel(self)
		self.gxlabels["mini_rem"].setGeometry(QtCore.QRect(self.winsize_h*0.4,self.winsize_v*0.88,self.winsize_h*0.08 ,self.winsize_v*0.08))
		icon_r = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/rem_menu.png")
		icon_r = icon_r.scaled(self.winsize_h*0.08,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["mini_rem"].setPixmap(icon_r)
		
		self.gxlabels["mini_avatar"] = QtGui.QLabel(self)
		self.gxlabels["mini_avatar"].setGeometry(QtCore.QRect(self.winsize_h*0.55,self.winsize_v*0.88,self.winsize_h*0.08 ,self.winsize_v*0.08))
		icon_avatar = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/avatar_menu.png")
		icon_avatar = icon_avatar.scaled(self.winsize_h*0.08,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["mini_avatar"].setPixmap(icon_avatar)

		self.gxlabels["mini_db"] = QtGui.QLabel(self)
		self.gxlabels["mini_db"].setGeometry(QtCore.QRect(self.winsize_h*0.7,self.winsize_v*0.88,self.winsize_h*0.08 ,self.winsize_v*0.08))
		icon_db = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/db_menu.png")
		icon_db = icon_db.scaled(self.winsize_h*0.08,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["mini_db"].setPixmap(icon_db)

		self.gxlabels["mini_sun"] = QtGui.QLabel(self)
		self.gxlabels["mini_sun"].setGeometry(QtCore.QRect(self.winsize_h*0.875,self.winsize_v*0.905,self.winsize_h*0.04,self.winsize_v*0.04))
		icon_sun = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/sun_main.png")
		icon_sun = icon_sun.scaled(self.winsize_h*0.04,self.winsize_v*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["mini_sun"].setPixmap(icon_sun)


		# Start Calibration labels

		self.gxlabels["calibration"] = QtGui.QLabel(self)
		self.gxlabels["calibration"].setGeometry(QtCore.QRect(self.winsize_h*0.4,self.winsize_v*0.5,self.winsize_h*0.2 ,self.winsize_v*0.1))
		icon_db = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/calibration.png")
		icon_db = icon_db.scaled(self.winsize_h*0.2,self.winsize_v*0.1,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["calibration"].setPixmap(icon_db)


		self.gxlabels["calibration_white"] = QtGui.QLabel(self)
		self.gxlabels["calibration_white"].setGeometry(QtCore.QRect(self.winsize_h*0.7,self.winsize_v*0.7,self.winsize_h*0.15 ,self.winsize_v*0.05))
		icon_db = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/calibration_charg.png")
		icon_db = icon_db.scaled(self.winsize_h*0.15,self.winsize_v*0.05,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["calibration_white"].setPixmap(icon_db)

		



		#Buttons

		self.controlButtons["close"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['close'].setIconSize(QSize(0,0))
		self.controlButtons['close'].setGeometry(QtCore.QRect(self.winsize_h*0.945,self.winsize_v*0.04,self.winsize_h*0.035 ,self.winsize_v*0.045))  

		self.controlButtons["hide"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['hide'].setIconSize(QSize(0,0))
		self.controlButtons['hide'].setGeometry(QtCore.QRect(self.winsize_h*0.895,self.winsize_v*0.04,self.winsize_h*0.035 ,self.winsize_v*0.045))

		# Mini Buttons

		self.controlButtons["mini_re"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['mini_re'].setIconSize(QSize(0,0))
		self.controlButtons['mini_re'].setGeometry(QtCore.QRect(self.winsize_h*0.095,self.winsize_v*0.88,self.winsize_h*0.055 ,self.winsize_v*0.085))

		self.controlButtons["mini_rem"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['mini_rem'].setIconSize(QSize(0,0))
		self.controlButtons['mini_rem'].setGeometry(QtCore.QRect(self.winsize_h*0.395,self.winsize_v*0.88,self.winsize_h*0.055 ,self.winsize_v*0.085))

		self.controlButtons["mini_db"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['mini_db'].setIconSize(QSize(0,0))
		self.controlButtons['mini_db'].setGeometry(QtCore.QRect(self.winsize_h*0.695,self.winsize_v*0.88,self.winsize_h*0.055 ,self.winsize_v*0.085))

		self.controlButtons["mini_sta"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['mini_sta'].setIconSize(QSize(0,0))
		self.controlButtons['mini_sta'].setGeometry(QtCore.QRect(self.winsize_h*0.245,self.winsize_v*0.88,self.winsize_h*0.055 ,self.winsize_v*0.085))

		self.controlButtons["mini_avatar"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['mini_avatar'].setIconSize(QSize(0,0))
		self.controlButtons['mini_avatar'].setGeometry(QtCore.QRect(self.winsize_h*0.545,self.winsize_v*0.88,self.winsize_h*0.055 ,self.winsize_v*0.085))


		self.controlButtons["calibration"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['calibration'].setIconSize(QSize(0,0))
		self.controlButtons['calibration'].setGeometry(QtCore.QRect(self.winsize_h*0.4,self.winsize_v*0.5,self.winsize_h*0.2 ,self.winsize_v*0.1))

		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.set_time)
		self.timer.start(1000)

		self.lcd = QtGui.QLCDNumber(self)
		self.lcd.setGeometry(QtCore.QRect(self.winsize_h*0.9,self.winsize_v*0.9,self.winsize_h*0.055,self.winsize_v*0.055))
		self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))
		self.lcd.setDigitCount(8)


		#self.set_signals()
		self.closeButton(self.confirm_close)
		self.hideButton()
		self.set_date()
		self.set_time()

		#self.show()


	def set_signals(self):
		self.onCalibration_end.connect(self.calibration_charging)
	

	def closeButton(self,f):

		self.controlButtons["close"].clicked.connect(f)


	def statisticsButton(self, f):

		self.controlButtons["mini_sta"].clicked.connect(f)



	def reminiscenceButton(self,f):

		self.controlButtons["mini_rem"].clicked.connect(f)

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

	def calibration(self, f):

		print('calib defined')

		self.controlButtons["calibration"].clicked.connect(f)


	def calibration_charging(self):

		print('cambio a azul')
		self.gxlabels["calibration_blue"] = QtGui.QLabel(self)
		self.gxlabels["calibration_blue"].setGeometry(QtCore.QRect(self.winsize_h*0.7,self.winsize_v*0.7,self.winsize_h*0.15 ,self.winsize_v*0.05))
		icon_db = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/calibration_blue.png")
		icon_db = icon_db.scaled(self.winsize_h*0.15,self.winsize_v*0.05,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["calibration_blue"].setPixmap(icon_db)
		self.gxlabels["calibration_blue"].show()
	






'''
def main():
    app=QtGui.QApplication(sys.argv)
    GUI=CalibrationWindow()
    sys.exit(app.exec_())
A=main()
'''
