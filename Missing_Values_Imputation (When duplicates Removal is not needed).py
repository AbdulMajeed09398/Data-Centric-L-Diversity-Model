import pandas as pd
import numpy as np

# Load thedataset
file_path = 'database name.csv' 
column_names = ['age', 'workclass', 'education', 'marital-status', 
      'race', 'sex', 'native-country', 'income']

data = pd.read_csv(file_path, names=column_names, sep=',\s', engine='python')
# Step 1: Replace '?' with NaN and handle missing values
def replace_missing_values(df, numerical_columns, categorical_columns):
    # Replace '?' with NaN for consistency
    df.replace("?", np.nan, inplace=True)
    for col in numerical_columns:
        df[col].fillna(df[col].mean(), inplace=True)
    for col in categorical_columns:
        # Only impute '?' (NaN) values, using the least frequent category
        least_frequent_category = df[col].value_counts().idxmin()
        df[col].fillna(least_frequent_category, inplace=True)
    
    return df

numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
categorical_columns = data.select_dtypes(include=['object']).columns

# Replace '?' with NaN and impute missing values, in our experiments, it is known vulnerability.
data = replace_missing_values(data, numerical_columns, categorical_columns)
print("Missing values (i.e., '?') have been imputed.")

numerical_count = len(numerical_columns)
categorical_count = len(categorical_columns)

# Below values must be changed based on the actual ground truth for each dataset.
expected_numerical_count = 1  
expected_categorical_count = 7  

print(f"Numerical columns count: {numerical_count}")
print(f"Categorical columns count: {categorical_count}")

if numerical_count == expected_numerical_count:
    print("The numerical column count matches the ground truth.")
else:
    print(f"Warning: The numerical column count does NOT match the ground truth. Expected {expected_numerical_count}, but got {numerical_count}.")

if categorical_count == expected_categorical_count:
    print("The categorical column count matches the ground truth.")
else:
    print(f"Warning: The categorical column count does NOT match the ground truth. Expected {expected_categorical_count}, but got {categorical_count}.")
#Save the cleaned data to a CSV file
output_file = "cleaned_data.csv"
data.to_csv(output_file, index=False)
