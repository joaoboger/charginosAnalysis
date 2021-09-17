import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

### Loading data ###

dfCharginos = pd.read_csv('/home/jboger/2021.1/analysisCMSSW/dfCharginos.csv', index_col=0)
print(dfCharginos.head())

### @dev: Return dataframe(df) labels in an array.
def getLabels(df):
    return [colum for colum in dfCharginos.columns]

### @dev: This function plots a correlation 2d histogram
###       of all dataframe (df) columns.
def corrDf(df, labels):
    dfCorr = df.corr()

    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111)

    cmap = 'inferno'
    im = ax.matshow(dfCorr, cmap = cmap)

    ax.set_xticks(np.arange(len(labels)))
    ax.set_yticks(np.arange(len(labels)))

    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)

    fig.colorbar(im)

    plt.show()

def hist(df, column):
    fig = plt.figure(figsize = (8,8))
    axs = fig.add_subplot(111)

    axs.hist(df[column], bins=100)

    plt.show()

hist(dfCharginos, 'pt')
