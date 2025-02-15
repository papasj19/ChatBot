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
    def __init__(self, userPhysMet, userWeatherMX, userWeatherMY, userFlag):
        self.userPhysMet = userPhysMet
        self.userWeatherMY = userWeatherMX
        self.userWeatherMX = userWeatherMY
        self.userFlag = userFlag


noEvolutions = {"Magmar", "Electabuzz", "Chansey", "Mr. Mime", "Pinsir"}
weakUgly = {"Ratata", "Oddish", "Abra", "Mankey", "Bulbasaur", "Magikarp"}
weakCute = {"Pichu", "Charmander", "Squirtle", "Dratini", "Growlithe"}
strongPhys = {"Machamp", "Primape", "Dragonite", "Venasaur", "Gyarados", "Arcanine"}
strongSpA = {"Alakazam", "Charizard", "Squirtle", "Pikachu", "Blastoise"}

fireType = {"Charmander", "Charizard", "Magmar", "Growlithe", "Arcanine"}
psyType = {"Alakazam", "Abra", "Chansey", "Mr. Mime"}
dragonType = {"Dratini", "Dragonite"}
fightType = {"Machamp", "Mankey", "Primeape"}
electricType = {"Pikachu", "Pichu", "Electabuzz"}
grassType = {"Oddish", "Pinsir", "Bulbasaur", "Venasaur"}
waterType = {"Squirtle", "Magikarp", "Gyarados", "Blastoise"}

severeWeatherWords = {"thunderstorm", "lightning", "thunder", "storm", "snow", "winter", "yellow"}
warmWeatherWords = {"sun", "beach", "warm", "hot", "sum", "red", "orange", "spicy"}
waterWords = {"boat", "lake", "spring", "rain", "blue", "purple", "swim"}
grassWords = {"autumn", "mess", "dirty", "green", "run", "hike", "brown"}

physicalWords = {"sport", "run", "hike", "weight", "lift", "autumn", "mess", "dirty", "green", "team", "crack", "brok"}
nonPhysWords = {"book", "art", "comput", "game", "clean", "org", "white", "black", "put", "away", "solo", "individ",
                "tidy", "alon", "perfect", "pristine"}

numberQuestions = [
    "How many pets have you had in your life?",
    "How many siblings do you have?"]

wordQuestions = [
    "How would you classify the status of your room?(Is it clean or tidy? or Dirty or messy?",
    "How would you classify the status of your computer screen? (Is it clean or dirty)",
    "How would you classify the status of your phone screen? (Is it clean? Cracked? Perfect?)"
    "What do you like to do in your free time",
    "Would you rather do physical(sports or run) or spiritual(books/art or computer)?",
    "What color is your phone background?",
    "What color is your dream car?",
    "What color is your pet?",
    "What color is your phone?",
    "What colors do you identify with the most?",
    "What are the colors of your parental figures?",
    "What is your favorite season? ",
    "What weather do you like the most?",
    "What was the weather the day you were born?"
]

# physical or nonphysical related
ynQuestionsP = [
    "Do you dislike spicy food?",
    "Is writing a book something you could accomplish right now?",
    "Are you a fast learner?",
    "Are you computer saavy?",
    "Do you enjoy reading?",
    "Is jumping off a roof crazy?",
    "Is ski-ing down a mountain crazy?"
]

# weather related
ynQuestionsW = [
    "Do you like getting caught in the rain?",
    "Do you enjoy listening to thunderstorms?",
    "Do you drink a lot of water?",
    "Do you use a lot of sun screen?",
    "Do you dislike sweating?"
]


def tokenize(sentence):
    tokens = nltk.word_tokenize(sentence)
    return tokens


def stem(words):
    ## we chose lancaster because we liked it more
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
            # increaseWx()
    for guy in waterWords:
        if (w == guy):
            thePerson.userWeatherMY -= 10
            # decreaseWy()
    for guy in grassWords:
        if (w == guy):
            thePerson.userWeatherMY += 10
            # increaseWy()
    for guy in physicalWords:
        if (w == guy):
            thePerson.userPhysMet += 10
            # increaseP()
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
            thePerson.userPhysMet += 10
            # decreaseP()
        elif (w == "N" or w == "n"):
            thePerson.userPhysMet -= 10
            # increaseP()


def checkAsked(rand, asked: list):
    return rand in asked



def proposeQuestion(numNums, numWords, numYNWs, numYNPs, thePerson):
    myNum = random.randint(1, 4)
    total = numWords + numNums + numYNPs + numYNWs
    myWordRand = 0
    YNQPasked = []
    YNPWordRand = 0
    YNQWasked = []
    YNWWorkRand = 0
    wordQasked = []
    userInput = 0
    while (total < 13):

        # word response
        if numWords < 5 and myNum == 1:
            myWordRand = random.randint(0, len(wordQuestions)-1)
            while checkAsked(myWordRand, wordQasked):
                myWordRand = random.randint(1, len(wordQuestions)-1)
            wordQasked.append(myWordRand)
            numWords = numWords + 1
            print("Please respond with normal words")
            print(wordQuestions[myWordRand])
            userInput = input("input: ")
            deconstr = doThings(userInput)
            for guy in deconstr:
                interpretWord(guy, thePerson)
        # number response
        elif (myNum == 2 and numNums < 2):
            print("Please respond with a number")
            if (numNums == 1):  # this is the special question to limit the evolutions
                print(numberQuestions[numNums])
                userInput = input("number: ")
                if (userInput == "0"):
                    thePerson.userFlag = 5
            else:
                print(numberQuestions[numNums])
                userInput = input("number: ")
            numNums = numNums + 1
        elif (myNum == 3 and numYNWs < 3):
            YNWWorkRand = random.randint(0, len(ynQuestionsW)-1)
            while checkAsked(YNWWorkRand, YNQWasked):
                YNWWorkRand = random.randint(1, len(ynQuestionsW)-1)
            YNQWasked.append(YNWWorkRand)
            print("Please respond with a Y|N")
            numYNWs = numYNWs + 1
            print(ynQuestionsW[YNWWorkRand])
            userInput = input("choice: ")
            interpretYN(userInput, 1, thePerson)
        elif (myNum == 4 and numYNPs < 3):
            YNPWordRand = random.randint(0, len(ynQuestionsP)-1)
            while checkAsked(YNPWordRand, YNQPasked):
                YNPWordRand = random.randint(0, len(ynQuestionsP)-1)
            YNQPasked.append(YNPWordRand)
            print("Please respond with a Y|N")
            numYNPs = numYNPs + 1
            print(ynQuestionsP[YNPWordRand])
            userInput = input("choice: ")
            interpretYN(userInput, 2, thePerson)
        total = numWords + numNums + numYNPs + numYNWs
        userInput = 0
        myNum = 0
        myNum = random.randint(1, 4)


def cycleElecSp():
    for el in electricType:
        for sp in strongSpA:
            if (el == sp):
                return el


def cycleElecPhy():
    for el in electricType:
        for sp in strongPhys:
            if (el == sp):
                return el


def cycleFireSp():
    for fi in fireType:
        for sp in strongSpA:
            if (fi == sp):
                return fi


def cycleFirePhy():
    for fi in fireType:
        for sp in strongPhys:
            if (fi == sp):
                return fi


def cycleWaterSp():
    for fi in waterType:
        for sp in strongSpA:
            if (fi == sp):
                return fi


def cycleWaterPhy():
    for fi in waterType:
        for sp in strongPhys:
            if (fi == sp):
                return fi


def cycleGrassPhy():
    for fi in grassType:
        for sp in strongPhys:
            if (fi == sp):
                return fi


def randomDragon():
    return random.choice(list(dragonType))


def randomFight():
    return random.choice(list(fightType))


def randomPsych():
    return random.choice(list(psyType))


def randomWU():
    return random.choice(list(weakUgly))


def randomWC():
    return random.choice(list(weakCute))


def randomNoEv():
    return random.choice(list(noEvolutions))


def determine(mruser, sp, phy):
    if (mruser.userPhysMet > 0):
        print(sp)
    elif (mruser.userPhysMet < 0):
        print(phy)
    elif (mruser.userPhysMet == 0):
        print(randomWC())


def useMetrics(senorUser):
    if (senorUser.userFlag == 5):
        if (senorUser.userWeatherMX < 0):
            for guy in electricType:
                for guytwo in noEvolutions:
                    if (guy == guytwo):
                        print(guy)
        elif (senorUser.userWeatherMX > 0):
            for guy in fireType:
                for guytwo in noEvolutions:
                    if (guy == guytwo):
                        print(guy)
        elif (senorUser.userWeatherMX == 0):
            print(randomNoEv())
    else:
        if (senorUser.userWeatherMX > senorUser.userPhysMet):
            if (senorUser.userWeatherMX < 0):
                if (senorUser.userWeatherMY > 0):
                    print(determine(senorUser, cycleElecSp(), cycleElecPhy()))
                elif (senorUser.userWeatherMY <= 0):
                    print(determine(senorUser, cycleWaterSp(), cycleWaterPhy()))
            elif (senorUser.userWeatherMX > 0):
                if (senorUser.userWeatherMY >= 0):
                    print(determine(senorUser, cycleFireSp(), cycleFirePhy()))
                elif (senorUser.userWeatherMY < 0):
                    print("Venasaur")
            elif (senorUser.userWeatherMX == 0):
                print(randomDragon())
        elif (senorUser.userWeatherMX < senorUser.userPhysMet):
            if (senorUser.userPhysMet >= 10):
                print(randomPsych())
            elif (senorUser.userPhysMet <= -10):
                print(randomFight())
            elif (senorUser.userPhysMet > -11 and senorUser.userPhysMet < 11):
                randomWU()


if __name__ == '__main__':
    numWordQs = 0
    numNumbQs = 0
    numWQs = 0
    numPQs = 0
    thePerson = TheUser(0, 0, 0, 0)

    print("Welcome to the Project\n\tThis will be conducted as a Personality test")
    print("\tYou will be presented with different types of questions and prompted for a response\n")
    proposeQuestion(numNumbQs, numWordQs, numWQs, numPQs, thePerson)
    print("\nThe questions have now completed... Please stand by while we view your results\n")
    print("\nThe pokemon chosen for your journey was chosen to be: ")
    useMetrics(thePerson)






