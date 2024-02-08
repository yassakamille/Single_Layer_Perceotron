import tkinter as tk
from tkinter import *
from tkinter import messagebox
from readData import ReadDATA, Accuracy, decision_boundary, NormalizeX,ConfusionMatrix
from Adaline import Adaline
from Perceptron import Perceptron
from sklearn import metrics


messagebox = messagebox
root = Tk()
root.title("First NN Task")
Var1 = StringVar()
title_1 = Label(root, textvariable=Var1)
Var1.set("Class 1")
title_1.place(x=10,y=10)
title_1.pack()
entry1 = Entry(root,width=40)  # first input
entry1.focus_set()
entry1.pack()

Var2 = StringVar()
title_2 = Label(root, textvariable=Var2)
Var2.set("Class 2")
title_2.pack()
entry2 = tk.Entry(root, width=40)  # second input
entry2.pack()

Var3 = StringVar()
title_3 = Label(root, textvariable=Var3)
Var3.set("Feature 1")
title_3.pack()
entry3 = tk.Entry(root, width=40)  # Third input
entry3.pack()

Var4 = StringVar()
title_4 = Label(root, textvariable=Var4)
Var4.set("Feature 2")
title_4.pack()
entry4 = tk.Entry(root, width=40)  # Fourth input
entry4.pack()

Var5 = StringVar()
title_5 = Label(root, textvariable=Var5)
Var5.set("Epochs")
title_5.pack()
entry5 = tk.Entry(root, width=40)  # Fifth input
entry5.pack()

Var6 = StringVar()
title_6 = Label(root, textvariable=Var6)
Var6.set("Learning Rate")
title_6.pack()
entry6 = tk.Entry(root, width=40)  # Sixth input
entry6.pack()


def classification_perceptron(Class1_input_1=entry1.get(), Class2_input_2=entry2.get(), Feature1_input_1=entry3.get(),
                              Feature2_input_2=entry4.get(), Epochs=entry5.get(), Learning_rate=entry6.get()):
    Class1_input_1 = entry1.get()
    Class2_input_2 = entry2.get()
    Feature1_input_1 = entry3.get()
    Feature2_input_2 = entry4.get()
    Epochs = entry5.get()
    Learning_rate = entry6.get()
    bios = var.get()

    if not Class1_input_1 or not Class2_input_2 or not Feature1_input_1 or not Feature2_input_2 or not Epochs or not Learning_rate:
        print("Invalid: Please enter values for all inputs.\n")
    else:
        X_train, X_test, y_train, y_test = ReadDATA(Class1_input_1, Class2_input_2, Feature1_input_1, Feature2_input_2)

        model = Perceptron(learning_rate=float(Learning_rate), max_iterations=int(Epochs),
                           b=int(bios), class1=Class1_input_1, class2=Class2_input_2, f1=Feature1_input_1,
                           f2=Feature2_input_2)
        model.train(X_train, y_train)
        predict = model.predict(X_test)
        print('Accuracy =', Accuracy(y_test, predict), '%')
        decision_boundary(model, X_test, y_test, Class1_input_1, Class2_input_2, Feature1_input_1, Feature2_input_2)
        ConfusionMatrix(y_test,predict)
        Perceptron.model = model


def classification_adaline(Class1_input_1=entry1.get(), Class2_input_2=entry2.get(), Feature1_input_1=entry3.get(),
                           Feature2_input_2=entry4.get(), Epochs=entry5.get(), Learning_rate=entry6.get()):
    Class1_input_1 = entry1.get()
    Class2_input_2 = entry2.get()
    Feature1_input_1 = entry3.get()
    Feature2_input_2 = entry4.get()
    Epochs = entry5.get()
    Learning_rate = entry6.get()
    bios = var.get()
    if not Class1_input_1 or not Class2_input_2 or not Feature1_input_1 or not Feature2_input_2 or not Epochs or not Learning_rate:
        print("Invalid: Please enter values for all inputs.\n")
    else:
        X_train, X_test, y_train, y_test = ReadDATA(Class1_input_1, Class2_input_2, Feature1_input_1, Feature2_input_2)

        model = Adaline(learning_rate=float(Learning_rate), max_iterations=int(Epochs), error_threshold=0.01,
                        b=int(bios), class1=Class1_input_1, class2=Class2_input_2, f1=Feature1_input_1,
                        f2=Feature2_input_2)
        model.fit(X_train, y_train)
        predict = model.predict(X_test)
        print('Accuracy =', Accuracy(y_test, predict), '%')
        decision_boundary(model, X_test, y_test, Class1_input_1, Class2_input_2, Feature1_input_1, Feature2_input_2)
        ConfusionMatrix(y_test, predict)
        Adaline.model = model


def test_Adaline(Feature1_input_1=entry3.get(), Feature2_input_2=entry4.get()):
    Feature1_input_1 = entry3.get()
    Feature2_input_2 = entry4.get()

    if not Feature1_input_1 or not Feature2_input_2:
        print("Invalid: Please enter values for all inputs.\n")
    else:
        predict = 'Train model first'
        try:
            x = list([float(Feature1_input_1),float(Feature2_input_2)])
            x = NormalizeX(x=x, f1=Adaline.model.Feature1, f2=Adaline.model.Feature2, class1=Adaline.model.class1,
                           class2=Adaline.model.class2)
            predict = Adaline.model.testModel(x)
            print(predict)
        except:
            print('')
        messagebox.showinfo('Predicted',predict)


def test_perceptron(Feature1_input_1=entry3.get(), Feature2_input_2=entry4.get()):
    Feature1_input_1 = entry3.get()
    Feature2_input_2 = entry4.get()

    if not Feature1_input_1 or not Feature2_input_2:
        print("Invalid: Please enter values for all inputs.\n")
    else:
        predict = 'Train model first'

        try:
            x = list([float(Feature1_input_1), float(Feature2_input_2)])
            x = NormalizeX(x=x, f1=Perceptron.model.Feature1, f2=Perceptron.model.Feature2,
                           class1=Perceptron.model.class1, class2=Perceptron.model.class2)
            predict = Perceptron.model.testModel(x)
            print(predict)
        except:
            print('')
        messagebox.showinfo('Predicted', predict)


# Buttons
button1 = tk.Button(root,text="Classify Perceptron", width=20, command=classification_perceptron)
button2 = tk.Button(root,text="Classify Adaline", width=20, command=classification_adaline)
button3 = tk.Button(root,text="Test Perceptron", width=20, command=test_perceptron)
button4 = tk.Button(root,text="Test Adaline", width=20, command=test_Adaline)

# BIOS
Var7 = StringVar()
title_7 = Label(root, textvariable=Var7)
Var7.set("Bios")
title_7.pack()

var = tk.IntVar()
bios = var.get()
radio_button_01 = tk.Radiobutton(root, text="0", variable=var, value=0)
radio_button_01.pack()

radio_button_1 = tk.Radiobutton(root, text="1", variable=var, value=1)
radio_button_1.pack()

button1.place(x=50, y=250)
button2.place(x=50, y=280)
button3.place(x=320, y=250)
button4.place(x=320, y=280)
root.geometry('500x320')
root.mainloop()
