import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

df = pd.read_csv("spam.csv")                 # label: 1 = Spam, 0 = Not Spam
X = df.drop("label", axis=1)
y = df["label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

sc = StandardScaler()                        # scale features (needed for KNN and SVM)
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

models = {"KNN": KNeighborsClassifier(n_neighbors=3),
          "SVM": SVC(kernel="linear")}
for name, m in models.items():
    m.fit(X_train, y_train)
    pred = m.predict(X_test)
    print(f"\n{name}")
    print("Accuracy :", round(accuracy_score(y_test, pred), 2))
    print("Precision:", round(precision_score(y_test, pred), 2))
    print("Recall   :", round(recall_score(y_test, pred), 2))
    print("Confusion matrix:\n", confusion_matrix(y_test, pred))
