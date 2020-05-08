# STEP 0: LIBRARIES IMPORT

import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


# STEP 1: IMPORT DATASET
dataset = pd.read_csv('heart.csv')
dataset.head()
dataset.info()
dataset.keys()


# STEP 3: PREPARE THE DATA FOR TRAINING / DATA CLEANING

 # Divide The Dataset Into Training and Testing Sets #

X = dataset.drop(['target'], axis=1) # drop the target column since it is not needed in the model training
y = dataset['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)  # 70% training and 30% testing


#  STEP 4: MODEL TRAINING
print('the number records in the training set is ', len(X_train))
print('the number records in the testing set is ', len(X_test))


# Logistic Regression
lr_classifier = LogisticRegression()
lr_classifier.fit(X_train, y_train)


# STEP 6: MODEL TESTING
lr_accuracy_train = round(lr_classifier.score(X_train, y_train) * 100, 2)
print('Accuracy in the training set is %', lr_accuracy_train)
lr_accuracy_test = round(lr_classifier.score(X_test, y_test) * 100, 2)
print('Accuracy in the testing set is %', lr_accuracy_test)

# Saving model to disk
pickle.dump(lr_classifier, open('model.pkl', 'wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl', 'rb'))
prediction = model.predict(tst)

if prediction:
    print("The patient has a disease!")
else:
    print("The patient doesn't has a disease!")
