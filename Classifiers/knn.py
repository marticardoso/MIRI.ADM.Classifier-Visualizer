####################
## KNN Classifier ##
####################

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

def createModel(parameters, trainData, trainLabel):
    k = parameters['k']
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(trainData, trainLabel)
    return knn