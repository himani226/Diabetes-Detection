import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from warnings import simplefilter
import pickle
import os

# importing and cleaning data
data=pd.read_csv("diabetes.csv")
data['Glucose'].fillna(data['Glucose'].median(skipna=True),inplace=True)
data['BloodPressure'].fillna(data['BloodPressure'].median(skipna=True),inplace=True)
data['SkinThickness'].fillna(data['SkinThickness'].median(skipna=True),inplace=True)
data['Insulin'].fillna(data['Insulin'].median(skipna=True),inplace=True)
data['BMI'].fillna(data['BMI'].median(skipna=True),inplace=True)

# Splitting Data
train,test=train_test_split(data,test_size=0.2,random_state=0,stratify=data['Outcome'])
train_X=train[train.columns[:8]]              # Feature Matrix
train_Y=train['Outcome']                      # Target Matrix
test_X=test[train.columns[:8]]
test_Y=test['Outcome']

# Data Scaling
scaler = StandardScaler()
simplefilter('ignore')
X_train_scaled = scaler.fit_transform(train_X)
X_test_scaled = scaler.fit_transform(test_X)



exists = os.path.isfile('model.pkl')
if exists:
    model = pickle.load(open('model.pkl', 'rb'))
else:
    clf = MLPClassifier(activation='relu',random_state=2)
    clf.fit(X_train_scaled, train_Y)

    # store the model
    pickle.dump(clf, open('model.pkl','wb'))
    model = pickle.load(open('model.pkl', 'rb'))