from sklearn.svm import SVC

def createLinearModel(parameters, trainData, trainLabel):
    model = SVC(kernel="linear", C=parameters['c'])
    model.fit(trainData, trainLabel)
    return model

def createModel(parameters, trainData, trainLabel):
    model = SVC(gamma=parameters['gamma'], C=parameters['c'])
    model.fit(trainData, trainLabel)
    return model
