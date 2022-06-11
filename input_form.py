import numpy as np
import pandas as pd
from nltk.stem import WordNetLemmatizer
import os
import re
import nltk
from nltk.corpus import stopwords

def get_all_query(title, text):
    total = title + text
    total = [total]
    return total

def clean_query(sentence):
    sentence = str(sentence)
    print(sentence)
    print(type(sentence))
    stop_words = stopwords.words("english")
    filter_sentence = ""
    lemmatizer      = WordNetLemmatizer()
    sentence        = re.sub(r"[^\w\s]", "", sentence)
    words = nltk.word_tokenize(sentence) #tokenization
    words = [w for w in words if not w in stop_words]
    for word in words:
        filter_sentence = filter_sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()
    return [filter_sentence]
