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
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if M == []:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    if k>l:
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
                if i>j and not(M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')


                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]
                if not(self.arestaValida(aresta)):
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

        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
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
        return a[a.index(Grafo.SEPARADOR_ARESTA)+1:]

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

            self.N.append(v) # Adiciona vértice na lista de vértices
            self.M.append([]) # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) -1:
                    self.M[k].append(0) # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-') # adiciona os elementos da linha do vértice
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
        espaco = ' '*(self.__maior_vertice)

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
                    if (int(self.M[i][j])==0):
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
            for i in range (len(NaoAdjacentes)):
                if (NaoAdjacentes[i][0]!= NaoAdjacentes[i][2]):
                    #print(NaoAdjacentes[i])
                    R.append(NaoAdjacentes[i])

            if (R in self.ListaArestas() or R==[]):
                return True
            else:
                return False

            #if (NaoAdjacentes.self.ha_laco()):
            #    return False
            #return True

            #print(NaoAdjacentes)
            #R.append(NaoAdjacentes + self.ListaArestas())
            #print(self.ListaArestas())
            #print(R)
            #if (R[0]==self.ListaArestas()):
            #    return True
            #else:
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

    def grau(self,VerticeDesejado):
        '''
        Explicação: Através da função arestas_sobre_vertice temos acesso a todas as arestas que contem o desejado vértice, assim
        só contando a quantidade de elementos da lista (arestas_sobre_vertice) temos o resultado que é o grau.
        '''
        ArestasQueIncidem = self.arestas_sobre_vertice(VerticeDesejado)
        Resultado = len(ArestasQueIncidem)
        return Resultado

    def arestas_sobre_vertice(self,VerticeDesejado):
        '''
        Explicação: Através da função ListaArestas que percorre a matriz, temos acesso as arestas da matriz assim, podemos  'perguntar'
        se o vertice desejado esta como X do modelo X-Y ou está no Y. Se estiver o colocamos em uma lista especial que só concentra
        arestas que contenham o vertice desejado.
        '''
        LA = self.ListaArestas()
        ArestasDesejadas = []
        for i in range(len(LA)):
            Aresta = LA[i]
            if (Aresta[0]==VerticeDesejado or Aresta[2]==VerticeDesejado):
                ArestasDesejadas.append(Aresta)
            #if (Aresta[2]==VerticeDesejado):  Ultima alteração 2109
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
                            #Se for maior que 1 então temos mais de uma arestas que incidem nos mesmos vertices.
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
                if (self.M[i][j]!='-'):
                    if (int(self.M[i][j])>0):
                        for k in range(int(self.M[i][j])):
                            Aresta = self.N[i] + '-' + self.N[j]
                            ListaArestas.append(Aresta)
        return ListaArestas

    """
        Nova CicloHamiltoniano: A função responsável por verificar se existe um ciclo 
        para um dado vértice em self.N

        Ela vai rodar até encontrar algum ciclo hamiltoniano... Assim que encontrar um ciclo,
        ela já irá retorna-lo
    """

    ### ======================= ROTEIRO 5 ==========================

    def caminhoEureliano(self):
        total = grau = 0
        i = 1
        n = len(self.N)

        while(total <= 2 and i < n):
            grau = 0
            for j in range(0, n):
                item = self.M[i][j]
                if(item != '-'): 
                    grau += int(item)

            if grau % 2 == 1:
                total += 1
            i += 1

        if(total >= 2):
            print('Não existe.')
        else: print('Ss')

    def CicloHamiltoniano(self): 
        todosOsCiclosDoGrafo = {}
        for vertice in self.N:
            cicloExisteParaDadoVertice = self.ExisteCicloParaOVertice(vertice)
            # todosOsCiclosDoGrafo[vertice] = cicloExisteParaDadoVertice

            if(cicloExisteParaDadoVertice): 
                # pass
                return cicloExisteParaDadoVertice

        # for vertice in self.N:
        #     print("Caminho do vertice {} : {}".format(vertice, todosOsCiclosDoGrafo[vertice]))
        # return todosOsCiclosDoGrafo


    # Antiga ciclo, ela serve como base para a CicloHamiltoniano.
    def ExisteCicloParaOVertice(self, vertice):
        '''
        Chamamos o Busca (Um busca em profundidade) e se no primeiro if ela for None (vazia) significa que não é um ciclo hamiltoniano, logo
        retornamos false, caso passe por esse if, vemos se o último vertice percorrido possui uma ligação direta com o vértice precurssor
        (pai). Exemplos ['a','b','c'], veremos que o 'c' possui um ligação (aresta) 'a-c' ou 'c-a', se sim ele é conectado, e nessa caso
        é um ciclo hamiltoniano. Se não, retorna o False.
        '''
        ListaFinal = self.Busca(vertice)

        if ListaFinal is None:  #Ou seja, a lista de Resultados com as arestas está vazio.
            return False
        else:
            A1 = ListaFinal[-1] + '-' + vertice
            A2 = vertice + '-' + ListaFinal[-1]
            if (A1 in self.ListaArestas()):
                ListaFinal.append(vertice)
                return ListaFinal
            elif (A2 in self.ListaArestas()):
                ListaFinal.append(vertice)
                return ListaFinal
            else:
                return False

    def Busca(self, vertice, Resultado=None):
        '''
        Fazemos uma lista com todas as arestas que contem o vértice inicial, que começamos com self.n[0]; Depois temos o caso de parada,
        onde perguntamos se o ultimo vértice percorrido já foi adicionado em Resultado e se o tamanho é igual a número de vértices,
        significando que todos os vértices foram percorridos. Se sim, retorna ao CicloHamiltoniano, onde pergunta se existem alguma aresta
        no grafo que vai diretamente do último até o primeiro, se sim, é adicionado (mostrando que é um ciclo), se não retorna Falso.
        Voltando ao Busca, depois desse if temos um else, que começa a busca, com a lista de arestas, pegamos a primeira, e separamos os
        vértices, exemplo '5-1' ficando '5' e '1'; Temos logo em seguida um caso especial (grafo de apenas um único vértice) que mostra que
        se sua aresta (se existir) liga a ele mesmo, se sim é configurado como um ciclo (simples), caso contrário é ignorado e no final
        retorna o [] (lista vazia). Com grafos com mais de um vértices, laços são automáticamente ignorados. Logo depois, temos um caso
        que mostra que não tem nada para buscar (arestas percorridas) e aí adicionamos o último vértice percorrido, para posteriormente
        comprovar se é um ciclo hamiltoniano (percorreu todas as arestas) ou não. Então temos a 'última' parte, onde perguntamos se o '5'
        ou '1' (V1 ou V2) já estão na lista final. Se o V1 é igual ao vértice que eu estou (no momento), eu adiciono na lista o V1 e
        pergunto se o V2 já esta se não, ele é adiconado e vira o 'vértice' (na qual procuraremos aresta que agora o contenham), se sim,
        já estiver adicionado, não o adiciona mais (para não repetir) e ele vira o meu 'vertice'. E o mesmo se repete com o elif segunte;
        *O else, é quando já adiconados o V1 ou V2 e passamos para outra aresas com o V1 ou V2 diferente (um novo caminho)
        '''

        if (Resultado == None): Resultado = []
        ArestasComVertice = []
        for aresta in (self.ListaArestas()):
            if (aresta[0] == vertice): ArestasComVertice.append(aresta)
            if (aresta[2] == vertice): ArestasComVertice.append(aresta) # return ArestasComVertice ['5-1', '5-4', '5-4', '5-7', '5-7'] no exemplo 'g1'
        #if (vertice in Resultado and len(Resultado)==len(self.N)-1): return Resultado
        if (vertice in Resultado and len(Resultado)==len(self.N)): return Resultado

        else:
            for aresta in range(len(ArestasComVertice)):
                ArestaAtual = ArestasComVertice[aresta]     #Seria a primeira aresta, seguindo o exemplo é o '5-1'
                V1, V2 = ArestaAtual[0], ArestaAtual[2]     #Dividiriamos a aresta em dois vértices separados '5' e '1'
                if (V1 == V2):                              #De grafos maiores que 2 vertices ignoramos o laco. Excerto se existir apenas um único vértice;
                    if len(self.N)==1:                      #Esse é quando existe apenas um único vértice;
                        Resultado.append(V1)                #Assim, apos verificar que aresta incidem em si mesma, a aceitamos como um ciclo.
                        return Resultado
                    continue
                if (len(ArestasComVertice) == 1):
                    if (V1 not in Resultado and V1 == vertice): Resultado.append(V1)
                    elif (V2 not in Resultado and V2 == vertice): Resultado.append(V2)
                elif (V1 not in Resultado or V2 not in Resultado):
                    """
                     Pai: A; 

                    ['A-B', 'A-C']

                    1 RESULTADO P/ CADA COMBINAÇÃO = 2 RESULTADO
                    
                     """
                    if (V1==vertice):
                        if (V1 not in Resultado): Resultado.append(V1)
                        if (V2 not in Resultado): Resultado.append(V2)
                        self.Busca(vertice=V2, Resultado=Resultado)
                    if (V2==vertice):
                        if (V2 not in Resultado): Resultado.append(V2)
                        if (V1 not in Resultado): Resultado.append(V1)
                        self.Busca(vertice=V1, Resultado=Resultado)
                else:
                    continue

        # ERRO TA AQUI!
        if len(Resultado) == len(self.N):
            if self.N[0] in Resultado: return Resultado #Esse é quando existe apenas um único vértice;

        elif (Resultado[0]==vertice):
            print(Resultado[0], vertice)

            return Resultado  #Esse é em modo geral.

    '''
    def busca(self, vertice, Resultado=None):
       # Vértice não está na lista? (O que fazer quando eu tiver que continuar o próximo)
        for aresta in ArestasComVertice:
            arestaAtual = self.ListaArestas[aresta]
            V1, V2 =continue
                # Caso arestaAtual[0], arestaAtual[2]  # Se não for 2, é 1
            # Caso for um laco
            if (V1 == V2):  # Devemos lembrar se for um grafo exemplo ‘b-b’ apenas, ele é considerado hamiltoniano.
                 único em que não se tem mais o que buscar
            if (len(ArestasComVertice) == 1):
                if (V1 not in Resultado and V1 == vertice):
                    Resultado.append(V1)
                elif (V2 not in Resultado and V2 == vertice):
                        Resultado.append(V2)  #No método de matriz não temos ‘arestas’ definidas com chaves mas sim o seu valor
            # if (aresta not in Resultado):  # verifica se a aresta ja foi analisada? A gente passa para a próxima aresta da lista 2
            if (V1 not in Resultado or V2 not in Resultado):  # Exemplo O vertice é ‘A’ e a ‘aresta’ é ‘A-B’ da lista [‘A-B’,’C-A’]
                if (V1 == vertice):
                    if (V1 not in Resultado): Resultado.append(V1)
                    #if (aresta not in Resultado) and (V2 not in Resultado): Resultado.append(aresta)
                    self.busca(vertice=V2, Resultado=Resultado)
                elif (V2 == vertice):
                    Resultado.append(V2)
                    #if (aresta not in Resultado) and (V1 not in Resultado): Resultado.append(aresta)
                    self.busca(vertice=V1, Resultado=Resultado)
                else:
                    continue
        # Retornar o resultado
        return Resultado


    def Ciclo(self):
        Teste = []
        LA = self.ListaArestas()
        Inicial = LA[0][0] #Nesse caso do g1 seria o vértice 5  E  LA[0] seria o par '5-1'
        Teste.append(Inicial)
        for i in range (len(LA)): #Len(LA) = 14 arestas
            if ((LA[i][0] or LA[i][2]))==Inicial and (len(Teste)==self.N):
                return Teste
            else:
                if (LA[i][0])==Inicial:
                    Teste.append(LA[i][2])
                    Inicial = LA[i][2]
                if (LA[i][2])==Inicial:
                    Teste.append(LA[i][0])
                    Inicial = LA[i][0]
        return Teste


    def ProximaAresta(self, vertice,Resultado=None):
        if (Resultado == None): Resultado = []

        ArestasComVertice = []
        for aresta in (self.ListaArestas()):
            if (aresta[0]==vertice):
                ArestasComVertice.append(aresta)
            if (aresta[2]==vertice):
                ArestasComVertice.append(aresta)
        #return ArestasComVertice ['5-1', '5-4', '5-4', '5-7', '5-7'] no exemplo 'g1'

        for aresta in ArestasComVertice:
            ArestaAtual = ArestasComVertice[aresta] #Seria a primeira aresta, seguindo o exemplo é o '5-1'
            V1, V2 = ArestaAtual[0], ArestaAtual[2]  #Dividiriamos a aresta em dois vértices separados '5' e '1'
            if (V1==V2):
                continue
            if (len(ArestasComVertice) == 1):
                if (V1 not in Resultado and V1 == vertice):
                    Resultado.append(V1)
                elif (V2 not in Resultado and V2 == vertice):
                    Resultado.append(V2)
                    
        def Ciclo(self):
        Teste = []
        LA = self.ListaArestas()
        Inicial = LA[0][0] #Nesse caso do g1 seria o vértice 5  E  LA[0] seria o par '5-1'
        Teste.append(Inicial)
        for i in range (len(LA)): #Len(LA) = 14 arestas
            if ((LA[i][0] or LA[i][2]))==Inicial and (len(Teste)==self.N):
                return Teste
            else:
                if (LA[i][0])==Inicial:
                    Teste.append(LA[i][2])
                    Inicial = LA[i][2]
                if (LA[i][2])==Inicial:
                    Teste.append(LA[i][0])
                    Inicial = LA[i][0]
        return Teste


    def ProximaAresta(self, vertice,Resultado=None):
        if (Resultado == None): Resultado = []

        ArestasComVertice = []
        for aresta in (self.ListaArestas()):
            if (aresta[0]==vertice):
                ArestasComVertice.append(aresta)
            if (aresta[2]==vertice):
                ArestasComVertice.append(aresta)
        #return ArestasComVertice ['5-1', '5-4', '5-4', '5-7', '5-7'] no exemplo 'g1'

        for aresta in ArestasComVertice:
            ArestaAtual = ArestasComVertice[aresta] #Seria a primeira aresta, seguindo o exemplo é o '5-1'
            V1, V2 = ArestaAtual[0], ArestaAtual[2]  #Dividiriamos a aresta em dois vértices separados '5' e '1'
            if (V1==V2):
                continue
            if (len(ArestasComVertice) == 1):
                if (V1 not in Resultado and V1 == vertice):
                    Resultado.append(V1)
                elif (V2 not in Resultado and V2 == vertice):
                    Resultado.append(V2)
                    
'''

