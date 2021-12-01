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

        self.petQ2 = "What are your pets' names?"
        self.dogQ2 = "What is the name of your dog?"
        self.dogsQ2 = "What are the names of your dogs?"
        self.catQ2 = "What is the name of your cat ?"
        self.catsQ2 = "What are the names of your cats?"


        self.petQ3 = "How long have you had your pets?"
        self.dogQ3 = "How long have you had your dog?"
        self.dogsQ3 = "How long have you had your dogs?"
        self.catQ3 = "How long have you had your cat?"
        self.catsQ3 = "How long have you had your cats?"


        self.petQ4 = "What is the breed of your pets?"
        self.dogQ4 = "What is the breed of your dog?"
        self.dogsQ4 = "What is the breed of your dogs?"
        self.catQ4 = "What is the breed of your cat?"
        self.catsQ4 = "What is the breed of your cats?"


        self.whenq1 = ["Please tell me when this photo was taken?", "This photo seems a little old. When it was taken?", "Did you remember when this photo was taken? Please tell me!"]

        self.noanswer = ["That's a shame. hope you have a good day", "Maybe next time we willwork together", " No problem. see you next time", "That's a shame. See you around!"]









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


    def no_begin(self):

        i = random.randint(0, len(self.noanswer) - 1)
        return self.noanswer[i]










if __name__ == '__main__':
    s = Dialogs()
    s.load_dialogs()

 