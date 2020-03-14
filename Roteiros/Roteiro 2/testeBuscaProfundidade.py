
# ALUNOS: ELISMAR E MARIA LUIZA

from grafo import *
import unittest

class TestedeGrafo(unittest.TestCase):
    def setUp(self):
        #Grafos completos
        self.completo1 = Grafo(['A','B','C'], {'a1':'A-B', 'a2':'B-C', 'a3':'C-A'})
        self.completo2 = Grafo(['A', 'B'], {'a1':'A-B'})

        self.completoAateG = Grafo(['A','B','C','D','E','F','G'], {'a1':'A-B', 'a2':'B-C', 'a3':'C-B', 'a4':'C-D', 'a5':'D-E', 'a6':'E-F', 'a7': 'D-G', 'a8':'B-G'})

        self.completo_ciclo = Grafo(['A','B','C','D','E','F'], {'a1':'A-B','a2':'B-A','a3':'C-A','a4':'C-B','a5':'C-D','a6':'C-E','a7':'E-F'})
        self.completo_ciclo2 = Grafo(['A','B','C','D'], {'a1':'A-B','a2':'B-C','a3':'C-D','a4':'A-D','a5':'A-C','a6':'D-B'})

        #Grafos com laços ou arestas paralelas
        self.lacos1 = Grafo(['A', 'B', 'C', 'D'], {'a1':'C-A', 'a2':'A-A', 'a4':'D-C', 'a5':'B-D'})
        self.lacos2 = Grafo(['A', 'B'], {'a1':'B-A'})
        self.lacosUnico = Grafo(['A', 'B'], {'a1':'A-B', 'a2':'A-A'})
        self.arestas_simples_com_laco = Grafo(['A','B'], {'A1':'A-A','A2':'A-B','A3':'B-A'})
        self.arestas_simples_com_laco1 = Grafo(['A', 'B','C','D'], {'A1': 'A-A', 'A2': 'A-B', 'A3': 'B-A','A4':'A-C','A5':'C-D'})

        #Grafos do exercicio
        self.paraiba = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z', 'a10':'J-J'})
        self.exemplo2 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I' ,'K', 'J'], {'1':'A-B', '2':'A-G', '3':'A-J', '4':'K-G', 
            '5':'K-J', '6':'J-G', '7':'J-I', '8':'G-I', '9':'G-H', '10':'H-F', '11':'F-B'
            , '12':'B-G', '13':'B-C', '14':'C-D', '15':'D-E', '16':'B-D', '17':'B-E'})

        #Grafo simples
        self.simples1 = Grafo(['A','B','C'], {'a1':'A-B','a2':'B-C','a3':'C-B'})
        self.simples2 = Grafo(['A', 'B', 'C','D'], {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-D','a4':'D-B'})
        self.simples3 = Grafo(['A','B','C'], {'a1':'A-B','a2':'B-C','a3':'C-A'})
        self.simples4 = Grafo(['A', 'B', 'C'], {'a1': 'A-C', 'a2': 'B-C', 'a3': 'B-A'})

    def TesteExemplosDoExercicio(self):
        TestedeGrafo.assertEqual(self, self.paraiba.buscaEmProfundidade('J'), ['J', 'a1', 'C', 'a2', 'E', 'a4', 'P', 'a6', 'M', 'a8', 'T', 'a9', 'Z'])
        TestedeGrafo.assertEqual(self, self.exemplo2.buscaEmProfundidade('K'), ['K', '4', 'G', '2', 'A', '1', 'B', '11', 'F', '10', 'H', '13', 'C', '14', 'D', '15', 'E', '3', 'J', '7', 'I'])

    def TesteGrafosCompletos(self):
        TestedeGrafo.assertEqual(self, self.completo1.buscaEmProfundidade('A'),  ['A', 'a1', 'B', 'a2', 'C'] )
        TestedeGrafo.assertEqual(self, self.completo1.buscaEmProfundidade('B'),  ['B', 'a1', 'A', 'a3', 'C'] )

        TestedeGrafo.assertEqual(self, self.completoAateG.buscaEmProfundidade('A'), ['A','a1','B','a2','C','a4','D','a5','E','a6','F','a7','G'])
        TestedeGrafo.assertEqual(self, self.completoAateG.buscaEmProfundidade('B'), ['B','a1','A','a2','C','a4','D','a5','E','a6','F','a7','G'])

        TestedeGrafo.assertEqual(self, self.completoAateG.buscaEmProfundidade('C'), ['C','a2','B','a1','A','a8','G','a7','D','a5','E','a6','F'])
        TestedeGrafo.assertEqual(self, self.completoAateG.buscaEmProfundidade('D'), ['D', 'a4', 'C', 'a2', 'B', 'a1', 'A', 'a8', 'G', 'a5', 'E', 'a6', 'F'])
        TestedeGrafo.assertEqual(self, self.completoAateG.buscaEmProfundidade('E'), ['E', 'a5', 'D', 'a4', 'C', 'a2', 'B', 'a1', 'A', 'a8', 'G', 'a6', 'F'])
        TestedeGrafo.assertEqual(self, self.completoAateG.buscaEmProfundidade('G'), ['G', 'a7', 'D', 'a4', 'C', 'a2', 'B', 'a1', 'A', 'a5', 'E', 'a6', 'F'])

        TestedeGrafo.assertEqual(self,self.completo_ciclo.buscaEmProfundidade('C'), ['C','a3','A','a1','B','a5','D','a6','E','a7','F'])
        TestedeGrafo.assertEqual(self,self.completo_ciclo2.buscaEmProfundidade('C'), ['C','a2','B','a1','A','a4','D'])
        TestedeGrafo.assertEqual(self, self.completo_ciclo2.buscaEmProfundidade('D'),['D','a3','C','a2','B','a1','A'])

    def TesteGrafosComLaco(self):
        TestedeGrafo.assertEqual(self, self.lacos1.buscaEmProfundidade('A'), ['A', 'a1', 'C', 'a4', 'D', 'a5', 'B'])
        TestedeGrafo.assertEqual(self,self.lacos2.buscaEmProfundidade('B'), ['B','a1','A'])
        TestedeGrafo.assertEqual(self, self.arestas_simples_com_laco.buscaEmProfundidade('B'), ['B', 'A2', 'A'])
        TestedeGrafo.assertEqual(self, self.arestas_simples_com_laco.buscaEmProfundidade('A'), ['A', 'A2', 'B'])
        TestedeGrafo.assertEqual(self, self.arestas_simples_com_laco1.buscaEmProfundidade('A'), ['A', 'A2', 'B','A4','C','A5','D'])


    def TesteGrafoSimples(self):
        TestedeGrafo.assertEqual(self, self.simples1.buscaEmProfundidade('A', ['A','a1','B','a3','C']))
        TestedeGrafo.assertEqual(self, self.simples1.buscaEmProfundidade('B', ['B', 'a1', 'A', 'a3','C']))
        TestedeGrafo.assertEqual(self, self.simples1.buscaEmProfundidade('C', ['C', 'a3', 'B', 'a1','A']))
        TestedeGrafo.assertEqual(self, self.simples2.buscaEmProfundidade('A', ['A', 'a1', 'B', 'a2', 'C','a3','D']))
        TestedeGrafo.assertEqual(self, self.simples2.buscaEmProfundidade('B', ['B', 'a1', 'A', 'a2', 'C', 'a3', 'D']))
        TestedeGrafo.assertEqual(self, self.simples2.buscaEmProfundidade('C', ['C', 'a2', 'B', 'a1', 'A', 'a3', 'D']))
        TestedeGrafo.assertEqual(self, self.simples2.buscaEmProfundidade('D', ['D', 'a3', 'C', 'a2', 'B', 'a1', 'A']))
        TestedeGrafo.assertEqual(self, self.simples3.buscaEmProfundidade('A', ['A', 'a1', 'B', 'a2', 'C']))
        TestedeGrafo.assertEqual(self, self.simples4.buscaEmProfundidade('A', ['A', 'a1', 'C', 'a2', 'B']))


