import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager
#plt.rcParams['text.usetex'] = True
rc('mathtext', default='regular')

time = (1e1,
   1.3e1,
   1.6e1,
   2e1,
   2.3e1,
   2.5e1,
   2.6e1,
   3e1,
   3.3e1,
   3.6e1,
   4e1,
   4.4e1,
   5e1,
   5.7e1,
   6.6e1,
   8e1,
  1e2,
  1.2e2)
conv = (14.0156,
   14.0156,
   14.0156,
   14.0156,
   14.0156,
   14.0156,
   13.7198,
   13.4240,
   13.1283,
   12.8325,
   12.5368,
   10.7416,
    8.9464,
    7.1512,
    5.3560,
    3.5609,
    3.5609,
    3.5609)
proposed = (41.22,
   41.22,
   41.22,
   41.22,
   41.22,
   41.22,
   41.22,
   40.22,
   37.0496,
   32.6981,
   23.8466,
   19.9630,
   16.0795,
   12.1959,
    8.3124,
    4.4288,
    4.4288,
    4.4288)

conv2 = (12.5368,
12.5368,
12.5368,
12.5368,
1.25E+01,
12.5368,
12.5368,
10.7416,
8.9464,
7.1512,
5.356,
3.5609,
3.5609,
3.5609,
3.5609,
3.5609,
3.5609,
3.5609)

prop2 = (24.1586,
24.1586,
24.1586,
24.1586,
24.1586,
2.42E+01,
2.42E+01,
22.0391,
15.9195,
11.8,
7.6804,
4.5609,
3.5609,
3.5609,
3.5609,
3.5609,
3.5609,
3.5609)

conv3 = (5.6145,
5.6145,
5.6145,
5.93E+00,
6.2495,
6.567,
6.8844,
5.9984,
4.7949,
3.5913,
2.3878,
1.1843,
1.1843,
1.1843,
1.1843,
1.1843,
1.1843,
1.1843)


prop3 = (9.1523,
9.1523,
9.1523,
10.7691,
12.3859,
14.0028,
15.6196,
14.0261,
10.8156,
7.6052,
4.3947,
1.1843,
1.1843,
1.1843,
1.1843,
1.1843,
1.1843,
1.1843)

conv4 = (6.2541,
6.2541,
6.2541,
6.2541,
6.2541,
6.2541,
5.893,
5.717,
5.541,
5.541,
4.5815,
3.6221,
2.6626,
1.7031,
0.7436,
0.7436,
0.7436,
0.7436)

prop4 = (14.5166,
14.5166,
14.5166,
14.5166,
14.5166,
14.5166,
14.5166,
14.5166,
14.5166,
13.5166,
11.762,
9.0074,
6.2528,
3.4982,
1.7436,
0.7436,
0.7436,
0.7436)
f, ax1 = plt.subplots()

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, proposed, color="navy",marker="p", markersize=7, label=r'sequential T-SIC $K$ = 3')
lns2 = ax1.plot(time, conv ,color="sandybrown",marker="d", markersize=7,  label=r'conv T-SIC K = 3')
lns3 = ax1.plot(time, prop2, color="navy",marker="p", linestyle='dashed',markersize=7, label=r'sequential T-SIC $K$ = 8')
lns4 = ax1.plot(time, conv2 ,color="saddlebrown",marker="d",linestyle='dashed', markersize=7,  label=r'conv T-SIC K = 8')
#lns5 = ax1.plot(time, prop3, color="crimson",marker="p", markersize=7, label=r'sequential T-SIC k = 15')
#lns6 = ax1.plot(time, conv3 ,color="purple",marker="d",linestyle='dashed', markersize=7,  label=r'conv T-SIC k = 15')
lns5 = ax1.plot(time, prop4, color="navy",marker="p", linestyle='dashdot',markersize=7, label=r'sequential T-SIC K = 20')
lns6 = ax1.plot(time, conv4 ,color="peru",marker="d",linestyle='dashdot', markersize=7,  label=r'conv T-SIC K = 20')
lns = lns1
      #+lns2
labs = [l.get_label() for l in lns]

ax1.legend(loc=2, fontsize=10)

font = font_manager.FontProperties(family='Arial', style='normal', size=12)
ax1.legend(prop=font)

d = .015  # how big to make the diagonal lines in axes coordinates
#ax1.set_xticks(time)
for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")
ax1.set_ylim(-0.1,45)  # most of the data
ax1.set_xlim(00.0, 125.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
#plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
#plt.text(1.5,255.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
#plt.xlabel(r"Sum of total interference on each user data constraint (W)",fontname="Arial",fontsize=14)
plt.xlabel(r"Total interference constraint (W)",fontname="Arial",fontsize=14)
plt.ylabel(r"Energy efficiency (bits/Joules)",fontname="Arial",fontsize=14)
plt.show()
