from Grafo import *
# from test_Roteiro7 import VerificarTests

# test = VerificarTests()
# test.setUp()
# test.test_Dijkstra()


# Esse grafo é o da aula.
g1 = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])

""" 

    Sobre os pesos...

    Eu criei um método direto na classe dele (espero q n nos mate) para adicionar uma aresta com peso direto na matriz,
    pra não precisar ficarmos repetindo o adicionaAresta.

    adicionaArestaComPeso(self, aresta, peso)

"""
g1.adicionaArestaComPeso('A-B', 2)
g1.adicionaArestaComPeso('A-F', 1) 
g1.adicionaArestaComPeso('A-D', 1) 
g1.adicionaArestaComPeso('B-C', 2) 
g1.adicionaArestaComPeso('D-C', 5) 
g1.adicionaArestaComPeso('C-E', 3) 
g1.adicionaArestaComPeso('D-E', 7) 
g1.adicionaArestaComPeso('D-F', 1) 
g1.adicionaArestaComPeso('E-F', 9) 

result = g1.prim()

print(result)
for key in result.keys():
    print("{} é filho de {}".format(key, result[key]))
