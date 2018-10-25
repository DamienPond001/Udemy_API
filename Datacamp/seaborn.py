# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Plot a linear regression between 'weight' and 'hp'
sns.lmplot(x='weight', y='hp', data=auto)

# Display the plot
plt.show()

#RESIDUALS
# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot(x='hp', y='mpg', data=auto, color='green')

# Display the plot
plt.show()

#HIGHER ORDER
# Generate a scatter plot of 'weight' and 'mpg' using red circles
plt.scatter(auto['weight'], auto['mpg'], label='data', color='red', marker='o')

# Plot in blue a linear regression of order 1 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, label='order 1',  color='blue', order=1, scatter=None)

# Plot in green a linear regression of order 2 between 'weight' and 'mpg'
sns.regplot(x='weight', y='mpg', data=auto, label='order 2', color='green', order=2, scatter=None)

# Add a legend and display the plot
plt.legend(loc='upper right')
plt.show()


# Plot a linear regression between 'weight' and 'hp', with a hue (specifies categories) of 'origin' and palette of 'Set1'
sns.lmplot('weight', 'hp', data=auto, hue='origin', palette='Set1')

# Display the plot
plt.show()

# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
sns.lmplot('weight', 'hp', data=auto, row='origin')

# Display the plot
plt.show()