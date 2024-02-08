import pandas as pd
import numpy as np


class Adaline:
    def __init__(self,learning_rate,max_iterations,error_threshold,b,class1,class2,f1,f2):
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.w0 = None
        self.w1 = None
        self.w2 = None
        self.b = b
        self.error_threshold = error_threshold
        self.class1 = class1
        self.class2 = class2
        self.Feature1 = f1
        self.Feature2 = f2

    def signum(self,x):
        x = list(x)
        return 1 if self.calc_y(x[0], x[1]) >= 0 else -1

    def calc_y(self, x1, x2):
        return self.w1 * x1 + self.w2 * x2 + self.b * self.w0

    def testModel(self, x):
        if self.w1 is not None:
            if self.signum(x) >= 0:
                return self.class1
            else:
                return self.class2
        else:
            return 'Run Train First'

    def fit(self,X,t):
        if not isinstance(X,pd.DataFrame):
            raise ValueError("Input data X should be a Pandas DataFrame.")

        num_samples, _ = X.shape
        self.w0 = np.random.randn()
        self.w1 = np.random.randn()
        self.w2 = np.random.randn()

        # print(self.w1, self.w2)
        # print("after")
        for iteration in range(self.max_iterations):
            sumErrors = 0
            for i in range(num_samples):
                x1 = X.iloc[i,0]
                x2 = X.iloc[i,1]



                y = self.calc_y(x1,x2)
                e = t[i] - y

                self.w0 += self.learning_rate * e * 1
                self.w1 += self.learning_rate * e * x1
                self.w2 += self.learning_rate * e * x2

                sumErrors += (e ** 2)

            mse = sumErrors / (2 * num_samples)
            # print(f"Iteration {iteration + 1}, MSE: {mse}")

            if mse <= self.error_threshold:
                # print(f"Converged after {iteration + 1} iterations.")
                break

    def predict(self,X):
        # print(self.w1, self.w2)
        if not isinstance(X,pd.DataFrame):
            raise ValueError("Input data X should be a Pandas DataFrame.")
        predictions = []
        for i in range(X.shape[0]):
            predictions.append(self.signum(X.iloc[i]))
        return predictions
