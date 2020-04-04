import resultados as res
import seaborn;
seaborn.set(); seaborn.set_color_codes("bright")

# Geração das figuras do paper aceito no IEEE CEC'20

def generateFig(figname, saidivalue, yaxisrange):
    # cria o dataframe
    print(f"--- Criando dataframe de execuções com SAIDI = {saidivalue}")
    dataframe = res.build_dataframe(saidi=saidivalue, popsize=400, crossrate=1)
    # plotagem dos gráficos
    print(f"--- Plotando BoxPlots")
    fig, _ = res.graficos.BoxPlot(dataframe, figsize=(7,7), yrange=yaxisrange)
    # salva a figura em um arquivo de imagem
    print(f"--- Salvando em {figname}")
    fig.savefig(figname)
    return

generateFig("Fig1 Saidi 1.jpg", saidivalue=1, yaxisrange=(4.3e+5, 5.1e+5))
generateFig("Fig2 Saidi 5.jpg", saidivalue=5, yaxisrange=(2.3e+5, 3.1e+5))
generateFig("Fig3 Saidi 10.jpg", saidivalue=10, yaxisrange=(2.3e+5, 3.1e+5))