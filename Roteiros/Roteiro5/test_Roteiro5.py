import unittest
from Grafo_Nao_Direc import *

class VerificarTests(unittest.TestCase):

    """
        Observação: No nosso algoritmo a ordem das arestas influenciam no resultado.
        Por exemplo, podemos chegar no mesmo resultado mas em uma ordem diferente, pois
        nosso algoritmo segue a ordem dos vertices.
    """
    def setUp(self):
        self.g1 = Grafo(['5', '1', '3', '6', '4', '0', '2', '7'])
        self.g1.adicionaAresta('5-1')
        self.g1.adicionaAresta('1-3')
        self.g1.adicionaAresta('3-6')
        self.g1.adicionaAresta('6-4')
        self.g1.adicionaAresta('4-5')
        self.g1.adicionaAresta('5-4')
        self.g1.adicionaAresta('5-7')
        self.g1.adicionaAresta('5-7')
        self.g1.adicionaAresta('7-3')
        self.g1.adicionaAresta('7-2')
        self.g1.adicionaAresta('2-0')
        self.g1.adicionaAresta('0-4')
        self.g1.adicionaAresta('2-6')
        self.g1.adicionaAresta('0-6')

        self.g2 = Grafo(['5', '1', '3', '6', '4', '0', '2', '7'])
        self.g2.adicionaAresta('5-1')
        self.g2.adicionaAresta('1-3')
        self.g2.adicionaAresta('3-6')
        self.g2.adicionaAresta('6-4')
        self.g2.adicionaAresta('4-5')
        self.g2.adicionaAresta('5-4')
        self.g2.adicionaAresta('5-7')
        self.g2.adicionaAresta('5-7')
        self.g2.adicionaAresta('7-3')
        self.g2.adicionaAresta('7-2')
        self.g2.adicionaAresta('2-0')
        self.g2.adicionaAresta('4-7')
        self.g2.adicionaAresta('2-6')
        self.g2.adicionaAresta('0-6')

        self.g3 = Grafo(['0','1','2','3','4','5','6','7','8','9'])
        self.g3.adicionaAresta('0-5')
        self.g3.adicionaAresta('0-1')
        self.g3.adicionaAresta('0-2')
        self.g3.adicionaAresta('0-3')
        self.g3.adicionaAresta('1-4')
        self.g3.adicionaAresta('2-4')
        self.g3.adicionaAresta('2-3')
        self.g3.adicionaAresta('3-6')
        self.g3.adicionaAresta('7-6')
        self.g3.adicionaAresta('4-6')
        self.g3.adicionaAresta('3-6')
        self.g3.adicionaAresta('7-3')
        self.g3.adicionaAresta('8-7')
        self.g3.adicionaAresta('9-8')
        self.g3.adicionaAresta('8-6')
        self.g3.adicionaAresta('4-9')
        self.g3.adicionaAresta('5-9')
        
        self.g4 = Grafo(['B', 'C', 'D', 'E'])
        self.g4.adicionaAresta('B-C')
        self.g4.adicionaAresta('C-D')
        self.g4.adicionaAresta('D-E')
        self.g4.adicionaAresta('E-C')
        self.g4.adicionaAresta('B-E')
        self.g4.adicionaAresta('D-B')
        
        self.g5 = Grafo(['I','J','K','L','M'])
        self.g5.adicionaAresta('I-J')
        self.g5.adicionaAresta('J-K')
        self.g5.adicionaAresta('J-L')
        self.g5.adicionaAresta('M-I')
        self.g5.adicionaAresta('K-M')
        self.g5.adicionaAresta('K-I')
        self.g5.adicionaAresta('I-L')
        self.g5.adicionaAresta('M-L')
        
        self.g6 = Grafo(['Z', 'P', 'I', 'U', 'V', 'T'])
        self.g6.adicionaAresta('P-Z')
        self.g6.adicionaAresta('U-P')
        self.g6.adicionaAresta('I-P')
        self.g6.adicionaAresta('I-Z')
        self.g6.adicionaAresta('T-Z')
        self.g6.adicionaAresta('V-T')
        self.g6.adicionaAresta('I-T')
        self.g6.adicionaAresta('U-V')
        self.g6.adicionaAresta('U-Z')

        self.g7 = Grafo(['B'])
        self.g7.adicionaAresta('B-B')

        self.g8 = Grafo(['B','A'])
        self.g8.adicionaAresta('B-B')
        self.g8.adicionaAresta('A-B')
        self.g8.adicionaAresta('A-B')

        self.g9 = Grafo(['B', 'A'])
        self.g9.adicionaAresta('B-B')
        self.g9.adicionaAresta('A-A')

        self.G10 = Grafo(['A', 'B', 'C', 'D'])
        self.G10.adicionaAresta('A-B')
        self.G10.adicionaAresta('B-C')
        self.G10.adicionaAresta('C-D')
        self.G10.adicionaAresta('A-D')
        self.G10.adicionaAresta('A-C')
        self.G10.adicionaAresta('D-B')

        self.completoAateG = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.completoAateG.adicionaAresta('A-B')
        self.completoAateG.adicionaAresta('B-C')
        self.completoAateG.adicionaAresta('C-B')
        self.completoAateG.adicionaAresta('C-D')
        self.completoAateG.adicionaAresta('D-E')
        self.completoAateG.adicionaAresta('E-F')
        self.completoAateG.adicionaAresta('D-G')
        self.completoAateG.adicionaAresta('B-G')

        self.ciclo_simples = Grafo(['A', 'B', 'C', 'D', 'E', 'F'])
        self.ciclo_simples.adicionaAresta('A-B')
        self.ciclo_simples.adicionaAresta('B-A')
        self.ciclo_simples.adicionaAresta('C-A')
        self.ciclo_simples.adicionaAresta('C-B')
        self.ciclo_simples.adicionaAresta('C-D')
        self.ciclo_simples.adicionaAresta('C-E')
        self.ciclo_simples.adicionaAresta('E-F')

        self.simples1 = Grafo(['A', 'B', 'C'])
        self.simples1.adicionaAresta('A-B')
        self.simples1.adicionaAresta('B-C')
        self.simples1.adicionaAresta('C-B')

        self.simples2 = Grafo(['A', 'B', 'C', 'D'])
        self.simples2.adicionaAresta('A-B')
        self.simples2.adicionaAresta('B-C')
        self.simples2.adicionaAresta('C-B')
        self.simples2.adicionaAresta('D-B')

        self.simples3 = Grafo(['A', 'B', 'C', 'D'])
        self.simples3.adicionaAresta('A-B')
        self.simples3.adicionaAresta('B-A')
        self.simples3.adicionaAresta('B-C')
        self.simples3.adicionaAresta('C-C')
        self.simples3.adicionaAresta('C-D')
        self.simples3.adicionaAresta('A-D')

        self.completo0 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
        self.completo0.adicionaAresta('A-E')
        self.completo0.adicionaAresta('E-F')
        self.completo0.adicionaAresta('F-G')
        self.completo0.adicionaAresta('G-B')
        self.completo0.adicionaAresta('B-A')
        self.completo0.adicionaAresta('A-I')
        self.completo0.adicionaAresta('A-D')
        self.completo0.adicionaAresta('A-C')
        self.completo0.adicionaAresta('C-H')

        self.completo1 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'J', 'H', 'I'])
        self.completo1.adicionaAresta('A-C')
        self.completo1.adicionaAresta('A-B')
        self.completo1.adicionaAresta('C-D')
        self.completo1.adicionaAresta('C-E')
        self.completo1.adicionaAresta('B-A')
        self.completo1.adicionaAresta('B-D')
        self.completo1.adicionaAresta('B-E')
        self.completo1.adicionaAresta('E-D')
        self.completo1.adicionaAresta('E-A')
        self.completo1.adicionaAresta('E-F')
        self.completo1.adicionaAresta('F-J')
        self.completo1.adicionaAresta('J-F')
        self.completo1.adicionaAresta('E-D')
        self.completo1.adicionaAresta('H-D')
        self.completo1.adicionaAresta('E-H')
        self.completo1.adicionaAresta('H-I')
        self.completo1.adicionaAresta('I-A')

        self.incompleto0 = Grafo(['h', 't', 'o', 'j', 'k', 'l', 'm', 'n'])
        self.incompleto0.adicionaAresta('o-o')
        self.incompleto0.adicionaAresta('t-l')
        self.incompleto0.adicionaAresta('l-t')
        self.incompleto0.adicionaAresta('l-k')
        self.incompleto0.adicionaAresta('o-j')
        self.incompleto0.adicionaAresta('t-o')
        self.incompleto0.adicionaAresta('m-t')
        self.incompleto0.adicionaAresta('k-j')
        self.incompleto0.adicionaAresta('l-k')
        self.incompleto0.adicionaAresta('l-m')
        self.incompleto0.adicionaAresta('n-m')

        self.lacos3 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'H'])
        self.lacos3.adicionaAresta('A-B')
        self.lacos3.adicionaAresta('A-A')
        self.lacos3.adicionaAresta('B-B')
        self.lacos3.adicionaAresta('A-C')
        self.lacos3.adicionaAresta('C-D')
        self.lacos3.adicionaAresta('D-E')
        self.lacos3.adicionaAresta('E-E')
        self.lacos3.adicionaAresta('E-F')
        self.lacos3.adicionaAresta('E-B')
        self.lacos3.adicionaAresta('E-C')
        self.lacos3.adicionaAresta('C-H')


    def test_CicloHamiltoniano(self):
        self.assertEqual(self.g1.CicloHamiltoniano(), ['5', '1', '3', '6', '4', '0', '2', '7', '5'])
        self.assertEqual(self.g2.CicloHamiltoniano(), ['3', '1', '5', '4', '6', '0', '2', '7', '3'])
        self.assertEqual(self.g3.CicloHamiltoniano(), ['0', '1', '4', '2', '3', '6', '7', '8', '9', '5', '0'])
        self.assertEqual(self.simples2.CicloHamiltoniano(), ['B', 'A', 'C', 'D', 'B'])
        self.assertEqual(self.g4.CicloHamiltoniano(), ['B', 'C', 'D', 'E', 'B'])
        self.assertEqual(self.ciclo_simples.CicloHamiltoniano(), ['E', 'C', 'A', 'B', 'D', 'F', 'E'])
        self.assertEqual(self.g5.CicloHamiltoniano(), ['I', 'J', 'K', 'M', 'L', 'I'])
        self.assertEqual(self.g6.CicloHamiltoniano(), ['Z', 'P', 'I', 'T', 'V', 'U', 'Z'])
        self.assertEqual(self.simples1.CicloHamiltoniano(), ['B', 'A', 'C', 'B'])
        self.assertEqual(self.g7.CicloHamiltoniano(), ['B', 'B'])
        self.assertEqual(self.completo1.CicloHamiltoniano(), ['A', 'B', 'D', 'C', 'E', 'F', 'J', 'H', 'I', 'A'])
        self.assertEqual(self.completoAateG.CicloHamiltoniano(), ['B', 'A', 'C', 'D', 'E', 'F', 'G', 'B'])
        self.assertEqual(self.g8.CicloHamiltoniano(), ['B', 'A','B'])
        self.assertFalse(self.g9.CicloHamiltoniano())
        self.assertEqual(self.G10.CicloHamiltoniano(), ['A', 'B', 'C', 'D', 'A'])
        self.assertEqual(self.lacos3.CicloHamiltoniano(), ['C', 'A', 'B', 'E', 'D', 'F', 'H', 'C'])
        self.assertEqual(self.completo0.CicloHamiltoniano(), ['A', 'B', 'G', 'F', 'E', 'C', 'H', 'D', 'I', 'A'])
        self.assertFalse(self.incompleto0.CicloHamiltoniano())
        self.assertEqual(self.simples3.CicloHamiltoniano(), ['A', 'B', 'C', 'D', 'A'])