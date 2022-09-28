import cv2
import numpy as np
import dlib


class Visual_EngagementTracker(object):


	def __init__(self, Datahandler):

		self.DB  = Datahandler

		self.cap = cv2.VideoCapture(0)

		self.detector = dlib.get_frontal_face_detector()

		self.predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat') 

		self.gaze_ratio = 0

		self.eye_direction = None


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

	
		height, width, _ = frame.shape
		mask = np.zeros((height,width), np.uint8)

		#cv2.polylines(frame, [left_eye_region], True, 255,2)
		cv2.fillPoly(mask,[left_eye_region], 255)

		eye = cv2.bitwise_and(gray, gray, mask = mask)


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


		while self.go_on:

			_, frame = cap.read()
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			faces = detector(gray)

			for face in faces:

				landmarks = predictor(gray, face)

				#Gaze_detection 

				gaze_ratio_left_eye = get_gazeRatio([36,37,38,39,40,41], landmarks=landmarks)
				gaze_ratio_right_eye = get_gazeRatio([42,43,44,45,46,47], landmarks=landmarks)

				#print(gaze_ratio_left_eye)
				#print(gaze_ratio_right_eye)

				gaze_ratio = float(gaze_ratio_left_eye + gaze_ratio_right_eye)/ float(2)
				print(gaze_ratio)

				if gaze_ratio <= 1:
					eye_direction = 'right'

				elif 1 < gaze_ratio < 1.7:

					eye_direction ='center'

				else:
					eye_direction = 'left'


			

				cv2.putText(frame, eye_direction, (50,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),3)
				#cv2.putText(frame, str(gaze_ratio_left_eye), (50,150), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255),3)


			cv2.imshow("Frame", frame)

			key = cv2.waitKey(1)

			if key == 27:

				break


		cap.release()
		cv2.destroyAllWindows()


	def start(self):

		self.go_on = True


	def pause(self):

		self.go_on = False


	def getData(self):

		pass

	def launch_thread(self):

		self.t = threading.Thread(target = self.process)
		self.t.start()
