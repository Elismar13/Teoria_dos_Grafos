from Grafo_Nao_Direc import Grafo

# g1 = Grafo(['5', '1', '3', '6', '4', '0', '2', '7'])
# g1.adicionaAresta('5-1')
# g1.adicionaAresta('1-3')
# g1.adicionaAresta('3-6')
# g1.adicionaAresta('6-4')
# g1.adicionaAresta('4-5')
# g1.adicionaAresta('5-4')
# g1.adicionaAresta('5-7')
# g1.adicionaAresta('5-7')
# g1.adicionaAresta('7-3')
# g1.adicionaAresta('7-2')
# g1.adicionaAresta('2-0')
# g1.adicionaAresta('0-4')
# g1.adicionaAresta('2-6')
# g1.adicionaAresta('0-6')

# print(g1.CicloHamiltoniano())

# completo0 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])

# completo0.adicionaAresta('A-E')
# completo0.adicionaAresta('E-F')
# completo0.adicionaAresta('F-G')
# completo0.adicionaAresta('G-B')
# completo0.adicionaAresta('B-A')
# completo0.adicionaAresta('A-I')
# completo0.adicionaAresta('A-D')
# completo0.adicionaAresta('A-C')
# completo0.adicionaAresta('C-H')

# completo1 = Grafo(['A', 'B', 'C', 'D', 'E','F','J','H','I'])
# completo1.adicionaAresta('A-C')
# completo1.adicionaAresta('A-B')
# completo1.adicionaAresta('C-D')
# completo1.adicionaAresta('C-E')
# completo1.adicionaAresta('B-A')
# completo1.adicionaAresta('B-D')
# completo1.adicionaAresta('B-E')
# completo1.adicionaAresta('E-D')
# completo1.adicionaAresta('E-A')
# completo1.adicionaAresta('E-F')
# completo1.adicionaAresta('F-J')
# completo1.adicionaAresta('J-F')
# completo1.adicionaAresta('E-D')
# completo1.adicionaAresta('H-D')
# completo1.adicionaAresta('E-H')
# completo1.adicionaAresta('H-I')
# completo1.adicionaAresta('I-A')

# print(completo1.CicloHamiltoniano())

# #g3 = Grafo(['B','C',''])
# #g3.adicionaAresta('B-B')


# #g3.adicionaAresta('12-1')


# g6 = Grafo(['Z', 'P', 'I', 'U', 'V', 'T'])
# g6.adicionaAresta('P-Z')
# g6.adicionaAresta('U-P')
# g6.adicionaAresta('I-P')
# g6.adicionaAresta('I-Z')
# g6.adicionaAresta('T-Z')
# g6.adicionaAresta('V-T')
# g6.adicionaAresta('I-T')
# g6.adicionaAresta('U-V')
# g6.adicionaAresta('U-Z')

# #b = ['B']
# #print(b[-1])
# #a = ['5', '1', '3', '6', '4', '0', '2', '7']
# #print(a[-1])

# Arestas = ['5-1', '5-4', '5-4', '5-7', '5-7', '1-3', '3-6', '3-7', '6-4', '6-0', '6-2', '4-0', '0-2', '2-7']

# #print(g3.CicloHamiltoniano())
# #print(g2.CicloHamiltoniano())

# bug = Grafo(['B', 'E', 'D', 'C', 'A'])
# bug.adicionaAresta('A-B')
# bug.adicionaAresta('B-E')
# bug.adicionaAresta('A-C')
# bug.adicionaAresta('B-D')
# bug.adicionaAresta('C-E')
# bug.adicionaAresta('C-D')
# bug.adicionaAresta('D-E')
# print(bug.CicloHamiltoniano())

# print(bug3.caminhoEureliano())

# bug2 = Grafo(['A', 'B', 'C'])
# bug2.adicionaAresta('A-B')
# bug2.adicionaAresta('B-C')
# print(bug2.CicloHamiltoniano())

# print(bug2.caminhoEureliano())

bug2 = Grafo(['A', 'B', 'C'])
bug2.adicionaAresta('A-B')
bug2.adicionaAresta('B-C')
print(bug2.CicloHamiltoniano())


bug3 = Grafo(['D', 'B', 'C', 'A', 'E'])
bug3.adicionaAresta('A-B')
bug3.adicionaAresta('B-C')
bug3.adicionaAresta('C-D')
bug3.adicionaAresta('D-E')
print(bug3.CicloHamiltoniano())


grafoSimples = Grafo(['A', 'B', 'C'])
grafoSimples.adicionaAresta('A-B')
grafoSimples.adicionaAresta('B-C')
grafoSimples.adicionaAresta('C-A')
print(grafoSimples.CicloHamiltoniano())