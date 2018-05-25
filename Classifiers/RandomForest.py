from sklearn.ensemble import RandomForestClassifier

def createModel(parameters, trainData, trainLabel):
    model = RandomForestClassifier(max_depth=parameters['max_depth'], n_estimators=parameters['n'], max_features=parameters['max_features'])
    model.fit(trainData, trainLabel)
    return model
