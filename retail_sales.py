import pandas as pd
import numpy as np
from scipy.stats import zscore
data = {
    "Day": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Revenue": [45, 52, np.nan, 48, 390, 55, np.nan, 50, 47, 53]
}
df = pd.DataFrame(data)
print("Missing values in Revenue:", df["Revenue"].isnull().sum())
df["Revenue"] = df["Revenue"].fillna(df["Revenue"].median())
print("\nAfter median fill:")
print(df)
df["Revenue_MinMax"] = (df["Revenue"] - df["Revenue"].min()) / (df["Revenue"].max() - df["Revenue"].min())
df["Revenue_Zscore"] = zscore(df["Revenue"])
Q1 = df["Revenue"].quantile(0.25)
Q3 = df["Revenue"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df["Outlier"] = (df["Revenue"] < lower_bound) | (df["Revenue"] > upper_bound)
print("\nFinal Table:")
print(df)
print("\nIQR outliers detected on day(s):", df[df["Outlier"]]["Day"].tolist())