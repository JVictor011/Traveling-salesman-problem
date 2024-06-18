from utils import escrever_resultado, ler_matriz_distancias
import random

def calcular_distancia_total(matriz, itinerario):
    distancia_total = 0.0
    for i in range(len(itinerario) - 1):  # Parar no penúltimo elemento
        cidade_a = itinerario[i]
        cidade_b = itinerario[i + 1]
        distancia_total += matriz[cidade_a][cidade_b]
    
    # Adiciona a distância de volta ao ponto inicial
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

def hill_climb(matriz, solucao_inicial):
    melhor_solucao = solucao_inicial
    melhor_distancia = calcular_distancia_total(matriz, melhor_solucao)
    
    while True:
        vizinhos = obter_vizinhos(melhor_solucao)
        encontrou_melhor = False
        
        for vizinho in vizinhos:
            distancia_vizinho = calcular_distancia_total(matriz, vizinho)
            if distancia_vizinho < melhor_distancia:
                melhor_solucao = vizinho
                melhor_distancia = distancia_vizinho
                encontrou_melhor = True
        
        if not encontrou_melhor:
            break
    
    return melhor_solucao, melhor_distancia

# Caminho para o arquivo de distâncias
caminho_arquivo_distancias = 'five_d.txt'

# Caminho para o arquivo de resultados
caminho_arquivo_resultados = 'five_s.txt'

# Ler o arquivo de distâncias
matriz_distancias = ler_matriz_distancias(caminho_arquivo_distancias)

# Exibir a matriz de distâncias
print("Matriz de Distâncias:")
for linha in matriz_distancias:
    print(linha)

# Gerar uma solução inicial aleatória
solucao_inicial = gerar_solucao_inicial(len(matriz_distancias))

# Exibir a solução inicial e seu comprimento
print("\nSolução Inicial:", solucao_inicial)
distancia_inicial = calcular_distancia_total(matriz_distancias, solucao_inicial)
print("Comprimento do Tour Inicial:", distancia_inicial)

# Executar Hill Climbing para encontrar o itinerário mínimo
melhor_itinerario, melhor_distancia = hill_climb(matriz_distancias, solucao_inicial)

# Escrever o resultado no arquivo
escrever_resultado(caminho_arquivo_resultados, melhor_itinerario, melhor_distancia)

# Exibir o resultado
print("\nMelhor Itinerário Encontrado:", melhor_itinerario)
print("Comprimento do Melhor Tour:", melhor_distancia)
