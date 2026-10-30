import sys, string
import numpy as np
import matplotlib.pyplot as plt

#E1 = np.load("Eig_bk_trunc.npy")
#E2 = np.load("Eig_bk_trunc_redo.npy")
E = np.load("Eig_bk_trunc.npy")
Nk = 12
nb, nk = E.shape


print(E.shape)
fig, ax = plt.subplots()
K = range(nk)
for i in range(nb):
    #ax.plot(K,E1[i] - E1[49,0]  ,color = 'k',linewidth=1.8)
    #ax.plot(K,E2[i] - E2[51,0]  ,color = 'C0',linewidth=1.8, linestyle = '--')
    ax.plot(K,E[i] - E[50,0]  ,color = 'k',linewidth=1.8, linestyle = '-')

#E_corr = np.load("../Bands/Eig_bk_trunc.npy")
#evb_corr = -4.054900
#for i in range(nb):
#    ax.plot(K,E_corr[i] - evb_corr  ,color = 'r',linewidth=1.8, linestyle = '--')


yl = 1.6
yu = 1.85
ax.plot([4,4],[yl,yu],linewidth=3.0,color='k')
ax.plot([7,7],[yl,yu],linewidth=3.0,color='k')
plt.ylim(yl,yu)
plt.xlim(0,11)
ax.set_xticks([0,4,7,11])
ax.set_xticklabels(["$\gamma$",r"$\mu$",r"$\kappa$", "$\gamma$"],fontsize = 20)
ax.tick_params(labelsize = 18)
plt.ylabel("Energy (eV)", fontsize = 18)
plt.tight_layout()
plt.savefig("cb", dpi = 300)
plt.show()
