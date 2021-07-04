class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        self.grafo[u][v] = 1

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])


grafo_direcionado = Grafo(6)


grafo_direcionado.adiciona_aresta(0, 3)
grafo_direcionado.adiciona_aresta(0, 5)
grafo_direcionado.adiciona_aresta(1, 3)
grafo_direcionado.adiciona_aresta(2, 1)
grafo_direcionado.adiciona_aresta(3, 2)
grafo_direcionado.adiciona_aresta(3, 4)
grafo_direcionado.adiciona_aresta(4, 5)
grafo_direcionado.adiciona_aresta(5, 1)


grafo_direcionado.mostra_matriz()
