import SpeechAvatar
import threading
import time


class avatarController(object):

	def __init__(self):

		self.t = threading.Thread(target = self.process)

	def launch(self):

		print("Avatar launched from Contoller")

		self.t.start()

	def process(self):

		self.avatar = SpeechAvatar.SpeechAvatar()

		self.avatar.welcome_sentence()
		self.

