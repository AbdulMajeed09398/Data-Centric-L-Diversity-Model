import pandas as pd
# Path to dataset
data = pd.read_csv('adultss.csv')
print(data.columns)
# Sensitive attribute: 'income'
sensitive_attribute = 'income'
# Analyze the frequency distribution of the SA ('income')
frequency_distribution = data[sensitive_attribute].value_counts()
# Print the frequency distribution, if desirable.
print(frequency_distribution)
# Compute the imbalance ratio
minority_class_count = frequency_distribution.min()
majority_class_count = frequency_distribution.max()
imbalance_ratio = majority_class_count / minority_class_count
print(f"Imbalance Ratio: {imbalance_ratio:.2f}")
# Determine the number of records needed to balance the distribution
# Rare SA value needs augmentation.
records_needed_for_balance = majority_class_count - minority_class_count
print(f"Records needed to balance the dataset: {records_needed_for_balance}")



