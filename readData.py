import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics


def encodeData(y,class1,class2):
    res = []
    for i in y:
        if i == class1:
            res.append(1)
        elif i == class2:
            res.append(-1)
    return res


def handleNull(data):
    mean_value = data['MinorAxisLength'].mean()
    data['MinorAxisLength'].fillna(value=mean_value, inplace=True)


def decision_boundary(model, xxPLt, yyPLT, class1, class2, feature1, feature2):
    # Get the learned weights and bias from your model
    w1 = model.w1
    w2 = model.w2
    b = model.w0 * model.b
    # Create a mesh grid for the decision boundary

    x_min, x_max = xxPLt.iloc[:,0].min() - 1, xxPLt.iloc[:,0].max() + 1
    xx = np.arange(x_min,x_max,0.01)
    yy = - (w1 / w2) * xx - (b / w2)

    # Scatter the data points for both classes
    plt.scatter(xxPLt.iloc[np.array(yyPLT) == -1,0], xxPLt.iloc[np.array(yyPLT) == -1,1], c='b', label=class1)
    plt.scatter(xxPLt.iloc[np.array(yyPLT) == 1,0], xxPLt.iloc[np.array(yyPLT) == 1,1], c='r', label=class2)

    # Plot the decision boundary line
    plt.plot(xx, yy, c='g',label='Decision Boundary')

    plt.xlabel(feature1)
    plt.ylabel(feature2)
    plt.legend(loc='best')
    plt.title('Decision Boundary')

    plt.show()


def ReadDATA(class1, class2, feature1, feature2):
    data = pd.read_csv('Dry_Bean_Dataset.csv')
    handleNull(data)

    # drop class(y)
    data = data[(data['Class'] == class1) | (data['Class'] == class2)]

    Normalization(data)

    x = pd.DataFrame([data[feature1], data[feature2]]).transpose()

    y = data.iloc[:, -1]
    y = encodeData(y, class1, class2)
    # X_train, X_test, y_train, y_test
    return train_test_split(x,y,test_size=0.40,shuffle=True,random_state=10,stratify=y)


def Normalization(data):
    data['Area'] /= np.mean(data['Area'])
    data['Perimeter'] /= np.mean(data['Perimeter'])
    data['MinorAxisLength'] /= np.mean(data['MinorAxisLength'])
    data['MajorAxisLength'] /= np.mean(data['MajorAxisLength'])


def NormalizeX(x,f1,f2,class1,class2):
    data = pd.read_csv('Dry_Bean_Dataset.csv')
    handleNull(data)
    data = data[(data['Class'] == class1) | (data['Class'] == class2)]
    x[0] /= np.mean(data[f1])
    x[1] /= np.mean(data[f2])
    return x


def Accuracy(y,predicts):
    correct = 0
    for i in range(len(y)):
        if y[i] == predicts[i]:
            correct += 1
    return (correct / len(y)) * 100
def ConfusionMatrix(actual,predicted):
    true_positives = 0
    true_negatives = 0
    false_positives = 0
    false_negatives = 0

    # Calculate values for the confusion matrix
    for a, p in zip(actual, predicted):
        if a == 1 and p == 1:
            true_positives += 1
        elif a == -1 and p == -1:
            true_negatives += 1
        elif a == -1 and p == 1:
            false_positives += 1
        elif a == 1 and p == -1:
            false_negatives += 1

    # Create the confusion matrix
    confusion_matrix = {
        'True Positives': true_positives,
        'True Negatives': true_negatives,
        'False Positives': false_positives,
        'False Negatives': false_negatives
    }

    # Display the confusion matrix
    print("Confusion Matrix:")
    for label, value in confusion_matrix.items():
        print(f"{label}: {value}")