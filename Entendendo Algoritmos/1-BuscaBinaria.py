import time
# Capítulo 1. Busca Binária - O(log(n))

# Método de forma recursiva:
def buscaBin(lista, numero, inicio, meio, fim):
    # Se o índice medio da verificação passar a extensão direita, então não existe o item na lista
    if meio > fim:
        return -1
    else:
        # Se o item do indice médio for o que estamos procurando então retorna o índice médio (caso base)
        if numero == lista[meio]:
            return meio
        # Senão, verifica-se se esse procurado é maior que o item do indice médio
        elif numero > lista[meio]:
            # Em caso positivo, se realiza o recorto de lado esquerdo da lista chamando o método de novo
            return buscaBin(lista, numero, meio+1, int((meio+1 + fim)/2), fim)
        # Se não for maior, verifica-se se o procurado é menor que o item da posição média
        elif numero < lista[meio]:
            # Em caso positivo, se realiza o recorte do lado direito chamando o método de novo
            return buscaBin(lista, numero, inicio, int((meio-1 + inicio)/2), meio-1)

# Método de forma iterativa:
def buscaBinIter(lista, numero, inicio, meio, fim):
    # Enquanto o índice medio da verificação passar a extensão direita, existe item verificavel
    while meio <= fim:
        if numero == lista[meio]:
            return meio
        else:
            if numero > lista[meio]:
                inicio = meio+1
            elif numero < lista[meio]:
                fim = meio-1
            meio = int((fim+inicio)/2)
    # Se saiu do laço então não existe o item na lista
    return -1


listanum = list(range(1, 101))

# Método usando biblioteca do Python
# Mais aplicações: https://docs.python.org/3/library/bisect.html
import bisect
def buscaBinBib(lista, numero):
    # Consegue o índice do valor mais próximo ou igual a número pela esquerda (ou seja, menor ou igual)
    i = bisect.bisect_left(lista, numero)
    # Se i não ultrapassa o length e a verificação de numero é verdadeira, retorna o indice
    if i != len(lista) and lista[i] == numero:
        return i
    # Caso contrário, tratamento de erro
    raise ValueError

# Executando Recursão
inicio = time.time()
print(buscaBin(listanum, 100, 0, int(len(listanum)/2), len(listanum)-1))
fim = time.time()
print(f"Tempo Recursão: {fim-inicio} segs")

# Executando Iteração
inicio = time.time()
print(buscaBinIter(listanum, 100, 0, int(len(listanum)/2), len(listanum)-1))
fim = time.time()
print(f"Tempo Iteração: {fim-inicio} segs")

# Executando Biblioteca
inicio = time.time()
print(buscaBinBib(listanum, 100))
fim = time.time()
print(f"Tempo Biblioteca: {fim-inicio} segs")

