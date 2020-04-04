# API para acessar dados gerados pelas execuções do AG

from pandas import read_csv, DataFrame
from numpy import array

# Lista de dados de parâmetros
CROSSOVERS = {
    "UX": 'UNIFORM', 
    "1P": '1POINTS', 
    "2P": '2POINTS',
    "4P": '4POINTS',
    "8P": '8POINTS',
    "16P": '16POINTS',
    "32P": '32POINTS'
}
# Lista de taxas e cruzamento
CROSS_RATE_LIST = [0.6, 0.8, 1.0]
# Lista de valores de restrição SAIDI
SAIDI_LIST = [1, 5, 10]
# Lista de tamanhos de população
POPSIZE_LIST = [200, 400, 600]

# Use o GET com os parâmetros qu definiem uma configuração de execução
def get_costs(operator, saidi=1, popsize=200, crossrate=1, as_array=False, as_list=False):
    """GET(CUSTOS)

    Retorna uma lista (ou numpy.array) com os custos finais a partir de um arquivo
    escolhido pelos parâmetros
    """
    filename = "SAIDI_"+ str(saidi) +"/"+ operator +"_G100_P"+ str(popsize) +"_CR"+ str(crossrate) +".csv"
    dataframe = read_csv(filename, sep=',', engine='c')
    if as_array and as_list:
        return None
    elif as_array and not as_list:
        return array(dataframe['Custo'])
    elif not as_array and as_list:
        return list(dataframe['Custo'])
    return dataframe['Custo']


# Construção de um DataFrame a partir de parâmetros selecionados
# os parametros são:
# --- saidi     = valor definido para o SAIDI na execução
# --- popsize   = Tamanho da população
# --- crossrate = Percentual de cruzamento
def build_dataframe(saidi, popsize, crossrate):
    """Constrói um pandas.DataFrame com todos os custos para todos os crossovers

    Parâmetros:
    --- saidi     = valor definido para o SAIDI na execução
    --- popsize   = Tamanho da população
    --- crossrate = Percentual de cruzamento
    """
    dicio = dict()
    for k in CROSSOVERS:
        dicio[k] = get_costs(CROSSOVERS[k], saidi, popsize, crossrate, as_list=True)
    return DataFrame(dicio)
