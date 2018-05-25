from sklearn.naive_bayes import GaussianNB

def createModel(parameters,trainData, trainLabel):
    model = GaussianNB()
    model.fit(trainData, trainLabel)
    return model
