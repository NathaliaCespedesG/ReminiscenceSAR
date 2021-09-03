#Object detection, includig person recognition
#To detect the objects the ImageAI library
#uses DeepLearning 
from imageai.Detection import ObjectDetection
import os

class Object_Detection(object):

    def __init__(self, path = 'None'):

        self.photoPath = path
        self.modelFile = "Workspace_Understanding/Models/resnet50_coco_best_v2.1.0.h5"
        self.execution_path = os.getcwd()
        # Detector Initialization
        self.detector = ObjectDetection()
        self.setting_model()
        print('Hereeeeeeeeeeeeeeeee')
        print(self.photoPath)

    def setting_model(self):

        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath(os.path.join(self.execution_path , self.modelFile))


    def loading_model(self):

        self.detector.loadModel("fast")

    def detection(self):


        cont = 1

        self.object = []

        self.detections = self.detector.detectObjectsFromImage(input_image= os.path.join(self.execution_path , self.photoPath), output_image_path=os.path.join(self.execution_path , "imagenew.jpg"))

        for eachObject in self.detections:
            print(eachObject["name"] , " : " , eachObject["percentage_probability"] ) 

            self.object.append(eachObject["name"])


    def getData(self):

        return(self.object)






'''
def main():

    Objects = Object_Detection()
    Objects.loading_model()
    Objects.detection()
    data = Objects.getData()
    print(data)


A = main()
'''


