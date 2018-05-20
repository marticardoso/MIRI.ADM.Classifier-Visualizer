from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
from sklearn.utils.extmath import cartesian
def knn(k, trainData, trainLabel, testData):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(trainData, trainLabel)
    return knn.predict(testData)

def knnCreateModel(k, trainData, trainLabel):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(trainData, trainLabel)
    return knn

def createModel(classifier, parameters, trainData, trainLabel):
    if(classifier=="knn"):
        k = parameters['k']
        return knnCreateModel(k,trainData, trainLabel)
    # More classifiers

def predict(model, testData):
    return model.predict(testData)

    
'''
mat = np.matrix([[int(0),int(0),'white']]*(4))
print mat
mat[:,:-1] = cartesian([range(2),range(2)])
print mat[1,1]
for i in mat:
    print i[0,1]

data = np.array([[1,2, "blue"],[2,3,"red"],[2,3,"red"],[2,3,"red"],[2,3,"red"]])
for i in data:
    print i
print len(data)

x2 = pd.DataFrame(data, columns=['X', 'Y', 'Class'])
x2.loc[1,"Class"] = 'blue'
print x2.loc[1,"Class"]
attr = x2.drop('Class', axis=1)
label = x2["Class"]
#x2 = pd.DataFrame( columns=['X', 'Y', 'Class'])

x2.loc[5] = [1,2,"blue"]

print x2.loc[2,:]
print len(x2)
x2[0] =[1,2,"blue"]
print x2
for i in range(len(x2)):
    print i
x = knn(1, attr, label, attr)

print x
'''