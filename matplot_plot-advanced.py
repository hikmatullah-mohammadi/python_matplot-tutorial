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

# plot our data
plt.plot(ages, all_dev_salary, label='All dev', linestyle='-')
plt.plot(ages, py_dev_salary, label='Py dev', linestyle='-.', marker='*')

# fill some specific locations
plt.fill_between(ages, y1=py_dev_salary, y2=average_overall,\
                 where=(py_dev_salary>average_overall), interpolate=True,\
                 label='Above the median', alpha=0.75)

plt.fill_between(ages, y1=py_dev_salary, y2=average_overall,\
                 where=(py_dev_salary<average_overall), interpolate=True,\
                 label='Under the median', color='red', alpha=0.75)


# some specifications
plt.title('Median salary of Developers')
plt.xlabel('Ages')
plt.ylabel('Salary')
plt.legend(loc='upper left')

plt.show()
