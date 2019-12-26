# -*- coding: utf-8 -*-
"""Titanic_Code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1na1ZtJ5TXJCn4vKht7RkAJw1l3u4LSym
"""

import pandas as pd
import numpy as np

"""### Data Input"""

train_df=pd.read_csv('train.csv')

test_df=pd.read_csv('test.csv')

surv=pd.read_csv('test_survived.csv')

# Adding new features and removing unwanted features

data = [train_df, test_df]
titles = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}

for dataset in data:
    # extract titles
    dataset['Title'] = dataset.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
    # replace titles with a more common title or as Rare
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt', 'Col','Don', 'Dr',\
                                            'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')
    # convert titles into numbers
    dataset['Title'] = dataset['Title'].map(titles)
    # filling NaN with 0, to get safe
    dataset['Title'] = dataset['Title'].fillna(0)
train_df = train_df.drop(['Name'], axis=1)
test_df = test_df.drop(['Name'], axis=1)

import re
deck = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "U": 8}
data = [train_df, test_df]

for dataset in data:
    dataset['Cabin'] = dataset['Cabin'].fillna("U0")
    dataset['Deck'] = dataset['Cabin'].map(lambda x: re.compile("([a-zA-Z]+)").search(x).group())
    dataset['Deck'] = dataset['Deck'].map(deck)
    dataset['Deck'] = dataset['Deck'].fillna(0)
    dataset['Deck'] = dataset['Deck'].astype(int)
# we can now drop the cabin feature
train_df = train_df.drop(['Cabin'], axis=1)
test_df = test_df.drop(['Cabin'], axis=1)

train_df=train_df.drop(['PassengerId'],axis=1)

train_df=train_df.drop(['SibSp'],axis=1)
train_df=train_df.drop(['Parch'],axis=1)
train_df=train_df.drop(['Ticket'],axis=1)
train_df=train_df.drop(['Fare'],axis=1)

test_df=test_df.drop(['SibSp'],axis=1)
test_df=test_df.drop(['Parch'],axis=1)
test_df=test_df.drop(['Ticket'],axis=1)
test_df=test_df.drop(['Fare'],axis=1)





# missing values in Embarked
cv='S'
data=[train_df,test_df]
for i in data:
  i['Embarked']=i['Embarked'].fillna(cv)

#features and test data
features=train_df.iloc[:,1:].values

features_ans=train_df.iloc[:,0].values

test_data=test_df.iloc[:,1:].values
test_ans=surv.iloc[:,1].values

# Filling the missing values in Age feature
from sklearn.preprocessing import Imputer
imp=Imputer(missing_values="NaN",axis=0,strategy='mean')

impute1=imp.fit(features[:,[2]])

# transforming
features[:,[2]]=impute1.transform(features[:,[2]])

impute2=imp.fit(test_data[:,[2]])

#transforming test data
test_data[:,[2]]=impute2.transform(test_data[:,[2]])

# Label Encoder
from sklearn.preprocessing import LabelEncoder

#Encoding Sex feature
le1=LabelEncoder()
le2=LabelEncoder()

features[:,1]=le1.fit_transform(features[:,1])

test_data[:,1]=le2.fit_transform(test_data[:,1])

le3=LabelEncoder()
le4=LabelEncoder()

features[:,3]=le3.fit_transform(features[:,3])

test_data[:,3]=le4.fit_transform(test_data[:,3])

features[:,2]=features[:,2].astype(int)

test_data[:,2]=test_data[:,2].astype(int)

test_data[:,0:10]


from sklearn.ensemble import RandomForestClassifier
random_forest = RandomForestClassifier(n_estimators=100)
random_forest.fit(features, features_ans)

Y_prediction = random_forest.predict(test_data)

random_forest.score(features, features_ans)
acc_random_forest = round(random_forest.score(features, features_ans) * 100, 2)

random_forest.predict([[1,2,27,1,2,1]])

import pickle

filename='final_model.pkl'
pickle.dump(random_forest,open(filename,'wb'))

features

train_df.head(2)
