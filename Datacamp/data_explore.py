import pandas as pd

df = pd.read_csv('....')

df.head()
df.tail()
df.columns
df.shape

#Display summary stats of numeric columns
df.describe()


#Display frequencies of categorical columns
df['Borough'].value_counts(dropna=False)

#display means and counts of columns
df[['col1', 'col2']].count()
df[['col1', 'col2']].mean()

df['2015'].quantile([0.05, 0.95])

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()

# Create the boxplot
df.boxplot(column='initial_cost', by='Borough', rot=90)

# Display the plot
plt.show()