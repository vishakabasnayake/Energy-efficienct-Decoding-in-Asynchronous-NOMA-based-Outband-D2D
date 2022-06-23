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
10)

conv= (
0.0565104268,
3.22E-02,
1.68E-02,
0.007774570138,
0.002994509731,
0.0009149277766,
0.0002275794829,
4.03E-05,
4.78E-06,
3.28E-07)

proposed = (
0.03482658312,
1.98E-02,
1.03E-02,
0.004784636728,
0.001836139717,
0.0005614667082,
0.0001495544815,
2.69E-05,
3.19E-06,
2.17E-07)

convw= (
    0.1115,
    0.1008,
    0.0718,
    0.0508,
    0.0297,
    0.0151,
    0.0084,
    0.0063,
    0.0063,
    0.0063)

proposedw = (
0.1046,
0.0688,
0.0470,
0.0268,
0.0147,
0.0075,
0.0040,
0.0027,
0.0025,
0.0025
)

convi= (
0.1124359807,
0.07008661238,
0.04634468244,
0.02421694375,
0.0114514016,
0.004746304089,
0.001656310181,
0.0006728160686,
0.0004728160686,
0.0004728160686
)

proposedi = (
0.06945616623,
0.04313337167,
0.02850885331,
0.01483653075,
0.006991319383,
0.002908536903,
0.001012228594,
0.0004916020238,
2.97E-04,
2.97E-04,
)

f, ax1 = plt.subplots()
ax1.set_yscale('log')
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
#strongest user
lns1 = ax1.plot(time, proposed, color="black",marker=".", markersize=5, label=r'sequential T-SIC (nearest user)')
lns2 = ax1.plot(time, conv,color="peru",marker=".",linestyle='dashed', markersize=5,  label=r'conv T-SIC (nearest user)')

#intermediate user
lns1 = ax1.plot(time, proposedi, color="black",marker="x", markersize=5, label=r'sequential T-SIC (middle user)')
lns2 = ax1.plot(time, convi,color="peru",marker="x",linestyle='dashed', markersize=5,  label=r'conv T-SIC (middle user)')


#weakest user
lns1 = ax1.plot(time, proposedw, color="black",marker="p", markersize=5, label=r'sequential T-SIC (farthest user)')
lns2 = ax1.plot(time, convw,color="peru",marker="p",linestyle='dashed', markersize=5,  label=r'conv T-SIC (farthest user)')
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
ax1.set_ylim(-0.0,0.4)  # most of the data
ax1.set_xlim(-0.2, 10.2)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
plt.text(0.2,0.25e-3,'number of transmitters: 10',fontsize=13,fontname="Arial")
#plt.text(1.5,255.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"received power ratio",fontname="Arial",fontsize=14)
plt.ylabel(r"Theoretical bit error rate (BER)",fontname="Arial",fontsize=14)
plt.show()
