import numpy as np

city1=[30,32,31,29]
city2=[25,26,24,25]
city3=[35,38,36,37]

cities=[city1,city2,city3]

for i,c in enumerate(cities):
    print("Mean:",np.mean(c),"Std:",np.std(c))

ranges=[max(c)-min(c) for c in cities]
print("Highest range city:",ranges.index(max(ranges))+1)
print("Most consistent city:",ranges.index(min(ranges))+1)
