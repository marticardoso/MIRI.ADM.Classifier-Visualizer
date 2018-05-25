from sklearn.neural_network import MLPClassifier

def createModel(parameters, trainData, trainLabel):
    hiddenLayers = max(parameters['hiddenLayers'],1)
    numNeurons = max(parameters['numNeurons'],1)
    hidden_layer_sizes = tuple([numNeurons]*hiddenLayers)
    model = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, max_iter=500)
    model.fit(trainData, trainLabel)
    return model
