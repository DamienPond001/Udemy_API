# Create the DataFrame: usa
usa = medals[medals.NOC == "USA"]

# Group usa by ['Edition', 'Medal'] and aggregate over 'Athlete'
usa_medals_by_year = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

#unstacks the Edition index, keeps Medal as index
# Reshape usa_medals_by_year by unstacking
usa_medals_by_year = usa_medals_by_year.unstack(level="Medal")

# Plot the DataFrame usa_medals_by_year
usa_medals_by_year.plot()
plt.show()
