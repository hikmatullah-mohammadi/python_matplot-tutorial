# import required libraries
from matplotlib import pyplot as plt
from datetime import datetime
import pandas as pd
import numpy as np

# load data
data = np.loadtxt('wind.data')
# median for each row
median_w_s = data[:30, 3:].mean(axis=-1)

# first January
dates_ = np.array(data[:30, :3])

dates = []
for i in dates_:
    dates.append('19'+str(i).strip('[]'))

# convert to datetime
dates = pd.to_datetime(dates).sort_values()

# plot the data
plt.plot_date(dates, median_w_s, linestyle='-.')

# auto format the dates
plt.gcf().autofmt_xdate()

plt.title('median wind speed each day in first month')
# display the figure
plt.show()
