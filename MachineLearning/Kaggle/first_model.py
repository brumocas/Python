import pandas as pd

# melbourne input file path
melbourne_input_file = "melb_data.csv"

# load the data
melbourne_data = pd.read_csv(melbourne_input_file)

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

# Making the first Machine Learning Model
# Choosing the target
y = melbourne_data.Price
print(y)

# Choosing "Features"
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
print()
print(melbourne_features)

x = melbourne_data[melbourne_features]
print(x)
print(x.describe())
print(x.head())

# Buildind the model
print()
print()

from sklearn.tree import DecisionTreeRegressor
# Define model. Specify a number for    random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(x, y)

print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
print(melbourne_model.predict(x.head()))