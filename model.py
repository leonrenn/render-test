import numpy as np

W = np.array([[0.5, -0.2]])
b = np.array([0.1])

def predict(x):
    x = np.array(x)
    y = 1 / (1 + np.exp(-(x @ W.T + b)))
    return float(y[0])
