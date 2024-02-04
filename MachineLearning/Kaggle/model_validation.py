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


# Choosing "Features"
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']


x = melbourne_data[melbourne_features]


# Buildind the model

from sklearn.tree import DecisionTreeRegressor
# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(x, y)

melbourne_model.predict(x)

from sklearn.metrics import mean_absolute_error
predicted_home_prices = melbourne_model.predict(x)
print(mean_absolute_error(y, predicted_home_prices))

from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(x, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))