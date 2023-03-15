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


# if you need to download some random lib it is probably here
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('stopwords')

class TheUser:
    def __init__(self, userPhysMet, userWeatherMX, userWeatherMY):
        self.userPhysMet = userPhysMet
        self.userWeatherMY = userWeatherMX
        self.userWeatherMX = userWeatherMY


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

severeWeatherWords = {"thunderstorm", "lightning", "thunder", "storm", "snow", "winter", "yellow"}
warmWeatherWords = {"Sun", "Beach", "Warm", "hot", "sum", "Red", "Orange", "Spicy"}
waterWords = {"Boat", "Lake", "Spring", "Rain", "Blue", "Purple", "Swim"}
grassWords = {"Autumn", "Mess", "Dirty", "Green", "Run", "Hike", "Brown"}

physicalWords = {"Sport", "Run", "Hike", "Weight", "Lift", "Autumn", "Mess", "Dirty", "Green", "Team"}
nonPhysWords = {"Book", "Art", "Comput", "Game", "Clean", "Org", "White", "Black", "Put", "Away", "Solo", "Individ"}

numberQuestions = [
    "How many pets have you had in your life?",
    "How many siblings do you have?"]

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

# physical or non physical related
ynQuestionsP = {
    "Do you dislike spicy food?",
    "Is writing a book something you could accomplish right now?",
    "Are you a fast learner?",
    "Are you computer saavy?",
    "Do you enjoy reading?"
}

# weather related
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
    lemmed = lemmatize(filtered)  # we are not using because it trimmed the word too much
    stemmed = stem(filtered)
    return stemmed


def processInfo(info):
    processedInfo = []

    return processedInfo


def interpretWord(w, thePerson):
    for guy in severeWeatherWords:
        if (w == guy):
            thePerson.userWeatherMX -= 10
            # decreaseWx()
    for guy in warmWeatherWords:
        if (w == guy):
            thePerson.userWeatherMX += 10
            #increaseWx()
    for guy in waterWords:
        if (w == guy):
            thePerson.userWeatherMY -= 10
            #decreaseWy()
    for guy in grassWords:
        if (w == guy):
            thePerson.userWeatherMY += 10
            #increaseWy()
    for guy in physicalWords:
        if (w == guy):
            thePerson.userPhysMet += 10
            #increaseP()
    for guy in nonPhysWords:
        if (w == guy):
            thePerson.userPhysMet -= 10


def interpretYN(w, spin, thePerson):
    if (spin == 1):
        # weather
        if (w == "Y" or w == "y"):
            thePerson.userWeatherMX -= 10
        elif (w == "N" or w == "n"):
            thePerson.userWeatherMX += 10
    elif (spin == 2):
        # physicality
        if (w == "Y" or w == "y"):
            thePerson.userPhysMet -= 10
            #decreaseP()
        elif (w == "N" or w == "n"):
            thePerson.userPhysMet += 10
            #increaseP()


def proposeQuestion(numNums, numWords, numYNWs, numYNPs, thePerson):
    myNum = random.randint(1, 4)
    total = numWords + numNums + numYNPs + numYNWs
    userInput = 0
    noEvolFlag = False
    while (total < 11):

        # word response
        if (numWords < 3 and myNum == 1):
            numWords = numWords + 1
            print("Please respond with normal words")
            print(random.choice(list(wordQuestions)))
            userInput = input("input: ")
            deconstr = doThings(userInput)
            for guy in deconstr:
                interpretWord(guy, thePerson)
        # number response
        elif (numNums < 2 and myNum == 2):
            print("Please respond with a number")
            if (numNums == 1):  # this is the special question to limit the evolutions
                print(numberQuestions[numNums])
                userInput = input("choice: ")
                if (userInput == 0):
                    noEvolutionsFlag = True
            else:
                print(numberQuestions[numNums])
                userInput = input("choice: ")
            numNums = numNums + 1
        elif (numYNWs < 3 and myNum == 3):
            print("Please respond with a Y|N")
            numYNWs = numYNWs + 1
            print(random.choice(list(ynQuestionsW)))
            userInput = input("choice: ")
            interpretYN(userInput, 1, thePerson)
        elif (numYNPs < 3 and myNum == 4):
            print("Please respond with a Y|N")
            numYNPs = numYNPs + 1
            print(random.choice(list(ynQuestionsP)))
            userInput = input("choice: ")
            interpretYN(userInput, 2, thePerson)
        total = numWords + numNums + numYNPs + numYNWs
        userInput = 0
        myNum = 0
        myNum = random.randint(1, 4)
    return noEvolFlag


def useMetrics(senorUser):
    if(senorUser.userWeatherMX < 0):
        print("Water or Electric type")
    elif(senorUser.userWeatherMX > 0):
        print("Fire or Grass")
    elif(senorUser == 0):
        print("More info needed")

    if(senorUser.userPhysMet <= -10):
        print("nerd")
    elif(senorUser.userPhysMet >= 10):
        print("Mahcamp")
    elif(senorUser.userPhysMet >-11 and senorUser.userPhysMet < 11 ):
        print("weak ugly bc im tired")


if __name__ == '__main__':
    numWordQs = 0
    numNumbQs = 0
    numWQs = 0
    numPQs = 0
    noEvolFlag = False
    thePerson = TheUser(0, 0, 0)

    print("Welcome to the Project\n\tThis will be conducted as a Personality test")
    print("\tYou will be presented with different types of questions and prompted for a response\n")
    noEvolFlag = proposeQuestion(numNumbQs, numWordQs, numWQs, numPQs, thePerson)
    print("\nThe questions have now completed... Please stand by while we view your results\n")
    useMetrics(thePerson)






