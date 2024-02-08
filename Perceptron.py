import pandas as pd
import numpy as np


class Perceptron:
    def __init__(self, learning_rate, max_iterations, b, class1, class2, f1, f2):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.w0 = None
        self.w1 = None
        self.w2 = None
        self.b = b
        self.class1 = class1
        self.class2 = class2
        self.Feature1 = f1
        self.Feature2 = f2

    def testModel(self,x):
        if self.w1 is not None:
            prediction = self.signum(self.w1 * x[0] + self.w2 * x[1] + self.w0 * self.b)
            if prediction >= 0:
                return self.class1
            else:
                return self.class2
        else:
            return 'Run Train First'


    def signum(self, x):
        return 1 if x >= 0 else -1

    def train(self, X, t):
        if not isinstance(X, pd.DataFrame):
            raise ValueError("Input data X should be a Pandas DataFrame.")
        num_samples, num_features = X.shape
        self.w0 = np.random.rand()
        self.w1 = np.random.rand()
        self.w2 = np.random.rand()
        for iteration in range(self.max_iterations):
            misclassified = 0
            for i in range(num_samples):
                x1 = X.iloc[i, 0]
                x2 = X.iloc[i, 1]
                ti = t[i]
                y = self.signum(self.w1 * x1 + self.w2 * x2 + self.b)

                if y != ti:
                    misclassified += 1
                    delta_w0 = self.learning_rate * (ti - y) * 1
                    delta_w1 = self.learning_rate * (ti - y) * x1
                    delta_w2 = self.learning_rate * (ti - y) * x2
                    self.w0 += delta_w0
                    self.w1 += delta_w1
                    self.w2 += delta_w2

            if misclassified == 0:
                # print(f"Converged after {iteration + 1} iterations.")
                break

    def predict(self, X):
        if not isinstance(X, pd.DataFrame):
            raise ValueError("Input data X should be a Pandas DataFrame.")

        predictions = []
        for i in range(X.shape[0]):
            x1 = X.iloc[i, 0]
            x2 = X.iloc[i, 1]

            prediction = self.signum(self.w1 * x1 + self.w2 * x2 + self.w0 * self.b)
            predictions.append(prediction)
        return predictions
