import random

def calcular_distancia_total(matriz, itinerario):
    distancia_total = 0.0
    for i in range(len(itinerario) - 1):
        cidade_a = itinerario[i]
        cidade_b = itinerario[i + 1]
        distancia_total += matriz[cidade_a][cidade_b]
    
    distancia_total += matriz[itinerario[-1]][itinerario[0]]
    return distancia_total

def gerar_solucao_inicial(num_cidades):
    solucao = list(range(num_cidades))
    random.shuffle(solucao)
    return solucao

def obter_vizinhos(solucao):
    vizinhos = []
    for i in range(len(solucao)):
        for j in range(i + 1, len(solucao)):
            vizinho = solucao[:]
            vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
            vizinhos.append(vizinho)
    return vizinhos

def escrever_resultado(arquivo, itinerario, distancia):
    with open(arquivo, 'w') as f:
        f.write("Melhor Itinerário Encontrado:\n")
        f.write(str(itinerario) + "\n")
        f.write("Comprimento do Melhor Tour:\n")
        f.write(str(distancia) + "\n")

def ler_matriz_distancias(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    
    matriz = []
    for linha in linhas:
        valores = linha.split()
        matriz.append([float(valor) for valor in valores])
    
    return matriz