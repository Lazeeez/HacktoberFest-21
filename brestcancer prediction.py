import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import tkinter as tk
class Predictor:

    def has_disease(self, row):
        self.train(self)
        #Class:   (2 for benign, 4 for malignant)
        return True if self.predict(self, row) == 4 else False

    @staticmethod
    def train(self):
        dataset = pd.read_csv('./data/breast-cancer.csv')
        dataset = dataset[dataset.Bare_Nuclei != '?']
        dataset = dataset.drop(['Sample code number'], axis=1)
        y = dataset['Class']
        X = dataset.drop(['Class'], axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=0)
        self.classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=0)
        self.classifier.fit(X_train, y_train)
        score = self.classifier.score(X_test, y_test)
        print('--Training Complete--')
        print('Score: ' + str(score))

    @staticmethod
    def predict(self, row):
        user_df = np.array(row).reshape(1, 9)
        # user_df = self.standardScaler.transform(user_df)
        predicted = self.classifier.predict(user_df)
        print("Predicted: " + str(predicted[0]))
        return predicted[0]


la=str()
def onClick():
    row=[[cthick.get(),ucsize.get(),ucshape.get(),ma.get(),cecsize.get(),bn.get(),bc.get(),nn.get(),mito.get()]]
    print(row)
    predictor = Predictor()
    o = predictor.has_disease(row)
    root2 = tk.Tk()
    root2.title("Prediction Window")
    if (o == True):
        print("Person Have Breast Cancer")
        la="Person Have Breast Cancer"
        tk.Label(root2, text=la, font=("times new roman", 20), fg="white", bg="maroon", height=2).grid(row=0, column=1)
    else:
        print("Person Is Healthy")
        la="Person Is Healthy"
        tk.Label(root2, text=la, font=("times new roman", 20), fg="white", bg="green", height=2).grid(row=0, column=1)

    return True
root = tk.Tk()
root.title("Breast Cancer Predictor")
tk.Label(root,text="""Fill Values between 1 - 10""",font=("times new roman", 12)).grid(row=0)
tk.Label(root,text='Clump Thickness ',padx=20, font=("times new roman", 12)).grid(row=1,column=0)
cthick = tk.IntVar()
tk.Entry(root,textvariable=cthick).grid(row=1,column=1)

tk.Label(root,text="""Uniformity of Cell Size""",padx=20, font=("times new roman", 12)).grid(row=2,column=0)
ucsize = tk.IntVar()
tk.Entry(root,textvariable=ucsize).grid(row=2,column=1)

tk.Label(root,text='Uniformity of Cell Shape', font=("times new roman", 12)).grid(row=3,column=0)
ucshape = tk.IntVar()
tk.Entry(root,textvariable=ucshape).grid(row=3,column=1)

tk.Label(root,text='Marginal Adhesion', font=("times new roman", 12)).grid(row=4,column=0)
ma = tk.IntVar()
tk.Entry(root,textvariable=ma).grid(row=4,column=1)

tk.Label(root,text='Single Epithelial Cell Size', font=("times new roman", 12)).grid(row=5,column=0)
cecsize = tk.IntVar()
tk.Entry(root,textvariable=cecsize).grid(row=5,column=1)

tk.Label(root,text="""Bare Nuclei""",padx=20, font=("times new roman", 12)).grid(row=6,column=0)
bn=tk.IntVar()
tk.Entry(root,textvariable=bn).grid(row=6,column=1)

tk.Label(root,text="""Bland Chromatin""",padx=20, font=("times new roman", 12)).grid(row=7,column=0)
bc=tk.IntVar()
tk.Entry(root,textvariable=bc).grid(row=7,column=1)

tk.Label(root,text='Normal Nucleoli', font=("times new roman", 12)).grid(row=8,column=0)
nn = tk.IntVar()
tk.Entry(root,textvariable=nn).grid(row=8,column=1)

tk.Label(root,text="""Mitoses""",padx=20, font=("times new roman", 12)).grid(row=9,column=0)
mito=tk.IntVar()
tk.Entry(root,textvariable=mito).grid(row=9,column=1)

tk.Button(root, text='Predict', command=onClick).grid(row=11, column=1)

root.mainloop()
