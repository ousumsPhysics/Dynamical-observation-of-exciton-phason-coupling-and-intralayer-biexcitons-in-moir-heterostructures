from numpy import *
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (6.5/2.54,5.5/2.54)
#plt.rcParams.update({'font.size': 8, 'font.family':'Helvetica'})
plt.rcParams['axes.linewidth'] = 0.5

# find absorbance
c = 1973 
d = 9.5   

def Abs(eps2, omega):
    return eps2*omega*(d/c)*100

def main():
    # read the output file
    a = loadtxt('./abs_Kucbare.txt')
    #g_dft = 1.6
    soc_red = (1.3984 - 1.6936)
    g_dft_soc = 1.307
    g_gw_soc = 2.262 
    g_gw_nosoc = 2.259 
    g_dft_nosoc = 1.635
    print("QP_gap",g_gw_soc)
    QP_sh = g_gw_nosoc - g_dft_nosoc + soc_red #+ moire_sh
    print("QP_sh: ", QP_sh)
    print("QP_sh SOC: ", QP_sh - soc_red)
    fig, ax = plt.subplots(figsize = (8,5))

    abso_2p3 = Abs(a_2p3[:,1], a_2p3[:,0])
    omega_2p3 = a_2p3[:,0] +  QP_sh
    abso = Abs(a[:,1], a[:,0])
    omega = a[:,0] +  QP_sh
    plt.plot(omega, abso, c='k', label='PUMP',
            ls='-',lw=2.75)
    plt.xlabel('Photon energy (eV)', fontsize=26)
    plt.ylabel('Absorbance (%)', fontsize=26)
    plt.xlim(1.5, 1.85)
    ax.tick_params(axis='both', labelsize=24)
    plt.minorticks_on()
    plt.tick_params(width=3.5)

    for location in ['left', 'right', 'top', 'bottom']:
        ax.spines[location].set_linewidth(2.0)
    plt.tight_layout()
    plt.savefig('WSe2WS2_intra.png', dpi=400, bbox_inches='tight')
    plt.show()

    return None



def read_absorption_noeh(fn):
    f = open(fn)
    # 4 lines in absorption_noeh.dat are descriptions of datastructure.
    f.readline()
    f.readline()
    f.readline()
    f.readline()

    # Read whole data at once.
    lines = f.readlines()

    num_omega = len(lines)
    omega = zeros(num_omega)
    eps2 = zeros(num_omega)
    eps1 = zeros(num_omega)
    jdos = zeros(num_omega)

    for i, line in enumerate(lines):
        omega[i], eps2[i], eps1[i], jdos[i] = float64(line.split())

    return omega, eps2, eps1, jdos


#def read_absorption_noeh(fn):
#    f = open(fn)
#    # 4 lines in absorption_noeh.dat are descriptions of datastructure.
#
#    # Read whole data at once.
#    lines = f.readlines()
#
#    num_omega = len(lines)
#    omega = zeros(num_omega)
#    eps2 = zeros(num_omega)
#    eps1 = zeros(num_omega)
#    jdos = zeros(num_omega)
#
#    for i, line in enumerate(lines):
#        omega[i], eps2[i] = float64(line.split())
#
#    return omega, eps2

if __name__=='__main__':
    main()
