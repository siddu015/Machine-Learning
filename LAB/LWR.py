import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

california = fetch_california_housing()
X = california.data
y = california.target


def lowess(X, y, f=0.5, kernel='gaussian', n_neighbors=5):
    y_pred = np.zeros_like(y)

    for i in range(len(y)):
        distances = np.linalg.norm(X - X[i], axis=1)
        idx = distances < (distances.max() - distances.min()) * f
        subset = X[idx]
        subset_y = y[idx]

        reg = LinearRegression()
        reg.fit(subset, subset_y)

        if kernel == 'gaussian':
            weights = np.exp(-(np.abs(X - X[i]) / (X.max() - X.min()) * f)**2)
        elif kernel == 'triangular':
            weights = np.maximum(1 - np.abs(X - X[i]) / (X.max() - X.min()) * f, 0)

        weights /= np.sum(weights)

        y_pred[i] = np.sum(weights * reg.predict(X[i][None, :]))

    mse = mean_squared_error(y, y_pred)

    return y_pred, mse


y_pred, mse = lowess(X, y)

plt.scatter(X[:, 3], y, s=10)
plt.xlabel("Number of bedrooms")
plt.ylabel('MEDV(Median value of owner-occupied homes in 1000$')
plt.title('Locally Weighted Scatterplot Smoothing (LOWESS)')

plt.plot(X[:, 3], y_pred, color='red', linewidth=2)
plt.show()

print("Mean squared error:", mse)
