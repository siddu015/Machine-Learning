import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

california = fetch_california_housing()
X = california.data
y = california.target

def lowess(X, y, f=0.5):
    y_pred = np.zeros_like(y)

    for i in range(len(X)):
        distances = np.abs(X - X[i])
        weights = np.exp(-(distances / (X.max() - X.min()) * f) ** 2)
        weights /= np.sum(weights)

        reg = LinearRegression()
        reg.fit(X, y, sample_weight=weights.flatten())
        y_pred[i] = reg.predict(X[i].reshape(1, -1))

    mse = mean_squared_error(y, y_pred)
    return y_pred, mse

y_pred, mse = lowess(X, y)

plt.scatter(X, y, s=10)
plt.plot(X, y_pred, color='red', linewidth=2)
plt.xlabel("Average number of rooms")
plt.ylabel('Median House Value ($1000s)')
plt.title('Locally Weighted Scatterplot Smoothing (LOWESS)')
plt.show()

print("Mean squared error:", mse)
