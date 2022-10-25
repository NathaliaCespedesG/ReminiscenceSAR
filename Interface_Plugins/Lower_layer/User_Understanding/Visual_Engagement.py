import os
import cv2
import numpy as np
import dlib
import sys
import threading
import time







class Visual_EngagementTracker(object):


	def __init__(self, DataHandler = None, pred_path = None):

		self.DB  = DataHandler

		

		self.detector = dlib.get_frontal_face_detector()


		#predictors/shape_predictor_68_face_landmarks.dat

		self.predictor = dlib.shape_predictor('C:/Users/Nathalia Cespedes/Desktop/Reminiscence_Interface_Robot/Interface_Plugins/Lower_layer/User_Understanding/predictors/shape_predictor_68_face_landmarks.dat') 

		self.gaze_ratio = 0

		self.eye_direction = None

		self.gaze = None


		self.gaze_ratio = None

		self.angles = [0] * 4



		print('Primero')


	def get_gazeRatio(self, eye_points, landmarks):

		# Gaze detection
		# Points where the eye region is enclosed
		left_eye_region = np.array([(landmarks.part(eye_points[0]).x, landmarks.part(eye_points[0]).y),
									(landmarks.part(eye_points[1]).x, landmarks.part(eye_points[1]).y),
									(landmarks.part(eye_points[2]).x, landmarks.part(eye_points[2]).y),
									(landmarks.part(eye_points[3]).x, landmarks.part(eye_points[3]).y),
									(landmarks.part(eye_points[4]).x, landmarks.part(eye_points[4]).y),
									(landmarks.part(eye_points[5]).x, landmarks.part(eye_points[5]).y)], np.int32)

		#Drawing a poligon with the array of the points encountered before
		#cv2.polylines(frame, [left_eye_region], True, (0,0,255),2)

	
		height, width, _ = self.frame.shape
		mask = np.zeros((height,width), np.uint8)

		#cv2.polylines(frame, [left_eye_region], True, 255,2)
		cv2.fillPoly(mask,[left_eye_region], 255)

		eye = cv2.bitwise_and(self.gray, self.gray, mask = mask)


		#cv2.imshow('eye', eye)
		#chosing the eye region in the camera frame
		min_x = np.min(left_eye_region[:,0])
		max_x = np.max(left_eye_region[:,0])
		min_y = np.min(left_eye_region[:,1])
		max_y = np.max(left_eye_region[:,1])

		gray_eye = eye[min_y:max_y, min_x:max_x]
		#gray_eye = cv2.cvtColor(eye, cv2.COLOR_BGR2GRAY)
		_, threshold_eye = cv2.threshold(gray_eye,70,255,cv2.THRESH_BINARY)
		height, width = threshold_eye.shape

		leftside_thresh = threshold_eye[0:height, 0:int(width/2)]
		leftside_white = cv2.countNonZero(leftside_thresh)

		rigthside_thresh = threshold_eye[0:height, int(width/2):width]
		rightside_white = cv2.countNonZero(rigthside_thresh)

		try:
			gaze_ratio = float(leftside_white)/float(rightside_white)

		except ZeroDivisionError:

			gaze_ratio = 0

		
		return(gaze_ratio)



	def process(self):

		print('Here in process')


		self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)


		while self.go_on:

			_, self.frame = self.cap.read()
			self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
			faces = self.detector(self.gray)

			model_3D = self.reference_3Dmodel()

			for face in faces:

				landmarks = self.predictor(self.gray, face)

				model_2D = self.reference_2Dmodel(landmarks = landmarks)

				#size of the image
				height, width, channel = self.frame.shape
				#Camera Intrinsic propertis
				fl = width
				cx = height/2
				cy = width/2
				camera_matrix = self.camera_matrix(fl,(cx,cy))

				mdists = np.zeros((4,1), dtype = np.float64)

				#Calculate rotation and translation vector using solvePnD

				success, rotation, translation = cv2.solvePnP(model_3D, model_2D, camera_matrix, mdists)

				#Calculating angle

				rmat, jac = cv2.Rodrigues(rotation)
				self.angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)



				#Gaze_detection 

				gaze_ratio_left_eye = self.get_gazeRatio([36,37,38,39,40,41], landmarks = landmarks)
				gaze_ratio_right_eye = self.get_gazeRatio([42,43,44,45,46,47], landmarks = landmarks)

				#print(gaze_ratio_left_eye)
				#print(gaze_ratio_right_eye)

				self.gaze_ratio = float(gaze_ratio_left_eye + gaze_ratio_right_eye)/ float(2)
				#print(gaze_ratio)

				if self.gaze_ratio <= 1:
					self.eye_direction = 'right'

				elif 1 < self.gaze_ratio < 1.7:

					self.eye_direction ='center'

				else:
					self.eye_direction = 'left'

				#gaze = "Looking: "

				if self.angles[1] < -15:
					self.gaze = "Left"
				elif self.angles[1] > 15:
					self.gaze = "Right"
				else:
					self.gaze = "Forward"


			

				#cv2.putText(self.frame, eye_direction, (50,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),3)

				#cv2.putText(self.frame, gaze, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),3)
				#cv2.putText(frame, str(gaze_ratio_left_eye), (50,150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),3)


			#cv2.imshow("Frame", self.frame)

			#key = cv2.waitKey(1)

			#if key == 27:

				#break


		self.cap.release()
		#cv2.destroyAllWindows()

	def start(self):

		self.go_on = True


	def pause(self):

		self.go_on = False


	def getData(self):

		return [self.gaze, self.eye_direction]


	def get_calibration(self):

		return [self.gaze_ratio, self.angles[1]]


	def camera_matrix(self, fl, center):

		mat = [[fl, 1, center[0]],
				[0, fl, center[1]],
				[0, 0, 1]]

		return np.array(mat, dtype=np.float)

	def reference_3Dmodel(self):

		model = [[0.0, 0.0, 0.0],
				[0.0, -330.0, -65.0],
				[-225.0, 170.0, -135.0],
				[225.0, 170.0, -135.0],
				[-150.0, -150.0, -125.0],
				[150.0, -150.0, -125.0]]

		m = np.array(model, dtype = np.float64)
		return m


	def launch_thread(self):

		self.t = threading.Thread(target = self.process)
		self.t.start()

	def reference_2Dmodel(self, landmarks):

		points = [[landmarks.part(30).x, landmarks.part(30).y],
					[landmarks.part(8).x, landmarks.part(8).y],
					[landmarks.part(36).x, landmarks.part(36).y],
					[landmarks.part(45).x, landmarks.part(45).y],
					[landmarks.part(48).x, landmarks.part(48).y],
					[landmarks.part(54).x, landmarks.part(54).y]]

		return np.array(points, dtype = np.float64)


'''

def main():

	a = Visual_EngagementTracker(DataHandler = None)
	a.start()
	a.launch_thread()
	time.sleep(60)

	for x in range(500):

		data = a.get_calibration()
		print('data', data)
		time.sleep(1)


	a.pause()

A = main()

'''

