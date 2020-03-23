from grafo import *

g = Grafo(['F', 'B', 'C', 'D', 'E', 'A'], {'a1':'A-B', 'a2':'B-C', 'a3':'D-F', 'a4':'F-E', 'a5':'C-D', 'a6':'E-C'})
a = Grafo(['A', 'B', 'C'], {'a1':'A-C', 'a2':'A-B'})

#completoAateG = Grafo(['A','B','C','D','E','F','G'], {'a1':'A-B', 'a2':'B-C', 'a3':'C-B', 'a4':'C-D', 'a5':'D-E', 'a6':'E-F', 'a7': 'D-G', 'a8':'B-G'})
arvore = Grafo(['A', 'B', 'C', 'D', 'E', 'F'], {"a1":"A-B", 'a2':'A-E', 'a3':'C-B', 'a4':"D-B", 'a5':'E-F'})

#print(a.ehConexo())
#print(g.ehConexo())
#print(a.ehConexo())

#print(arvore.CaminhoComComprimento(5))

b = Grafo(['A', 'B', 'C', 'D', 'E', 'F'], {'a1':'A-B', 'a2':'A-C', 'a3':'A-D', 'a4':'D-E', 'a5':'D-F', 'a6':'E-F'})
print(g.Caminho(1))





