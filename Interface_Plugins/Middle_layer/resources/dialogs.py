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
        self.choose_photo = "Please choose one"

        self.commenting_photo = " you have chose a great image!"
        self.analizing_photo = "Let me analize the photo, then I will talk with you about it"

        self.oneperson = ["I see XX  person in the photo", "There is one person in the photo", "I can recognize XX person in the photo", "My eyes see XX person in the photo"]
        self.persons = ["I see XX people in the photo", "There are XX people in the photo", "I can recognize XX people in the photo"]
        
        self.whoquestion = ["Are you the person in the photo?", "What is the name of the person in the picture?", "Oh!, that person looks nice, who is it?"]
        self.whoquestions = ["Are you in the photo?", "Can you tell me the names of the people in the photo?", "Oh!, that people look nice, who are they"]


        
        self.conective_dialogueswho1 = ["Seems interesting! Can you tell me more about you?"]
        self.connective_dialogueswhos1 = ["Mmmm, Are they your family or your frieds?", "Mmmm, Is the people in the photo are your relatives?", "Ahhh, I see, Are they your family? "]

        

        self.connective_dialogueswho2 = ["Seems interesting! Can you tell me more about you?"]
        self.connective_dialogueswhos2 = ["Mmmm, Are they your family or your frieds?", "Mmmm, Is the people in the photo are your relatives?", "Mmm"]



        #self.connective_dialogueswho1 = ["Seems interesting! Can you tell me more about the people in the photo"]
        #self.connective_dialogueswho2 = ["I see, is the people in the photo close to you?"]


    def get_person_sentence(self):

        i = random.randint(0, len(self.oneperson) - 1)
        return self.oneperson[i]


    def get_numpersons_sentence(self):

        i = random.randint(0, len(self.persons) - 1)
        return self.persons[i]


    def get_whoquestion(self):

        i = random.randint(0, len(self.whoquestion) - 1)
        return self.whoquestion[i]


    def get_whoquestions(self):

        i = random.randint(0, len(self.whoquestions) - 1)
        return self.whoquestions[i]


    def get_connectiveWho1(self):
        i = random.randint(0, len(self.conective_dialogueswho1) - 1)
        return self.conective_dialogueswho1[i]

    def get_connectiveWhos1(self):
        i = random.randint(0, len(self.connective_dialogueswhos1) - 1)
        return self.connective_dialogueswhos1[i]


    def get_connectiveWho2(self):
        i = random.randint(0, len(self.conective_dialogueswho2) - 1)
        return self.whoquestion[i]

    def get_connectiveWhos2(self):
        i = random.randint(0, len(self.connective_dialogueswhos2) - 1)
        return self.whoquestion[i]








if __name__ == '__main__':
    s = Dialogs()
    s.load_dialogs()

 