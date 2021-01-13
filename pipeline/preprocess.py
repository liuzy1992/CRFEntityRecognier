#!/usr/bin/env python3

import pandas as pd
import numpy as np
from .sentgetter import SentenceGetter
from sklearn.model_selection import train_test_split

def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]
    
    features = {
        'bias': 1.0, 
        'word.lower()': word.lower(), 
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        'postag': postag,
        'postag[:2]': postag[:2],
    }
    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            '-1:postag': postag1,
            '-1:postag[:2]': postag1[:2],
        })
    else:
        features['BOS'] = True
    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            '+1:postag': postag1,
            '+1:postag[:2]': postag1[:2],
        })
    else:
        features['EOS'] = True

    return features

def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for token, postag, label in sent]

def sent2tokens(sent):
    return [token for token, postag, label in sent]

def preprocess(infile):
    df = pd.read_csv(infile, 
                     sep='\t', 
                     header=0, 
                     encoding='utf-8', 
                     engine='python', 
                     dtype={'Sent_ID': str, 'Word': str, 'POS': str, 'Tag': str})
    
    classes = np.unique(df.Tag.values).tolist()
    eval_classes = classes.copy()
    eval_classes.remove('O')

    getter = SentenceGetter(df)
    sentences = getter.sentences

    x = [sent2features(s) for s in sentences]
    y = [sent2labels(s) for s in sentences]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

    return x_train, x_test, y_train, y_test, eval_classes
