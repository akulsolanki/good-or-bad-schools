from itertools import product

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np


# Load data
iris = datasets.load_iris()
X, y = iris.data[:, [0, 1]], iris.target
data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])

dt = DecisionTreeClassifier(max_depth=4)
knn = KNeighborsClassifier(n_neighbors=7)
svc = SVC(gamma=.1, kernel='rbf', probability=True)
mlp = MLPClassifier()

# Train the classifiers
dt.fit(X, y)
knn.fit(X, y)
svc.fit(X, y)
mlp.fit(X,y)


# https://scikit-learn.org/stable/auto_examples/ensemble/plot_voting_decision_regions.html

#Mathematical

boston = datasets.load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
print(df.shape)
df.head()

from sklearn.model_selection import train_test_split
X, Y = df, boston.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.33, random_state = 5)

from sklearn.linear_model import LinearRegression

lm = LinearRegression().fit(X_train, Y_train)

Y_pred = lm.predict(X_test)
print("Score is:",lm.score(X_test,Y_test))

my_formatted_list = [ '%.2f' % i for i in lm.coef_ ]
str1 = 'x + '.join(str(e) for e in my_formatted_list)
print("\n \nFormula is:\n y = ", str1, ' + ', str(lm.intercept_) )
