import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

CreditData = pd.read_csv("credit_data/creditset.csv")

features = CreditData[["income", "age", "loan"]]

#targetVariables = CreditData.default
targetVariables = CreditData
featureTrain, featureTest, targetTrain, targetTest= train_test_split(features, targetVariables, test_size=.2)

model = LogisticRegression()
#fittedModel = model.fit(featureTrain, targetTrain)
predictions = fittedModel.predict(featureTest)

print confusion_matrix(targetTest, predictions)
