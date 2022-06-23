import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

#ee vs min rate constraint

#time = (1e-6,1e-5,1e-4,0.001,0.01,0.05,0.1,0.25,0.5,0.75,1,2,3,4,5,6,7,8,9,10)
time = (1,1e1,1e2,1e3,1e4,5e4,1e5,2.5e5,5e5,7.5e5,1e6,2e6,3e6,4e6,5e6,6e6,7e6,8e6,9e6,1e7)
conv1= (26.84,
26.84,
26.84,
26.84,
26.84,
26.84,
26.84,
26.84,
26.84,
26.84,
25.84,
21.472,
16.104,
10.736,
5.368,
0,
0,
0,
0,
0)

proposed1 = (34.6519,
   34.6519,
   34.6519,
   34.6519,
   34.6519,
   34.6519,
   34.6519,
   34.6519,
   33.6519,
   32.2658,
   30.4937,
   26.3354,
   20.7911,
   18.8607,
    8.3164,
    4.1582,
    1.3861,
         0,
         0,
         0)

conv2= (18.4377,
   18.4377,
   18.4377,
   18.4377,
   18.4377,
   18.4377,
   18.4377,
   18.4377,
   16.4377,
   12.4377,
   6.1516,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0)

proposed2 = (33.0053,
   33.0053,
   33.0053,
   33.0053,
   33.0053,
    33.0053,
    33.0053,
    30.0053,
    23.0053,
    13.1223,
    6.5213,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
)

conv3 = (14.0156,
   14.0555,
   14.02072,
   14.09114,
   14.0552,
   13.5188,
   12.3826,
    10.9464,
    8.1512,
    6.7151,
    5.6380,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0)

proposed3 = (24.7222,
   24.7222,
   24.7222,
   24.7222,
   24.5146,
   23.1314,
   20.6418,
   17.0458,
   12.5509,
    8.9549,
    6.2579,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0)

conv4 = (9.2442,
    9.2442,
    9.2442,
    9.2442,
    9.1625,
    8.9991,
    8.7541,
    7.2273,
    5.0188,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0)

prop4=(15.9352,
   15.9352,
   15.9352,
   15.9352,
   15.9248,
   15.2040,
   13.0728,
   11.4312,
   8,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0)

conv5 = (7.3464,
    7.0585,
    6.7349,
    6.4442,
    6.1800,
    4.9300,
    3.7522,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0)

prop5 = (12.6290,
    12.6763,
   12.6582,
   12.5662,
   12.4994,
   11.4855,
   10.2245,
   8.6763,
   6.6763,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0,
   0)

f, ax1 = plt.subplots()
ax1.set_xscale('log')
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, proposed1, color="navy",marker="p", markersize=7, label=r'sequential T-SIC $K$ = 3')
lns2 = ax1.plot(time, conv1,color="saddlebrown",marker="d", markersize=7,  label=r'conv T-SIC $K$ = 3')
#lns3 = ax1.plot(time, proposed2, color="navy",marker="p", linestyle='dotted',markersize=7, label=r'sequential T-SIC $k$ = 5')
#lns4 = ax1.plot(time, conv2,color="saddlebrown",marker="d",linestyle='dotted', markersize=7,  label=r'conv T-SIC $k$ = 5')
lns5 = ax1.plot(time, proposed3, color="navy",marker="p",linestyle='dashdot', markersize=7, label=r'sequential T-SIC $K$ = 8')
lns6= ax1.plot(time, conv3,color="saddlebrown",marker="d",linestyle='dashdot', markersize=7,  label=r'conv T-SIC $K$ = 8')
lns5 = ax1.plot(time, prop5, color="navy",marker="p", linestyle='dashed',markersize=7, label=r'sequential T-SIC $K$ = 20')
lns6= ax1.plot(time, conv5,color="saddlebrown",marker="d",linestyle='dashed', markersize=7,  label=r'conv T-SIC $K$ = 20')

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
ax1.set_ylim(-0.5,55)  # most of the data
ax1.set_xlim(0.75, 1e7)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1.5,205.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Minimum rate constraint (bits/s)",fontname="Arial",fontsize=14)
plt.ylabel(r"Energy efficiency (bits/Joules)",fontname="Arial",fontsize=14)
plt.show()
