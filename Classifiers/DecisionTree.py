
from sklearn.tree import DecisionTreeClassifier

def createModel(parameters, trainData, trainLabel):
    max_depth = parameters['max_depth']
    model = DecisionTreeClassifier(max_depth=max_depth)
    model.fit(trainData, trainLabel)
    return model

def predict(model, testData):
    return model.predict(testData)