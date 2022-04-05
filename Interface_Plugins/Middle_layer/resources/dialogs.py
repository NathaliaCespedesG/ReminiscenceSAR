#!/usr/bin/python2.7
import time
import random

class Dialogs(object):

    def __init__(self):

        self.initTime = time.time()

        self.load_dialogs()

    def load_dialogs(self):
        
        print('here')
        self.welcome_sentence = "^start(animations/Stand/Gestures/Hey_6) Hello ^wait(animations/Stand/Gestures/Hey_6), ^start(animations/Stand/Gestures/Me_1)my name is Ava!^wait(animations/Stand/Gestures/Me_1)"
        self.welcome_sentence2 = "^start(animations/Stand/Gestures/Exited_1)It's great to know you ^wait(animations/Stand/Gestures/Exited_1). Today we will talk about you and some of your photos ^start(animations/Stand/Gestures/Enthusiastic_4)"
        self.welcome_sentence3 = "Please push the upload images button, To see what we've got"


        self.image_validationbad = "It seems that your photos are not ^start(animations/Stand/Gestures/No_1) complete ^wait(animations/Stand/Gestures/No_1)"  
        self.image_validationbad1 = "^start(animations/Stand/Gestures/Explain_1) Would you like to continue?, or, Do you want to upload a new image? ^wait(animations/Stand/Gestures/Explain_1)"


        self.image_validationgreat = "^start(animations/Stand/Gestures/Happy_4) Cool !, your photos are great! ^wait(animations/Stand/Gestures/Happy_4)"
        self.image_validationgreat1 = "Let's continue with the reminiscence"
        self.choose_photo = "^start(animations/Stand/Gestures/Choice_1)Please choose one ^wait(animations/Stand/Gestures/Choice_1)"

        self.commenting_photo = " you have chose a great image!"
        self.analizing_photo = "^start(animations/Stand/Gestures/Thinking_1)Let me analize the photo, then I will talk with you about it ^wait(animations/Stand/Gestures/Thinking_1)"


        
        self.conv_beginning = "^start(animations/Stand/Gestures/Explain_10)Please say yes if you want to continue, if you don't please say no ^wait(animations/Stand/Gestures/Explain_10)"
        self.yes_beginning = ["^start(animations/Stand/Gestures/Hysterical_1)That's great, then we can start!^wait(animations/Stand/Gestures/Hysterical_1)", "Cool!, let's talk then", "^start(animations/Stand/Gestures/Hysterical_1)Im happy to hear that you want to talk with me!^wait(animations/Stand/Gestures/Hysterical_1)"] 

        self.oneperson = ["I see XX  person in the photo", "There is one person in the photo", "I can recognize XX person in the photo", "My eyes see XX person in the photo"]
        self.persons = ["I see XX people in the photo", "There are XX people in the photo", "I can recognize XX people in the photo", "My eyes see XX people in the photo"]
        
        self.whoquestion = ["What is the name of the person in the picture?", "Oh!, that person looks nice, can you tell me the name?", "May I have the name of the person in the picture?", "How you call the person in the photo?", "Could I ask the name of the person in the picture?"]
        self.whoquestions = ["Can you tell me the names of the people in the photo?", "Oh!, that people look nice, can you tell me their names?", "May I have the names of the people in the picture", "Could I ask the names of the people in the picture?"]

        
        self.connective_dialogueswho2 = ["Are you the person in the photo?","Who is the person in the photo?"]
        self.connective_dialogueswhos1 = [" Are they your family or your friends?", " Are the people in the photo your relatives?", "Ah I see, Are they your family?", "How do you know them?", "Are the people in the photo your family? ", "How do you meet the people in the photo?"]

        

        self.connective_dialogueswho1 = ["About how old were the person when the photo was taken?", "How old is the person in the photo?"]
        self.connective_dialogueswhos2 = ["Ah, I see, are the people in the photo close to you?", "How do you feel when you are around this people?", "Do you enjoy the company of this people?" ]


        self.connective_dialogueswho3 = ["Is this person close to you?", "Are you close to this person?", "What is your favorite moment with the person in the picture?"]
        self.connective_dialogueswhos3 = ["What is your favorite memory with these people?", "What is the funniest memory with these people?"]



        self.pet_who = ["I can see some animals in the photo", "There is XX dog and SS cat in your photo", "I can recognize XX person in the photo", "How cute, I can see XX dog and SS cat in your photo"]

        self.dog_who = ["Also, I can see one dog in the photo ","Also, I see one dog in the photo, it is beautiful", "Aw, that dog in the picture is super cute"]
        self.dog_whos = "The dogs in the photo are beautiful"
        self.cat_who = "What a beautiful cat"
        self.cat_who = "Those cats are beautiful"

        self.petQ1 = "Are those animals yours?"
        self.dogQ1 = "Is the dog yours?"
        self.dogsQ1 = "Are those dogs yours?"
        self.catQ1 = "Is the cat yours?"
        self.catsQ1 = "Are those cats yours?"

        self.petQ2 = "Do you know the names of the animals in the photo?"
        self.dogQ2 = "What is the name of the dog I recognize in the photo?"
        self.dogsQ2 = "What are the names of the dogs in the photo?"
        self.catQ2 = "What is the name of the cat ?"
        self.catsQ2 = "What are the names of the cats?"


        self.petQ3 = "Are the animals in the photo your favorite?"
        self.dogQ3 = "What is the breed of the dog in the photo?" 
        self.dogsQ3 = "What is the breed of the dogs in the photo?"
        self.catQ3 = "What is the breed of the cat in the photo?"
        self.catsQ3 = "What is the breed of the cats in the photo?"


        self.petQ4 = "What is the breed of your pets?"
        self.dogQ4 = "Is the dog your favorite animal?"
        self.dogsQ4 = "Are the dogs your favorite animal?"
        self.catQ4 = "Is the cat your favorite animal?"
        self.catsQ4 = "Are the cats your favorite animals?"


        self.whenq1 = ["Please tell me when this photo was taken?", "This photo seems a little old. When it was taken?", "Did you remember when this photo was taken? Please tell me!"]

        self.whenq2 = ["Did you enjoy the time when this photo was taken?", "Was a good time when this photo was taken?"]

        self.noanswer = ["That's a shame. Hope you have a good day, see ya!", "Maybe next time we will work together. Bye!", " No problem. See you next time, bye!", "That's a shame. See you around!"]


        self.whereq1 = "It looks like  you were in a food place, I can see some cups and cutlery. Where you were when the photo was taken?"
        self.whereq11 = "I cannot identify well the place, but it seems it is a food place. Where you were in the photo?"
        self.where =  ["Is this a place you visit usually ?", "Have you ever been more times in this place?"]
        self.where1 = ["What's the think you most appreciate about this place?", "Whats your favorite thing about this place?", "Would you plan to visit this place in the future?"]


        self.yes_catch = ["Ohh, I think you say yes but I couldn't hear well. Can you repeat?", "Did you say yes?. My ears are wrong today. Can you repeat?"]
        self.no_catch = ["Ohh, I think you say no but I couldn't hear well. Can you repeat?", "Did you say no?. My ears are wrong today. Can you repeat?"]
        
        self.sorry = ""


    def yes_bsentence(self):

        i = random.randint(0, len(self.yes_beginning) - 1)
        return self.yes_beginning[i]


    def yes_nocatch(self):

        i = random.randint(0, len(self.yes_catch) - 1)
        return self.yes_catch[i]

    def no_nocatch(self):

        i = random.randint(0, len(self.no_catch) - 1)
        return self.no_catch[i]

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
        i = random.randint(0, len(self.connective_dialogueswho1) - 1)
        return self.connective_dialogueswho1[i]

    def get_connectiveWhos1(self):
        i = random.randint(0, len(self.connective_dialogueswhos1) - 1)
        return self.connective_dialogueswhos1[i]


    def get_connectiveWho2(self):
        i = random.randint(0, len(self.connective_dialogueswho2) - 1)
        return self.connective_dialogueswho2[i]

    def get_connectiveWhos2(self):
        i = random.randint(0, len(self.connective_dialogueswhos2) - 1)
        return self.connective_dialogueswhos2[i]

    def get_connectiveWho3(self):
        i = random.randint(0, len(self.connective_dialogueswho3) - 1)
        return self.connective_dialogueswho3[i]

    def get_connectiveWhos3(self):
        i = random.randint(0, len(self.connective_dialogueswhos3) - 1)
        return self.connective_dialogueswhos3[i]


    def get_petWho(self):

        i = random.randint(0, len(self.pet_who) - 1)
        return self.pet_who[i]

    def get_dogWho(self):
        i = random.randint(0, len(self.dog_who) - 1)
        return self.dog_who[i]

    def get_When1(self):

        i = random.randint(0, len(self.whenq1) - 1)
        return self.whenq1[i]


    def get_When2(self):

        i = random.randint(0, len(self.whenq2) - 1)
        return self.whenq2[i]


    def no_begin(self):

        i = random.randint(0, len(self.noanswer) - 1)
        return self.noanswer[i]





    def get_whereq(self):

        i = random.randint(0, len(self.where) - 1)
        return self.where[i]


    def get_where1q(self):

        i = random.randint(0, len(self.where1) - 1)
        return self.where1[i]










if __name__ == '__main__':
    s = Dialogs()
    s.load_dialogs()

 