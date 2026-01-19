import numpy as np
import pandas as pd
from advisor import air_quality_advisor

# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("city_day.csv", na_values='=')

# -------------------------------
# Data Cleaning
# -------------------------------
data2 = df.copy()
data2 = data2.fillna(data2.mean(numeric_only=True))

# Encode City
cities = list(set(data2["City"]))
city_dict = {cities[i]: i for i in range(len(cities))}
data2["City"] = data2["City"].map(city_dict)

# Drop unused columns
data2 = data2.drop(["Date", "AQI_Bucket"], axis=1)

# -------------------------------
# Feature & Label Split
# -------------------------------
features = data2[['City','PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene']]
labels = data2['AQI']

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(features, labels, test_size=0.2, random_state=2)

# -------------------------------
# Train Model
# -------------------------------
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(max_depth=6, random_state=0)
model.fit(Xtrain, Ytrain)

# -------------------------------
# Model Evaluation
# -------------------------------
y_pred = model.predict(Xtest)

from sklearn.metrics import r2_score
accuracy = r2_score(Ytest, y_pred)
print("Model R2 Score:", round(accuracy, 3))

# -------------------------------
# AI Air Quality Monitoring Assistant
# -------------------------------
print("\n--- AI Air Quality Monitoring Assistant ---")

print("\nAvailable Cities:")
for city in list(city_dict.keys())[:10]:
    print("-", city)

user_city = input("\nEnter City Name: ")

if user_city not in city_dict:
    print("City not found in dataset. Using default city.")
    city_code = list(city_dict.values())[0]
else:
    city_code = city_dict[user_city]

print("\nEnter pollutant values:")

pm25 = float(input("PM2.5: "))
pm10 = float(input("PM10: "))
no = float(input("NO: "))
no2 = float(input("NO2: "))
nox = float(input("NOx: "))
nh3 = float(input("NH3: "))
co = float(input("CO: "))
so2 = float(input("SO2: "))
o3 = float(input("O3: "))
benzene = float(input("Benzene: "))
toluene = float(input("Toluene: "))
xylene = float(input("Xylene: "))

input_data = np.array([[city_code, pm25, pm10, no, no2, nox, nh3, co, so2, o3, benzene, toluene, xylene]])

predicted_aqi = int(model.predict(input_data)[0])

level, advice = air_quality_advisor(predicted_aqi)

print("\n--- Air Quality Report ---")
print("City:", user_city)
print("Predicted AQI:", predicted_aqi)
print("Air Quality Level:", level)
print("Health Advisory:", advice)
