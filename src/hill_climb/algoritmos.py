from src.utils import calcular_distancia_total, obter_vizinhos

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