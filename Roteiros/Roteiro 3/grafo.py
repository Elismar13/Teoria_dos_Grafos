class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parãmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que cont�m dois vértices separados por um traço.
        '''
        for v in N:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not(self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A


    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como par�metro est� dentro do padr�o estabelecido.
        Uma aresta � representada por um string com o formato a-b, onde:
        a � um substring de aresta que � o nome de um v�rtice adjacente � aresta.
        - � um caractere separador. Uma aresta s� pode ter um �nico caractere como esse.
        b � um substring de aresta que � o nome do outro v�rtice adjacente � aresta.
        Al�m disso, uma aresta s� � v�lida se conectar dois v�rtices existentes no grafo.
        :param aresta: A aresta que se quer verificar se est� no formato correto.
        :return: Um valor booleano que indica se a aresta est� no formato correto.
        '''

        # N�o pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # �ndice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador n�o pode ser o primeiro ou o �ltimo caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        # Verifica se as arestas antes de depois do elemento separador existem no Grafo
        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um v�rtice passado como par�metro est� dentro do padr�o estabelecido.
        Um v�rtice � um string qualquer que n�o pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o v�rtice a ser analisado.
        :return: Um valor booleano que indica se o v�rtice est� no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um v�rtice passado como par�metro pertence ao grafo.
        :param vertice: O v�rtice que deve ser verificado.
        :return: Um valor booleano que indica se o v�rtice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como par�metro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um v�rtice no Grafo caso o v�rtice seja v�lido e n�o exista outro v�rtice com o mesmo nome
        :param v: O v�rtice a ser adicionado
        :raises: VerticeInvalidoException se o v�rtice passado como par�metro n�o puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')


    #### =========================== COMEÇA AKI ======================================

    # A) Encontre todos os pares de vértices não adjacentes.
    def vertices_nao_adjacentes(self):
        Arestas = self.A.keys()
        ListaArestas = list(self.A.values())
        Retorno = []

        for vertice in self.N:
            for vertice2 in self.N:
                ArestaContem = vertice + '-' + vertice2
                ArestaContem2 = vertice2 + '-' + vertice
                if ( (not (ArestaContem in ListaArestas)) and (not (ArestaContem2 in ListaArestas)) ): 
                    Retorno.append(ArestaContem)

        return Retorno;

    # B) Há algum vértice adjacente a ele mesmo? (Retorne True ou False)
    def ha_laco(self):
        '''Esse conta com três parâmetros, justamente caso dejese conferir se os pontos das arestas existem'''
        nome = self.N
        a = self.A

        Lista = []
        NOME1, NOME2 = '',''
        for e in a.values():
            for i in range(len(e)):
                if e[i] != '-':
                    NOME2 += e[i]
                else:
                    NOME1 = NOME2
                    NOME2 = ''
            if (NOME1==NOME2 and NOME2 in nome ):
                return True
            else:
                NOME1, NOME2 = '', ''
        return False


    # C) Há arestas paralelas? (Retorne True ou False)

    # Função auxiliar
    def CONFERIR(self,nome,a):
        NOME1, NOME2 = '', ''
        for e in a.values():
            for i in range(len(e)):
                if e[i] != '-':
                    NOME2 += e[i]
                else:
                    NOME1 = NOME2
                    NOME2 = ''
            if (NOME1 == NOME2 and NOME2 in nome):
                return True
            else:
                NOME1, NOME2 = '', ''
        return False

    def ha_paralelas(self):
        A = self.CONFERIR(self.N,self.A)
        if (A == True):
            return True
        else:
            return False

    # D) Qual o grau de um vértice arbitrário?
    def grau(self, vertice):
        Ocorrencia = 0

        Arestas = list(self.A.values())
        for a in Arestas:
            if( vertice in a ): Ocorrencia += 1
        
        return (Ocorrencia)

    # E) Quais arestas incidem sobre um vértice N arbitrário?
    def arestas_sobre_vertice( self, vertice ):
        Arestas = self.A.keys()
        Lista = list()
        
        for chave in Arestas:
            if( vertice in self.A[chave] ):
                Lista.append(chave)
            
        return Lista;

    # f) Esse grafo é completo?
    #Auxiliar
    def CONFERERIR_ARESTAS(self,nome,a):
        for e in a.values():
            NOME1, NOME2 = '', ''
            for i in range(len(e)):
                if e[i] != '-':
                    NOME2 += e[i]
                else:
                    NOME1 = NOME2
                    NOME2 = ''
            if (NOME1 not in nome or NOME2 not in nome):
                return False
        return True

    #Auxiliar
    def FATORIAL(self, NUMERO):
        if (NUMERO == 1 or NUMERO == 0):
            return 1
        else:
            return self.FATORIAL(NUMERO - 1)


    def eh_completo(self):
        nome = self.N
        a = self.A

        m = len(nome)
        p =  m-2
        z = len(list(a.values()))
        X = self.FATORIAL(m)
        #print(X)
        if (X==z):
            A = self.CONFERERIR_ARESTAS(nome,a)
            if (A==True):
                return True;
            else:
                return False;
        else:
            return False;

        
    """
        ======== Verifica Depois =======
        def VERIFICAR_LACO(self, a):
        '''Esse é o caso que não queria passar os nomes do vértices, assim não conferindo se os pontos da arestas existem.'''
        Lista = []
        NOME1, NOME2 = '', ''
        for e in a.values():
            for i in range(len(e)):
                if e[i] != '-':
                    NOME2 += e[i]
                else:
                    NOME1 = NOME2
                    NOME2 = ''
            if (NOME1 == NOME2):
                return True
            else:
                NOME1, NOME2 = '', ''
        return False
    """


    '''def ARESTAS_PARALELAS(self,nome,d):
        Lista,A = [],[]
       #A = d.values()
        for e in d.values():
            A.append(e)
        a = self.CONFERIR(A)
        for i in a:
            if (a[i] > 1):
                Lista.append(a[i])
        if Lista != []:
            return True
        else:
            return False'''


    '''
    def vertices_nao_adjacentes(self):
        for vertice1 in self.N:
            V = vertice1 + '-'
            for vertice2 in self.N:
    '''
    

    #=========================== PARTE DE HENRIQUE ====================================

    def adicionaAresta(self, nome, a):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        if self.arestaValida(a):
            self.A[nome] = a
            print('A:', a)
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    def __str__(self):
        Lista=[]
        '''
        Fornece uma representa��o do tipo String do grafo.
        O String cont�m um sequ�ncia dos v�rtices separados por v�rgula, seguido de uma sequ�ncia das arestas no formato padr�o.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # S� coloca a v�rgula se n�o for o �ltimo v�rtice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not(i == len(self.A) - 1): # S� coloca a v�rgula se n�o for a �ltima aresta
                Lista.append(grafo_str)
                grafo_str += ", "

        return grafo_str