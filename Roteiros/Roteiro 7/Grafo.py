# -*- coding: utf-8 -*-

class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class MatrizInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, V=None, M=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que
        indica a quantidade de arestas que ligam aqueles vértices
        '''

        if V == None:
            V = list()
        if M == None:
            M = list()

        for v in V:
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if M == []:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    if k > l:
                        M[k].append('-')
                    else:
                        M[k].append(0)

        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                if i > j and not (M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')

                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]
                if not (self.arestaValida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = list(M)

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo.SEPARADOR_ARESTA) + 1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__segundo_vertice_aresta(a))

    def existeAresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)  # Adiciona vértice na lista de vértices
            self.M.append([])  # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) - 1:
                    self.M[k].append(0)  # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-')  # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, a):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''

        if self.arestaValida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] += 1
            else:
                self.M[i_a2][i_a1] += 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def remove_aresta(self, a):
        '''
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            if self.existeAresta(a):
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                if i_a1 < i_a2:
                    self.M[i_a1][i_a2] -= 1
                else:
                    self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' ' * (self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str

    # O Roteiro 4:

    def vertices_nao_adjacentes(self):
        '''
        Explicação: Em sua definição é basicamente todas as outras combinação (na matriz) que não foram inicialmente declaradas;
        '''
        ListaNaoArestas = []
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if (self.M[i][j] != '-'):
                    if (int(self.M[i][j]) == 0):
                        Aresta = self.N[i] + '-' + self.N[j]
                        ListaNaoArestas.append(Aresta)
        return ListaNaoArestas

    def eh_completo(self):
        '''
        Explicção: Primeira sabemos que para ser definido completo ele não pode ter nem laço nem arestas paralelas, então o primeiro passo que fizemos foi
        verificar se exitem laço ou arestas paralelas, em seguida sabemos que para ser completo ele precisa que todos os seus vertices distintos sejam
        adjacentes,então criamos uma lista para guardar os  adjacentes baseado na função vertices_nao_ adjacentes, percorremos essa lista, que possuem
        lacos, e tiramos pois se comparamos com um grafo completo não pode ter laços, em seguida refificamos se as aresas inicialmente passadas em sua
        formação encontra os vertices adjacentes se sim, ele é completo. Ou se a lista R é vazia, significa que todos os vertices adjacentes já foram
        passados inicial (Para ter certeza que é completo).
        '''
        R = []
        Paralelas = self.ha_paralelas()
        Lacos = self.ha_laco()
        if (Paralelas or Lacos):
            return False
        else:
            NaoAdjacentes = self.vertices_nao_adjacentes()
            for i in range(len(NaoAdjacentes)):
                if (NaoAdjacentes[i][0] != NaoAdjacentes[i][2]):
                    # print(NaoAdjacentes[i])
                    R.append(NaoAdjacentes[i])

            if (R in self.ListaArestas() or R == []):
                return True
            else:
                return False

            # if (NaoAdjacentes.self.ha_laco()):
            #    return False
            # return True

            # print(NaoAdjacentes)
            # R.append(NaoAdjacentes + self.ListaArestas())
            # print(self.ListaArestas())
            # print(R)
            # if (R[0]==self.ListaArestas()):
            #    return True
            # else:
            #    return False

    def ha_paralelas(self):
        '''
        Explicação: Com a Paralelas (que contem um True ou False) temos como saber se ha_paralelas ou não. Baseada na função auxiliar
        que percorre a lista apenas para saber que a combinação Vértice[i] com Vértice[j] é maior que 1, porque se for, indica que
        existe mais de uma aretas que incidem nos mesmos vértices, neste momento ele retorna True, caso ele percorra toda a matriz e
        não encontre uma combinação Vértice[i] com Vértice[j] que seja maior que 1, então indica que existem apenas uma aresta que
        incidem sobre aquele respectivo vértice.
        '''
        Paralelas = self.Paralelas()
        if Paralelas:
            return True
        else:
            return False

    def grau(self, VerticeDesejado):
        '''
        Explicação: Através da função arestas_sobre_vertice temos acesso a todas as arestas que contem o desejado vértice, assim
        só contando a quantidade de elementos da lista (arestas_sobre_vertice) temos o resultado que é o grau.
        '''
        ArestasQueIncidem = self.arestas_sobre_vertice(VerticeDesejado)
        Resultado = len(ArestasQueIncidem)
        return Resultado

    def arestas_sobre_vertice(self, VerticeDesejado):
        '''
        Explicação: Através da função ListaArestas que percorre a matriz, temos acesso as arestas da matriz assim, podemos  'perguntar'
        se o vertice desejado esta como X do modelo X-Y ou está no Y. Se estiver o colocamos em uma lista especial que só concentra
        arestas que contenham o vertice desejado.
        '''
        LA = self.ListaArestas()
        ArestasDesejadas = []
        for i in range(len(LA)):
            A = LA[i]
            Aresta = A.split('-')
            if (Aresta[0] == VerticeDesejado or Aresta[1] == VerticeDesejado):
                ArestasDesejadas.append(A)
            # if (Aresta[2]==VerticeDesejado):  Ultima alteração 2109
            #    ArestasDesejadas.append(Aresta) Ultima alteração 2109
        return ArestasDesejadas

    def ha_laco(self):
        '''
        Explicação: Na diagonal principal se encontra a junção dos vértices (J-J,C-C), então se existir um laço, na respectiva posição
        da diagonal principal estará um número de acordo com a quantidade de laços, então se ao percorrer a diagonal principal, se encontrarmos
        um valor diferente de zero, significa que existe pelo menos um laço. Escolhemos somar tudo de uma vez por aparatentar para nós um melhor
        sentido. Mas em todos os casos, se encontrar um valor diferente de 0 já será considerado True.
        '''
        Soma_Diagonal = sum(self.M[i][i] for i in range(len(self.N)))
        if (Soma_Diagonal) > 0:
            return True
        else:
            return False

    def Paralelas(self):
        '''
        Explicação: É uma função bem semelhante a função abaixo, a sua diferença é que ela percorre a lista apenas para saber que a combinação
        Vértice[i] com Vértice[j] é maior que 1, porque se for, indica que existe mais de uma aretas que incidem nos mesmos vértices, neste
        momento ele retorna True, caso ele percorra toda a matriz e não encontre uma combinação Vértice[i] com Vértice[j] que seja maior que 1,
        então indica que existem apenas uma aresta que incidem sobre aquele respectivo vértice.
        '''
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if (self.M[i][j] != '-'):
                    if (int(self.M[i][j]) > 0):
                        if (int(self.M[i][j]) > 1):
                            # Se for maior que 1 então temos mais de uma arestas que incidem nos mesmos vertices.
                            return True
        return False

    def ListaArestas(self):
        '''
        Explicação: Percorremos a matriz e quando encontramos um numero, criamos a aresta e a quantidad de vezes que ele esta no grafo
        e colocamos em uma ListaArestas, que contém todas as aretas do grafo.
        '''
        ListaArestas = []
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if (self.M[i][j] != '-'):
                    if (int(self.M[i][j]) > 0):
                        for k in range(int(self.M[i][j])):
                            Aresta = self.N[i] + '-' + self.N[j]
                            ListaArestas.append(Aresta)
        return ListaArestas

    ###########################################################################################################
    ################################################ ROTEIRO 7 ################################################
    ###########################################################################################################

    def Dijkstra(self, Partida, Destino, CargaInicial, CargaMax, PontosDeRecargas):
        Beta = self.Beta(self.N.index(Partida),len(self.N)) #Fazemos uma lista com betas, a partida como zero e os demais como infinito.
        Phi = self.ListaPhi_Pi_Bat(len(self.N))             #Fazemos uma lista com phi, com todos os elementes iguais a zero.
        Phi[self.N.index(Partida)] = 1                      #Estava zero. #Colocamos phi=1 no ponto de partida.
        Pi = self.ListaPhi_Pi_Bat(len(self.N))              #Fazemos uma lista com pi, com todos os elementes iguais a zero.
        Bat = self.ListaPhi_Pi_Bat(len(self.N))             #Fazemos uma lista com bat, com todos os elementes iguais a zero.
        Bat[self.N.index(Partida)] = CargaInicial           #A lista bat = Bateria, colocamos no ponto de partida o valor inicial.
        VerticeAtual = Partida

        while ( VerticeAtual != Destino ):

            ArestasSobreOVertice = self.arestas_sobre_vertice(VerticeAtual)
            # A lista ASV tem todas as arestas com o incidencia no vértice atual com phi==0 e phi==1
            # Teste # ArestasSobreOVertice = self.ListaComVertices(VerticeAtual,Phi,ASV)
            # Teste # A lista ArestasSobreOVertice só pode ter arestas relacionado com o vértice atual (obviamente) E com os phi==0;

            for i in range(len(ArestasSobreOVertice)):
                A = ArestasSobreOVertice[i]
                Aresta = A.split('-')

                if Aresta[0] == VerticeAtual:
                    V1 = self.N.index(Aresta[0])    #Descobrimos o indice do V1 (V1-V2)
                    V2 = self.N.index(Aresta[1])    #Descobrimos o indice do V2 (V1-V2)
                    #Reserva = Bat[V2]  # Reserva = Armazena o valor da bateria do seu vértice correspondente antes de uma possivel mudança;
                    Controle = True
                    Bat[V2] = Bat[V1] - 1   # Aqui fazemos a atulização da Bateria, visto que a cada novo caminho -1 de bateria.
                    if Bat[V2] == 0:        # Se a bateria acabar perguntamos se esta em um ponto de recarga ou se pelo menos acabou no Destino;
                        if Aresta[1] in PontosDeRecargas:
                            Bat[V2] = CargaMax
                        else:
                            Beta[V2] = float('inf')
                            if self.N[V2] == Destino:
                                Controle = True
                            else:
                                Controle = False
                    if Bat[V2] >= 0 and Controle : # Se tem bateria ou pelo menos esta no destino, deixamos que ele faça as atualizações;
                        if Beta[V2] > Beta[V1] + 1:
                            Beta[V2] = Beta[V1] + 1
                            Pi[V2] = VerticeAtual
                        if Aresta[1] in PontosDeRecargas:   ## Se chegamos a um vértice que tem recarga, recarregamos mesmo que ainda tenha
                            Bat[V2] = CargaMax              ## bateria armazenada.
                    #if Bat[V2]<0:
                    #    Bat[V2] = Reserva

                if Aresta[1] == VerticeAtual:
                    V1 = self.N.index(Aresta[0])    #Descobrimos o indice do V1 (V1-V2)
                    V2 = self.N.index(Aresta[1])    #Descobrimos o indice do V2 (V1-V2)
                    #Reserva = Bat[V1] #Reserva = Armazena o valor da bateria do seu vértice correspondente antes de uma possivel mudança;
                    Controle = True
                    Bat[V1] = Bat[V2] - 1   # Aqui fazemos a atulização da Bateria, visto que a cada novo caminho -1 de bateria.
                    if Bat[V1]<=0:          # Se a bateria acabar perguntamos se esta em um ponto de recarga ou se pelo menos acabou no Destino;
                        if Aresta[0] in PontosDeRecargas:
                            Bat[V1] = CargaMax
                        else:
                            Beta[V1] = float('inf')
                            if self.N[V1] == Destino:
                                Controle = True
                            else:
                                Controle = False
                    if Bat[V1]>=0 and Controle: # Se tem bateria ou pelo menos esta no destino, deixamos que ele faça as atualizações;
                        if Beta[V1] > Beta[V2] + 1:
                            Beta[V1] = Beta[V2] + 1
                            Pi[V1] = VerticeAtual
                        if Aresta[0] in PontosDeRecargas:   ## Se chegamos a um vértice que tem recarga, recarregamos mesmo que ainda tenha
                            Bat[V2] = CargaMax              ##  bateria armazenada.
                    #if Bat[V1] < 0:
                    #    Bat[V1] = Reserva

            Indice = self.IndiceDoProximoVertice(Phi,Beta)  #Retornamos o indice do proximo vértice.
            if Indice == None: # Se não existir arestas com phi=0 que incidam no vertice atual para perocorrer e não chegamos ao final
                return False   # então não tem possibilidade de chegar até o destino final.
            VerticeAtual = self.N[Indice] #Atualizamos o vértice atual.
            Phi[self.IndiceDoProximoVertice(Phi,Beta)] = 1  #Colocamos o phi(VerticeSAtual) = 1.

        Percuso = self.CaminhoDijkstra(Pi,Partida,Destino) # Se chegou aqui, significa que existe um caminho.
        Bat[self.N.index(Partida)] = CargaInicial          # Colocamos a carga inicial na beteira(partida)
        return Percuso                                     # Retornamos o percurso.

    def IndiceDoProximoVertice(self, Phi, Beta):        # Descobrir qual será o próximo 'VerticeAtual'
        Phi2, Aux = [], {}
        for i in range(len(Phi)):
            if Phi[i]==0 and Beta[i] < float('inf'):    # Comparamos se o seu phi é zero, ou seja, se não estamos percorrendo um mesmo vértice
                Phi2.append(i)                          # Também descobrimos se o seu beta é o menor. E colocamos em uma lista (Phi2)
        if Phi2==[]:                                    # Se essa nova lista for vazia, não tem mais vértices para percorrer.
            return None
        for i in Phi2:                                  # Aqui, colocamos todos os menores valores em um dicionário com a chave sendo a sua posição
            Aux[i] = Beta[i]                            # e o seu item/valor correspondeno ao seu respectivo beta.

        print(Phi, Beta, Aux)
        IndiceComMenorValor = min(Aux, key = lambda chave: int(Aux[chave]))     # Aqui usamos uma tecnica para descobrir o menor valor do item
        return IndiceComMenorValor                                              # E retornamos a sua chave;

    def CaminhoDijkstra(self,Pi,Partida,Destino):  # Retorna o caminho (percuso).
        IndiceDestino = self.N.index(Destino)      # Descobrimos o indice do Destino;
        Indice = Pi[IndiceDestino]                 # Indice recebe o vértice que liga ao Vértice de Destino.
        Caminho = [Destino]                        # Fazemos uma lista que receberá todos os vértices que fizerem parte do percurso.
        Controle = Destino                         # Controle = Quando estivermos fazendo a volta (já que começamos do fim para o inicio)
        I = 1                                      # ele receberá o vértice antecessor e assim comparamos se chegamos ao ponto de partida (inicio).
        while(Controle!=Partida):
            Caminho.append(Indice)                  # Colocamos o antecessor na lista (Caminho)
            C = Caminho[I]                          # C = Armazena o antecessor.
            Indice =  Pi[self.N.index(C)]           # Indice = Descobre o antecessor (pi) do antecessor (Parce confuso mas faz sentido)
            I += 1                                  #
            Controle = C                            # Controle que usamos para saber quando o percurso chegou ao fim (nesse caso ao inicio.)
        return Caminho

    def Beta(self,Partida,QTDE):    #Cria uma lista todos os elementos sendo infinito com exceção do nosso ponto de partida que recebe zero.
        B = []
        for i in range(QTDE):
            if i == Partida:
                B.append(0)
            else:
                B.append(float('inf'))
        return B

    def ListaPhi_Pi_Bat(self,QTDE):  #Cria uma lita com todos os elementos iguais a zero.
        L = []
        for i in range(QTDE):
            L.append(0)
        return L

    '''
    
    # def ListaComVertices(self,VerticeAtual,Phi,ArestasSobreOVertice):
    #    Lista = []
    #    for i in range(len(ArestasSobreOVertice)):
    #        a = ArestasSobreOVertice[i]
    #        asv = a.split('-')
    #        if asv[0] != VerticeAtual:
    #            indzero = self.N.index(asv[0])
    #            if (Phi[indzero]==0):
    #                Lista.append(a)
    #        if asv[1] != VerticeAtual:
    #            indum = self.N.index(asv[1])
    #            if (Phi[indum]==0):
    #                Lista.append(a)
    #    return Lista

   
        def Beta(self,Partida,QTDE):
            B = []
            for i in range(QTDE):
                if i == Partida:
                    B.append(0)
                else:
                    B.append(float('inf')) #Adiciona o infinito. Teoricamente. #print(B[i]>0)
            return B
    
        def ListaPhi_Pi(self,QTDE):
            L = []
            for i in range(QTDE):
                L.append(0)
            return L
    
        def IndiceDoProximoVertice(self, Phi, Beta):
            Phi2 = []
            for i in range(len(Phi)):
                if Phi[i]==0 and Beta[i] < float('inf'): #Guardamos as posições de quem possui o phi==0 e menor beta: [1, 3, 4] e todos são [1,1,1];
                    Phi2.append(i)
            IndiceComMenorValor = Beta.index(min(Phi2))
            return IndiceComMenorValor
            
            ou 
            
            Phi2, Aux = [], {}
            for i in range(len(Phi)):
                if Phi[i]==0 and Beta[i] < float('inf'):
                    Phi2.append(i)
            if Phi2==[]:
                return None
            for i in Phi2:
                Aux[i] = Beta[i]
            IndiceComMenorValor = min(Aux, key = lambda chave: int(Aux[chave]))
            return IndiceComMenorValor
            
        def DijkstraOriginal(self, Partida, Destino):
        Beta = self.Beta(self.N.index(Partida),len(self.N)) #Vai passar o index da Partida e a quantidade de vértices.
        Phi = self.ListaPhiEPi(len(self.N))
        Phi[0] = 1
        Pi = self.ListaPhiEPi(len(self.N)) 
        # Um print deles seria: ([0, inf, inf, inf, inf], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0])
        # ArestasSobreOVertice = self.arestas_sobre_vertice(Partida) #['A-B', 'A-D', 'A-E'] (Inicial)
        VerticeAtual = Partida # O vértice de inicil é o 'A' e o ind é 0

        while ( VerticeAtual != Destino ):
            
            ASV = self.arestas_sobre_vertice(VerticeAtual)
            ArestasSobreOVertice = self.ListaComVertices(VerticeAtual,Phi,ASV)

            for i in range(len(ArestasSobreOVertice)):
                A = ArestasSobreOVertice[i]
                Aresta = A.split('-')

                if Aresta[0] == VerticeAtual:
                    V1 = self.N.index(Aresta[0])
                    V2 = self.N.index(Aresta[2])
                    if Beta[V2] > Beta[V1] + 1:
                        Beta[V2] = Beta[V1] + 1
                        Pi[V2] = VerticeAtual
                if Aresta[2] == VerticeAtual:
                    V1 = self.N.index(Aresta[0])
                    V2 = self.N.index(Aresta[2])
                    if Beta[V1] > Beta[V2] + 1:
                        Beta[V1] += Beta[V2] + 1
                        Pi[V1] = VerticeAtual
                        
            VerticeAtual = self.N[self.IndiceDoProximoVertice(Phi,Beta)] 
            Phi[self.IndiceDoProximoVertice(Phi,Beta)] = 1

        Percuso = self.CaminhoDijkstra(Pi,Partida,Destino)
        return Percuso
        
        
        def CaminhoDijkstra(self,Pi,Partida,Destino):
            IndiceDestino = self.N.index(Destino)
            Indice = Pi[IndiceDestino]
            Caminho = [Destino]
            Controle = Destino
            I = 1
            while(Controle!=Partida):
                Caminho.append(Indice)
                C = Caminho[I]
                Indice =  Pi[self.N.index(C)]
                I += 1
                Controle = C
            return Caminho

    '''
