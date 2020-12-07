from Grafo import *
# from test_Roteiro7 import VerificarTests

# test = VerificarTests()
# test.setUp()
# test.test_Dijkstra()

def adiciona_ae(grafo, aresta, vezes):
    for vez in range(vezes):
        grafo.adicionaAresta(aresta)

g1 = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])

adiciona_ae(g1, 'A-B', 2)
adiciona_ae(g1, 'A-F', 1) 
adiciona_ae(g1, 'A-D', 1) 
adiciona_ae(g1, 'B-C', 2) 
adiciona_ae(g1, 'D-C', 5) 
adiciona_ae(g1, 'C-E', 3) 
adiciona_ae(g1, 'D-E', 7) 
adiciona_ae(g1, 'D-F', 1) 
adiciona_ae(g1, 'F-E', 9) 

print(g1.kruskal())
# print(g1.peso_aresta('D-E'))



# g2 = Grafo(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'])
# g2.adicionaAresta('1-2')
# g2.adicionaAresta('1-5')
# g2.adicionaAresta('1-11')
# g2.adicionaAresta('1-6')
# g2.adicionaAresta('2-3')
# g2.adicionaAresta('6-7')
# g2.adicionaAresta('6-10')
# g2.adicionaAresta('11-10')
# g2.adicionaAresta('3-4')
# g2.adicionaAresta('7-8')
# g2.adicionaAresta('10-12')
# g2.adicionaAresta('12-8')
# g2.adicionaAresta('4-9')
# g2.adicionaAresta('8-9')
# g2.adicionaAresta('12-13')
# g2.adicionaAresta('9-13')

# print(g2.Dijkstra('1','13',3 ,3 , ['4','8']))  # ['13', '9', '4', '3', '2', '1']
# print(g2.Dijkstra('1','13',3 ,3 , ['8']))      # ['13', '9', '8', '7', '6', '1']
# print(g2.Dijkstra('1','13',3 ,3 , []))       # False

# g3 = Grafo(['1', '2', '3', '4', '5', '6', '7'])
# g3.adicionaAresta('1-3')
# g3.adicionaAresta('1-4')
# g3.adicionaAresta('4-7')
# g3.adicionaAresta('3-2')
# g3.adicionaAresta('2-7')
# g3.adicionaAresta('5-7')
# g3.adicionaAresta('6-5')
# g3.adicionaAresta('2-6')

# print(g3.Dijkstra('7','4',1,4,[])) #['4', '7']
# print(g3.Dijkstra('2','4',1,4,['3','6'])) #['4', '1', '3', '2']
# print(g3.Dijkstra('1','5',3,5,['2','7'])) #['5', '7', '4', '1']

# g4 = Grafo(['0', '1', '2', '3'])
# g4.adicionaAresta('1-0')
# g4.adicionaAresta('2-0')
# g4.adicionaAresta('1-2')
# g4.adicionaAresta('2-3')

# print(g4.Dijkstra('0','3',1,2,['2'])) #['3', '2', '0']
# print(g4.Dijkstra('0','3',1,2,['1'])) #['3', '2', '1', '0']

# g5 = Grafo(['5','4','6','7','8','9'])
# g5.adicionaAresta('5-4')
# g5.adicionaAresta('5-9')
# g5.adicionaAresta('9-8')
# g5.adicionaAresta('5-8')
# g5.adicionaAresta('4-6')
# g5.adicionaAresta('6-7')

#print(g5.Dijkstra('8','7',1,5,['5','9'])) #['7', '6', '4', '5', '8']

# g6 = Grafo(['L','M','N','O','P'])
# g6.adicionaAresta('L-M')
# g6.adicionaAresta('L-O')
# g6.adicionaAresta('N-P')
# g6.adicionaAresta('M-P')
# g6.adicionaAresta('O-P')

# #print(g6.Dijkstra('N','L',2,5,['M','O']))  #['L', 'M', 'P', 'N']
# #print(g6.Dijkstra('L','N',2,5,['M','O']))  #['N', 'P', 'M', 'L']

# g7 = Grafo(['a','b','c','d'])
# g7.adicionaAresta('a-a')
# g7.adicionaAresta('a-b')
# g7.adicionaAresta('c-d')
# g7.adicionaAresta('d-c')
# g7.adicionaAresta('a-c')

# #print(g7.Dijkstra('b','d',1,3,['a'])) #['d','c','a','b']
# #print(g7.Dijkstra('c','d',1,3,['a']))  #['d','c']
# #print(g7.Dijkstra('c','d',1,3,['']))  #['d','c']

# g8 = Grafo(['J','K','L','M','N'])
# g8.adicionaAresta('J-K')
# g8.adicionaAresta('J-N')
# g8.adicionaAresta('N-M')
# g8.adicionaAresta('K-M')
# g8.adicionaAresta('L-N')
# g8.adicionaAresta('L-J')

# #print(g8.Dijkstra('K','L',1,2,['M'])) #['L', 'N', 'M', 'K']

# g9 = Grafo(['5', '1', '3', '6', '4', '0', '2', '7'])
# g9.adicionaAresta('5-1')
# g9.adicionaAresta('1-3')
# g9.adicionaAresta('3-6')
# g9.adicionaAresta('6-4')
# g9.adicionaAresta('4-5')
# g9.adicionaAresta('5-4')
# g9.adicionaAresta('5-7')
# g9.adicionaAresta('5-7')
# g9.adicionaAresta('7-3')
# g9.adicionaAresta('7-2')
# g9.adicionaAresta('2-0')
# g9.adicionaAresta('0-4')
# g9.adicionaAresta('2-6')
# g9.adicionaAresta('0-6')

# print(g9.Dijkstra('5','0',1,5,['1'])) #['0', '6', '3', '1', '5']
# print(g9.Dijkstra('1','4',2, 2, ['2']))

# g10 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
# g10.adicionaAresta('A-B')
# g10.adicionaAresta('B-C')
# g10.adicionaAresta('B-F')
# g10.adicionaAresta('C-E')
# g10.adicionaAresta('C-D')
# g10.adicionaAresta('E-D')
# g10.adicionaAresta('D-G')
# g10.adicionaAresta('F-G')

# #print(g10.Dijkstra('A','G',2,5,['C','F']))
# #print(g10.Dijkstra('B','E',2, 5, ['C', 'F']))


# completoAateG = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
# completoAateG.adicionaAresta('A-B')
# completoAateG.adicionaAresta('B-C')
# completoAateG.adicionaAresta('C-B')
# completoAateG.adicionaAresta('C-D')
# completoAateG.adicionaAresta('D-E')
# completoAateG.adicionaAresta('E-F')
# completoAateG.adicionaAresta('D-G')
# completoAateG.adicionaAresta('B-G')

# #print(completoAateG.Dijkstra('A','F',3,5,['E']))

# ciclo_simples = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])
# ciclo_simples.adicionaAresta('A-B')
# ciclo_simples.adicionaAresta('B-A')
# ciclo_simples.adicionaAresta('C-A')
# ciclo_simples.adicionaAresta('C-B')
# ciclo_simples.adicionaAresta('C-D')
# ciclo_simples.adicionaAresta('C-E')
# ciclo_simples.adicionaAresta('E-F')

# #print(ciclo_simples.Dijkstra('E','B',2,2,['D']))

# simples1 = Grafo(['A', 'B', 'C'])
# simples1.adicionaAresta('A-B')
# simples1.adicionaAresta('B-C')
# simples1.adicionaAresta('C-B')

# #print(simples1.Dijkstra('A','C',1,1,['B']))

# completo0 = Grafo(['A', 'B', 'D', 'E', 'F', 'G', 'I'])
# completo0.adicionaAresta('A-E')
# completo0.adicionaAresta('E-F')
# completo0.adicionaAresta('F-G')
# completo0.adicionaAresta('G-B')
# completo0.adicionaAresta('B-A')
# completo0.adicionaAresta('A-I')
# completo0.adicionaAresta('A-D')
# completo0.adicionaAresta('I-D')
# completo0.adicionaAresta('D-E')

# #print(completo0.Dijkstra('I','B',1,3,['G','F']))

# completo1 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'J', 'H', 'I'])
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
# completo1.adicionaAresta('H-J')

# #print(completo1.Dijkstra('A','J',2,4,['C'])) #['J', 'H', 'D', 'C', 'A']

# incompleto0 = Grafo(['h', 't', 'o', 'j', 'k', 'l', 'm', 'n'])
# incompleto0.adicionaAresta('o-o')
# incompleto0.adicionaAresta('t-l')
# incompleto0.adicionaAresta('l-t')
# incompleto0.adicionaAresta('l-k')
# incompleto0.adicionaAresta('o-j')
# incompleto0.adicionaAresta('t-o')
# incompleto0.adicionaAresta('m-t')
# incompleto0.adicionaAresta('k-j')
# incompleto0.adicionaAresta('l-k')
# incompleto0.adicionaAresta('l-m')
# incompleto0.adicionaAresta('n-m')

# print(incompleto0.Dijkstra('n','t',1,2,['m']))

#Arestas = ['A-B','A-D','A-E','E-C','B-C']
#for i in Arestas:
#    i = i.split('-')
#    print(i)

#a = '9-13'
#aa = a.split('-')

#B = [0, 1, 2, float('inf'), 1, 1, float('inf'), float('inf'), float('inf'), float('inf'), 1, float('inf'), float('inf')]
#P1 = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#P2 = [2, 4, 5, 10]

#P2, Aux = [], {}
#for i in range(len(P1)):
#    if P1[i] == 0 and B[i] < float('inf'):
#        P2.append(i)

#for i in P2:
#    Aux[i] = B[i]  # Em um dic = '2': '2'; '4': '1'; '5': '1'; '10': '1';

#print(Aux)
#IndiceComMenorValor = min(Aux, key=lambda chave: int(Aux[chave]))  ## Espero que esteja se referindo a segunda chave.
#print(IndiceComMenorValor)
#for i in Aux:
#    print(i,Aux[i])

#print(max(Aux[key]))
#return IndiceComMenorValor

# ELE DEVERIA ESCOLHER O BETA(4) = 1 (O primeiro menor)
# MAS ELE ESCOLHER O MENOR INDICE QUE NÃO NECESSARIMENTE É O MENOR.

#print(aa)
#print(g2.arestas_sobre_vertice('1'))

#print(g2)
#for i in a:
#    print(i[2])
#a = [2,1,float('inf'),3,5]
#print(a.index(max(a))) #Responde posição 2
#print(a.index(min(a))) #Responde posição 1