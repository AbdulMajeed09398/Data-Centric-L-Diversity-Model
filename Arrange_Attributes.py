import pandas as pd
# Specify the path to your dataset. It can be URL or file link.
data = pd.read_csv('database name.csv')
# Add the labels of the explicit identifiers (EIs). It is better to add labels of commonly encounterd EIs. 
explicit_identifiers = ['name', 'email', 'phone_number']
# Check if EIs are available in the dataset.
present_explicit_identifiers = [col for col in explicit_identifiers if col in data.columns]
# Drop all EIs if they exist in the real dataset.
if present_explicit_identifiers:
    data = data.drop(columns=present_explicit_identifiers)
    print(f"Dropped all the following EIs: {present_explicit_identifiers}")
else:
    print("No EIs found to drop as original data doesn't encompassed them.")
# Define quasi-identifiers (QIDs) (attributes that should be retained, as all QIDs labels after checking from each dataset.)
quasi_identifiers = ['age', 'workclass', 'education',  'sex']
#Specify the name of SA.
sensitive_attribute = ['income']
# Retain only QIDs and SA
data_cleaned = data[quasi_identifiers + sensitive_attribute]
output_file = 'Arranged_attributes_data.csv'
data_cleaned.to_csv(output_file, index=False)
# If desired: Print the  few rows of the cleaned data having SA at last index by uncommenting the below line.
#print(data_cleaned.head())
