#-------------------------------------------------------------------------
# AUTHOR: Abdur Rahman
# FILENAME: Knn.py
# SPECIFICATION: Use 1nn to classify positive or negative and find accuracy
# FOR: CS 4210- Assignment #2
# TIME SPENT: 20 min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)



errors = 0
#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    #add the training features to the 2D array X and remove the instance that will be used for testing in this iteration.
    #For instance, X = [[1, 3], [2, 1,], ...]]. Convert values to float to avoid warning messages
    #transform the original training classes to numbers and add them to the vector Y. Do not forget to remove the instance that will be used for testing in this iteration.
    #For instance, Y = [1, 2, ,...]. Convert values to float to avoid warning messages
    X = []
    Y = []
    j = 0
    while j <len(db):
        floatA = float(db[j][0])
        floatB = float(db[j][1])
        X.append([floatA,floatB])
        if db[j][2] == '-':
            Y.append(float(1))
        else:
            Y.append(float(2))
        j+=1

    #remove current instance
    a = X.pop(i)
    b = Y.pop(i)

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here

    class_predicted = clf.predict([a])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here

    if class_predicted != b:
        errors+=1

#print the error rate
#--> add your Python code here
errorRate = errors/len(db)
print(errorRate)





