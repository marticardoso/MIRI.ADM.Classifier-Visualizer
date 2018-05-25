# The class that contains all the values that can be modified in the GUI
class Values:

    points = []
    
    #TrainTestRatio
    trainTestRatio = 2.0/3.0
    
    #Points options 
    radius = 3
    nPointsPerClick = 10

    #Distribution
    isNormalDistribution = True
    unifDistMargin = 50
    normalSd = 20
    
    #Classifier
    classifier = "knn"
    classifiers = ["knn", "Naive Bayes", "Decision tree", "AdaBoost", "Random Forest", "SVM (linear kernel)", 'SVM (rbf kernel)',"MLP"]
    
    #Knn
    knn_k = 3
    
    #MLP
    MLP_numNeurons = 10
    MLP_hiddenLayers = 3

    #Decision Tree
    decisionTree_maxDepth = 5

    #Random forest
    randomForest_n = 10
    randomForest_maxDepth = 5

    #Linear SVM
    linearSVM_c = 0.025

    #SVM
    svm_gamma = 2
    svm_c = 1

