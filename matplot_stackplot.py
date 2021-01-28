from matplotlib import pyplot as plt


# minutes in a game
minutes = [1,2,3,4,5,6,7,8,9]

# players' marks  according to minutes
player_1 = [1,1,2,3,4,4,4,5,5]
player_2 = [0,0,0,2,3,4,4,4,5]
player_3 = [0,0,1,3,4,4,5,5,5]

labels = ['player_1', 'player_2', 'player_3']
plt.stackplot(minutes, player_1,player_1, player_2, player_3, labels = labels)



# some specificatons
plt.title('My Stack Plot')
plt.xlabel('minutes')
plt.legend(loc='upper left')
plt.tight_layout()

plt.show()
