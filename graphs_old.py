import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.loadtxt("/home/nisrael/example_code/test.dat", unpack = True)
N=len(x)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

ax = plt.subplot(111)
df1 = pd.DataFrame(x,
                   index=["A", "B"])
df2 = pd.DataFrame(x,
                   index=["A", "B"])


# Then, just call :
plot_clustered_stacked([df1, df2],["df1", "df2"])
#p1 = ax.bar(ind, x, width)
#ax.bar(x-0.2, y,width=0.2,color='b',align='center')
#ax.bar(x, z,width=0.2,color='g',align='center')
#ax.bar(x+0.2, k,width=0.2,color='r',align='center')
#p2 = plt.bar(ind, y, width, bottom=x)

#ax.ylabel('Scores')
#plt.title('Scores by group and gender')
#plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
#ax.yticks(np.arange(0, 100, 10))
#plt.legend((p1[0], p2[0]), ('Feature', 'Women'))

#plt.show()
