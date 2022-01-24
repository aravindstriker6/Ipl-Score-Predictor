import numpy as np
import pandas as pd
import joblib
from datetime import datetime

data = pd.read_csv('myPreprocessed.csv')
data['start_date'] = data['start_date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
data_coded= pd.get_dummies(data=data, columns=['batting_team','bowling_team','venue'])
data_coded.drop(['striker','non_striker','bowler'],axis=1,inplace=True)



X_train = data_coded.drop(labels='score', axis=1)[(data_coded['start_date'].dt.year >= 2014)&(data_coded['start_date'].dt.year <= 2017)]
X_test = data_coded.drop(labels='score', axis=1)[data_coded['start_date'].dt.year >= 2018]

y_train =data_coded[(data_coded['start_date'].dt.year >= 2014)&(data_coded['start_date'].dt.year <= 2017)]['score'].values
y_test =data_coded[data_coded['start_date'].dt.year >= 2018]['score'].values

X_train.drop(labels='start_date', axis=True, inplace=True)
X_test.drop(labels='start_date', axis=True, inplace=True)

from sklearn.linear_model import LinearRegression
model1 = LinearRegression()
model1.fit(X_train,y_train)
print(np.floor(model1.predict(X_test.loc[X_test['ball']==5.6])))

joblib.dump(model1, 'regression_model.joblib')
print(model1.score(X_test,y_test))
print(X_train.columns)
print(model1.predict([[1,5.6,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0]]))