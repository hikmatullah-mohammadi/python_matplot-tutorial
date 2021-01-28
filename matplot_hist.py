from matplotlib import pyplot as plt
import pandas as pn
import numpy as np
# load the data and take ages
data = pn.read_csv('survey_results.csv')
ages = data['Age']
ages = np.array([age for age in ages if not str(age).isalpha()])

median_age = ages.mean()
# groups of ages
bins = [i for i in range(10, 101, 10)]


# plot the data
plt.hist(ages, bins=bins, edgecolor='black', log=True)


# to draw a line indicating the median age
plt.axvline(median_age, color='red', label='Median age', linewidth=0.5)



plt.title('Ages of voters at stack overflow survey (2020)')
plt.xlabel('Ages')
plt.xlabel('Number of devs')
plt.legend()
plt.show()
