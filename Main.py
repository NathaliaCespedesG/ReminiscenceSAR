import Upper_layer.MenuWindow as MenuWindow
import Upper_layer.RegisterWindow as RegisterWindow
import Upper_layer.ReminiscenceWindow as ReminiscenceWindow
import Middle_layer.SpeechAvatar as SpeechAvatar
import Lower_layer.Lowerlevel_Main as Lower_level
import threading
import time
import threading
import sys
from PyQt4 import QtCore, QtGui


class Reminiscence_Therapy(object):

	def __init__(self):

		#Seting Upper, Middle and Lower layers

		self.MenuWindow = MenuWindow.MenuWindow()

		self.RegisterWindow = RegisterWindow.RegisterWindow()

		self.ReminiscenceWindow = ReminiscenceWindow.ReminiscenceWindow()

		self.SpeechAvatar  = SpeechAvatar.Avatar_Speech()

		self.photo = None

		self.set_signals()

	def set_signals(self):

		self.MenuWindow.registerButton(self.RegisterWindow.show)
		self.MenuWindow.reminiscenceButton(self.ReminiscenceWindow.show)
		self.ReminiscenceWindow.playButton(self.SpeechAvatar.welcome_sentence)
		self.ReminiscenceWindow.upload_images(self.image_validation)


	def image_validation(self):

		self.ReminiscenceWindow.show_images()
		m = self.ReminiscenceWindow.get_imageNull()
		if m == True:
			self.SpeechAvatar.image_validation(m)
		else:
			self.SpeechAvatar.image_validation(m)
			self.on_start()

	def on_start(self):

		self.ReminiscenceWindow.photo_buttons()

		self.ReminiscenceWindow.set_Photo1()

		#self. ReminiscenceWindow.set_signals(self.ReminiscenceWindow.get_path)


		#print('start a ')

		#a = self.ReminiscenceWindow.update_data()


		#print(a)


		pass







	#def reminisce_start(self):

		#self.ReminiscenceWindow.playButton(self.SpeechAvatar.welcome_sentence)

		#print(self.ReminiscenceWindow.imageNull)

		#pass







def main():

	app = QtGui.QApplication(sys.argv)
	rem = Reminiscence_Therapy()
	#rem.buttons_menu()
	#rem.reminisce_start()
	sys.exit(app.exec_())

A = main()




'''

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	a = Reminiscence_Therapy()
	sys.exit(app.exec_())

'''


