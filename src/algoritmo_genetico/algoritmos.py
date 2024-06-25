import random
from src.utils import calcular_distancia_total, gerar_solucao_inicial

def selecao(populacao, funcao_objetivo, k=55):
    selecionados = []
    for _ in range(len(populacao)):
        competidores = random.sample(populacao, k)
        competidor = min(competidores, key=funcao_objetivo)
        selecionados.append(competidor)
    return selecionados

def crossover(pai1, pai2):
    size = len(pai1)
    start, end = sorted(random.sample(range(size), 2))
    filho = [None] * size
    filho[start:end] = pai1[start:end]
    ptr = end
    for gene in pai2:
        if gene not in filho:
            if ptr >= size:
                ptr = 0
            while filho[ptr] is not None:
                ptr += 1
            filho[ptr] = gene
            ptr += 1
    return filho

def mutacao(individuo, taxa_mutacao=0.001):
    for i in range(len(individuo)):
        if random.random() < taxa_mutacao:
            j = random.randint(0, len(individuo) - 1)
            individuo[i], individuo[j] = individuo[j], individuo[i]

def condicao_parada(geracao_atual, max_geracoes):
    return geracao_atual >= max_geracoes

def melhor_individuo(populacao, funcao_objetivo):
    return min(populacao, key=funcao_objetivo)

def AlgoritmoGenetico(matriz_distancias, tamanho_populacao=400, max_geracoes=1000, taxa_mutacao=0.001):
    populacao = [gerar_solucao_inicial(len(matriz_distancias)) for _ in range(tamanho_populacao)]
    geracao = 0

    while not condicao_parada(geracao, max_geracoes):
        pais = selecao(populacao, lambda x: calcular_distancia_total(matriz_distancias, x))
        filhos = []
        for i in range(0, tamanho_populacao, 2):
            pai1, pai2 = pais[i], pais[i+1]
            filho1, filho2 = crossover(pai1, pai2), crossover(pai2, pai1)
            mutacao(filho1, taxa_mutacao)
            mutacao(filho2, taxa_mutacao)
            filhos.append(filho1)
            filhos.append(filho2)
        populacao = filhos
        geracao += 1

    return melhor_individuo(populacao, lambda x: calcular_distancia_total(matriz_distancias, x))
