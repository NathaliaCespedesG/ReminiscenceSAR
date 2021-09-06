### Python test for Photo's data extraction
import cv2
import sys 

class WS_Understanding(object):

	def __init__(self):

		#Loading paths from photos
		self.photoPath = "Images/Photo_2.jpeg"
		self.cascPath = "haarcascades/haarcascade_frontalface_default.xml"


	def Create_Cascade(self):
		#Creating the haar cascade
		self.faceCascade = cv2.CascadeClassifier(self.cascPath)
		self.Image_Reading()

	def Image_Reading(self):
		#Reading the image using CV2
		self.image = cv2.imread(self.photoPath)
		self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

	def Face_Detection(self):

		self.faces = self.faceCascade.detectMultiScale(
			self.gray,
			scaleFactor = 1.3,
			minNeighbors = 2,
			minSize = (10,10))

		print("Found {0} faces!".format(len(self.faces)))

		# Draw a rectangle around the faces
		for (x, y, w, h) in self.faces:
			cv2.rectangle(self.image, (x, y), (x+w, y+h), (0, 255, 0), 2)

	def Display_DetectedFaces(self):

		cv2.imshow("Faces foud", self.image)
		cv2.waitKey(0)


def main():

	FaceDetect = WS_Understanding()
	FaceDetect.Create_Cascade()
	FaceDetect.Face_Detection()
	FaceDetect.Display_DetectedFaces()

A = main()
