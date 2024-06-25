import random
import math
from src.utils import calcular_distancia_total, gerar_solucao_inicial, obter_vizinhos

def simulated_annealing(matriz_distancias, T0, Tf, L, alfa):
    T = T0
    S0 = gerar_solucao_inicial(len(matriz_distancias))
    S = S0
    S_star = S0
    melhor_custo = calcular_distancia_total(matriz_distancias, S_star)
    
    while T > Tf:
        for _ in range(L):
            S_linha = random.choice(obter_vizinhos(S))
            delta_custo = calcular_distancia_total(matriz_distancias, S_linha) - calcular_distancia_total(matriz_distancias, S)
            
            if delta_custo < 0 or random.random() < math.exp(-delta_custo / T):
                S = S_linha
            
            if calcular_distancia_total(matriz_distancias, S) < melhor_custo:
                S_star = S
                melhor_custo = calcular_distancia_total(matriz_distancias, S_star)
        
        T *= alfa
    
    return S_star, melhor_custo