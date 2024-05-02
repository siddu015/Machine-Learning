#P8: KNN
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the k-NN classifier
knn_classifier = KNeighborsClassifier(n_neighbors=3)

# Train the classifier
knn_classifier.fit(X_train, y_train)

# Make predictions on the test set
predictions = knn_classifier.predict(X_test)

# Calculate accuracy and print classification report
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Display correct and wrong predictions
correct_predictions = sum(predictions == y_test)
wrong_predictions = len(y_test) - correct_predictions

print("\nCorrect Predictions:")
for i in range(len(predictions)):
    if predictions[i] == y_test[i]:
        print(f"Predicted: {iris.target_names[predictions[i]]}, Actual: {iris.target_names[y_test[i]]}")

print("\nWrong Predictions:")


for i in range(len(predictions)):
    if predictions[i] != y_test[i]:
        print(f"Predicted: {iris.target_names[predictions[i]]}, Actual: {iris.target_names[y_test[i]]}")
