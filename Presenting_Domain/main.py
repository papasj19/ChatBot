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


def tokenize(sentence):
    tokens = nltk.word_tokenize(sentence)
    return tokens


def stem(sentence):
    words = tokenize(sentence)
    sentence_stemmed = []
    porter = PorterStemmer()
    for word in words:
        sentence_stemmed.append(word.format(word, porter.stem(word)))
    return sentence_stemmed


def lemmatize(sentence):
    lemmatized = []
    lemmatizer = WordNetLemmatizer()
    words = tokenize(sentence)
    for word in words:
        lemmatized.append(word.format(word, lemmatizer.lemmatize(word, pos="v")))
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
