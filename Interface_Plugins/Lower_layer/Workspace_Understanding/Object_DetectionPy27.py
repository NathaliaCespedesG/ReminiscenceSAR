#Object detection and person detection with
#OpenCV and Deep Neural Networks

import cv2
import numpy as np
import threading
import time


class Object_Detection(object):

	def __init__(self, path = 'None'):

		self.photoPath = path

		self.graph = 'C:/Users/Nathalia Cespedes/Desktop/Reminiscence_Interface_Robot/Interface_Plugins/Lower_layer/Workspace_Understanding/models/frozen_inference_graph.pb'
		self.config = 'C:/Users/Nathalia Cespedes/Desktop/Reminiscence_Interface_Robot/Interface_Plugins/Lower_layer/Workspace_Understanding/models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt.txt'
		self.framework = 'TensorFlow'

		self.detected_class = []

		#loadinf COCO class names

		with open('C:/Users/Nathalia Cespedes/Desktop/Reminiscence_Interface_Robot/Interface_Plugins/Lower_layer/Workspace_Understanding/models/object_detection_classes_coco.txt','r') as f:
			self.class_names = f.read().split('\n')

		self.COLORS = np.random.uniform(0, 255, size=(len(self.class_names), 3))

	def loading_model(self):

		# load the DNN model
		model = cv2.dnn.readNet(model = self.graph, config = self.config, framework = self.framework)
		# read the image from disk
		self.image = cv2.imread(self.photoPath)
		self.image_height, self.image_width, _ = self.image.shape
		#Creatinf a blob from image
		blob = cv2.dnn.blobFromImage(image = self.image, size = (300,300), mean = (104,117,123),
									 swapRB = True)
		#Create blob from image
		model.setInput(blob)
		#forwards pass through the model
		self.output = model.forward()

	def detection(self, n):

		num = n

		for detection in self.output[0, 0, :, :]:

			confidence = detection[2]

			if confidence > .4:
				class_id = detection[1]
				class_name = self.class_names[int(class_id)-1]
				color = self.COLORS[int(class_id)]
				box_x = detection[3] * self.image_width
				box_y = detection[4] * self.image_height
				box_width = detection[5] * self.image_width
				box_height = detection[6] * self.image_height
				cv2.rectangle(self.image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), color, thickness=2)
				cv2.putText(self.image, class_name, (int(box_x), int(box_y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
				self.detected_class.append(class_name)

		self.outputImage(num)

	def launch_thread(self):

		self.t = threading.Thread(target = self.detection)
		self.t.start()

	def getData(self):

		return(self.detected_class)

	def outputImage(self, n):

		cv2.imwrite('C:/Users/Nathalia Cespedes/Desktop/Reminiscence_Interface_Robot/' + 'output' + str(n) + '.jpg', self.image)



'''

def main():

    Objects = Object_Detection('Images/Photo_1.jpeg')
    Objects.loading_model()
    Objects.start()
    Objects.detection()
    #m = Objects.getData()
    #print(m)


A = main()


'''