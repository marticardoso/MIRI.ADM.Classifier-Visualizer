from sklearn.neural_network import MLPClassifier

def createModel(parameters, trainData, trainLabel):
    alpha = parameters['alpha']
    model = MLPClassifier(alpha= 0.9)
    model.fit(trainData, trainLabel)
    return model

def predict(model, testData):
    return model.predict(testData)