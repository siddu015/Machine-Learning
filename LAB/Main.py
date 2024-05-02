#P9 Corrected:non-parametric Locally Weighted Regression algorithm
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# Load the Boston housing dataset
boston = fetch_california_housing()
X = boston.data
y = boston.target

#Next, let's define a function to apply the LOWESS algorithm:
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def lowess(X, y, f=0.5, kernel='gaussian', n_neighbors=5):
    """
    Apply the LOWESS algorithm to the given input-output data.
    Parameters:
    X (array-like): Input data with shape (n_samples, n_features).
    y (array-like): Output data with shape (n_samples,).
    f (float): Fraction of the data used for fitting.
    kernel (str): Kernel function used to compute the weights. Can be either 'gaussian' or 'triangular'.
    n_neighbors (int): Number of neighbors used for smoothing.
    Returns:
    y_pred (array-like): Predicted output data with shape (n_samples,).
    """

    # Initialize the predicted output data
    y_pred = np.zeros_like(y)

    # Iterate over the input data
    for i in range(len(y)):
        #select a subset of the data around the i-th data point
        distances = np.linalg.norm(X - X[i], axis=1)  # Calculate distances along rows
        idx = distances < (distances.max() - distances.min()) * f  # Create boolean mask
        subset = X[idx]
        subset_y = y[idx]

    # Fit a linear regression model to the subset
    reg = LinearRegression()
    reg.fit(subset, subset_y)

    # Compute the weights for each data point in the subset
    if kernel == 'gaussian':
        weights = np.exp(-(np.abs(X - X[i]) / (X.max() - X.min()) * f)**2)
    elif kernel == 'triangular':
        weights = np.maximum(1 - np.abs(X - X[i]) / (X.max() - X.min()) * f, 0)

    # Normalize the weights
    weights /= np.sum(weights)

    # Compute the predicted output for the i-th data point
    y_pred[i] = np.sum(weights * reg.predict(X[i][None, :]))

    # Compute the mean squared error of the predicted output
    mse = mean_squared_error(y, y_pred)
    return y_pred, mse

#Now, let's apply the LOWESS algorithm to the Boston housing dataset and plot the results:
# Apply the LOWESS algorithm

y_pred, mse = lowess(X, y)


# Plot the input and output data
plt.scatter(X[:, 5], y, s=10)
plt.xlabel('RM (median value of owner-occupied homes in $1000s)')
plt.ylabel('MEDV (median value of owner-occupied homes in $1000s)')

# Plot the predicted output data
plt.plot(X[:, 5], y_pred, color='red', linewidth=2)
plt.show()

print("Mean squared error:", mse)