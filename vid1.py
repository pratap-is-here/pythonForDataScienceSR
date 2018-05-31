from sklearn import tree

#[height,weight,shoe size]
X=[[181,80,44],
    [177,70,43],
    [160,60,38],
    [154,54,37],
    [166,65,40],
    [190,90,47],
    [175,64,39],
    [177,70,40],
    [155,59,37],
    [171,75,42],
    [181,85,43]]
Y=['male','female','female','female','male','male','male','female','male','female','male']

clf1=tree.DecisionTreeClassifier()

clf1=clf1.fit(X,Y)

prediction=clf1.predict([[167.64,76.43,36.5]])

print "prediction using decision trees"

print prediction

from sklearn import svm

clf2=svm.SVC()

clf2.fit(X,Y)

prediction=clf2.predict([[167.64,76.43,36.5]])

print "prediction using support vector machine"

print prediction

from sklearn.naive_bayes import GaussianNB

clf3=GaussianNB()

clf3.fit(X,Y)

prediction=clf3.predict([[167.64,76.43,36.5]])

print "prediction using Gaussian Naive Bayes"

print prediction

from sklearn.neural_network import MLPClassifier

clf4=MLPClassifier(solver='lbfgs',alpha=1e-5, hidden_layer_sizes=(5,2),random_state=1)

clf4.fit(X,Y)

prediction=clf4.predict([[167.64,76.43,36.5]])

print "prediction using Neural Network"

print prediction

