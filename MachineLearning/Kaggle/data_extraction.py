import pandas as pd

# melbourne input file path
melbourne_input_file = "melb_data.csv"

# load the data
melbourne_data = pd.read_csv(melbourne_input_file)

# columns from the csv file
print(melbourne_data.columns)

# statistics about the csv file
stats = melbourne_data.describe()
print('\n\n',stats)

print(melbourne_data.count())
# The Melbourne data has some missing values (some houses for which some variables weren't recorded.)
# We'll learn to handle missing values in a later tutorial.  
# Your Iowa data doesn't have missing values in the columns you use. 
# So we will take the simplest option for now, and drop houses from our data. 
# Don't worry about this much for now, though the code is:
# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)
# Check if the na houses were deleted
print("\nna houses deleted \n")
print(melbourne_data.count())
