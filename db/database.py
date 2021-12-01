# Code to collect users data durinf the therapy with the robot
import os, sys
ab_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../db'))
sys.path.append(ab_path)

import lib.SessionsManager as SM

import shutil


class database(object):

	def __init__(self, ProjectHandler = None):

		#load path
		self.PH = ProjectHandler
		#Creating a general data manager
		self.General = General(ProjectHandler = self.PH)


class General(object):

	def __init__(self, ProjectHandler = None):
		#load project handler
		self.PH = ProjectHandler
		# Update user status
		self.UserStatus = {"name" : "no data", "registered" : False, "id":""}

		#Create session manager

		self.SM = SM.SessionManager(ProjectHandler = self.PH, UserStatus = self.UserStatus)

		self.TherapyStatus = {"user": "none", "mode":0}


	def register(self, user = None):
		#Function to register the patient in the DB
		self.UserStatus = self.SM.register_user(id_number = user['id'],
                                                name      = user['name'],
                                                age       = user['age'],
                                                gender    = user['gender'])

		self.TherapyStatus['user'] = self.UserStatus['name']


	def login(self, i):

		p = {"name"   : "",
			"gender" : "",
			"age"    : "",
			"id"     : i}


		self.SM.set_person(p = p)

		status = self.SM.check_user()

		self.SM.set_User(US = status)

		self.TherapyStatus['user'] = status['name']

		return status


	def clear_database(self):

		folder = self.PH

		if os.path.exists(folder):

			#remove directions

			for f in os.listdir(foler):
				f = os.path.join(folder, f)

				shutil.rmtree(f)

    	#clear users.cvs files

'''
def main():


	ph = 'C:/Users/natha/Desktop/Reminiscence_Interface/db/general'
	G = database(ProjectHandler = ph)

	G.General.SM.register_user(id_number = "1031137220",name ="alfonso casas", age =46, gender= "F")
	G.General.SM.loadEvent(t = "init",c = "none", v = "nd")
	G.General.SM.loadSensor(voice = 75, recog_obj = 3.4)
	G.General.SM.loadSensor(voice = 75, recog_obj = 3.4)
	G.General.SM.loadEvent(t = "end",c = "none", v = "nd")
	G.General.SM.finish_session()


A = main()
'''

