#Basics of reading in:
filename = 'file.txt'
file = open(filename, mode = 'r')  #'r' is top read, 'w' is to write
text = file.read()
file.close()

with open('huck_finn.txt', 'r') as file:   #with is referred to as the context manager
   print(file.read()) 
   
   
#Using NumPy - for numeric arrays
   #This allows use of sci-kit learn
import numpy as np

#Can use: 
data = np.loadtxt(filename, delimiter = "'", skiprows = 1, usecols=[0, 2], dtype=str)

#Alternatively, use Pandas (this is preferable)

import pandas as pd

data = pd.read_csv(filename,  sep = '\t', comment='#', na_values='Nothing')  #comment drops everything after '#', na_values are user specified nulls

data.head() #prints first 5 rows .head(10) displays 10 rows

data_array = data.values   #converts to numpy array

#Other types of import files:

#Pickled file: files containing python data structures that don't traslate to an obvious readible form (i.e. dicts, lists, tuples)
# Import pickle package
import pickle

# Open pickle file and load data: d
with open('data.pkl', 'rb') as file:
    d = pickle.load(file)
    
#Excel
file = "excel.xlsx"
data = pd.ExcelFile(file)

print(data.sheet_names)

df1 = data.parse('name_of_sheet')
df2 = data.parse(1) #index of sheet
df1 = data.parse(0, skiprows=[1], names=['Country', 'AAM due to War (2002)'])

#SAS 
# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
   df_sas = file.to_data_frame()
   
#Stata
# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')

#HDF5 (Hierarchical Data Format version 5)
import h5py

# Assign filename: file
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file. HDF5 files have a heirarchical structure that can be drilled down using the keys
for key in data.keys():
    print(key)

group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value 


#MATLAB
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')    #loads a dict with the variables : values of thingfs that were saved in the MATLAB workspace

