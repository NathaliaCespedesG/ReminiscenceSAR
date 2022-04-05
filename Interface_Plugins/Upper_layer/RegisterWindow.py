
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import*
from PyQt4.QtGui import*
import ctypes
from time import strftime

class RegisterWindow(QtGui.QMainWindow):

	#signals Register Window

	onEmpty = QtCore.pyqtSignal()
	onData = QtCore.pyqtSignal()
	onAlreadyRegistered = QtCore.pyqtSignal()
	onNotRegistered = QtCore.pyqtSignal()

	def __init__(self):
		super(RegisterWindow, self).__init__()

		#Setting tools
		self.gxlabels = {}

		self.fontlabels = {}

		self.controlButtons = {}

		self.getData = {}



		# Setting the grpahics modules
		self.init_ui()


		# Setting the signales of the GUI
		#self.set_signals()

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
		self.background.setPixmap(QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/black_menu.png"))
		self.background.setScaledContents(True)

		# Graphics Labels

		# Label
		self.gxlabels["date"] = QtGui.QLabel(self)
		self.gxlabels["date"].setGeometry(QtCore.QRect(self.winsize_h*0.03,self.winsize_v*0.08,self.winsize_h*0.5 ,self.winsize_v*0.08))
		icon_date = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/date_main.png")
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


		# Register icon

		self.gxlabels["register"] = QtGui.QLabel(self)
		self.gxlabels["register"].setGeometry(QtCore.QRect(self.winsize_h*0.2,self.winsize_v*0.3,self.winsize_h*0.4 ,self.winsize_v*0.4))
		icon_re = QtGui.QPixmap("Interface_Plugins/Upper_layer/ImgGui/re_rewindow.png")
		icon_re = icon_re.scaled(self.winsize_h*0.4,self.winsize_v*0.4,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["register"].setPixmap(icon_re)

		# Data icons

		self.gxlabels["name"] = QtGui.QLabel(self)
		self.gxlabels["name"].setGeometry(QtCore.QRect(self.winsize_h*0.5,self.winsize_v*0.35,self.winsize_h*0.3 ,self.winsize_v*0.08))
		icon_date = QtGui.QPixmap("Interface_Plugins/ImgGui/date_main.png")
		icon_date = icon_date.scaled(self.winsize_h*0.3,self.winsize_v*0.08,QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
		self.gxlabels["name"].setPixmap(icon_date)

		self.fontlabels["name"] = QtGui.QLabel(self)
		self.fontlabels["name"].setText("Name:")
		self.fontlabels["name"] .setStyleSheet("color:black;font:bold;font-size:18px; Sans Serif")
		self.fontlabels["name"] .setGeometry(QtCore.QRect(self.winsize_h*0.55,self.winsize_v*0.35,self.winsize_h*0.3 ,self.winsize_h*0.05))


		self.gxlabels["age"] = QtGui.QLabel(self)
		self.gxlabels["age"].setGeometry(QtCore.QRect(self.winsize_h*0.5,self.winsize_v*0.45,self.winsize_h*0.3 ,self.winsize_v*0.08))
		self.gxlabels["age"].setPixmap(icon_date)

		self.fontlabels["age"] = QtGui.QLabel(self)
		self.fontlabels["age"].setText("Age:")
		self.fontlabels["age"] .setStyleSheet("color:black;font:bold;font-size:18px; Sans Serif")
		self.fontlabels["age"] .setGeometry(QtCore.QRect(self.winsize_h*0.55,self.winsize_v*0.42,self.winsize_h*0.3 ,self.winsize_h*0.08))

		self.gxlabels["gender"] = QtGui.QLabel(self)
		self.gxlabels["gender"].setGeometry(QtCore.QRect(self.winsize_h*0.5,self.winsize_v*0.55,self.winsize_h*0.3 ,self.winsize_v*0.08))
		self.gxlabels["gender"].setPixmap(icon_date)

		self.fontlabels["gender"] = QtGui.QLabel(self)
		self.fontlabels["gender"].setText("Gender:")
		self.fontlabels["gender"] .setStyleSheet("color:black;font:bold;font-size:18px; Sans Serif")
		self.fontlabels["gender"] .setGeometry(QtCore.QRect(self.winsize_h*0.55,self.winsize_v*0.52,self.winsize_h*0.3 ,self.winsize_h*0.08))

		self.gxlabels["ID"] = QtGui.QLabel(self)
		self.gxlabels["ID"].setGeometry(QtCore.QRect(self.winsize_h*0.5,self.winsize_v*0.65,self.winsize_h*0.3 ,self.winsize_v*0.08))
		self.gxlabels["ID"].setPixmap(icon_date)

		self.fontlabels["gender"] = QtGui.QLabel(self)
		self.fontlabels["gender"].setText("ID:")
		self.fontlabels["gender"] .setStyleSheet("color:black;font:bold;font-size:18px; Sans Serif")
		self.fontlabels["gender"] .setGeometry(QtCore.QRect(self.winsize_h*0.55,self.winsize_v*0.62,self.winsize_h*0.3 ,self.winsize_h*0.08))





		# Buttons 

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

		
		# Edit labels

		self.getData['name'] = QtGui.QLineEdit(self)
		self.getData['name'].setStyleSheet("font-size:18px; Sans Serif")
		self.getData['name'].setGeometry(QtCore.QRect(self.winsize_h*0.65,self.winsize_v*0.353,self.winsize_h*0.2 ,self.winsize_h*0.04))

		self.getData['age'] = QtGui.QLineEdit(self)
		self.getData['age'].setStyleSheet("font-size:18px; Sans Serif")
		self.getData['age'].setGeometry(QtCore.QRect(self.winsize_h*0.65,self.winsize_v*0.453,self.winsize_h*0.2 ,self.winsize_h*0.04))

		self.getData['ID'] = QtGui.QLineEdit(self)
		self.getData['ID'].setStyleSheet("font-size:18px; Sans Serif")
		self.getData['ID'].setGeometry(QtCore.QRect(self.winsize_h*0.65,self.winsize_v*0.653,self.winsize_h*0.2 ,self.winsize_h*0.04))

		self.getData['gender'] = QtGui.QComboBox(self)
		self.getData['gender'].setStyleSheet("font-size:18px; Sans Serif")
		self.getData['gender'].setGeometry(QtCore.QRect(self.winsize_h*0.65,self.winsize_v*0.553,self.winsize_h*0.2 ,self.winsize_h*0.04))
		self.getData['gender'].addItem("M")
		self.getData['gender'].addItem("F")

		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.set_time)
		self.timer.start(1000)

		self.lcd = QtGui.QLCDNumber(self)
		self.lcd.setGeometry(QtCore.QRect(self.winsize_h*0.9,self.winsize_v*0.9,self.winsize_h*0.055,self.winsize_v*0.055))
		self.lcd.display(strftime("%H"+":"+"%M"+":"+"%S"))
		self.lcd.setDigitCount(8)


		self.closeButton(self.confirm_close)
		self.hideButton()
		self.set_date()
		self.set_time()

		#self.show()


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

	def get_patient_data(self):

		name      = str(self.getData['name'].text())
		age       = str(self.getData['age'].text())
		gender    = str(self.getData['gender'].currentText())
		id_number = str(self.getData['ID'].text())

		self.patient = {'name' : name ,'id' : id_number,'age':age,'gender':gender}
		#print('GET', self.patient)
		return self.patient


	def registerButton(self,f):

		self.controlButtons["mini_re"].clicked.connect(f)

	def avatarButton(self,f):

		self.controlButtons["mini_avatar"].clicked.connect(f)

	def statisticsButton(self,f):

		self.controlButtons["mini_sta"].clicked.connect(f)

	def dbButton(self,f):

		self.controlButtons["mini_db"].clicked.connect(f)

	def registerReminiscence(self,f):

		self.controlButtons["mini_rem"].clicked.connect(f)

		print('Register Reminisicence')

	def set_date(self):

		today = QtCore.QDate.currentDate()
		self.currdate.setText(today.toString())



'''
def main():
    app=QtGui.QApplication(sys.argv)
    GUI=RegisterWindow()
    GUI.registerButton(GUI.get_patient_data)
    sys.exit(app.exec_())
A=main()
'''