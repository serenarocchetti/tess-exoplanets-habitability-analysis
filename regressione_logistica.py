import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn import metrics

# Carico il file CSV
df = pd.read_csv("exofop_toilists.csv")

# Seleziono e rinomino le colonne necessarie
df_selected = df[[
    "Predicted Mass (M_Earth)",
    "Planet Radius (R_Earth)",
    "Planet Equil Temp (K)",
    "TSM",
    "ESM"
]].copy()

df_selected.columns = ["Mass", "Radius", "Teq", "TSM", "ESM"]

# Calcolo la densità media in g/cm³
earth_mass_kg = 5.972e24
earth_radius_m = 6.371e6

mass_kg = df_selected["Mass"] * earth_mass_kg
radius_m = df_selected["Radius"] * earth_radius_m
volume_m3 = (4/3) * 3.14159265359 * radius_m**3
density_kg_m3 = mass_kg / volume_m3
df_selected["Density"] = density_kg_m3 / 1000  # da kg/m³ a g/cm³

# Creo la variabile target Habitability
df_selected["Habitability"] = (
    (df_selected["Density"] > 4) &
    (df_selected["Teq"] >= 175) & (df_selected["Teq"] <= 270) &
    (df_selected["TSM"] >= 10) &
    (df_selected["ESM"] >= 7.5)
).astype(int)

df_selected = df_selected.dropna()
print(df_selected["Habitability"].value_counts())


# Selezione delle feature e target
X = df_selected[["Density", "Teq", "TSM", "ESM"]]
y = df_selected["Habitability"]

# Standardizzazione
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Regressione logistica
logreg = LogisticRegression(random_state=42)
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)
print(classification_report(y_test, y_pred))


