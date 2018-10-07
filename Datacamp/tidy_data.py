#Melting data is the process of turning columns of your data into rows of data. 
airquality_melt = pd.melt(airquality_melt, id_vars=['Month', 'Day'])
#id_vars = columns not wishing to melt
#value_vars = columns wishing to melt (deafult to all not in id_vars)

#Pivoting data is the opposite of melting it.
airquality_pivot = airquality_melt.pivot_table(index=["Month", "Day"], columns="measurement", values="reading")
#columns="measurement" : columns to pivot
#values="reading" : values to fill columns with

#the above create a heirarchical header format. To fix this:
airquality_pivot_reset = airquality_pivot.reset_index()

#Often there are duplicate values, these can be handled as follows:
airquality_pivot = airquality_dup.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)
#where the mean is taken

#Note in the below that Series atributes and functions are accessed on the .str function
# Melt ebola: ebola_melt
ebola_melt = pd.melt(ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

# Create the 'str_split' column
ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')

# Create the 'type' column
ebola_melt['type'] = ebola_melt.str_split.str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

# Print the head of ebola_melt
print(ebola_melt.head())