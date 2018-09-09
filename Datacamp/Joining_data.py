#Row concatenation
row_concat = pd.concat([uber1, uber2, uber3])
#where each is a df
#Note though that the original row indices will be maintained
#Use the ignore_index = True to reset the indices in sequential order

#Use the axis =1 to do column concatenation

#If we have many files to concatenate:
# Import necessary modules
import glob
import pandas as pd

# Write the pattern: pattern
pattern = '*.csv'
# * = all strings 
# ? = single character

# Save all file matches: csv_files
csv_files = glob.glob(pattern)
#this gives a list of files that match the pattern

# Create an empty list: frames
frames = []

#  Iterate over csv_files
for csv in csv_files:

    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)
    
    # Append df to frames
    frames.append(df)

# Concatenate frames into a single DataFrame: uber
uber = pd.concat(frames)