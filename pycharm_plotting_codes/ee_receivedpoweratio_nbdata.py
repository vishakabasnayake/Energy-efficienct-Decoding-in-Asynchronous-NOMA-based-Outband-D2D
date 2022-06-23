import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

time = (0,
1.111111111,
2.222222222,
3.333333333,
4.444444444,
5.555555556,
6.666666667,
7.777777778,
8.888888889,
10,15)

conv1= (
18.0281,
   19.1107,
   20.1601,
   21.1927,
   22.1830,
   23.1226,
   23.9959,
   24.8054,
   25.5352,
   26.2407,
   26.8400
)

proposed1 = (
21.3847,
   23.4452,
   25.5479,
   27.6470,
   29.7402,
   31.7928,
   33.7424,
   35.5780,
   37.1810,
   38.7417,
   38.7417)

conv2= (
    4.90731,
    6.2377,
    7.2123,
    8.1256,
    8.8710,
    9.4531,
    9.8720,
    10.1280,
    10.3225,
    10.3377,
10.3377
)

proposed2 = (
5.9618,
8.1172,
10.3631,
12.5636,
14.7339,
16.7653,
18.65,
20.2839,
21.8531,
23.0348,23.0348
)

conv3= (
4.4871,
    5.4706,
    5.8763,
    6.2631,
    6.4778,
    6.4466,
    6.4580,
    6.4210,
    6.4210,
    6.4210,6.4210,
)

proposed3 = (
4.9276,
6.7723,
8.2652,
9.7,
10.9061,
11.9653,
12.8804,
13.7034,
14.4833,
14.4833,14.4833
)

f, ax1 = plt.subplots()
#ax1.set_yscale('log')

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
#strongest user
lns1 = ax1.plot(time, proposed1, color="black",marker=".", markersize=5, label=r'sequential T-SIC K = 3')
lns2 = ax1.plot(time, conv1,color="peru",marker=".",linestyle='dashed', markersize=5,  label=r'conv T-SIC K = 3')

#intermediate user
lns1 = ax1.plot(time, proposed2, color="black",marker="x", markersize=5, label=r'sequential T-SIC K = 8')
lns2 = ax1.plot(time, conv2,color="peru",marker="x",linestyle='dashed', markersize=5,  label=r'conv T-SIC K = 8')


#weakest user
lns1 = ax1.plot(time, proposed3, color="black",marker="p", markersize=5, label=r'sequential T-SIC K = 20')
lns2 = ax1.plot(time, conv3,color="peru",marker="p",linestyle='dashed', markersize=5,  label=r'conv T-SIC K = 20')
lns = lns1
      #+lns2
labs = [l.get_label() for l in lns]

ax1.legend(loc=2, fontsize=10)

font = font_manager.FontProperties(family='Arial', style='normal', size=12)
ax1.legend(prop=font)

d = .015  # how big to make the diagonal lines in axes coordinates
ax1.set_xticks(time)
for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")
ax1.set_ylim(-0.0,60)  # most of the data
ax1.set_xlim(-0.0, 15.0)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
#plt.text(0.2,0.25e-3,'number of transmitters: 10',fontsize=13,fontname="Arial")
#plt.text(1.5,255.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"received power ratio",fontname="Arial",fontsize=14)
plt.ylabel(r"Energy efficiency (bits/Joules)",fontname="Arial",fontsize=14)
plt.show()
