from sklearn import svm
#print("SVM imported successfully")
##to import the default iris datasets
from sklearn import datasets
## to split training and test data
from sklearn.model_selection import train_test_split
#for getting accuracy score
from sklearn.metrics import accuracy_score
##load iris datasets from datasets package
iris = datasets.load_iris()
##the datatype of iris object is BUNCH in utils of sklearn
#print(type(iris))
##iris has an attribute data which is used to display the datasets values
##iris dataset has 4 attributes sepal_length, sepal_width, petal_length and petal_width
#print(iris.data)
##iris has an attribute feature_name to display the col name
#print(iris.feature_names)
## iris.target represents target- the 3 flowers iris-sytosa,verscicolor and virginica
#print(iris.target)
##iris.target_names presents target names
#print(iris.target_names)
#declaration of independent variable
X = iris.data
#print(X)
##dependent variable Y
Y = iris.target
##split the data into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, Y,test_size=0.2,random_state=4)

##converting 1d to 2d
#X_train_mod = X_train.reshape(-1,1)
#X_test_mod = X_test.reshape(-1,1)
#y_test_mod = y_test.reshape(-1,1)
#y_train_mod = y_train.reshape(-1,1)
##creating a model
model = svm.SVC(kernel = "linear")
##fitting my model with training data of independent X and dependent Y
model.fit(X_train, y_train)
##predict accuracy of model using the test data
accuracy = model.score(X_test, y_test)
#yield the result of predicted model using test data
y_pred_mod = model.predict(X_test)
#accuracy of classification
print(accuracy_score(y_test, y_pred_mod))
