import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

#priority: 4

time = (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
conv1= (5.09E-05,
1.11E-04,
1.64E-04,
2.10E-04,
2.60E-04,
3.10E-04,
3.57E-04,
4.06E-04,
4.56E-04,
5.07E-04,
5.56E-04,
6.10E-04,
6.61E-04,
7.09E-04,
7.62E-04,
8.21E-04,
8.69E-04,
9.24E-04,
9.73E-04)

proposed1 = (0.000809186,
0.0012185453,
0.001539575,
0.0020487583,
0.0023681107,
0.0026864127,
0.00349547,
0.0039054671,
0.0047137402,
0.0055221918,
0.0063318529,
0.0068413818,
0.0076512636,
0.0081605561,
0.0089700752,
0.0094781883,
0.0098866581,
0.0102937679,
0.0104937679)

proposed2 = (0.0002,
0.0006083042,
0.0008083042,
0.0012169348,
0.0020264135,
0.0025346004,
0.003044295,
0.0035529599,
0.0038697548,
0.0046783489,
0.005087252,
0.0058959435,
0.0063040778,
0.0071128396,
0.0074306294,
0.0077489398,
0.0085578865,
0.0093665321,
0.0097753731)

prop3 = (0.0008100635,
0.0012195207,
0.0017283554,
0.0025376941,
0.0030461211,
0.0035550964,
0.0037550964,
0.0039550964,
0.0047650196,
0.0052731716,
0.0060814184,
0.0068897129,
0.0070897129,
0.0078986563,
0.0087065733,
0.0095152035,
0.0103236033,
0.0111330174,
0.0113330174)

f, ax1 = plt.subplots()
ax1.set_yscale('log')
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, proposed2, color="blue",marker="p", markersize=7, label=r'sequential T-SIC $E_{th} = 0.8 mW$  ')
lns1 = ax1.plot(time, prop3, color="navy",marker="p", markersize=7, label=r'sequential T-SIC $E_{th} = 0.5 mW$  ')
lns1 = ax1.plot(time, proposed1, color="lightblue",marker="p", markersize=7, label=r'sequential T-SIC $E_{th} = 1.2 mW$  ')
lns2 = ax1.plot(time, conv1,color="saddlebrown",marker="d", markersize=7,  label=r'conv T-SIC ' )

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
ax1.set_ylim(2e-5,2e-1)  # most of the data
ax1.set_xlim(1, 20.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1.5,205.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Total number of superimposed data",fontname="Arial",fontsize=14)
plt.ylabel(r"Total SIC decoding delay (sec)",fontname="Arial",fontsize=14)
plt.show()
