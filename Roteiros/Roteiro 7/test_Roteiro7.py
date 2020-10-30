import unittest
from GrafoE import *

class VerificarTests(unittest.TestCase):

    def setUp(self):
        self.g1 = Grafo(['A', 'B', 'C', 'D', 'E'])
        self.g1.adicionaAresta('A-B')
        self.g1.adicionaAresta('A-D')
        self.g1.adicionaAresta('A-E')
        self.g1.adicionaAresta('E-C')
        self.g1.adicionaAresta('B-C')

        self.g2 = Grafo(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'])
        self.g2.adicionaAresta('1-2')
        self.g2.adicionaAresta('1-5')
        self.g2.adicionaAresta('1-11')
        self.g2.adicionaAresta('1-6')
        self.g2.adicionaAresta('2-3')
        self.g2.adicionaAresta('6-7')
        self.g2.adicionaAresta('6-10')
        self.g2.adicionaAresta('11-10')
        self.g2.adicionaAresta('3-4')
        self.g2.adicionaAresta('7-8')
        self.g2.adicionaAresta('10-12')
        self.g2.adicionaAresta('12-8')
        self.g2.adicionaAresta('4-9')
        self.g2.adicionaAresta('8-9')
        self.g2.adicionaAresta('12-13')
        self.g2.adicionaAresta('9-13')

        self.g3 = Grafo(['1', '2', '3', '4', '5', '6', '7'])
        self.g3.adicionaAresta('1-3')
        self.g3.adicionaAresta('1-4')
        self.g3.adicionaAresta('4-7')
        self.g3.adicionaAresta('3-2')
        self.g3.adicionaAresta('2-7')
        self.g3.adicionaAresta('5-7')
        self.g3.adicionaAresta('6-5')
        self.g3.adicionaAresta('2-6')

        self.g4 = Grafo(['0', '1', '2', '3'])
        self.g4.adicionaAresta('1-0')
        self.g4.adicionaAresta('2-0')
        self.g4.adicionaAresta('1-2')
        self.g4.adicionaAresta('2-3')

        self.g5 = Grafo(['5', '4', '6', '7', '8', '9'])
        self.g5.adicionaAresta('5-4')
        self.g5.adicionaAresta('5-9')
        self.g5.adicionaAresta('9-8')
        self.g5.adicionaAresta('5-8')
        self.g5.adicionaAresta('4-6')
        self.g5.adicionaAresta('6-7')

        self.g6 = Grafo(['L', 'M', 'N', 'O', 'P'])
        self.g6.adicionaAresta('L-M')
        self.g6.adicionaAresta('L-O')
        self.g6.adicionaAresta('N-P')
        self.g6.adicionaAresta('M-P')
        self.g6.adicionaAresta('O-P')

        self.g7 = Grafo(['a', 'b', 'c', 'd'])
        self.g7.adicionaAresta('a-a')
        self.g7.adicionaAresta('a-b')
        self.g7.adicionaAresta('c-d')
        self.g7.adicionaAresta('d-c')
        self.g7.adicionaAresta('a-c')

        self.g8 = Grafo(['J', 'K', 'L', 'M', 'N'])
        self.g8.adicionaAresta('J-K')
        self.g8.adicionaAresta('J-N')
        self.g8.adicionaAresta('N-M')
        self.g8.adicionaAresta('K-M')
        self.g8.adicionaAresta('L-N')
        self.g8.adicionaAresta('L-J')

        self.g9 = Grafo(['5', '1', '3', '6', '4', '0', '2', '7'])
        self.g9.adicionaAresta('5-1')
        self.g9.adicionaAresta('1-3')
        self.g9.adicionaAresta('3-6')
        self.g9.adicionaAresta('6-4')
        self.g9.adicionaAresta('4-5')
        self.g9.adicionaAresta('5-4')
        self.g9.adicionaAresta('5-7')
        self.g9.adicionaAresta('5-7')
        self.g9.adicionaAresta('7-3')
        self.g9.adicionaAresta('7-2')
        self.g9.adicionaAresta('2-0')
        self.g9.adicionaAresta('0-4')
        self.g9.adicionaAresta('2-6')
        self.g9.adicionaAresta('0-6')

        self.g10 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
        self.g10.adicionaAresta('A-B')
        self.g10.adicionaAresta('B-C')
        self.g10.adicionaAresta('B-F')
        self.g10.adicionaAresta('C-E')
        self.g10.adicionaAresta('C-D')
        self.g10.adicionaAresta('E-D')
        self.g10.adicionaAresta('D-G')
        self.g10.adicionaAresta('F-G')

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

        self.completo0 = Grafo(['A', 'B', 'D', 'E', 'F', 'G', 'I'])
        self.completo0.adicionaAresta('A-E')
        self.completo0.adicionaAresta('E-F')
        self.completo0.adicionaAresta('F-G')
        self.completo0.adicionaAresta('G-B')
        self.completo0.adicionaAresta('B-A')
        self.completo0.adicionaAresta('A-I')
        self.completo0.adicionaAresta('A-D')
        self.completo0.adicionaAresta('I-D')
        self.completo0.adicionaAresta('D-E')

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
        self.completo1.adicionaAresta('H-J')

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

        self.lacos4 = Grafo(['A', 'B'])
        self.lacos4.adicionaAresta('A-B')
        self.lacos4.adicionaAresta('A-B')

    def test_Dijkstra(self):

        self.assertEqual(self.g1.Dijkstra('A','C',1,1,['B']), ['C', 'B', 'A'])
        self.assertFalse(self.g1.Dijkstra('A','C',1,1,[]))
        self.assertEqual(self.g2.Dijkstra('1','13',3 ,3 , ['4','8']), ['13', '9', '4', '3', '2', '1'])
        self.assertEqual(self.g2.Dijkstra('1','13',3 ,3 , ['8']), ['13', '9', '8', '7', '6', '1'])
        self.assertFalse(self.g2.Dijkstra('1','13', 3, 3, []))
        self.assertEqual(self.g3.Dijkstra('7','4',1,4,[]), ['4', '7'])
        self.assertEqual(self.g3.Dijkstra('2','4',1,4,['3','6']), ['4', '1', '3', '2'])
        self.assertEqual(self.g3.Dijkstra('1','5',3,5,['2','7']), ['5','7','4','1'])
        self.assertEqual(self.g4.Dijkstra('0','3',1,2,['2']), ['3', '2', '0'])
        self.assertEqual(self.g4.Dijkstra('0','3',1,2,['1']), ['3', '2', '1', '0'])
        self.assertEqual(self.g5.Dijkstra('8','7',1,5,['5','9']), ['7', '6', '4', '5', '8'])
        self.assertEqual(self.g5.Dijkstra('8','7',1,6,['9']), ['7', '6', '4', '5', '9', '8'])
        self.assertFalse(self.g5.Dijkstra('8','7', 1, 6, []))
        self.assertEqual(self.g6.Dijkstra('N','L',2,5,['M','O']), ['L', 'M', 'P', 'N'])
        self.assertEqual(self.g6.Dijkstra('L','N',2,5,['M','O']), ['N', 'P', 'M', 'L'])
        self.assertEqual(self.g7.Dijkstra('b','d',1,3,['a']), ['d', 'c', 'a', 'b'])
        self.assertEqual(self.g7.Dijkstra('c','d', 1, 3, ['a']), ['d', 'c'])
        self.assertEqual(self.g7.Dijkstra('c','d', 1, 3, []), ['d', 'c'])
        self.assertEqual(self.g8.Dijkstra('K','L',1,2,['M']), ['L', 'N', 'M', 'K'])
        self.assertFalse(self.g8.Dijkstra('K','L',1,2,[]))
        self.assertEqual(self.g9.Dijkstra('5','0',1,5,['1']), ['0', '6', '3', '1', '5'])
        self.assertEqual(self.g9.Dijkstra('5','0',1, 2, ['1','6']), ['0', '6', '3', '1', '5'])
        self.assertEqual(self.g9.Dijkstra('1','4',1, 2, ['2','3']), ['4', '6', '3', '1'])
        self.assertEqual(self.g9.Dijkstra('1','4',2, 2, ['2']), ['4', '5', '1'])
        self.assertEqual(self.g10.Dijkstra('A','G',2,5,['C','F']), ['G', 'F', 'B', 'A'])
        self.assertFalse(self.g10.Dijkstra('A','G',1, 5, ['C', 'F']))
        self.assertEqual(self.g10.Dijkstra('B','E',2, 5, ['C', 'F']), ['E', 'C', 'B'])
        self.assertEqual(self.completoAateG.Dijkstra('A','G',3,5,['B','E']),['G','B','A'])
        self.assertEqual(self.completoAateG.Dijkstra('A','F',3,5,['B','E']), ['F', 'E', 'D', 'C', 'B', 'A'])
        self.assertFalse(self.completoAateG.Dijkstra('A','F',3,5, ['E']))
        self.assertEqual(self.ciclo_simples.Dijkstra('E', 'A', 2, 2,[]), ['A', 'C', 'E'])
        self.assertEqual(self.ciclo_simples.Dijkstra('E', 'B', 2, 2, ['D']), ['B', 'C', 'E'])
        self.assertEqual(self.ciclo_simples.Dijkstra('A', 'C', 1, 1, ['B']), ['C', 'B', 'A'])
        self.assertEqual(self.ciclo_simples.Dijkstra('A', 'F', 1, 4, ['B']), ['F','E','C', 'B', 'A'])
        self.assertFalse(self.completo0.Dijkstra('I','B',1,3,['G','F']))
        self.assertEqual(self.completo0.Dijkstra('I','B',2,3,['G']), ['B', 'A', 'I'])
        self.assertEqual(self.completo0.Dijkstra('I', 'G', 2, 3, ['D']), ['G', 'F', 'E', 'D', 'I'])
        self.assertEqual(self.completo0.Dijkstra('I', 'G', 1, 3, ['A']), ['G', 'B', 'A', 'I'])
        self.assertEqual(self.completo1.Dijkstra('J','F',2,4,[]), ['F', 'J'])
        self.assertEqual(self.completo1.Dijkstra('A','J',2,4,['C']), ['J', 'F', 'E', 'C', 'A'])
        self.assertEqual(self.incompleto0.Dijkstra('k','t',2, 2, []), ['t', 'l', 'k'])
        self.assertFalse(self.incompleto0.Dijkstra('k','t',1,2,['m']))
        self.assertEqual(self.incompleto0.Dijkstra('n','t',1,2,['m']), ['t', 'm', 'n'])
        self.assertEqual(self.lacos4.Dijkstra('A', 'A', 1, 1, []), ['A'])
        self.assertEqual(self.lacos4.Dijkstra('A', 'B', 1, 1, ['B']), ['B', 'A'])