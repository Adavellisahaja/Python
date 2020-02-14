import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# import data
dataset = pd.read_csv("glass.csv")
x_train = dataset.drop("Type",axis=1)
y_train = dataset["Type"]
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2, random_state=0)
# SVM
svc = SVC()
svc.fit(x_train, y_train)
y_pred = svc.predict(x_test)
print(classification_report(y_test, y_pred))
acc_svc = round(svc.score(x_train, y_train) * 100, 2)
print("svm accuracy is:", acc_svc)


