# Pesquisa CEC 2020

Arquivos que foram gerados a partir da execução do Algoritmo Genético aplicado
ao problema de alocação de chaves seccionadoras. Fonte dos estudos em operadores
de crossover que resultou em um artigo submetido e aceito para publicação no
[IEEE CEC 2020](https://wcci2020.org/).

## Arquivos

Os arquivos estão nas pastas `SAIDI_N`, onde N define o valor de SAIDI definido
para aquela bateria de testes.
As execuções foram configuradas com diferentes combinações de parâmetros, os
arquivos são nomeados de acordo com a configuração, por exemplo:

`16POINTS_G100_P200_CR1.csv` foi gerado com o AG usando o crossover de 16 pontos
de corte, 100 gerações, população com 200 indivíduos e taxa de cruzamento (_CR -
crossover rate_) de 100% (1.).

## Scripts Python

Os scripts python no diretório `resultados` permitem construir `pandas.DataFrame`s
a partir dos arquivos gerados com as execuções, e criar os boxplots usando as configurações definidas para as figuras incluídas no paper submetido.

```py
import resultados

df = resultados.build_dataframe(saidi=5, popsize=400, crossrate=0.8)

fig, _ = resultados.graficos.BoxPlot(df)
```

OBS: É necessário ter as bibliotecas `pandas`, `numpy` e `matplotlib` instaladas.

## Licença

[Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) &copy; Ronaldd Pinho
