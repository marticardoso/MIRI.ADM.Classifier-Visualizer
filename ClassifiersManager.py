
import Classifiers.knn as knn
import Classifiers.MLPClassifier as mlp
import Classifiers.NaiveBayes as naiveBayes
import Classifiers.DecisionTree as decisionTree
import Classifiers.AdaBoost as adaBoost

def createModel(classifier, parameters, trainData, trainLabel):
    if(classifier=="knn"):
        return knn.createModel(parameters,trainData, trainLabel)
    elif(classifier=="MLP"):
        return mlp.createModel(parameters,trainData, trainLabel)
    elif(classifier=="Naive Bayes"):
        return naiveBayes.createModel(parameters,trainData, trainLabel)
    elif(classifier=="Decision tree"):
        return decisionTree.createModel(parameters,trainData, trainLabel)
    elif(classifier=="AdaBoost"):
        return adaBoost.createModel(parameters,trainData, trainLabel)

    # More classifiers

def predict(classifier, model, testData):
    if(classifier=="knn"):
        return knn.predict(model, testData)
    elif(classifier=="MLP"):
        return mlp.predict(model, testData)
    elif(classifier=="Naive Bayes"):
        return naiveBayes.predict(model, testData)
    elif(classifier=="Decision tree"):
        return decisionTree.predict(model, testData)
    elif(classifier=="AdaBoost"):
        return adaBoost.predict(model, testData)