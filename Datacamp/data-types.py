# Convert the sex column to type 'category'
tips.sex = tips.sex.astype('category')  #converting to categorical vars helps with memory and further analysis

# Convert the smoker column to type 'category'
tips.smoker = tips.smoker.astype('category')

# Print the info of tips
print(tips.info())

#sometimes we may need to tell python how to deal with values it can't convert
tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors='coerce')
