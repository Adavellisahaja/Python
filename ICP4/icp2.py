import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import  classification_report
from sklearn.model_selection import train_test_split

# import data
dataset = pd.read_csv("glass.csv")
x_train = dataset.drop("Type",axis=1)
y_train = dataset["Type"]
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=0)
# SVM
gnb = GaussianNB()
gnb.fit(x_train, y_train)
Y_pred = gnb.predict(x_test)
print (classification_report(y_test,Y_pred))
acc_bayes = round(gnb.score(x_train, y_train) * 100, 2)
print("Naive Bayes accuracy is:",acc_bayes)


