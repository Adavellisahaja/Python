import pandas as pd
# from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn import metrics
import warnings

from sklearn.neighbors import KNeighborsClassifier

warnings.simplefilter("ignore")

# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set(style="white", color_codes=True)

dataset = pd.read_csv('train.csv')
# replacing null values with mean
dataset = dataset.fillna(dataset.mean())
x = dataset.iloc[:,1:]

#removing the features not correlated to the target class,
train = x.drop(['Name','Ticket', 'Cabin','Embarked'], axis=1)

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
labelEncoder = preprocessing.LabelEncoder()
labelEncoder.fit(train['Sex'])
train['Sex'] = labelEncoder.transform(train['Sex'])
train.info()
print("train head:")
print(train.head())

#caluculating the svm
feature_cols = ['Pclass', 'Age' ,'SibSp' ,'Parch' ,'Fare' , 'Sex']
from sklearn.svm import SVC
x_train = train[feature_cols]
y_train = train.Survived
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=0)
# SVM
svc = SVC()
svc.fit(x_train, y_train)
y_pred = svc.predict(x_test)
print(classification_report(y_test, y_pred))
acc_svc = round(svc.score(x_train, y_train) * 100, 2)
print("svm accuracy is:", acc_svc)


#calculating navie bayes model
from sklearn.naive_bayes import GaussianNB
x_train = train[feature_cols]
y_train = train.Survived
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=0)
gnb = GaussianNB()
gnb.fit(x_train, y_train)
Y_pred = gnb.predict(x_test)
print (classification_report(y_test,Y_pred))
acc_bayes = round(gnb.score(x_train, y_train) * 100, 2)
print("Naive Bayes accuracy is:",acc_bayes)

#caluculating knn
x_train = train[feature_cols]
y_train = train.Survived
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=0)
##KNN
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(x_train, y_train)
Y_pred = knn.predict(x_test)
acc_knn = round(knn.score(x_train, y_train) * 100, 2)
print("KNN accuracy is:",acc_knn)