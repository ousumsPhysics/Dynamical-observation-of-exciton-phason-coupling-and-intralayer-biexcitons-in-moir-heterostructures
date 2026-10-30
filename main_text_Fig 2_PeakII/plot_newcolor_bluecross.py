import numpy as np
import sys
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as mcolors
from matplotlib.colors import LinearSegmentedColormap

def orange_cmap(name="teal_seq"):
    teal_hex = "#DC4D01"  # classic teal
    return LinearSegmentedColormap.from_list(
        name,
        [(1, 1, 1), mcolors.to_rgb(teal_hex)]
    )
cmap_or = orange_cmap()


def make_plot(Axy,np1,np2,A1,A2,dxi,xh, yh):
    xi,yi,zi = interp(Axy, np1,np2, A1, A2,dxi)
    print(np.amax(zi), np.amin(zi))
    #hm = plt.pcolormesh(xi,yi,zi,cmap = 'magma', vmin = 0.0,vmax = 653.3,shading='auto')
    #hm = plt.pcolormesh(xi,yi,zi,cmap = 'magma', vmin = 0.0,vmax = 1200,shading='auto')
    hm = plt.pcolormesh(xi,yi,zi,cmap = "Oranges", vmin = 0.0,vmax = 10000,shading='auto')
    ax.set_aspect('equal', 'box')
    #plt.xlabel("x ($\AA$)", fontsize = 18)
    #plt.ylabel("y ($\AA$)", fontsize = 18)
    ax.tick_params(labelsize=14)
    l1 = (A1 + A2)/3.
    l2 = 2*(A1 + A2)/3.
    l3 = l1 + A1/3.
    l4 = l1 + A2/3.
    plt.plot([l1[0], l3[0]],[l1[1], l3[1]], color = 'k', linestyle = '--')
    plt.plot([l1[0], l4[0]],[l1[1], l4[1]], color = 'k', linestyle = '--')
    plt.plot([l3[0], l2[0]],[l3[1], l2[1]], color = 'k', linestyle = '--')
    plt.plot([l4[0], l2[0]],[l4[1], l2[1]], color = 'k', linestyle = '--')
    plt.xlim(l1[0]-30, l2[0] + 30)
    plt.ylim(l1[1]-30, l2[1] + 30)
    plt.xticks([])
    plt.yticks([])
    xy_cart = xh*A1/3. + yh*A2/3.
    print(xh,yh)
    plt.scatter(xy_cart[0], xy_cart[1], color = 'C0', s = 100, marker = 'x', lw = 3)
    plt.plot([242,262],[60,60], lw = 3.8, color = 'k')
    plt.text(238, 47, "3 nm", color ='k', fontsize = 19)
    #plt.tight_layout()
    return(hm)
#    plt.show()


def interp(Axy, np1,np2, A1, A2,dxi):
    dA1 = A1/np1
    dA2 = A2/np2
    X = []
    Y = []
    Z = []
    for i in range(np1):
        for j in range(np2):
            xy = i*dA1 + j*dA2
            X.append(xy[0])
            Y.append(xy[1])
            Z.append(Axy[i,j])
    xi = np.arange(0.0,A1[0]*1.5,dxi)
    yi = np.arange(0.0,A1[0]*1.5,dxi)
    xi,yi = np.meshgrid(xi,yi)
    zi = griddata((X,Y),Z,(xi,yi),method='linear',fill_value = 0)
    return xi, yi, zi


A1 = np.array([25.0,    0.000000,    0.000000])*3.28*3
A2 = np.array([12.5, 21.650635093373495,    0.000000])*3.28*3


Files = ["Vol_xy_1.014420141.01568652.npy", "Vol_xy_1.33402080000099991.334770399998.npy", "Vol_xy_1.6540080000011.654931999997.npy", "Vol_xy_1.9335840000021.934831999996.npy"]

XH = [1.01442014, 1.33402080, 1.654008, 1.933584]
YH = XH

ifile = eval(sys.argv[1])
#Axy = np.load("Vol_xy_1.040429394251.04042939425.npy")
#s = A1/3. + A2/3.
fig,ax = plt.subplots(dpi = 500)
xh,yh = XH[ifile], YH[ifile]
Axy_S1 = np.load( "Data_zavg_S11/"+ Files[ifile])
Axy_S2 = np.load( "Data_zavg_S12/"+ Files[ifile])
Axy = (Axy_S1 + Axy_S2)/2.
sh = np.shape(Axy)
np1 = sh[0]
np2 = sh[1]
plt.cla()
hm = make_plot(Axy,np1,np2,A1,A2,0.15, xh,yh)
#cbar = plt.colorbar(hm)
cbar = plt.colorbar(hm, ticks=[0, 10000], fraction = 0.05)
cbar.ax.set_yticklabels(['0', 'max/3'])
cbar.ax.tick_params(labelsize=18)
#plt.savefig("PeakI.svg",  format = 'svg', dpi = 500)
plt.tight_layout()
plt.savefig("PeakII" + str(xh) + ".png", dpi = 500)
#plt.savefig("PeakI.svg",  format = 'svg', dpi = 500)
plt.show()
