import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

time = (2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

conv= (
0.0016,
0.0039,
0.0064,
0.0094,
0.0126,
0.0164,
0.0208,
0.0255,
0.031,
0.0373,
0.0439,
0.0501,
0.0556,
0.0601,
0.0641,
0.0673,
0.0726,
0.0776,
0.0877)

proposed = (
0.0013,
0.0028,
0.0045,
0.0063,
0.0081,
0.0102,
0.0126,
0.0151,
0.0182,
0.0218,
0.0256,
0.0293,
0.0327,
0.0353,
0.0375,
0.039,
0.0413,
0.0433,
0.0478)

convw= (
0.0001,
0.0074,
0.0109,
0.0158,
0.0202,
0.0264,
0.0312,
0.0314,
0.029,
0.0378,
0.0362,
0.0414,
0.0519,
0.0582,
0.0629,
0.0678,
0.0654,
0.0706,
0.0617)

proposedw = (
0.0001,
0.0052,
0.0075,
0.0104,
0.013,
0.0171,
0.0201,
0.0201,
0.019,
0.0239,
0.0222,
0.0235,
0.0287,
0.0321,
0.0351,
0.0385,
0.0369,
0.0404,
0.0317)

convi= (
0.01,
0.0932,
0.1308,
0.1827,
0.2175,
0.2101,
0.2218,
0.2807,
0.3305,
0.3652,
0.4464,
0.4832,
0.5323,
0.5841,
0.6212,
0.6646,
0.7176,
0.6976,
0.6866
)

proposedi = (
0.0094,
0.0664,
0.0898,
0.1181,
0.1415,
0.1287,
0.1381,
0.1625,
0.1771,
0.1869,
0.2218,
0.2344,
0.2543,
0.2853,
0.3042,
0.3161,
0.3344,
0.3212,
0.3143)



f, ax1 = plt.subplots()
ax1.set_yscale('log')
ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
#strongest user
lns1 = ax1.plot(time, proposed, color="black",marker=".", markersize=3, label=r'sequential T-SIC (nearest user)')
lns2 = ax1.plot(time, conv,color="peru",marker="d",linestyle='dashed', markersize=7,  label=r'conv T-SIC (nearest user)')

#intermediate user
#lns1 = ax1.plot(time, proposedi, color="navy",marker="p", markersize=7, label=r'sequential T-SIC')
#lns2 = ax1.plot(time, convi,color="saddlebrown",marker="d",linestyle='dashed', markersize=7,  label=r'conv T-SIC')


#weakest user
#lns1 = ax1.plot(time, proposedw, color="pink",marker="p", markersize=7, label=r'sequential T-SIC')
#lns2 = ax1.plot(time, convw,color="lightgreen",marker="d",linestyle='dashed', markersize=7,  label=r'conv T-SIC')
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
ax1.set_ylim(-0.0,2e-1)  # most of the data
ax1.set_xlim(1, 20.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=11)
#plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
#plt.text(1.5,255.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Total number of transmitters",fontname="Arial",fontsize=14)
plt.ylabel(r"Theoretical bit error rate (BER)",fontname="Arial",fontsize=14)
plt.show()
