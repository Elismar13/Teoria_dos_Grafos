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
                return e
            else:
                NOME1, NOME2 = '', ''
        return False


    # C) Há arestas paralelas? (Retorne True ou False)

    # Função auxiliar
    def ha_paralelas(self):
        nome = self.N
        a = self.A

        NOME1, NOME2 = '', ''
        for e in a.values():
            for i in range(len(e)):
                if e[i] != '-':
                    NOME2 += e[i]
                else:
                    NOME1 = NOME2
                    NOME2 = ''
            if (NOME1 == NOME2 and NOME2 in nome):
                return e
            else:
                NOME1, NOME2 = '', ''
        return False

    #E) arestas sobre vertice
    def arestas_sobre_vertice( self, vertice ):
        Arestas = self.A.keys()
        Lista = list()
        
        for chave in Arestas:
            if( vertice in self.A[chave] ):
                Lista.append(chave)
            
        return Lista;

    #=========================== Roteiro 3 ====================================

    #Questão 3
    def ehConexo(self):
        for vertice in self.N:
            Resultado = self.VerificaArestasConectadas(vertice)
            ResultadoOrdenado = sorted(Resultado)
            #print(sorted(Resultado))
            if( ResultadoOrdenado != sorted(self.N) ): return False

        return True

    def VerificaArestasConectadas(self, vertice, Resultado=None):

        # Corrigindo bug do python em relação ao uso de variáveis como parâmetro
        if (Resultado == None): Resultado = []

        Arestas = self.A.keys()  # a1, a2, a3
        # self.A['a1'] = "A-C"

        # Lista com todas arestas que incidem no vértice
        ArestasComVertice = list()

        for aresta in Arestas:
            if (vertice in self.A[aresta]):
                ArestasComVertice.append(aresta)

        # realizando a busca em profundidade
        if (vertice in Resultado):  # Vértice já está na lista?  (Vulgo caso de parada) + como vericar se é retorno?
            return Resultado

        else:  # Vertice não está na lista? (o que fazer quando eu tiver que continuar o próximo)
            for aresta in ArestasComVertice:
                arestaAtual = self.A[aresta]
                V1, V2 = arestaAtual[0], arestaAtual[2]  # Se não for 2, é 1

                # Caso for um laco
                if (V1 == V2):
                    continue

                # Caso unico em que não se tem mais o que buscar
                if (len(ArestasComVertice) == 1):
                    if (V1 not in Resultado and V1 == vertice):
                        if (V1 not in Resultado) : Resultado.append(V1)
                    elif (V2 not in Resultado and V2 == vertice):
                        if (V2 not in Resultado) : Resultado.append(V2)

                if ( aresta not in Resultado ):  # verifica se a aresta ja foi analisada? A gente passa para a próxima aresta da lista 2
                    if (V1 not in Resultado or V2 not in Resultado):

                        if (V1 == vertice):
                            if (V1 not in Resultado): Resultado.append(V1)
                            self.VerificaArestasConectadas(vertice=V2, Resultado=Resultado)

                        elif (V2 == vertice):
                            if (V2 not in Resultado): Resultado.append(V2)
                            self.VerificaArestasConectadas(vertice=V1, Resultado=Resultado)
                    else:
                        continue

        # Retornar o resultado
        if (len(Resultado) > 1 and Resultado[0] == vertice): return Resultado

    #Questão 2
    def Caminho(self, comprimento):
        if(comprimento > 0 and comprimento < len(self.N)): #Se o comprimento for menor que a quantidade de vertices
            TamanhoCaminho = (comprimento * 2) + 1         #n vertices + n arestas + 1 vertice
            for Vertice in self.N:    
                Caminho = self.CaminhoGenerator(Vertice, comprimento)  #Busco um caminho que o vertice apareca

                if(Caminho != None and len(Caminho) == comprimento*2 - 1):
                    return Caminho
                else:
                    continue

        return False
        
    def CaminhoGenerator(self, vertice, comprimento, Resultado=None, PaiGeral=''):
        if( Resultado == None ): Resultado = [] 
        if( PaiGeral == '' ): PaiGeral = vertice


        Arestas = self.A.keys()  # a1, a2, a3
        ArestasComVertice = self.arestas_sobre_vertice( vertice )

        #Caso de parada
        if( len(ArestasComVertice) == 1 and ArestasComVertice[0] in Resultado ):
            Resultado.append( vertice )
            return Resultado
        #if(vertice in Resultado):
            #return False
        #percorrendo arestas que contem o pai
        CaminhoFinal = list()

        MaiorCaminho = 0
        for aresta in ArestasComVertice:
            V1, V2 = self.A[aresta].split('-')
            CaminhoAtual = []

            if ( aresta not in Resultado ):
                if ( V1 == vertice ): 
                    Resultado.append(V1)
                    Resultado.append(aresta)
                    CaminhoAtual = self.CaminhoGenerator( V2, comprimento, Resultado, PaiGeral )
                    
                if ( V2 == vertice ): 
                    Resultado.append(V2)
                    Resultado.append(aresta)
                    CaminhoAtual = self.CaminhoGenerator( V1, comprimento, Resultado, PaiGeral )
            else:
                continue

            if( vertice  == PaiGeral ):
                if( len(Resultado) >= comprimento*2 - 1 ):
                    return Resultado[0:comprimento*2 - 1]
                
                else:
                    Resultado = []

            #Caso em que só tenho uma aresta no

    def buscaEmProfundidade(self, vertice, Resultado=None):
        if(Resultado == None): Resultado = []

        Arestas = self.A.keys()

        ArestasComVertice = list()

        for aresta in Arestas:
            if( vertice in self.A[aresta] ):
                ArestasComVertice.append(aresta)

        # realizando a busca em profundidade
        if( vertice in Resultado ):     # Vértice já está na lista?  (Vulgo caso de parada) + como vericar se é retorno?
            return Resultado

        else:   #Vertice não está na lista? (o que fazer quando eu tiver que continuar o próximo)
            for aresta in ArestasComVertice:
                arestaAtual = self.A[aresta]
                V1, V2 = arestaAtual[0], arestaAtual[2]       #Se não for 2, é 1

                #Caso for um laco
                if (V1 == V2):
                    continue

                #Caso unico em que não se tem mais o que buscar
                if(len(ArestasComVertice) == 1):
                    if(V1 not in Resultado and V1 == vertice):
                        Resultado.append(V1)
                    elif(V2 not in Resultado and V2 == vertice):
                        Resultado.append(V2)

                if (aresta not in Resultado):   #verifica se a aresta ja foi analisada? A gente passa para a próxima aresta da lista 2
                    if(V1 not in Resultado or V2 not in Resultado):

                        if( V1 == vertice ):
                            if(V1 not in Resultado): Resultado.append(V1)
                            if (aresta not in Resultado) and (V2 not in Resultado): Resultado.append(aresta)
                            self.buscaEmProfundidade( vertice=V2, Resultado=Resultado )

                        elif ( V2 == vertice ):
                            if (V2 not in Resultado): Resultado.append(V2)
                            if (aresta not in Resultado) and (V1 not in Resultado): Resultado.append(aresta)
                            self.buscaEmProfundidade( vertice=V1, Resultado=Resultado )
                    else:
                        continue

        if(len(Resultado) > 0 and Resultado[0] == vertice): return Resultado

    #Funções auxiliares (QUESTÃO 3)




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