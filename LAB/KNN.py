from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

predictions = knn.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

print("\nClassification Report:\n", classification_report(y_test, predictions))

correct_predictions = (predictions == y_test)
wrong_predictions = ~correct_predictions

print("\nCorrect Predictions:")
for i in range(len(predictions)):
    if predictions[i] == y_test[i]:
        print(f"Predicted: {iris.target_names[predictions[i]]}, Actual: {iris.target_names[y_test[i]]}")

print("\nWrong Predictions:")
for i in range(len(predictions)):
    if predictions[i] != y_test[i]:
        print(f"Predicted: {iris.target_names[predictions[i]]}, Actual: {iris.target_names[y_test[i]]}")
