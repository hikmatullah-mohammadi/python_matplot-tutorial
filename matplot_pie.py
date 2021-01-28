import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

# read data
data = pd.read_csv('survey_result_langs.csv')
langs = data['Languages']

# count the papularity of languages    
langs_counter = Counter()
for record in langs:
    langs_counter.update(str(record).split(';'))
langs_counter = langs_counter.most_common(5)

# make two lists languages and their popularity
langs = [i[0] for i in langs_counter]
papularity = [i[1] for i in langs_counter]
explode = [0, 0, 0, 0.1, 0]


plt.pie(papularity, labels=langs, autopct='%.2f%%', \
        wedgeprops={'edgecolor':'black'}, shadow=True, explode=explode)

# specify the plot( add details)
plt.style.use('fast')
plt.title('Programming Languages Popularity on stack overfow(2020)')


# show the bar
plt.show()
