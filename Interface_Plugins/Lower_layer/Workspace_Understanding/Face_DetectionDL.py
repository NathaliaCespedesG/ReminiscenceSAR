## Face Detection With Deep Learning - MTCNN
# MTCNN: Uses a casca w 3 networks, (0) image pyramid
#(1)First model to identify candidate facial regions
#(2)Second model filters the bounding boxes
#(3)Output Network to propose facial landmarks

from matplotlib import pyplot
from matplotlib.patches import Rectangle
from mtcnn.mtcnn import MTCNN



class Face_Detection(object):
	"""docstring for ClassName"""
	def __init__(self):

		self.photoPath = "Images/Photo_1.jpeg"
		self.pixels = pyplot.imread(self.photoPath)
		print(self.pixels)
		


	def detection_process(self):

		self.detector = MTCNN()
		self.faces = self.detector.detect_faces(self.pixels)

	def draw_boxes(self):

		# load the image
		#self.data = pyplot.imread(self.photoPath)
		# plot the image
		pyplot.imshow(self.pixels)
		pyplot.show()
		# get the context for drawing boxes
		ax = pyplot.gca()
		# plot each box
		for result in self.faces:
			# get coordinates
			x, y, width, height = result['box']
			# create the shape
			rect = Rectangle((x, y), width, height, fill=False, color='red')
			# draw the box
			ax.add_patch(rect)
		# show the plot
		#pyplot.show()

		
		

def main():
	face = Face_Detection()
	face.detection_process()
	face.draw_boxes()

a= main()
