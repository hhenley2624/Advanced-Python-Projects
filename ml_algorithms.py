# import all the ML libraries needed to include nltk for stopwords and warnings to ignore possible warnings
import csv, joblib, matplotlib.pyplot as plt, nltk, pandas as pd, requests, sklearn.neighbors, sklearn.neural_network, sklearn.metrics, sklearn.model_selection, sklearn.tree, sklearn.feature_extraction.text, warnings
nltk.download("stopwords", quiet=True)
from nltk.corpus import stopwords
warnings.filterwarnings("ignore")

# Function that computes all three machine learning models
def machine_learning_models(model, model_name):
    """Create a try and except block in case the file does not load"""
    try:
        """Use pandas to remove unnecessary data"""
        data = pd.read_csv("kickstarter_data_full.csv", encoding = "latin-1")
        data_filtered = data[~data["Status"].isin(["Cancelled by Creator", "Cancelled by Kickstarter"])]

        """Create the arrays for x and y data"""
        text = data_filtered["Description"].tolist()
        y = data_filtered["Status"].tolist()

        """Create a document-term matrix"""
        vectorizer = sklearn.feature_extraction.text.CountVectorizer(stop_words=stopwords.words("english"), max_features=1000)
        vectors = vectorizer.fit_transform(text)
        x = vectors.toarray()

        """break data into training and test portion"""
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y)

        """Train the models and use the parameter model to change the model"""
        if model == "sklearn.tree.DecisionTreeClassifier":
            clf = sklearn.tree.DecisionTreeClassifier()
        elif model == "sklearn.neighbors.KNeighborsClassifier":
            clf = sklearn.neighbors.KNeighborsClassifier(7)
        else:
            clf = sklearn.neural_network.MLPClassifier()
        clf.fit(x_train, y_train)

        """Compute the accuracy of the model"""
        predictions = clf.predict(x_test)
        accuracy = sklearn.metrics.accuracy_score(y_test, predictions)
        print(f"{model_name} model is {accuracy *100} percent accurate. \n")
        return clf, x_test, y_test, model_name
    except:
        print("Error, please make sure you have the correct file path.")

# Function to compute confusion matrix and classification model
def confusion_and_classification(clf, x_test, y_test, model_name):
    """Show a confusion matrix"""
    predictions = clf.predict(x_test)
    cm = sklearn.metrics.confusion_matrix(y_test, predictions)
    disp = sklearn.metrics.ConfusionMatrixDisplay(cm)
    disp.plot()
    plt.show()

    """Show the classification report"""
    print(f"{model_name} Classification Report \n{sklearn.metrics.classification_report(y_test, predictions)}")

    """Save the most accurate model to a file"""
    return joblib.dump(clf, "neural_networks.joblib")

# Call the machine_learning_models function and store the returned values
decision_tree = machine_learning_models("sklearn.tree.DecisionTreeClassifier", "Decision Tree")
knn_result = machine_learning_models("sklearn.neighbors.KNeighborsClassifier", "KNN")
neural_network_result = machine_learning_models("sklearn.neural_network.MLPClassifier", "Neural Network")

# Call the confusion_and_classification function
confusion_and_classification(*neural_network_result)




