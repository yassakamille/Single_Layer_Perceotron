import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("First NN Task")



Var1 = StringVar()
title_1= Label(root,textvariable=Var1)
Var1.set("Class 1")
title_1.place(x=10,y=10)
title_1.pack()
entry1 = Entry(root, width=40)#first input
entry1.focus_set()
entry1.pack()

Var2 = StringVar()
title_2= Label(root,textvariable=Var2)
Var2.set("Class 2")
title_2.pack()
entry2 = tk.Entry(root, width=40)#second input
entry2.pack()

Var3 = StringVar()
title_3= Label(root,textvariable=Var3)
Var3.set("Feature 1")
title_3.pack()
entry3 = tk.Entry(root, width=40)#Third input
entry3.pack()

Var4 = StringVar()
title_4= Label(root,textvariable=Var4)
Var4.set("Feature 2")
title_4.pack()
entry4 = tk.Entry(root, width=40)#Fourth input
entry4.pack()

Var5= StringVar()
title_5= Label(root,textvariable=Var5)
Var5.set("Epochs")
title_5.pack()
entry5= tk.Entry(root, width=40)#Fifth input
entry5.pack()

Var6= StringVar()
title_6= Label(root,textvariable=Var6)
Var6.set("Learning Rate")
title_6.pack()
entry6= tk.Entry(root, width=40)#Sixth input
entry6.pack()

def classification_perceptron( Class1_input_1=entry1.get(),  Class2_input_2 = entry2.get(),
Feature1_input_1 = entry3.get(),Feature2_input_2 = entry4.get(),Epochs =entry5.get(),Learning_rate=entry6.get()):

    Class1_input_1 = entry1.get()
    Class2_input_2 = entry2.get()
    Feature1_input_1 = entry3.get()
    Feature2_input_2 = entry4.get()
    Epochs =entry5.get()
    Learning_rate=entry6.get()
    classification_result="beans"

    if not Class1_input_1 or not Class2_input_2 or not Feature1_input_1 or not Feature2_input_2 \
            or not Epochs or not Learning_rate  :
        print("Invalid: Please enter values for all inputs.\n")
    else:

        print("This inputs tends to be classified as "+classification_result+"\n")

    #Write Your Classification code here

def classification_adline( Class1_input_1=entry1.get(),  Class2_input_2 = entry2.get(),
Feature1_input_1 = entry3.get(),Feature2_input_2 = entry4.get(),Epochs =entry5.get(),Learning_rate=entry6.get()):

    Class1_input_1 = entry1.get()
    Class2_input_2 = entry2.get()
    Feature1_input_1 = entry3.get()
    Feature2_input_2 = entry4.get()
    Epochs =entry5.get()
    Learning_rate=entry6.get()
    classification_result="beans"

    if not Class1_input_1 or not Class2_input_2 or not Feature1_input_1 or not Feature2_input_2 \
            or not Epochs or not Learning_rate  :
        print("Invalid: Please enter values for all inputs.\n")
    else:

        print("This inputs tends to be classified as "+classification_result+"\n")

    #write your test for perceptron here

def test_Adline( Feature1_input_1 = entry3.get(), Feature2_input_2 = entry4.get()):
    Feature1_input_1 = entry3.get()
    Feature2_input_2 = entry4.get()
    Accuracy_adline= 0.9

    if not Feature1_input_1 or not Feature2_input_2:
        print("Invalid: Please enter values for all inputs.\n")
    else:
        print("Accurucy of Adline = "+ Accuracy_adline.__str__() +"\n")

    #write your test for Adline here

def test_perceptron(  Feature1_input_1 = entry3.get(), Feature2_input_2 = entry4.get()):
    Feature1_input_1 = entry3.get()
    Feature2_input_2 = entry4.get()
    Accuracy_perceptron= 0.9

    if not Feature1_input_1 or not Feature2_input_2:
        print("Invalid: Please enter values for all inputs.\n")
    else:
        print("Accurucy of perceptron = "+ Accuracy_perceptron.__str__() +"\n")

    #write your test for Adline here

button1 = tk.Button(root, text="Classify Perceptron",width=20 ,command=classification_perceptron)
button2 = tk.Button(root, text="Classify Adline",width=20 ,command=classification_adline)
button3= tk.Button(root, text="Test Perceptron",width=20, command=test_perceptron)
button4 = tk.Button(root, text="Test Adline",width=20, command=test_Adline)

# BIOS
Var7= StringVar()
title_7= Label(root,textvariable=Var7)
Var7.set("Bios")
title_7.pack()
var = tk.IntVar()
bios=var.get()

radio_button_01 = tk.Radiobutton(root, text="0", variable=var, value=0)
radio_button_01.pack()

radio_button_1 = tk.Radiobutton(root, text="1", variable=var, value=1)
radio_button_1.pack()

button1.place(x=50,y=250)
button2.place(x=50,y=280)
button3.place(x=320,y=250)
button4.place(x=320,y=280)
root.geometry('500x320')
root.mainloop()


