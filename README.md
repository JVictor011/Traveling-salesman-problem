# TSP (Traveling Salesman Problem) - O problema do caixeiro viajante

# Definição:
O problema do caixeiro viajante é um problema clássico em teoria dos grafos e otimização
combinatória. Ele pode ser enunciado da seguinte forma:
Dado um conjunto de cidades e as distâncias entre cada par delas (um grafo completo de
distâncias), o problema consiste em encontrar a menor rota possível que permita que um
caixeiro viajante visite cada cidade exatamente uma vez e retorne à cidade de origem.

# Exemplo Simples:
Imagine que você tem quatro cidades: A, B, C e D. As distâncias entre cada par de cidades
são conhecidas, e o objetivo é encontrar a rota que permita visitar todas as cidades uma vez
e voltar ao ponto de partida com a menor distância total percorrida.

# Características do Problema:
Combinatório: À medida que o número de cidades aumenta, o número de possíveis
rotas cresce exponencialmente. Para n cidades, há (n−1)!(n−1)! rotas possíveis
(considerando que o ponto de partida é fixo).

# NP-difícil: O TSP pertence a uma classe de problemas conhecida como NP-difícil.
Isso significa que não existe (até onde sabemos) um algoritmo eficiente que resolva todos
os casos do problema em tempo polinomial.

# Importância:
O TSP tem muitas aplicações práticas, como planejamento de rotas para entregas,
organização de circuitos eletrônicos, planejamento de viagens e mais.

# Sobre o trabalho:
Sua equipe irá utilizar métodos de busca local para buscar otimizar de forma satisfatória
cada uma das instâncias fornecidas do problema TSP, comparando com a solução ótima.
Uma base de dados é fornecida no link:
https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html
no formato de matrizes de distâncias para cada instância.

# Sobre a implementação:
Os seguintes algoritmos devem ser implementados para otimizar as instâncias:
1. Hill Climbing (Descida de encosta)
2. Algoritmo genético
3. Têmpera simulada
4. (opcional) Busca Tabu

# Relatório
Você deve produzir um relatório com as instâncias testadas. Cada instância testada por
cada método deve conter:
● Quantidade de passos de sua solução (por exemplo, no genético é a quantidade de
gerações produzidas);
● Total de tempo gasto no uso do algoritmo para obtenção da solução;
● Comparação da solução obtida com o valor da solução ótima;

# Dicas
1. Utilize uma representação adequada do problema. Uma boa representação impacta
diretamente na performance da solução;
2. Uma boa representação de transição de estados também é fundamental para a
obtenção de performance e boas soluções;
3. Gerar um estado inicial aleatório;