import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

df = pd.read_csv("uber.csv")
print("Missing values:\n", df.isnull().sum())

# i. Pre-process: remove missing rows, make a distance column
df = df.dropna()
def distance(lat1, lon1, lat2, lon2):          # haversine formula (km)
    p = np.pi / 180
    a = 0.5 - np.cos((lat2-lat1)*p)/2 + np.cos(lat1*p)*np.cos(lat2*p)*(1-np.cos((lon2-lon1)*p))/2
    return 2 * 6371 * np.arcsin(np.sqrt(a))
df["distance_km"] = distance(df.pickup_latitude, df.pickup_longitude,
                             df.dropoff_latitude, df.dropoff_longitude)

# ii. Outliers using IQR rule
q1, q3 = df.fare_amount.quantile([0.25, 0.75])
iqr = q3 - q1
out = df[(df.fare_amount < q1 - 1.5*iqr) | (df.fare_amount > q3 + 1.5*iqr)]
print("\nOutliers found:", len(out))
df = df.drop(out.index)

# iii. Correlation
print("\nCorrelation:\n", df[["passenger_count", "distance_km", "fare_amount"]].corr().round(2))

# iv. Models
X = df[["distance_km", "passenger_count"]]
y = df["fare_amount"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
models = {"Linear Regression": LinearRegression(),
          "Random Forest": RandomForestRegressor(n_estimators=100, random_state=1)}

# v. Evaluate
for name, m in models.items():
    m.fit(X_train, y_train)
    pred = m.predict(X_test)
    print(f"\n{name}")
    print("R2   :", round(r2_score(y_test, pred), 3))
    print("RMSE :", round(np.sqrt(mean_squared_error(y_test, pred)), 3))
    print("MAE  :", round(mean_absolute_error(y_test, pred), 3))
