#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import ast
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import pandas as pd
import nltk, re
from nltk import word_tokenize
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import os
PATH = os.path.abspath(os.path.join(__file__, "../."))

#open stopwords
with open(PATH+"\\"+'dataset\\my_stopwords.txt') as f:
    stopwords = f.read().splitlines()

def cleanText(text):
    text = text.lower()
    text = re.sub('\n', " ", text)
    text = re.sub('-', " ", text)
    text = re.sub("[^a-zA-Z]", " ", str(text))
    text = word_tokenize(text)
    text = [word for word in text if word not in stopwords]
    text = ' '.join(text)
    return text
    