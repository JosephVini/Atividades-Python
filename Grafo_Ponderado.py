class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        self.grafo[u][v] = peso
        self.grafo[v][u] = peso

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])


grafo_pondereado = Grafo(6)

grafo_pondereado.adiciona_aresta(0,4,5)
grafo_pondereado.adiciona_aresta(0,5,2)
grafo_pondereado.adiciona_aresta(1,3,3)
grafo_pondereado.adiciona_aresta(1,5,5)
grafo_pondereado.adiciona_aresta(2,3,1)
grafo_pondereado.adiciona_aresta(2,4,2)
grafo_pondereado.adiciona_aresta(3,4,2)
grafo_pondereado.adiciona_aresta(4,5,3)

grafo_pondereado.mostra_matriz()