#-------------------------------------------------------------------------
# AUTHOR: Abdur Rahman
# FILENAME: naive_bayes.py
# SPECIFICATION: Use Naive bayes classifer to classify whether or not to play tennis based on weather conditions
# FOR: CS 4210- Assignment #2
# TIME SPENT: 35 mins
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv
import copy


db = []

#reading the data in a csv file
with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)


ones = ["Sunny", "Hot", "High", "Weak"]
twos = ["Overcast", "Mild", "Normal", "Strong"]

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
# X =
X = copy.deepcopy(db)
i = 0
while i < len(X):
    j = 1
    while j < len(X[i]) - 1:
        if (X[i][j] in ones):
            X[i][j] = 1
        elif (X[i][j] in twos):
            X[i][j] = 2
        else:
            X[i][j] = 3
        j += 1
    del X[i][-1]
    del X[i][0]
    i += 1

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y = []
i = 0
while i < len(db):
    current = 0
    if (db[i][5] == "No"):
        current = 2
    else:
        current = 1
    Y.append(current)
    i += 1

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here
dbTest = []

#reading the data in a csv file
with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         dbTest.append (row)


Z = copy.deepcopy(dbTest)
i = 0
while i < len(Z):
    j = 1
    while j < len(Z[i]) - 1:
        if (Z[i][j] in ones):
            Z[i][j] = 1
        elif (Z[i][j] in twos):
            Z[i][j] = 2
        else:
            Z[i][j] = 3
        j += 1
    del Z[i][-1]
    del Z[i][0]
    i += 1



#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
i=0
while i<len(Z):
    prediction = clf.predict_proba([[Z[i][0],Z[i][1],Z[i][2],Z[i][3]]])[0]
    if prediction[0]>=0.75:
        print(str(dbTest[i][0]).ljust(13),str(dbTest[i][1]).ljust(15),str(dbTest[i][2]).ljust(15),str(dbTest[i][3]).ljust(15),str(dbTest[i][4]).ljust(15),"Yes".ljust(15),str(round(prediction[0],2)).ljust(15))
    elif prediction[1]>=0.75:
        print(str(dbTest[i][0]).ljust(13), str(dbTest[i][1]).ljust(15), str(dbTest[i][2]).ljust(15),
              str(dbTest[i][3]).ljust(15), str(dbTest[i][4]).ljust(15), "No".ljust(15), str(round(prediction[1],2)).ljust(15))
    i+=1


