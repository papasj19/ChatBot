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

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

number_question1 = "How many pets have you had in your life?"

questionA = "How would you classify the status of your room?"
questionB = "What colors do you identify with the most?"
questionC = "What is your favorite season? "


def tokenize(sentence):
    tokens = nltk.word_tokenize(sentence)
    return tokens


def stem(sentence):
    
    ## ****** CODE START ****** we chose lancaster because we liked it more
    words = tokenize(sentence)
    sentence_stemmedP = []
    sentence_stemmedL = []
    porter = PorterStemmer()
    lancaster = LancasterStemmer()
    for dude in words: 
        sentence_stemmedP.append(porter.stem(dude))
        sentence_stemmedL.append(lancaster.stem(dude))
        
    return sentence_stemmedL


def lemmatize(sentence):
    
    ## ****** CODE START ******
    lemmatized = []
    lemmatizer = WordNetLemmatizer()
    words = tokenize(sentence)
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


def fit_vocabulary(data):
    vocabulary = {}

    temp = []
    iter = 0

    for sentence in data:
        temp[iter] = data.split(" ")
        iter += 1
        dudes = stem(sentence)
    return vocabulary
    
    
    
def begin_program():
    print('Welcome to the Project')
    


if __name__ == '__main__':
    begin_program
