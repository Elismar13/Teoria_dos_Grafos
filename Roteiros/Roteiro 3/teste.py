from grafo import *

g = Grafo(['B', 'A', 'C', 'D', 'E', 'F'], {'a1':'A-B', 'a2':'B-C', 'a3':'D-F', 'a4':'F-E', 'a5':'C-D'})
a = Grafo(['A', 'B', 'C'], {'a1':'A-A', 'a2':'A-B'})

print(g.ehConexo())
print(a.ehConexo())
