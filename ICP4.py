#2. Implementing Naïve Bayes method using scikit-learn library
import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()

dataset = pd.read_csv('glass.csv')
X=dataset[['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe']]
Y=dataset['Type']
X_train, X_test, y_train, y_test=  train_test_split( X, Y, test_size=0.25, random_state=0)
gnb.fit(X_train,y_train)
print('accuracy is {:.2f}'.format(gnb.score(X_train,y_train)))
print('accuracy is {:.2f}'.format(gnb.score(X_test,y_test)))

#3 Implementing linear SVMmethodusing scikit library

import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import train_test_split
dataset = pd.read_csv('glass.csv')
X=dataset[['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe']]
Y=dataset['Type']
X_train, X_test, y_train, y_test=  train_test_split( X, Y, test_size=0.25, random_state=0)



svc = LinearSVC()
svc.fit(X_train, y_train)
Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_train, y_train) * 100, 2)
acc_svc1 = round(svc.score(X_test, y_test) * 100, 2)
print("training svm accuracy is:", acc_svc)
print(" testing svm accuracy is:", acc_svc1)

#4 SVM with RBF kernel on the same dataset

import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import train_test_split
dataset = pd.read_csv('glass.csv')
X=dataset[['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe']]
Y=dataset['Type']
X_train, X_test, y_train, y_test=  train_test_split( X, Y, test_size=0.25, random_state=0)



svc = SVC(kernel='rbf')
svc.fit(X_train, y_train)
Y_pred = svc.predict(X_test)
acc_svc = round(svc.score(X_train, y_train) * 100, 2)
acc_svc1 = round(svc.score(X_test, y_test) * 100, 2)
print("training svm accuracy is:", acc_svc)
print(" testing svm accuracy is:", acc_svc1)





