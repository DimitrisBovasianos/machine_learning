import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import numpy as np

url = "/home/dimitris/test1.csv"

names = ['first_letter','second_letter','third_letter','second_to_last_letter','last_letter','word']

dataset = pandas.read_csv(url,names=names)
#Dimensions of the dataset.
#print(dataset.shape)

#Peek the first 20 rows of our data.
print(dataset.head(20))


#split the dataset 80%-20%
array = dataset.values
X = array[:,0:5]
Y = array[:,5]
validation_size = 0.2 #this give us the percentance we gonna split
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

scoring = 'accuracy'
models = []
#cause we dont know the which algorith to use,we test to find the most accurate
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn

#This will give us an independent final check on the accuracy of the best model.
model = GaussianNB()
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)
for i in range(len(Y_validation)):
    print("x={}, predict={}".format(Y_validation[i],predictions[i]))
print(accuracy_score(Y_validation, predictions))
#The confusion matrix provides an indication of the three errors made.
print(confusion_matrix(Y_validation, predictions))
# Finally, the classification report provides a breakdown of each class by precision
print(classification_report(Y_validation, predictions))
#Testing for a word
word = 'goodmorning'
sample = [word[0],word[1],word[2],word[len(word)-2],word[len(word)-1]]
for i in range(0,len(sample)):
    sample[i] = ord(sample[i])
x = [np.array(sample)]
print(x)
predict = model.predict(x)
print(predict)
