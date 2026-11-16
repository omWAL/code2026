import pandas as pd, warnings
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
warnings.filterwarnings("ignore")

# i. Read dataset
df = pd.read_csv("churn.csv")
df = df.drop("CustomerId", axis=1)                         # ID is not useful
df = pd.get_dummies(df, columns=["Geography", "Gender"], drop_first=True)  # text -> numbers

# ii. Features / target and train-test split
X = df.drop("Exited", axis=1)
y = df["Exited"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1, stratify=y)

# iii. Normalize
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# iv. Build model, then improved model (more neurons, more layers, more epochs, regularization)
m1 = MLPClassifier(hidden_layer_sizes=(4,), max_iter=200, random_state=1)
m2 = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=2000, alpha=0.01, random_state=1)

# v. Accuracy and confusion matrix
for name, m in [("Basic model", m1), ("Improved model", m2)]:
    m.fit(X_train, y_train)
    pred = m.predict(X_test)
    print(f"\n{name}")
    print("Accuracy:", round(accuracy_score(y_test, pred), 2))
    print("Confusion matrix:\n", confusion_matrix(y_test, pred))
