import pandas as pd
# Data balancing code/module.
additional_records = pd.read_csv('synthetic_records.csv')
# We assume that the structures are the same.
print("\nColumns of the additional records CSV:")
print(additional_records.columns)
# Filter to include only records with the minority class ('>50K') as majority class is fixed.
additional_minority_records = additional_records[additional_records[sensitive_attribute] == '>50K']
records_to_add = additional_minority_records.head(records_needed_for_balance)

#Combine the majority class and the updated minority class
majority_class = data[data[sensitive_attribute] == '<=50K']
balanced_data = pd.concat([majority_class, records_to_add])
#Verify the new distribution of the SA
new_distribution = balanced_data[sensitive_attribute].value_counts()
print("\nNew frequencies after balancing:")
print(new_distribution)

#Optionally, save the balanced dataset to a new CSV file
balanced_data.to_csv('balanced_a_data.csv', index=False)
