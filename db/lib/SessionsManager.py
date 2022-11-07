import time
import os
import datetime

#Object that manages all the user data

class SessionManager(object):

	def __init__(self, ProjectHandler = None, UserStatus = None):

		#Loading database paths
		self.PH = ProjectHandler
		# Loading User status 
		self.UserStatus = UserStatus
		#current date
		self.date = datetime.datetime.now()

	def loadSensor(self, voice = None, recog_obj = None):

		self.SensorFile = open(self.sensor_name, 'a')

		data = str(voice) + ";" + str(recog_obj) + ";" + str(datetime.datetime.now()) + "\n"
		self.SensorFile.write(data)
		self.SensorFile.close()

	def loadEvent(self, t = "nd", c = "nd", v ="nd"):

		self.EventFile = open(self.event_name, 'a')
		data = str(t)+ ";"+ str(c)+ ";"+ str(v) + ";" + str(datetime.datetime.now()) + "\n"
		self.EventFile.write(data)
		self.EventFile.close()



	def loadCalibration(self, ag = "nd", hp="nd"):

		self.CalibrationFile = open(self.calibration_data, 'a')
		data = str(ag) + ";" + str(hp) + "\n"
		self.CalibrationFile.write(data)
		self.CalibrationFile.close()


	def loadAudioFile(self, f):

		Audio = f


	def set_User(self, US):

		# User status

		self.UserStatus = US

	def create_session(self):

		#Creating the session for each user
		p = self.PH
		#Create folders for each user
		user_folder = p +"/"+str(self.UserStatus['id'])

		if not os.path.exists(user_folder):
			os.makedirs(user_folder)
			self.times_files = open(user_folder+"/times.csv", 'a+')
			self.times_files.write("times")
			self.times_files.close()

		#create folder
		folder = user_folder +"/"+ str(self.date.year) +"-"+ str(self.date.month)+"-"+ str(self.date.day)
		if not os.path.exists(folder):
			os.makedirs(folder)

		#Create sensors and event files
		self.sensor_name = folder + "/Sensors.csv"
		self.event_name = folder + "/Events.csv"
		self.calibration_data = folder + "/Calibration.csv"
		self.SensorFile = open(self.sensor_name, 'w+')
		self.EventFile = open(self.event_name, 'w+')
		self.CalibrationFile = open(self.calibration_data, "w+")
		#Headers on each file
		self.SensorFile.write("Sound_Tag;Objects_Recognized;Timestamp\n")
		self.EventFile.write("Type;Cause;value;Timestamp\n")
		self.CalibrationFile.write("Averge_Gaze; Average_Headpose\n")
		self.SensorFile.close()
		self.EventFile.close()
		self.CalibrationFile.close()


	def finish_session(self):

		#closing files 
		self.SensorFile.close()
		self.EventFile.close()

	def set_person(self, p):
		self.person = p

	def register_user(self, id_number= "nd", age = "nd", gender = "nd", name = "nd"):

		print("Registering")
		self.person = {"name"   : name,
						"gender" : gender,
						"age"    : age,
						"id" : id_number}

		print(self.person)


		self.save_user()
		self.set_User(US = self.UserStatus)
		self.create_session()
		return self.UserStatus

	def save_user(self):

		print('In save_user')

		#Check the user in the database

		self.UserStatus = self.check_user()
		print('UserStatus', self.UserStatus)

		path = self.PH

		if not self.UserStatus['registered']:

			print('Here not registered')

			#path = self.PH

			if os.path.exists(path + "/Users.csv"):

				f = open(path + "/Users.csv", 'a')

				#save new user information

				f.write(self.person['id']          +";"+
                    self.person['name']        +";"+
                    self.person['gender']      +";"+
                    str(self.person['age'])    +'\n'
                    )

		else:
			print('registered')

			f = open(path + "/Users.csv", 'w+')
			f.write("Id;Name;Gender;Age;\n")
			f.close()

			f = open(path + "/Users.csv", 'a')
			#save new user information
			f.write(self.person['id']          +";"+
					self.person['name']        +";"+
					self.person['gender']      +";"+
					str(self.person['age'])    +'\n'
					)
			#close the file
			f.close()


	def check_user(self):

		path = self.PH

		if os.path.exists(path + "/Users.csv"):

			f = open(path + "/Users.csv", 'r')
			lines = f.readlines()
			f.close()
			users = lines[1:]
			#check patient lists
			for p in users:
				pl = p.split(";")
				if pl[0] == self.person['id']:

					#load personf info

					self.person['name']           = pl[1]
					self.person['gender']         = pl[2]
					self.person['age']            = pl[3]
					print("patient already existing in db")
					return {"name" : self.person['name'], "registered" : True, "id" : self.person['id']}

			return{"name" : self.person['name'], "registered" : False, "id" : self.person['id']}

		else:

			f = open(path + "/Users.csv", 'w+')
			f.write("Id;Name;Gender;Age\n")
			f.close()
			return {"name" : self.person['name'], "registered" : False, "id" : self.person['id']}




























