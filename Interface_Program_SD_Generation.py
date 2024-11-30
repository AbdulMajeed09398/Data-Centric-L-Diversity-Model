# add time library for computing time analysis.
import time
start = time.process_time()
from ctgan import CTGAN
from ctgan import load_demo
# The demo file has path to one datasets which can be customized for others dataset.
real_data = load_demo()
# Names of the columns that are discrete, must be modified for each dataset.
discrete_columns = [
    'marital-status',
    'workclass',
    'occupation',
    'education',
    'sex',
    'relationship',
    'native-country',
    'race',
    'income']
# Verify if the dataset is properly loaded or not by printing some columns.
print(real_data)
# Modify the epochs if desirable.
ctgan = CTGAN(epochs=10)
ctgan.fit(real_data, discrete_columns)

# Create synthetic data, specify the # of records to be curated.
synthetic_data = ctgan.sample(32561)
print(time.process_time() - start)
