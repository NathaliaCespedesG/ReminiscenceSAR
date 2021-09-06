import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import ctypes
from time import strftime


class MenuWindow(QtGui.QMainWindow):

	def __init__(self):
		super(MenuWindow, self).__init__()

		#Setting tools
		self.gxlabels = {}

		self.fontlabels = {}

		self.controlButtons = {}


		# Setting the grpahics modules
		self.init_ui()


		# Setting the signales of the GUI
		self.set_signals()

	def init_ui(self):

		#Set window title 
		self.setWindowTitle("Reminisicence Interface")
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
		self.background.setPixmap(QtGui.QPixmap("Upper_layer/ImgGui/black_menu.png"))
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
		icon_hide = QtGui.QPixmap("Upper_layer/ImgGui/hide_main.png")
		icon_hide = icon_hide.scaled(self.winsize_h*0.04,self.winsize_v*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["hide"].setPixmap(icon_hide)

			# Close

		self.gxlabels["close"] = QtGui.QLabel(self)
		self.gxlabels["close"].setGeometry(QtCore.QRect(self.winsize_h*0.95,self.winsize_v*0.04,self.winsize_h*0.04 ,self.winsize_v*0.04))
		icon_close = QtGui.QPixmap("Upper_layer/ImgGui/close_main.png")
		icon_close = icon_close.scaled(self.winsize_h*0.04,self.winsize_v*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["close"].setPixmap(icon_close)


			# Register

		self.gxlabels["register"] = QtGui.QLabel(self)
		self.gxlabels["register"].setGeometry(QtCore.QRect(self.winsize_h*0.22,self.winsize_v*0.35,self.winsize_h*0.17 ,self.winsize_v*0.17))
		icon_register = QtGui.QPixmap("Upper_layer/ImgGui/register_menu.png")
		icon_register = icon_register.scaled(self.winsize_h*0.17,self.winsize_v*0.17,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["register"].setPixmap(icon_register)

		self.fontlabels["register"] = QtGui.QLabel(self)
		self.fontlabels["register"].setText("Register")
		self.fontlabels["register"] .setStyleSheet("color:white;font-size:17px; Sans Serif")
		self.fontlabels["register"] .setGeometry(QtCore.QRect(self.winsize_h*0.24,self.winsize_v*0.5,self.winsize_h*0.3 ,self.winsize_h*0.05))


			# AvatarSett

		self.gxlabels["avatar"] = QtGui.QLabel(self)
		self.gxlabels["avatar"].setGeometry(QtCore.QRect(self.winsize_h*0.45,self.winsize_v*0.35,self.winsize_h*0.17 ,self.winsize_v*0.17))
		icon_avatar = QtGui.QPixmap("Upper_layer/ImgGui/avatar_menu.png")
		icon_avatar = icon_avatar.scaled(self.winsize_h*0.17,self.winsize_v*0.17,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["avatar"].setPixmap(icon_avatar)

		self.fontlabels["avatar"] = QtGui.QLabel(self)
		self.fontlabels["avatar"].setText("Avatar Settings")
		self.fontlabels["avatar"] .setStyleSheet("color:white;font-size:17px; Sans Serif")
		self.fontlabels["avatar"] .setGeometry(QtCore.QRect(self.winsize_h*0.46,self.winsize_v*0.5,self.winsize_h*0.3 ,self.winsize_h*0.05))


			# Statistics

		self.gxlabels["statistics"] = QtGui.QLabel(self)
		self.gxlabels["statistics"].setGeometry(QtCore.QRect(self.winsize_h*0.67,self.winsize_v*0.35,self.winsize_h*0.17 ,self.winsize_v*0.17))
		icon_statis = QtGui.QPixmap("Upper_layer/ImgGui/stati_menu.png")
		icon_statis = icon_statis.scaled(self.winsize_h*0.17,self.winsize_v*0.17,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["statistics"].setPixmap(icon_statis)

		self.fontlabels["statistics"] = QtGui.QLabel(self)
		self.fontlabels["statistics"].setText("Statistics")
		self.fontlabels["statistics"] .setStyleSheet("color:white;font-size:17px; Sans Serif")
		self.fontlabels["statistics"] .setGeometry(QtCore.QRect(self.winsize_h*0.69,self.winsize_v*0.5,self.winsize_h*0.3 ,self.winsize_h*0.05))


			# Database

		self.gxlabels["db"] = QtGui.QLabel(self)
		self.gxlabels["db"].setGeometry(QtCore.QRect(self.winsize_h*0.32,self.winsize_v*0.60,self.winsize_h*0.17 ,self.winsize_v*0.17))
		icon_db = QtGui.QPixmap("Upper_layer/ImgGui/db_menu.png")
		icon_db = icon_db.scaled(self.winsize_h*0.17,self.winsize_v*0.17,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["db"].setPixmap(icon_db)

		self.fontlabels["db"] = QtGui.QLabel(self)
		self.fontlabels["db"].setText("Database")
		self.fontlabels["db"] .setStyleSheet("color:white;font-size:17px; Sans Serif")
		self.fontlabels["db"] .setGeometry(QtCore.QRect(self.winsize_h*0.34,self.winsize_v*0.75,self.winsize_h*0.3 ,self.winsize_h*0.05))


			#Reminiscence

		self.gxlabels["rem"] = QtGui.QLabel(self)
		self.gxlabels["rem"].setGeometry(QtCore.QRect(self.winsize_h*0.58,self.winsize_v*0.60,self.winsize_h*0.17 ,self.winsize_v*0.17))
		icon_r = QtGui.QPixmap("Upper_layer/ImgGui/rem_menu.png")
		icon_r = icon_r.scaled(self.winsize_h*0.17,self.winsize_v*0.17,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["rem"].setPixmap(icon_r)

		self.fontlabels["rem"] = QtGui.QLabel(self)
		self.fontlabels["rem"].setText("Upper_layer/Reminisicence Session")
		self.fontlabels["rem"] .setStyleSheet("color:white;font-size:17px; Sans Serif")
		self.fontlabels["rem"] .setGeometry(QtCore.QRect(self.winsize_h*0.57,self.winsize_v*0.75,self.winsize_h*0.3 ,self.winsize_h*0.05))


			# Minimenu

		self.gxlabels["mini_re"] = QtGui.QLabel(self)
		self.gxlabels["mini_re"].setGeometry(QtCore.QRect(self.winsize_h*0.1,self.winsize_v*0.88,self.winsize_h*0.08 ,self.winsize_v*0.08))
		icon_register = QtGui.QPixmap("Upper_layer/ImgGui/register_menu.png")
		icon_register = icon_register.scaled(self.winsize_h*0.08,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["mini_re"].setPixmap(icon_register)

		self.gxlabels["mini_sta"] = QtGui.QLabel(self)
		self.gxlabels["mini_sta"].setGeometry(QtCore.QRect(self.winsize_h*0.25,self.winsize_v*0.88,self.winsize_h*0.08 ,self.winsize_v*0.08))
		icon_statis = QtGui.QPixmap("Upper_layer/ImgGui/stati_menu.png")
		icon_statis = icon_statis.scaled(self.winsize_h*0.08,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["mini_sta"].setPixmap(icon_statis)

		self.gxlabels["mini_rem"] = QtGui.QLabel(self)
		self.gxlabels["mini_rem"].setGeometry(QtCore.QRect(self.winsize_h*0.4,self.winsize_v*0.88,self.winsize_h*0.08 ,self.winsize_v*0.08))
		icon_r = QtGui.QPixmap("Upper_layer/ImgGui/rem_menu.png")
		icon_r = icon_r.scaled(self.winsize_h*0.08,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["mini_rem"].setPixmap(icon_r)
		
		self.gxlabels["mini_avatar"] = QtGui.QLabel(self)
		self.gxlabels["mini_avatar"].setGeometry(QtCore.QRect(self.winsize_h*0.55,self.winsize_v*0.88,self.winsize_h*0.08 ,self.winsize_v*0.08))
		icon_avatar = QtGui.QPixmap("Upper_layer/ImgGui/avatar_menu.png")
		icon_avatar = icon_avatar.scaled(self.winsize_h*0.08,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["mini_avatar"].setPixmap(icon_avatar)

		self.gxlabels["mini_db"] = QtGui.QLabel(self)
		self.gxlabels["mini_db"].setGeometry(QtCore.QRect(self.winsize_h*0.7,self.winsize_v*0.88,self.winsize_h*0.08 ,self.winsize_v*0.08))
		icon_db = QtGui.QPixmap("Upper_layer/ImgGui/db_menu.png")
		icon_db = icon_db.scaled(self.winsize_h*0.08,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["mini_db"].setPixmap(icon_db)


		



		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.set_time)
		self.timer.start(1000)

		self.lcd = QtGui.QLCDNumber(self)
		self.lcd.setGeometry(QtCore.QRect(self.winsize_h*0.9,self.winsize_v*0.9,self.winsize_h*0.055,self.winsize_v*0.055))
		self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))
		self.lcd.setDigitCount(8)



		self.gxlabels["mini_sun"] = QtGui.QLabel(self)
		self.gxlabels["mini_sun"].setGeometry(QtCore.QRect(self.winsize_h*0.875,self.winsize_v*0.905,self.winsize_h*0.04,self.winsize_v*0.04))
		icon_sun = QtGui.QPixmap("Upper_layer/ImgGui/sun_main.png")
		icon_sun = icon_sun.scaled(self.winsize_h*0.04,self.winsize_v*0.04,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["mini_sun"].setPixmap(icon_sun)


		# Buttons 

		self.controlButtons["close"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['close'].setIconSize(QSize(0,0))
		self.controlButtons['close'].setGeometry(QtCore.QRect(self.winsize_h*0.945,self.winsize_v*0.04,self.winsize_h*0.035 ,self.winsize_v*0.045))  

		self.controlButtons["hide"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['hide'].setIconSize(QSize(0,0))
		self.controlButtons['hide'].setGeometry(QtCore.QRect(self.winsize_h*0.895,self.winsize_v*0.04,self.winsize_h*0.035 ,self.winsize_v*0.045))

		self.controlButtons["register"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['register'].setIconSize(QSize(0,0))
		self.controlButtons['register'].setGeometry(QtCore.QRect(self.winsize_h*0.215,self.winsize_v*0.345,self.winsize_h*0.11 ,self.winsize_v*0.18))

		self.controlButtons["avatar"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['avatar'].setIconSize(QSize(0,0))
		self.controlButtons['avatar'].setGeometry(QtCore.QRect(self.winsize_h*0.445,self.winsize_v*0.345,self.winsize_h*0.11 ,self.winsize_v*0.18))

		self.controlButtons["statistics"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['statistics'].setIconSize(QSize(0,0))
		self.controlButtons['statistics'].setGeometry(QtCore.QRect(self.winsize_h*0.665,self.winsize_v*0.345,self.winsize_h*0.11 ,self.winsize_v*0.18))

		self.controlButtons["db"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['db'].setIconSize(QSize(0,0))
		self.controlButtons['db'].setGeometry(QtCore.QRect(self.winsize_h*0.315,self.winsize_v*0.595,self.winsize_h*0.11 ,self.winsize_v*0.18))

		self.controlButtons["rem"] =  QtGui.QCommandLinkButton(self)
		self.controlButtons['rem'].setIconSize(QSize(0,0))
		self.controlButtons['rem'].setGeometry(QtCore.QRect(self.winsize_h*0.575,self.winsize_v*0.595,self.winsize_h*0.11 ,self.winsize_v*0.18))


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


		
		

		

		self.closeButton(self.confirm_close)
		self.hideButton()
		self.set_date()
		self.set_time()

		#self.show()

	def set_signals(self):

		pass

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

	def registerButton(self,f):

		print('here')

		self.controlButtons["register"].clicked.connect(f)
		self.controlButtons["mini_re"].clicked.connect(f)

	def avatarButton(self,f):

		self.controlButtons["avatar"].clicked.connect(f)
		self.controlButtons["mini_avatar"].clicked.connect(f)

	def statisticsButton(self,f):

		self.controlButtons["statistics"].clicked.connect(f)
		self.controlButtons["mini_sta"].clicked.connect(f)

	def dbButton(self,f):

		self.controlButtons["db"].clicked.connect(f)
		self.controlButtons["mini_db"].clicked.connect(f)

	def reminiscenceButton(self,f):

		self.controlButtons["rem"].clicked.connect(f)
		self.controlButtons["mini_rem"].clicked.connect(f)

	def set_date(self):

		today = QtCore.QDate.currentDate()
		self.currdate.setText(today.toString())


	def set_time(self):

		self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))


'''
def main():
    app=QtGui.QApplication(sys.argv)
    GUI=MenuWindow()
    sys.exit(app.exec_())
A=main()
'''


