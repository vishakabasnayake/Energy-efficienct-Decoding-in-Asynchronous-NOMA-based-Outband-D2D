import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

#priority: 4

time = (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
conv1= (14.9172351991285,
11.3478347059128,
9.15400738529980,
7.67167770203235,
6.60390513088856,
5.79847705898559,
5.16945233831367,
4.66468249776597,
4.25070752988302,
3.90508050694700,
3.61218471516772,
3.36082126193513,
3.14275103298148,
2.95177802127491,
2.78315329693414,
2.63317603496678,
2.49891959169003,
2.37803919058227,
2.26863420284123)

proposed1 = (14.9172351991285,
13.7499438557905,
12.6249344262444,
11.6556343835349,
10.8319305836033,
10.1283507730902,
9.52166925284191,
8.99330075186768,
8.52879998928745,
8.11695844853108,
7.74901402172834,
7.41804449099229,
7.11851907393784,
6.84596939698607,
6.59674720755046,
6.36784445420309,
6.15675829725003,
5.96138872090470,
5.96138872090470)


conv2=(14.9172,
   11.1568,
    8.5618,
    6.2637,
    4.8257,
    3.9236,
    3.5474,
    3.4265,
    3.4265,
    3.4265,
    3.4265,
    3.2168,
    3.1315,
    3.1253,
    3.0662,
    3.0809,
    3.031,
    2.931,
    2.93)

prop2=(14.9172,
   12.8849,
   10.4148,
    8.6627,
    8.3384,
    6.3779,
    6.1568,
    6.1568,
    6.1568,
    6.1568,
    6.1368,
    6.1068,
    6.07254,
    5.956941,
    5.93627,
    5.9314,
    5.8000,
    5.7000,
    5.7000)

conv3 = (14.9172,
10.6165,
8.938,
6.8062,
6.2844,
5.3866,
5.1364,
4.2566,
4.2394,
3.7154,
3.5127,
3.1584,
2.9102,
2.3425,
2.4178,
2.333,
2.2526,
2.1435,
2.1432)

prop3 = (14.9172,
   12.9058,
   11.5563,
   10.1787,
    9.0369,
    8.1582,
    7.4361,
    6.6944,
    6.1336,
    5.5900,
    5.1004,
    4.5123,
    4.0827,
    3.8098,
    3.5138,
    3.2996,
    3.1583,
    2.9232,
    2.9203
)

conv4 = (14.9172,
10.6165,
8.938,
7.1143,
6.5925,
5.6946,
5.4444,
4.7577,
4.3204,
3.7964,
3.5937,
3.334,
3.2025,
3.0067,
2.9966,
2.6324,
2.5747,
2.3308,
2.3332
)
prop4 = (14.9172,
   13.4200,
   12.3100,
   11.2501,
   10.4175,
    9.7058,
    9.1176,
    8.5847,
    8.0733,
    7.5778,
    7.1001,
    6.6282,
    6.1869,
    5.7909,
    5.4219,
    5.0759,
    4.7309,
    4.3960,
    4.3978)

f, ax1 = plt.subplots()
#ax1.set_yscale('log')
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, proposed1, color="black",marker=".", markersize=5, label=r'sequential T-SIC $E_{th}$=0.5 mW ')
lns2 = ax1.plot(time, conv1,color="peru",marker=".",linestyle='dashed', markersize=5,  label=r'conv T-SIC $E_{th}$=0.5 mW' )
lns7 = ax1.plot(time, prop4, color="black",marker="x", markersize=5, label=r'sequential T-SIC $E_{th}$= 0.8 mW')
lns8= ax1.plot(time, conv1,color="peru",marker="d",linestyle='dashed', markersize=5,  label=r'conv T-SIC $E_{th}$ = 0.8 mW')
lns5 = ax1.plot(time, prop3, color="black",marker="p", markersize=5, label=r'sequential T-SIC $E_{th}$= 1.2 mW')
lns6= ax1.plot(time, conv1,color="peru",marker="x",linestyle='dashed', markersize=5,  label=r'conv T-SIC $E_{th}$ = 1.2 mW')

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
ax1.set_ylim(0.1,20)  # most of the data
ax1.set_xlim(1, 20.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1.5,205.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Total number of transmitters (K)",fontname="Arial",fontsize=14)
plt.ylabel(r"Energy efficiency (bits/Joules)",fontname="Arial",fontsize=14)
plt.show()
