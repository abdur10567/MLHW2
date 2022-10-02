# -------------------------------------------------------------------------
# AUTHOR: Abdur Rahman
# FILENAME: decision_tree_2
# SPECIFICATION: compare accuracy of decision trees based on amount of data used to train them.
# FOR: CS 4210- Assignment #2
# TIME SPENT:
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries

import copy
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
ones = ["Young", "Myope", "No", "Normal", "No"]
twos = ["Prepresbyopic", "Hypermetrope", "Yes", "Reduced", "Yes"]


# read the test data and add this data to dbTest
# --> add your Python code here
# dbTest =
dbTest = []
with open("contact_lens_test.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTest.append(row)

# for data in dbTest:
# transform the features of the test instances to numbers following the same strategy done during training,
Z = copy.deepcopy(dbTest)
i = 0
while i < len(Z):
    j = 0
    while j < len(Z[i]):
        if (Z[i][j] in ones):
            Z[i][j] = 1
        elif (Z[i][j] in twos):
            Z[i][j] = 2
        else:
            Z[i][j] = 3
        j += 1
    i += 1


for ds in dataSets:

    print(ds)
    dbTraining = []
    X = []
    Y = []

    # reading the training data in a csv file
    with open(ds, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i > 0:  # skipping the header
                dbTraining.append(row)

    X = copy.deepcopy(dbTraining)

    # transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    # --> add your Python code here
    i = 0
    while i < len(X):
        j = 0
        while j < len(X[i]) - 1:
            if (X[i][j] in ones):
                X[i][j] = 1
            elif (X[i][j] in twos):
                X[i][j] = 2
            else:
                X[i][j] = 3
            j += 1
        del X[i][-1]
        i += 1


    # transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    # --> addd your Python code here
    # Y =
    i = 0
    while i < len(dbTraining):
        current = 0
        if (dbTraining[i][4] == "No"):
            current = 1
        else:
            current = 2
        Y.append(current)
        i += 1

    accuracy = 1.00
    # loop your training and test tasks 10 times here
    for i in range(10):
        # fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3)
        clf = clf.fit(X, Y)




        # and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
        # where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
        # --> add your Python code here
        i = 0
        predictions = []
        while i < len(Z):
            class_prediction = clf.predict([[Z[i][0],Z[i][1],Z[i][2],Z[i][3]]])[0]
            predictions.append(class_prediction)
            i+=1



        # compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
        # --> add your Python code here
        i = 0
        correct = 0
        while i < len(Z):
            if Z[i][4] == predictions[i]:
                correct+=1
            i+=1


        # find the lowest accuracy of this model during the 10 runs (training and test set)
        # --> add your Python code here
        if (correct/len(Z)) < accuracy:
            accuracy = (correct/len(Z))

    # print the lowest accuracy of this model during the 10 runs (training and test set).
    # your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    # --> add your Python code here
    print("Accuracy:",accuracy)
