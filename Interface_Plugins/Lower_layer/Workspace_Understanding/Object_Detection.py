#Object detection, includig person recognition
#To detect the objects the ImageAI library
#uses DeepLearning 
from imageai.Detection import ObjectDetection
import os
import threading
import time


class Object_Detection(object):

    def __init__(self, path = 'None'):

        self.photoPath = path
        self.modelFile = "C:/Users/natha/Desktop/Reminiscence_Interface/Interface_Plugins/Lower_layer/Workspace_Understanding/Models/resnet50_coco_best_v2.1.0.h5"
        self.execution_path = os.getcwd()
        # Detector Initialization
        self.detector = ObjectDetection()
        self.setting_model()
        #print('Hereeeeeeeeeeeeeeeee')
        #print(self.photoPath)

        self.data = []

    def setting_model(self):

        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath(os.path.join(self.execution_path , self.modelFile))


    def loading_model(self):

        self.detector.loadModel("fast")

    def detection(self):

        #while self.go_On:

        cont = 1

        self.object = []

        self.detections = self.detector.detectObjectsFromImage(input_image= os.path.join(self.execution_path , self.photoPath), output_image_path=os.path.join(self.execution_path , "imagenew.jpg"))

        for eachObject in self.detections:
            #print(eachObject["name"] , " : " , eachObject["percentage_probability"] ) 
            self.object.append(eachObject["name"])
            #print(self.object)
            #print(self.object)



    def launch_thread(self):

        self.t = threading.Thread(target = self.detection)
        self.t.start()



    def start(self):

        self.go_On = True


    def shutdown(self):

        self.go_On = False


    def getData(self):

        return(self.object)




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