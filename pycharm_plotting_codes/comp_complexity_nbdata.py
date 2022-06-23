import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

time = (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

proposed = (4.6052,
9.4907,
13.34266,
17.08796,
20.34498,
23.46898,
26.53684,
29.6456,
32.74572,
35.55738,
37.98532,
40.0887,
42.53322,
46.16914,
52.81784,
62.79512,
78.78638,
96.17283333,
123.4186
)

conv = (4,
9,
16,
25,
36,
49,
64,
81,
100,
121,
144,
169,
196,
225,
256,
289,
324,
361,
400)

f, ax1 = plt.subplots()

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, proposed, color="black",marker=".", markersize=7, label=r'sequential T-SIC')
lns2 = ax1.plot(time, conv,color="peru",marker="d",linestyle='dashed', markersize=7,  label=r'conv T-SIC')
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
ax1.set_ylim(-0.1,415)  # most of the data

ax1.set_xlim(1, 20.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
#plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
#plt.text(1.5,255.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Total number of transmitters (K)",fontname="Arial",fontsize=14)
plt.ylabel(r"Theoretical computational complexity",fontname="Arial",fontsize=14)
plt.show()
