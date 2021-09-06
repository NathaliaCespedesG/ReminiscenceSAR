import time
import random

class Dialogs(object):

    def __init__(self):

        self.initTime = time.time()

        self.load_dialogs()

    def load_dialogs(self):
        
        print('here')
        self.welcome_sentence = "Hello, my name is Ava"
        self.welcome_sentence2 = "It's great to know you. Today we will talk about you and some of your photos"
        self.welcome_sentence3 = "Please push the upload images button, To see what we've got"


        self.image_validationbad = "It seems that your photos are not complete"  
        self.image_validationbad1 = "You want to continue?, or, You want to upload a new image?"


        self.image_validationgreat = "Cool !, your photos are great!"
        self.image_validationgreat1 = "Let's continue with the reminiscence"
        self.choose_photo = "Please choose a photo"

        self.commenting_photo = "Wow!, you have chose a great image."
        self.analizing_photo = "Let me analize the photo, then I will talk with you about this photo"

        self.numpersons = ["I see XX  in the photo", "I recognize XX person in the photo, am I right?"]
        self.whoquestions = "Can you tell me who are they?"
        self.connective_dialogueswho = ["Seems interesting! Can you tell me more", "I see, they are close to you? "]


    def get_numpersons_sentence(self):

        i = random.randint(0, len(self.numpersons) - 1)
        return self.numpersons[i]

    def get_connectivewho(self):

        i = random.randint(0, len(self.connective_dialogueswho) - 1)
        return self.connective_dialogueswho[i]



if __name__ == '__main__':
    s = Dialogs()
    s.load_dialogs()

 