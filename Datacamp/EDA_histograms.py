# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Compute number of data points: n_data
n_data = len(versicolor_petal_length)

# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)

# Convert number of bins to integer: n_bins
n_bins = int(n_bins)

# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length, bins=n_bins)
plt.xlabel('petal length (cm)')
plt.ylabel('count')

# Show histogram
plt.show()