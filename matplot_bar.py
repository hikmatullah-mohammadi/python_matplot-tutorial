import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter



data = pd.read_csv('survey_result_langs.csv')
langs = data['Languages']

counter = Counter()
for record in langs:
    langs = str(record).split(';')
    counter.update(langs)

counter = counter.most_common()
counter.reverse()

langs = list(i for i,j in counter)
popularity = list(j for i,j in counter)


plt.barh(langs, popularity)

# specify the plot( add details)
plt.style.use('fast')
plt.title('Programming Languages Popularity on stack overfow(2020)')

plt.xlabel('Popularity')

# show the bar
plt.show()
