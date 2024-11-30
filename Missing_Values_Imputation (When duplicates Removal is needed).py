import pandas as pd
import numpy as np
# Load the dataset
file_path = 'database name.csv'  # Specify the path to your CSV file
column_names = ['age', 'workclass', 'education', 'sex', 'income']
data = pd.read_csv(file_path, names=column_names, sep=',\s', engine='python')

# Step 1: Replace '?' with NaN and handle missing values for '?'
def replace_missing_values(df, numerical_columns, categorical_columns):
    
    df.replace("?", np.nan, inplace=True)

    for col in numerical_columns:
        df[col].fillna(df[col].mean(), inplace=True)
   
    for col in categorical_columns:
        least_frequent_category = df[col].value_counts().idxmin()
        df[col].fillna(least_frequent_category, inplace=True)
    
    return df
# Separate numerical and categorical columns
numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
print(numerical_columns)
categorical_columns = data.select_dtypes(include=['object']).columns
print(categorical_columns)
# Replace '?' with NaN and impute missing values
data = replace_missing_values(data, numerical_columns, categorical_columns)
print("Missing values (i.e., '?') have been imputed.")

# Step 2: Outlier detection for Numerical Attributes using IQR and replace with mean
def detect_and_replace_outliers_numerical(df, numerical_columns):
    for col in numerical_columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        
        # Define outlier thresholds
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Replace outliers with the mean of the column
        mean_value = df[col].mean()
        
        # Find and replace outliers in the column
        df[col] = np.where((df[col] < lower_bound) | (df[col] > upper_bound), mean_value, df[col])
    
    return df

# Detect and replace numerical outliers with the mean
data = detect_and_replace_outliers_numerical(data, numerical_columns)
print("Numerical outliers replaced with mean values.")

# Step 2: Remove consecutive duplicate rows
def remove_consecutive_duplicates(df):
    df = df.loc[(df != df.shift()).any(axis=1)]
    return df
data = remove_consecutive_duplicates(data)
print(data)
print("Consecutive duplicate rows have been removed.")
# Step 3: Save the cleaned data to a CSV file
output_file = "cleaned_data.csv"
data.to_csv(output_file, index=False)
