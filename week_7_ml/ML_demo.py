"""
This a Machine Learning script that will guide you through the basics using the Scikit-learn module in Python. IF you have no experience in Machine Learning it is highly recommended to read the report on Machine Learning on the Coding Dojo website before attempting to understand this script. We will load a dataset which has labels and use it for unsupervised ML first and then for supervised classification later. Any question you can always address to nicolas.arning@bdi.ox.ac.uk
"""
# These are a few general libraries we need for some of the math action going on behing the scenes and some of the plotting

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from pandas.plotting import scatter_matrix
import sys
import numpy as np

# This is all the sub modules of Scikit learn which is the main library for Machine learning in Python
from sklearn.preprocessing import MinMaxScaler 
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA, NMF
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.feature_selection import VarianceThreshold, SelectKBest, chi2
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, LabelBinarizer
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold, RepeatedStratifiedKFold, LeaveOneOut
from sklearn.linear_model import RidgeClassifier
from sklearn.svm import LinearSVC, SVC, NuSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import  RandomForestClassifier, AdaBoostClassifier, ExtraTreesClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score,  classification_report, roc_curve, auc, precision_recall_fscore_support
from sklearn.utils import resample
from sklearn.datasets import load_iris

# Load Dataset. The iris dataset gets shipped with scikit learn. We then store it in two variables X and y. Where X is a 2D array (the programming equivalent of a spreadsheet) of the data and y are the labels. Every row in X should have a label in y. They both are sorted in the same way
X, y = load_iris( return_X_y = True)

print X, y # lets take a look at the data

X_dataframe = pd.DataFrame( data = X, index = y) # Here we load the data into a pandas dataframe to take a closer look and make the plotting easier. For all the plotting that is done here you can check our week_3 python plotting to see how we do it.

print X_dataframe

# Exploratory Data analysis
plt.figure(figsize = [ 10, 100])
sns.heatmap( X_dataframe, yticklabels = y) # A quick heatmap to see the values present in the dataset
plt.show()

X_dataframe.plot(kind = "hist", sharex = False, alpha = 0.3, subplots = True) # A quick histogram to see the distribution of the data
plt.show()

scatter_matrix( X_dataframe, diagonal = "kde") # A scatter matrix to plot every column against each other in a scatterplot. Here you can already seen whether there is a separation within the data which might make classification easier
plt.show()


## Unsupervised learning
# This is how loads of the ML is done in scikit learn. First you import the algorithm as an object with maybe a few parameters. Then you fit it to your data. The fitted classifier can then be used on new unseen data
# Importing the algorithm
pca = PCA( n_components = 3) # A principal component analysis which can be used as a clustering algorithm (finding underlying groupings wihtin data) as well as dimensionality reduction (boiling down a table with a lot of columns to a table only having few but containing virtually all of the information) 
# Fitting the algorithm to our data
pca.fit(X) 
# Now we use the fitted PCA to reduce our dataset
X_reduced = pca.transform( X)


# lets look at the output
print "normal input" , X
print "dimensionality reduced", X_reduced
 
# Lets plot the dimensionality reduced table in three dimensions 
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])
plt.show()

# Now lets do the same for an Linear disciminant analysis, which can also be used as a dimensionality reduction but can make use of the labels of the data and therefore might perform better in reducing the data. I will let both algorithms against each other to see what is better at clustering (whilst using the labels from the data in the plot for colouring). A better separation of the different colours coudl indicate a mre successfull clustering
lda = LinearDiscriminantAnalysis( n_components = 2)
lda.fit(X, y)
X_reduced_lda = lda.transform( X)

pca = PCA( n_components = 2)
pca.fit(X)
X_reduced_pca = pca.transform( X)

f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.scatter( X_reduced_lda[ :, 0], X_reduced_lda[ :, 1], c=y)
ax1.set_title("LDA")
ax2.scatter(X_reduced_pca[ :, 0], X_reduced_pca[ :, 1], c=y)
ax2.set_title("PCA")
plt.show()

# K-means clustering is another unsupervised clustering algorithm, where k is the number of clusters you suspect is in the data
plt.close()
fig = plt.figure()
k_means = KMeans(n_clusters=2)
k_means.fit(X)
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
labels = k_means.labels_

ax.scatter(X[:, 3], X[:, 0], X[:, 2],
plt.title( "Kmeans Clustering")
fig.show()
plt.show()

# Agglomorative clustering is a form of hierarchical clustering, where the clusters are iteratively expanded until all datapoints are included. This leads to a tree like structure. You can cut the tree at a specific point to generate the amount of clusters you need
fig = plt.figure()
k_means =  AgglomerativeClustering(linkage = "average"  , n_clusters=3)
k_means.fit(X)
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)
labels = k_means.labels_

ax.scatter(X[:, 3], X[:, 0], X[:, 2],
plt.title(" Agglomerative Clustering")
plt.show()



# Supervised Machine learning
# Here we will use a plethora of different classification algorithms and make use of the easy architecture of sklearn. So this is a list of different algorithm object we will loop through. All of these are classifiers that can learn attributes of a class from labeled training data and apply that knowledge to classify unseen data.
classifiers = [
    ( KNeighborsClassifier(10), "K-Nearest Neighbour" ), # The first item of this tuple is the classifier object the second is just the name to use as the title for the plot
    ( SVC(kernel="linear", C=1)," Support Vector Machine Linear" ),
    ( SVC(gamma=2, C=1),"SVM RBF" ),
    ( GaussianProcessClassifier(),"Gaussian Process" ),
    ( DecisionTreeClassifier(max_depth=5),"Decision Tree" ),
    ( RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),"Random Forest" ),
    ( MLPClassifier(alpha=1),"Multilayered Perceptron" ),
    ( AdaBoostClassifier(),"ADA Boost" ),
    ( GaussianNB(),"Gaussian Naive Bayesian" ),
    ( QuadraticDiscriminantAnalysis(), "Quadratic Discriminant" ),
    ]

# The next two functions are just for plotting. It is not important to fully understand them
def make_meshgrid(x, y, h=.01):

    x_min, x_max = x.min() - 0, x.max() + 1
    y_min, y_max = y.min() - 0, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    return xx, yy


def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

# Here we want to use the reduced dataframe bc it is easier to plot in two dimensional space
X = X_reduced_pca

# Here is where we split the data into training and testing, so that we can check on the test dataset how well our classifier performs
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
X0, X1 = X[:, 0], X[:, 1]
xx, yy = make_meshgrid(X0, X1)


for classifier in classifiers: # lets loop through the different classifiers
    classifier_name = classifier[ 1] 
    clf = classifier[ 0]
    f, (ax1, ax2) = plt.subplots(1, 2, sharey=True) # two subplots hich share the y axis
    ax1.scatter(X_train[:, 0], X_train[:, 1], c=y_train, edgecolors='k') # plot the training data on the left
    clf.fit(X_train, y_train) # fit the classifier on the training data
    score = clf.score(X_test, y_test) # see how well we do on the testing data
    score = round(score, 4)
    print classifier_name, score # this will show you how well each classifier is doing
    plot_contours(ax2, clf, xx, yy, alpha=0.8) # lets plot the decision boundaries between the classes
    ax2.scatter(X_test[:, 0], X_test[:, 1], c=y_test,  alpha=0.6, edgecolors='k') # plot the test dataset on top of these decision boundaries. Here we can see where the classifier went wrong
    plt.title( classifier_name +  "\naccuracy = {}".format(score))
    plt.show()

# Now lets do a gridsearch in which we optimisie a classifier for the best hyperparameter. We will use k-nearest-neighbour and try differnt ks (k chooses how many neighbours are taken into account for decision making)
classifier2optimise = KNeighborsClassifier() 
classifier_name = "K-nearest-neighbour"
parameter_grid_dict = {'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]} 

# This is a gridsearch object which will use 5 fold cross validation to find the best parameter from the param_grid object.
grid= GridSearchCV(classifier2optimise, param_grid = parameter_grid_dict,  cv=5, refit = True, n_jobs = 4)
grid.fit(X_train, y_train) # Fit the grid object on the data

for key, value in grid.best_params_.iteritems():
            print key, "=" ,value

clf =  KNeighborsClassifier(10) # this is just to display the not optimised classifier
f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True) # get three plots with the training, the not optimised classifier and the optimised classifier
ax1.scatter(X_train[:, 0], X_train[:, 1], c=y_train, edgecolors='k')
# Here we fit and score the initial classifier
clf.fit(X_train, y_train) 
score =clf.score(X_test, y_test)
score = round(score, 4)
print classifier_name, score
plot_contours(ax2, clf, xx, yy, alpha=0.8)
ax2.scatter(X_test[:, 0], X_test[:, 1], c=y_test,  alpha=0.6, edgecolors='k')

optimised_clf = grid.best_estimator_ # This here is the optimised classifier
score = optimised_clf.score(X_test, y_test)
score = round(score, 4)
print "grisearch optimised", score
plot_contours(ax3, optimised_clf, xx, yy, alpha=0.8) # lets plot the classifiers against each other. Hopefully here we will see that we have improved the classifier. As the dataset as such is a very easy classification problem it could be that the classification was initially already so good it cant be optimised
ax3.scatter(X_test[:, 0], X_test[:, 1], c=y_test,  alpha=0.6, edgecolors='k')
plt.title( "optimised " + classifier_name +  "\naccuracy = {}".format(score))
plt.show()

"""
This is it for now on applied Machine learning. I hope you can see that it is not as much black magic as it appears to be and Scikit-learn makes it very easy to get into. However keep in mind that this is just the very tip of the iceberg and there is way more stuff even in scikit-learn to explore. Here for example we haven't touched the topic of regression or deep learning which warrants their own sessions. Any question please direct towards nicolas.arning@bdi.ox.ac.uk
"""


