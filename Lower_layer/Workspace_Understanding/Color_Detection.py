##Color Detectection for ambient
import cv2
import numpy as np

class Color_Detection(object):

	def __init__(self, path = 'None'):

		self.impath = path
		print('path from Color_Detection')
		print(self.impath)
		self.photoPath = cv2.imread(self.impath)
		self.imgHSV = cv2.cvtColor(self.photoPath, cv2.COLOR_BGR2HSV)
		self.environmentType ='None'
		self.imgSize = np.shape(self.imgHSV)[0]*np.shape(self.imgHSV)[1]

	def green_detection(self):

		h_min = 31
		h_max = 99
		s_min = 55
		s_max = 223
		v_min = 0
		v_max = 255

		self.lowerGreen = np.array([h_min,s_min,v_min])
		self.upperGreen = np.array([h_max,s_max,v_max])

		self.maskGreen = cv2.inRange(self.imgHSV, self.lowerGreen, self.upperGreen)
		print(np.shape(self.maskGreen)[0]*np.shape(self.maskGreen)[1])


		self.numGreen = ((self.maskGreen == 255).sum()*100)/self.imgSize

	def blue_detection(self):
		
		h_min = 44
		h_max = 107
		s_min = 84
		s_max = 225
		v_min = 91
		v_max = 255

		self.lowerBlue = np.array([h_min,s_min,v_min])
		self.upperBlue = np.array([h_max,s_max,v_max])

		self.maskBlue = cv2.inRange(self.imgHSV, self.lowerBlue, self.upperBlue)
		self.numBlue = ((self.maskBlue == 255).sum()*100)/self.imgSize

	def red_detection(self):
		
		h_min = 0
		h_max = 28
		s_min = 140
		s_max = 255
		v_min = 0
		v_max = 255

		self.lowerRed = np.array([h_min,s_min,v_min])
		self.upperRed = np.array([h_max,s_max,v_max])

		self.maskRed = cv2.inRange(self.imgHSV, self.lowerRed, self.upperRed)
		self.numRed = ((self.maskRed == 255).sum()*100)/self.imgSize


	def black_detection(self):
		
		h_min = 0
		h_max = 179
		s_min = 0
		s_max = 255
		v_min = 0
		v_max = 34

		self.lowerBlack = np.array([h_min,s_min,v_min])
		self.upperBlack = np.array([h_max,s_max,v_max])

		self.maskBlack = cv2.inRange(self.imgHSV, self.lowerBlack, self.upperBlack)
		self.numBlack = ((self.maskBlack == 255).sum()*100)/self.imgSize


	def gray_detection(self):

		h_min = 6
		h_max = 179
		s_min = 0
		s_max = 90
		v_min = 92
		v_max = 121

		self.lowerGray = np.array([h_min,s_min,v_min])
		self.upperGray = np.array([h_max,s_max,v_max])

		self.maskGray = cv2.inRange(self.imgHSV, self.lowerGray, self.upperGray)
		self.numGray = ((self.maskGray == 255).sum()*100)/self.imgSize

		#cv2.imshow("Mask Gray", self.maskGray)

		#cv2.waitKey(0)


	def white_detection(self):

		h_min = 0
		h_max = 9
		s_min = 0
		s_max = 255
		v_min = 255
		v_max = 255

		self.lowerWhite = np.array([h_min,s_min,v_min])
		self.upperWhite = np.array([h_max,s_max,v_max])

		self.maskWhite = cv2.inRange(self.imgHSV, self.lowerWhite, self.upperWhite)
		self.numWhite = ((self.maskWhite == 255).sum()*100)/self.imgSize



	def process(self):

		self.green_detection()
		self.blue_detection()
		self.red_detection()
		self.black_detection()
		self.gray_detection()
		self.white_detection()

	def color_main(self):

		self.Color = {'Green':self.numGreen, 'Blue':self.numBlue, 'Red':self.numRed, 'Black':self.numBlack, 'Gray':self.numGray, 'White':self.numWhite}
		print(self.Color)
		# Defining Main Color
		values = self.Color.values()
		self.maxVal = max(values)
		#print(self.maxVal)
		self.mainColor = [k for k, v in self.Color.items() if v == self.maxVal]
		#print('Main', self.mainColor)



	def getData(self):

		return(self.mainColor)




'''
def main():

	color = Color_Detection()
	color.process()
	color.color_main()
	data = color.getData()
	print(data)


A = main()
'''