# Capitulo 2. Ordenação Por Seleção

# Lista Ligada - Definições da estrutura
class Aluno():
    def __init__(self, nota: int, nome: str) -> None:
        self.nota = nota
        self.nome = nome

class Node():
    def __init__(self, aluno: Aluno, prox: Aluno = None, prev: Aluno = None) -> None:
        self.aluno = aluno
        self.prox = prox
        self.prev = prev
        # prox e prev iniciam como None, pois são alocados ao serem declarados

# Estruturas da Lista Ligada em Classes
class ListaLigada():
    '''Classe com a montagem e ações de uma lista ligada'''
    def __init__(self) -> None:
        self.__cabeca = None
        self.__cauda = None
        self.__tamanho = 0
    
    def is_empty(self) -> bool: # Verificação de conteúdo
        return self.__tamanho == 0

    def add_last(self, aluno: Aluno) -> None: # adicionar nó no fim da lista
        new_node = Node(aluno)
        try:
            if self.is_empty():
                self.__cabeca = new_node
                self.__cauda = new_node
            else:
                self.__cauda.prox = new_node
                new_node.prev = self.__cauda
                self.__cauda = new_node
            self.__tamanho += 1
        except Exception as e:
            print(f'Não foi possível inserção: {e}')

    def add_first(self, aluno: Aluno) -> None: # adicionar nó no começo da lista
        new_node = Node(aluno)
        try:
            if self.is_empty():
                self.__cabeca = new_node
                self.__cauda = new_node
            else:
                new_node.prox = self.__cabeca
                self.__cabeca.prev = new_node
                self.__cabeca = new_node
            self.__tamanho += 1
        except Exception as e:
            print(f'Não foi possível inserção: {e}')

    def add(self, index: int, aluno: Aluno) -> None: # adição de nó em qualquer ponto da lista - O(n), sendo n o ponto

        if index < 0 or index > self.__tamanho:
            raise ValueError

        new_node = Node(aluno)
        if index == 0:
            self.add_first(aluno)
        elif index == self.__tamanho:
            self.add_last(aluno)
        else:
            aux = self.__cabeca
            print(self.__tamanho)
            for i in range(0, index-1):
                aux = aux.prox

            new_node.prox = aux.prox
            aux.prox = new_node
            new_node.prox.prev = new_node
            new_node.prev = aux

            self.__tamanho += 1

    def busca_sequencial_index(self, aluno: Aluno) -> int: # busca sequencial por int - O(n)
        aux = self.__cabeca
        for i in range(0, self.__tamanho):
            if aux.aluno.nome == aluno.nome and aux.aluno.nota == aluno.nota:
                return i
            else:
                aux = aux.prox
        return -1

    def busca_sequencial_aluno(self, index: int) -> Aluno: # busca sequencial por nó - O(n)
        if index < 0 or index >= self.__tamanho:
            raise ValueError

        aux = self.__cabeca
        for i in range(0, index+1):
            aux = aux.prox
        return aux

    def contains(self, aluno: Aluno) -> bool: # verificação de item na lista - O(n)
        return self.busca_sequencial_index() != -1

    def exibe_lista(self) -> None:
        aux = self.__cabeca
        print(f'Exibindo Lista:')
        while aux != None:
            print(f'Nome: {aux.aluno.nome} Nota: {aux.aluno.nota}')
            aux = aux.prox
        print(f'Fim da lista.')

    def busca_maior(self)-> Node:
        aux = self.__cauda
        maior = aux
        while aux != None:
            if aux.aluno.nota > maior.aluno.nota:
                maior = aux
            aux = aux.prev
        return maior

    def busca_menor(self)-> Node:
        aux = self.__cabeca
        menor = aux
        while aux != None:
            if aux.aluno.nota < menor.aluno.nota:
                menor = aux
            aux = aux.prox
        return menor

    def ordena_lista(self) -> None:
        def trocas(Node1, Node2)-> None:
            n1_aux = (Node1.prev, Node1.prox)
            n2_aux = (Node2.prev, Node2.prox)
            Node1.prev, Node1.prox = n2_aux
            Node2.prev, Node2.prox = n1_aux
            
        
        menor = self.busca_menor()
        trocas(self.__cabeca, menor)
        self.__cabeca = menor
        maior = self.busca_maior()
        trocas(self.__cauda, maior)
        self.__cauda = maior
        
        aux = self.__cabeca.prox
        
        while aux != self.__cauda:
            
            aux_aux = aux
            while aux_aux != self.__cauda:
                print('passou')
                if aux.aluno.nota > aux_aux.aluno.nota:
                    trocas(aux, aux_aux)
                aux_aux = aux.prox
            aux = aux.prox
            


# Declaração de uma lista ligada simples:
lista = ListaLigada()
lista.add(0, Aluno(6, 'João'))
lista.add(1, Aluno(7, 'Maria'))
lista.add(2, Aluno(5, 'José'))
lista.add(1, Aluno(4, 'Ana'))

lista.exibe_lista()

lista.ordena_lista()


