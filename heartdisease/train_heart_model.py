#!/usr/bin/env python3 -W ignore
#
# (Aarav Pal, Adah Kapoor, Neel Bansal 2024)

# imports
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#
# Database url: https://archive.ics.uci.edu/dataset/45/heart+disease

# The dataset was downloaded and only "processed.cleveland.data" was used for model training
# There are 303 records with 14 columns including the target label
# the header record was missing, so we added a header record so that we can have the column names in pandas

# The "target" field refers to the presence of heart disease in the patient.  It is integer valued from 0
# (no presence) to 4. Experiments with the Cleveland database have concentrated on simply attempting
# to distinguish presence (values 1,2,3,4) from absence (value 0) -- from heart-disease.names
# The 'uci_heart_mod_binary.csv' is slightly different as I combined 1, 2, 3, and 4 into just 1,
# making it easier for the model.

# read in the data to pandas dataframe
df = pd.read_csv('uci_heart_mod_binary.csv')

# Create the Variables (X) and labels (y) dataframe
y = df['target']
X = df.drop('target', axis=1)


# Create training (X, y) and test (X, y) datasets
# Keeping test as 33% of all the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

# Initialize RandomForest classifier and train it with x_train and y_train
model = RandomForestClassifier(criterion='gini', max_depth=7, min_samples_leaf=5, n_estimators=200)
model.fit(X_train, y_train)


# Performance metrics - train & test
trn_pred = model.predict(X_train)
print("Training accuracy score of the model is:", accuracy_score(y_train, trn_pred) * 100, "%")

tst_pred = model.predict(X_test)
print("Testing accuracy score of the model is:", accuracy_score(y_test, tst_pred) * 100, "%")
