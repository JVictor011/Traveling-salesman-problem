from src.utils import escrever_resultado, ler_matriz_distancias, gerar_solucao_inicial, calcular_distancia_total
from src.hill_climb.algoritmos import hill_climb
from src.algoritmo_genetico.algoritmos import AlgoritmoGenetico
from src.tempera_simulada.algoritmos import simulated_annealing
from time import time

def main():
    caminho_arquivo_distancias = 'src/data/fri26_d.txt'
    caminho_arquivo_resultados = 'src/data/fri26_s.txt'

    matriz_distancias = ler_matriz_distancias(caminho_arquivo_distancias)

    print("Matriz de Distâncias:")
    for linha in matriz_distancias:
        print(linha)

    solucao_inicial = gerar_solucao_inicial(len(matriz_distancias))

    print("\nSolução Inicial:", solucao_inicial)
    distancia_inicial = calcular_distancia_total(matriz_distancias, solucao_inicial)
    print("Comprimento do Tour Inicial:", distancia_inicial)

    def executar_hill_climb():
        melhor_itinerario, melhor_distancia = hill_climb(matriz_distancias, solucao_inicial)
        escrever_resultado(caminho_arquivo_resultados, melhor_itinerario, melhor_distancia)
        print("\nMelhor Itinerário Encontrado:", melhor_itinerario)
        print("Comprimento do Melhor Tour:", melhor_distancia)

    def executar_algoritmo_genetico():
        melhor_itinerario_ag = AlgoritmoGenetico(matriz_distancias)
        melhor_distancia_ag = calcular_distancia_total(matriz_distancias, melhor_itinerario_ag)
        escrever_resultado(caminho_arquivo_resultados, melhor_itinerario_ag, melhor_distancia_ag)
        print("\nMelhor Itinerário Encontrado pelo Algoritmo Genético:", melhor_itinerario_ag)
        print("Comprimento do Melhor Tour pelo Algoritmo Genético:", melhor_distancia_ag)

    def executar_tempera_simulada():
        melhor_itinerario, melhor_distancia = simulated_annealing(matriz_distancias, 1000.0, 0.001, 100, 0.99)
        escrever_resultado(caminho_arquivo_resultados, melhor_itinerario, melhor_distancia)
        print("\nMelhor Itinerário Encontrado pelo Simulated Annealing:", melhor_itinerario)
        print("Comprimento do Melhor Tour pelo Simulated Annealing:", melhor_distancia)

    print("Escolha o algoritmo a ser executado:")
    print("1. Hill Climb")
    print("2. Algoritmo Genético")
    print("3. Tempera Simulada")
    escolha = int(input("Digite o número do algoritmo desejado: "))

    if escolha == 1:
        timeInicial = time()
        executar_hill_climb()
        timeFinal = time() - timeInicial
        print("Tempo de execução do Hill Climb:", timeFinal)
    elif escolha == 2:
        timeInicial = time()
        executar_algoritmo_genetico()
        timeFinal = time() - timeInicial
        print("Tempo de execução do Algoritmo Genético:", timeFinal)
    elif escolha == 3:
        timeInicial = time()
        executar_tempera_simulada()
        timeFinal = time() - timeInicial
        print("Tempo de execução do Têmpera simulada:", timeFinal)
    else:
        print("Escolha inválida")

if __name__ == "__main__":
    main()
