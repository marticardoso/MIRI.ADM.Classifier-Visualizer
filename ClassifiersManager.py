# It is the manager of the classification, can create a model and predict
import Classifiers.knn as knn
import Classifiers.MLPClassifier as mlp
import Classifiers.NaiveBayes as naiveBayes
import Classifiers.DecisionTree as decisionTree
import Classifiers.AdaBoost as adaBoost
import Classifiers.RandomForest as randomForest
import Classifiers.SVM as svm
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
    elif(classifier=="Random Forest"):
        return randomForest.createModel(parameters,trainData, trainLabel)
    elif(classifier=="SVM (linear kernel)"):
        return svm.createLinearModel(parameters,trainData, trainLabel)
    elif(classifier=='SVM (rbf kernel)'):
        return svm.createModel(parameters,trainData, trainLabel)

    # More classifiers

def predict(classifier, model, testData):
    return model.predict(testData)