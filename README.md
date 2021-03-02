# Resultados do Estudo

> Resultados do estudo comparativo em operadores de crossover de algoritmos
> genéticos aplicados ao problema de alocação de chaves seccionadoras no
> planejamento de redes de distribuição de energia.

Arquivos que foram gerados a partir da execução do Algoritmo Genético aplicado
ao problema de alocação de chaves seccionadoras. Fonte dos estudos em operadores
de crossover que resultou em um artigo submetido e aceito para publicação no
[_IEEE Congress on Evolutionary Computation 2020_](https://wcci2020.org/).

Paper disponível em: https://ieeexplore.ieee.org/document/9185795

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
a partir dos arquivos gerados com as execuções, e criar os boxplots usando as
configurações definidas para as figuras incluídas no paper submetido.

```py
import resultados

df = resultados.build_dataframe(saidi=5, popsize=400, crossrate=0.8)

fig, _ = resultados.graficos.BoxPlot(df)
```

OBS: É necessário ter as bibliotecas `pandas`, `numpy` e `matplotlib` instaladas.

## Licença

Este trabalho é licenciado sob os termos de [Creative Commons Attribution-ShareAlike 4.0
International License][cc-by-sa].

[CC BY-SA 4.0][cc-by-sa] &copy; Ronaldd Pinho

[cc-by-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
