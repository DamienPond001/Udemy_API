import numpy as np

np.mean(data)
np.median(data)
np.var(versicolor_petal_length)
np.std(versicolor_petal_length)

#covariance matrix: 
# returns a 2D array where entries [0,1] and [1,0] are the covariances.
# Entry [0,0] is the variance of the data in x, and entry [1,1] is the variance of the data in y
np.cov(versicolor_petal_length, versicolor_petal_width)

def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x,y)

    # Return entry [0,1]
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length, versicolor_petal_width)

# Print the result
print(r)


# Specify array of percentiles: percentiles
percentiles = np.array([2.5, 25, 50, 75, 97.5])

# Compute percentiles: ptiles_vers
ptiles_vers= np.percentile(versicolor_petal_length, percentiles)

# Print the result
print(ptiles_vers)


# Create box plot with Seaborn's default settings
_ = sns.boxplot(x='species', y='petal length (cm)', data=df)

# Label the axes
plt.xlabel('species')
plt.ylabel('petal length (cm)')

# Show the plot
plt.show()
