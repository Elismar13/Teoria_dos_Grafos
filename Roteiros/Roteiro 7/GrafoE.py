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

    def Dijkstra(self, vertice_partida, vertice_destino, carga_bateria, carga_max, pontos_recarga):
        vertices_mapeados = self.mapeamento_dos_vertices(self.N, pontos_recarga) # criando o mapa com todas informações
        # setando as informações do vertice de partida
        vertices_mapeados[vertice_partida]['beta'] = 0
        vertices_mapeados[vertice_partida]['rotulo'] = 1
        vertices_mapeados[vertice_partida]['bateria'] = carga_bateria

        vertice_atual = vertice_partida

        # Condição do loop geral
        while( vertice_atual != vertice_destino ):
            # Pego todos os vertices que estão ligados ao vertice atual
            arestas_incidentes_no_vertice = self.arestas_sobre_vertice(vertice_atual)

            # Para cada aresta incidente sobre o vertice...
            for aresta in arestas_incidentes_no_vertice:
                V1, V2 = aresta.split('-')
                # Qual o vertice atual e qual o vizinho?
                vertice_atual = V1 if (V1 == vertice_atual) else V2
                vertice_vizinho = V1 if (not V1 == vertice_atual) else V2

                # Inicialmente, consideramos que o drone possui bateria suficiente
                bateria_suficiente = True

                # Começamos, então, a realizar todos processamentos
                vertice_analisado_vizinho = vertices_mapeados[vertice_vizinho] #Primeiro, pego o mapa do vertice VIZINHO ao analisado em questão.
                vertice_analisado_atual = vertices_mapeados[vertice_atual] #Segundo, pego o mapa do vertice analisado em questão.

                vertice_analisado_vizinho['bateria'] = vertice_analisado_atual['bateria'] - 1 # Aqui fazemos a atulização da Bateria do vertice ATUAL+1, visto que a cada novo caminho gasta -1 de bateria.
                
                if vertice_analisado_vizinho['bateria'] <= 0:        # Se a bateria acabar perguntamos se esta em um ponto de recarga ou se pelo menos acabou no Destino;
                    if vertice_vizinho in pontos_recarga:
                        vertice_analisado_vizinho['bateria'] = carga_max
                    else:
                        vertice_analisado_vizinho['beta'] = float('inf')
                        posicao_vertice_na_lista_de_vertices = self.N.index(vertice_vizinho)
                        if self.N[posicao_vertice_na_lista_de_vertices] == vertice_destino:
                            bateria_suficiente = True
                        else:
                            bateria_suficiente = False
                if vertice_analisado_vizinho['bateria'] >= 0 and bateria_suficiente : # Se tem bateria ou pelo menos esta no destino, deixamos que ele faça as atualizações;
                    if vertice_analisado_vizinho['beta'] > vertice_analisado_atual['beta'] + 1:
                        vertice_analisado_vizinho['beta'] = vertice_analisado_atual['beta'] + 1
                        vertice_analisado_vizinho['antecessor'] = vertice_atual
                    if vertice_vizinho in pontos_recarga:   ## Se chegamos a um vértice que tem recarga, recarregamos mesmo que ainda tenha
                        vertice_analisado_vizinho['bateria'] = carga_max              ## bateria armazenada.

                # Atualizo os valores dos vertices processados no mapa
                vertices_mapeados[vertice_vizinho] = vertice_analisado_vizinho
                vertices_mapeados[vertice_atual] = vertice_analisado_atual

            vertice_atual = self.procura_vertice_com_pi_zero_e_menor_beta(vertices_mapeados) # Atualizamos o vértice atual.
            if vertice_atual == None: # Se não existir arestas com phi=0 que incidam no vertice atual para perocorrer e não chegamos ao final
                return False   # então não tem possibilidade de chegar até o destino final.

            vertices_mapeados[vertice_atual]['phi'] = 1 #Colocamos o phi(VerticeSAtual) = 1.

        # DEBUG PARA SABER O QUE ESTÁ SENDO PROCESSADO
        # self.mostraMapaNaTela(vertices_mapeados)
        return self.geraCaminhoAPartirDoMapa(vertices_mapeados, vertice_partida, vertice_destino)





        

    def mapeamento_dos_vertices(self, lista_vertices, pontos_recarga):
        mapa = dict()

        # Preenchendo o beta, o phi e o rótulo
        for vertice in lista_vertices:
            mapa[vertice] = {
                'vertice': vertice,
                'beta': float('inf'),
                'bateria': 0,
                'phi': 0,
                'rotulo': 0,
                'antecessor': '',
                'recarga': False,
            }
        
        for vertice in pontos_recarga:
            mapa[vertice]['recarga'] = True
        return mapa

    def procura_vertice_com_pi_zero_e_menor_beta(self, mapa: dict): 
        # Pego uma lista com todos os vertices com phi = 0
        vertices_validos = []
        for vertice in mapa.keys():
            if( mapa[vertice]['phi'] == 0 and mapa[vertice]['beta'] < float('inf') ): 
                # Adiciono todos os vertices TEMPORÁRIOS e seus BETAS em uma tupla.
                vertices_validos.append( (vertice, mapa[vertice]['beta']) )
        
        # Se tiver um dado vertice TEMPORARIO COM BETA MENOR QUE INFINITO
        if(vertices_validos != []):

            #Faço uma busca linear para saber quais deles tem o menor beta
            vertice_com_menor_beta = ('A', float('inf'))
            for vertice in vertices_validos:
                if(vertice_com_menor_beta[1] > vertice[1]):
                    vertice_com_menor_beta = vertice
            
            # Por fim, retorno apenas o vertice.
            return vertice_com_menor_beta[0]
        # Não há mais nada a se fazer por aqui...
        return None

    def geraCaminhoAPartirDoMapa(self, mapa: dict, vertice_partida, vertice_destino):
        """
            OBS: Irei fazer esta função buscando de 'trás pra frente',
            pois fica mais semântico com a estrutura de dados utilizada nesta minha versão.
        """

        # Declaro a lista de vertices do caminho e começo com o vértice de destino
        melhorCaminho = [vertice_destino]
        vertice_atual = vertice_destino
        # Loop para preencher o caminho, enquanto ainda não encontrar o vertice de partida
        while(vertice_atual != vertice_partida):
            # Atualizo o vertice atual com o antecessor dele
            vertice_atual = mapa[vertice_atual]['antecessor']
            melhorCaminho.append(vertice_atual)
        return melhorCaminho

    # Função apenas para depuração, pode ignorar
    def mostraMapaNaTela(self, mapa):
        for elemento in mapa.keys():
            elemento_no_mapa = mapa[elemento]

            print("===== VERTICE {} ======".format(elemento))

            for chave in elemento_no_mapa.keys():
                print("{}: {}".format(chave, elemento_no_mapa[chave]))