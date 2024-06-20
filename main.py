from src.utils import escrever_resultado, ler_matriz_distancias, obter_vizinhos, gerar_solucao_inicial, calcular_distancia_total
from src.hill_climb.algoritmos import hill_climb
from src.algoritmo_genetico.algoritmos import AlgoritmoGenetico

# Caminho para o arquivo de distâncias
caminho_arquivo_distancias = 'src/result/five_d.txt'

# Caminho para o arquivo de resultados
caminho_arquivo_resultados = 'src/result/five_s.txt'

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

melhor_itinerario_ag = AlgoritmoGenetico(matriz_distancias)


melhor_distancia_ag = calcular_distancia_total(matriz_distancias, melhor_itinerario_ag)

escrever_resultado(caminho_arquivo_resultados, melhor_itinerario_ag, melhor_distancia_ag)

# Exibir o resultado do Algoritmo Genético
print("\nMelhor Itinerário Encontrado pelo Algoritmo Genético:", melhor_itinerario_ag)
print("Comprimento do Melhor Tour pelo Algoritmo Genético:", melhor_distancia_ag)