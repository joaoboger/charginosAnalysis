import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

### Loading data ###
charginos = np.loadtxt('/home/jboger/2021.1/analysisCMSSW/charginos.txt', dtype=float, delimiter='\t',usecols=range(10))
tracks = np.loadtxt('/home/jboger/2021.1/analysisCMSSW/tracksCharginos.txt', dtype=float, delimiter='\t', usecols=range(5))

pId = []
status = []
charge = []
mass = []
pt = []
phi = []
eta = []
p = []
beta = []
gamma = []

for chargino in charginos:
    pId.append(int(chargino[0]))
    status.append(int(chargino[1]))
    charge.append(chargino[2])
    mass.append(chargino[3])
    pt.append(chargino[4])
    phi.append(chargino[5])
    eta.append(chargino[6])
    p.append(chargino[7])
    beta.append(chargino[8])
    gamma.append(chargino[9])

trackCharge = []
trackPt = []
trackPhi = []
trackEta = []
trackValidHits = []

for track in tracks:
    trackCharge.append(track[0])
    trackPt.append(track[1])
    trackPhi.append(track[2])
    trackEta.append(track[3])
    trackValidHits.append(track[4])

def histo1(data, label, nbins):
    ### Setting up MPL ###
    plt.rc('font', size=15)

    fig, axs = plt.subplots()
    fig.set_figheight(8)
    fig.set_figwidth(8)

    ### Histogram ###
    tmpData = data
    tmpData.sort()
    bins = np.linspace(tmpData[0], tmpData[-1], nbins)

    axs.hist(data, bins, density = False, color = '#5e090d', label = r'$\~{C}^{\pm 1}$')

    axs.set_xlabel(label)
    axs.set_ylabel(r"$\#_{\~{C}^{\pm 1}}$")

    axs.legend()

    plt.show()

def histo2(data1, data2, label1, label2):
    plt.rc('font', size=15)

    fig,axs = plt.subplots()
    fig.set_figheight(8)
    fig.set_figwidth(8)

    tmpData1 = data1
    tmpData1.sort()
    tmpData2 = data2
    tmpData2.sort()

    rangex = tmpData1[-1]
    rangey = tmpData2[-1]
    h = axs.hist2d(data1, data2, bins = 150, range = [[0, 1500],[-4, 4]], cmap = 'inferno')

    r = np.corrcoef(data1, data2)
    print(r)

    axs.set_xlabel(r'$p_{T}$')
    axs.set_ylabel(r'$\eta$')
    axs.set_xlim([0, 1500])
    axs.set_ylim([-4, 4])
    fig.suptitle(r"$r_{p_{T}\eta}$ = %.3f" % (r[0][1]))

    fig.colorbar(h[3])

    plt.show()

def histo2b2(data1, data2, data3, data4, label1, label2, label3, label4):
    plt.rc('font', size=12)

    fig, axs = plt.subplots(2,2)
    fig.set_figheight(8)
    fig.set_figwidth(8)

    tmpPt = data1
    tmpPt.sort()
    ptBins = np.linspace(tmpPt[0], 5000, 100)
    tmpEta = data2
    tmpEta.sort()
    etaBins = np.linspace(tmpEta[0], tmpEta[-1], 100)
    tmpBeta = data3
    tmpBeta.sort()
    betaBins = np.linspace(tmpBeta[0], tmpBeta[-1], 100)
    tmpGamma = data4
    tmpGamma.sort()
    gammaBins = np.linspace(tmpGamma[0], tmpGamma[-1], 30)

    axs[0,0].hist(data1, ptBins, density = False, color = '#5e090d', label = r'$\~{C}^{\pm 1}$')

    axs[0,0].set_xlabel(label1)
    axs[0,0].set_ylabel(r"$\#_{\~{C}^{\pm 1}}$")

    #axs[0,0].legend()
    
    axs[0,1].hist(data2, etaBins, density = False, color = '#5e090d', label = r'$\~{C}^{\pm 1}$')

    axs[0,1].set_xlabel(label2)
    axs[0,1].set_ylabel(r"$\#_{\~{C}^{\pm 1}}$")

    #axs[0,1].legend()

    axs[1,0].hist(data3, betaBins, density = False, color = '#5e090d', label = r'$\~{C}^{\pm 1}$')

    axs[1,0].set_xlabel(label3)
    axs[1,0].set_ylabel(r"$\#_{\~{C}^{\pm 1}}$")

    #axs[1,0].legend()

    axs[1,1].hist(data4, gammaBins, density = False, color = '#5e090d', label = r'$\~{C}^{\pm 1}$')

    axs[1,1].set_xlabel(label4)
    axs[1,1].set_ylabel(r"$\#_{\~{C}^{\pm 1}}$")

    #axs[1,1].legend()

    fig.suptitle(r'Tracks (9,428 entries)')

    plt.show()


#histo1(pt, r'$p_{T}$', 100)
#histo1(eta, r'$\phi$', 100)
#histo1(beta, r'$\beta$', 100)
#histo1(gamma, r'$\gamma$', 100)

#histo2b2(pt, eta, beta, gamma, r'$p_{T}$', r'$\eta$', r'$\beta$', r'$\gamma$')

#histo2(pt, eta, r'$p_{T}$', r'$\eta$')

#histo2b2(trackPt, trackEta, trackPhi, trackValidHits, r'$p_{T}$', r'$\eta$', r'$\phi$', r'$\#_{Valid Hits}$')
