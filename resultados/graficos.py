import matplotlib.pyplot as plt
from numpy import array

from .api import build_dataframe, CROSSOVERS, CROSS_RATE_LIST


# Definições de componentes de gráficos bem como linhas, pontos, etc...
red_square = dict(markerfacecolor='r', marker='s')
red_circle = dict(makerfacecolor='r', marker='o')
red_diamond = dict(markerfacecolor='r', marker='D', markeredgecolor='white')
black_diamond = dict(markerfacecolor='black', marker='D', markeredgecolor='white')
black_box = dict(linestyle='-', color='white', facecolor='black')


# Plotagem em BoxPlot
# Recebe um dataframe criado com o método build_dataframe e plota as colunas
# Aqui é feita a estilização
def BoxPlot(dataframe, axes=None, boxwidth=0.6, figsize=(8,8), yrange=None):
    if axes==None:
        fig, ax = plt.subplots(figsize=figsize)
    else:
        ax = axes
    data = [array(dataframe[col]) for col in dataframe]
    
    plot = ax.boxplot(data,
        widths=boxwidth,
        labels=list(CROSSOVERS.keys()),
        patch_artist=True,
        boxprops=black_box,
        showmeans=True,
        meanprops=red_diamond,
        flierprops=black_diamond)

    if yrange is not None:
        ax.set_ylim(yrange)

    for line in plot["medians"]:
        line.set_color("white")

    ax.legend(
        (plot["means"][0], plot["fliers"][0]),
        ("Average", "Outliers"),
        loc='upper right'
    )
    
    if axes is None:
        return fig, ax
    else:
        return


def plot_with_popsize(p, saidi_value=1, figsize=(16,4)):
    df_crossrates = [build_dataframe(saidi=saidi_value, popsize=p, crossrate=cr) for cr in CROSS_RATE_LIST]

    i=0
    fig, ax = plt.subplots(1, 3, figsize=figsize, sharey=True, sharex=True)
    ax[0].set_ylabel("Final cost found ($)")
    for df in df_crossrates:
        BoxPlot(df, ax[i])
        ax[i].set(title=f"Crossover rate = {int(CROSS_RATE_LIST[i]*100)}%")
        ax[i].set_xticklabels(CROSSOVERS.keys(), fontdict={'fontsize': 14})
        i+=1
        
    return fig, ax

