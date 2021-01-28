import numpy as np
from matplotlib import pyplot as plt


# our x values
ages = np.arange(25, 36)

# All developers' salary
all_dev_salary = np.array([38496, 42000, 46752, 49320, 53200, 56000,\
                           62316, 63928, 67317, 68748, 73752])
##Python developers' salary
py_dev_salary = np.array([45372, 48876, 53850, 57287, 63016, 65998,\
                          70003, 70000,71496, 75370, 83640])
average_overall = 60306.3

# create subplots
'''we can have multiple figures as well by calling subplots method multiple times'''
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)

# plot the data
ax1.plot(ages, all_dev_salary, label='All dev', linestyle='-',\
         color='#33f9f3')
ax2.plot(ages, py_dev_salary, label='Py dev', linestyle='-.',\
         marker='*')


# some specifications
ax1.set_title('Median salary of Developers')
ax2.set_xlabel('Ages')
ax1.set_ylabel('Salaries')
ax2.set_ylabel('Salaries')
ax1.legend(loc='upper left')
ax2.legend(loc='upper left')
ax1.grid(True)

# display the plots
plt.show()
