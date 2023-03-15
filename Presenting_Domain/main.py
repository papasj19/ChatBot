import nltk
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer, SnowballStemmer
from nltk.corpus import stopwords

import pandas as pd

import sklearn
from sklearn.feature_extraction.text import CountVectorizer

import sklearn
from sklearn import datasets, metrics, feature_extraction
from sklearn.feature_extraction.text import CountVectorizer
import sklearn.manifold
import scipy

import random

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

noEvolutions = {"Magmar", "Electabuzz", "Chansey", "Mr. Mime", "Pinsir"}
weakUgly = {"Ratata", "Oddish", "Abra", "Mankey", "Bulbasaur", "Magikarp"}
weakCute = {"Pichu", "Charmander", "Squirtle", "Dratini"}
strongPhys = {"Machamp", "Primape", "Dragonite", "Venasaur", "Gyarados"}
strongSpA = {"Alakazam", "Charizard", "Squirtle", "Pikachu", "Blastoise"}

fireType = {"Charmander", "Charizard", "Magmar"}
psyType = {"Alakazam", "Abra", "Chansey", "Mr. Mime"}
dragonType = {"Dratini", "Dragonite"}
fightType = {"Machamp", "Mankey", "Primeape"}
electricType = {"Pikachu", "Pichu", "Electabuzz"}
grassType = {"Oddish", "Pinsir", "Bulbasaur", "Venasaur"}
waterType = {"Squirtle", "Magikarp", "Gyarados", "Blastoise"}

severeWeatherWords = {"ThunderStorm", "Lightning", "Thunder", "Storm", "Snow", "Winter", "Yellow"}
warmWeatherWords = {"Sun", "Beach", "Warm", "Hot", "Summer", "Red", "Orange", "Spicy"}
waterWords = {"Boat", "Lake", "Spring", "Rain", "Blue", "Purple", "Swim"}
grassWords = {"Autumn", "Mess", "Dirty", "Green", "Run", "Hike", "Brown"}

physicalWords = {"Sport", "Run", "Hike", "Weight", "Lift", "Autumn", "Mess", "Dirty", "Green", "Team"}
nonPhysWords = {"Book", "Art", "Comput", "Game", "Clean", "Org", "White", "Black", "Put", "Away", "Solo", "Individ"}

noEvolutionsFlag = False

numberQuestions = {
    "How many pets have you had in your life?",
    "How many siblings do you have?"}

wordQuestions = {
    "How would you classify the status of your room?",
    "What do you like to do in your free time",
    "What color is your phone background?",
    "What color is your dream car?",
    "What color is your pet?",
    "What colors do you identify with the most?",
    "What is your favorite season? ",
    "What weather do you like the most? "
}

#physical or non physical related
ynQuestionsP = {
    "Do you dislike spicy food?",
    "Is writing a book something you could accomplish right now?",
    "Are you a fast learner?",
    "Are you computer saavy?",
    "Do you enjoy reading?"
}

#weather related
ynQuestionsW = {
    "Do you like getting caught in the rain?",
    "Do you enjoy listening to thunderstorms?",
    "Do you drink a lot of water?",
    "Do you use a lot of sun screen?",
    "Do you dislike sweating?"
}




def tokenize(sentence):
    tokens = nltk.word_tokenize(sentence)
    return tokens


def stem(words):
    
    ## ****** CODE START ****** we chose lancaster because we liked it more
   
    sentence_stemmedP = []
    sentence_stemmedL = []
    porter = PorterStemmer()
    lancaster = LancasterStemmer()
    for dude in words: 
        sentence_stemmedP.append(porter.stem(dude))
        sentence_stemmedL.append(lancaster.stem(dude))
        
    return sentence_stemmedL


def lemmatize(words):
    
    ## ****** CODE START ******
    lemmatized = []
    lemmatizer = WordNetLemmatizer()
    for word in words:
      lemmatized.append(lemmatizer.lemmatize(word, pos="v"))

    return lemmatized


def filter_stop_words(sentence):
    words = tokenize(sentence)
    stop_words = stopwords.words('english')
    filtered = []
    for word in words:
        if word not in stop_words:
            filtered.append(word)
    return filtered


def doThings(sentence):
    filtered = []
    lemmed = []
    stemmed = []
    filtered = filter_stop_words(sentence)
    lemmed = lemmatize(filtered) #we are not using because it trimmed the word too much
    stemmed = stem(filtered)
    return stemmed

def processInfo(info): 
    processedInfo = []

    return processedInfo

def interpretWord(w, metricPhy, metricWx, metricWy):
    for guy in severeWeatherWords:
        if(w == guy):
            metricWx = metricWx - 10
    for guy in warmWeatherWords:
        if(w == guy):
            metricWx = metricWx + 10
    for guy in waterWords:
        if(w == guy):
            metricWy = metricWy - 10
    for guy in grassWords:
        if(w == guy):
            metricWy = metricWy + 10
    for guy in physicalWords:
        if(w == guy):
            metricPhy = metricPhy + 10
    for guy in nonPhysWords:
        if(w == guy):
            metricPhy = metricPhy - 10

def interpretYN(w,type,metricPhy, metricWx):
    if(type == 1):
        #weather
        if(w == "Y" | w == "y"):
            metricWx = metricWx - 10
        elif(w == "N" | w == "n"):
            metricWx = metricWx + 10
    elif(type == 2):
        #physicality
        if(w == "Y" | w == "y"):
            metricPhy = metricPhy - 10
        elif(w == "N" | w == "n"):
            metricPhy = metricPhy + 10

    
    
    
def beginProgram():
    print('Welcome to the Project\n\tThis is a personality test, you will be asked a series of questions and you will write your reply')


def proposeQuestion(numNums, numWords, numYNWs, numYNPs, physicalMet, weatherMetx, weatherMety):
    myNum = random.uniform(1,4)
    
    #word response
    if(numWords < 3 & myNum == 1):
        numWords = numWords + 1
        print("Please respond with normal words")
        print(random.choice(list(wordQuestions)))
    #number response
    elif(numNums < 2 & myNum == 2):
        print("Please respond with a number")
        if(numNums == 1):   #this is the special question to limit the evolutions
            print(numberQuestions[1])
            #scan user input for siblings
            userInput = 0 
            if(userInput == 0):
                noEvolutionsFlag = True
        else:
            print(numberQuestions[numNums])
        numNums = numNums + 1  
    elif(numYNWs < 3 & myNum == 3):
        print("Please respond with a Y|N")
        numYNWs = numYNWs + 1
        print(random.choice(list(ynQuestionsW))) 
        #scan user input (remove below line)
        userInput = "N" 
        interpretYN(userInput,1,physicalMet,weatherMetx)
    elif(numYNPs < 3 & myNum == 4):
        print("Please respond with a Y|N")
        numYNPs = numYNPs + 1
        print(random.choice(list(ynQuestionsP)))
        #scan user input (remove below line)
        userInput = "N" 
        interpretYN(userInput,2,physicalMet,weatherMetx)


if __name__ == '__main__':
    numWordQsAsked = 0
    numNumbQsAsked = 0
    numYNWQsAsked = 0
    numYNPQsAsked = 0



    beginProgram()



