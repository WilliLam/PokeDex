import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
pokedex = pd.read_csv("pokemon.csv")

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
	print(pokedex.describe())

# par = np.polyfit(pokedex['Attack'], pokedex['Defense'], 1, full=True)
# for i in pokedex:
	# i['']
aodratio = pokedex['Attack']/pokedex['Defense']

print(aodratio)
print(aodratio.name)
aodratio.rename_axis("aodratio")

pokedex['aodratio'] = aodratio
get3s = pokedex.sort_values(['aodratio'])
print(get3s[-3:]) #top3
print(get3s[:3]) #bottom3

plt.scatter(pokedex['Attack'], pokedex['Defense'],marker='x' )
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.plot()
# plt.show()

victories = pd.read_csv("combats.csv")
# print(victories)
victories.sort_values(['Winner'])
victcount = Counter()
# for i, r in victories.iterrows():
# 	victcount[r['Winner']] +=1
# for i in victcount.most_common(10):
# 	print(i[1],'wins\n', pokedex.iloc[i[0]-1, 1])
# print('Most wins:' , victcount.most_common(10))
#
# grasspokes = pokedex.loc[(pokedex['Class 1'] == 'Grass') | (pokedex['Class 2'] == 'Grass')]
# rockpokes = pokedex.loc[(pokedex['Class 1'] == 'Rock') |( pokedex['Class 2'] == 'Rock')]
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
# 	print('grass pokemon stats \n' ,grasspokes.describe())
# 	print('rock pokemon stats \n', rockpokes.describe())
#
print(list(pokedex))
pokedex['Total stats'] = pokedex.iloc[:, 4:10].sum(axis=1)
print(pokedex)
print(('Mega' in pokedex['Name']))
thing = pokedex.loc[(pokedex['Name'] == '')]
print(thing)
for i, r in pokedex.iterrows():
	print(r['Name'], type(r'Name'))
for i, r in pokedex.iterrows():
	print(str(r['Name']))
	if "Mega" in str(r['Name']):
		pokedex.loc[i, 'Mega'] = 'True'
	else:
		pokedex.loc[i, 'Mega'] = 'False'
#  = sum(pokedex.iloc[:, 5:8])

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
	# pass
	print((pokedex))


