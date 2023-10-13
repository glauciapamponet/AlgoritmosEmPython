# Capítulo 3. Recursão

# A recursão é um metodo de iterar em operações dentro de uma função usando como iterador a pilha de execução
# do código. Em geral, a recursão não traz benefícios de desmpenho para um algoritmmo, mas traz benefícios
# de refatoração e de limpeza e organização ao código ao qual ela é usada. Entretanto, ao usar recursão em
# um algoritmo, a depender do tamanho de n para operações e das prórpias atribuições necessárias dentro da
# função, a recursão pode ser menos benéfica que a iteração em loop, pois a cada chamada da função recursiva,
# novas alocações de memória são feitas para o recurso da função, o que acaba sendo custoso em memória.
# NOTA: Recursão de cauda pode ser uma solução para os problemas da recursão convencional.

# A - Problema da Fazenda no capítulo 4. QuickSort: Como dividir uma fazenda de área retangular em quadrados que sejam de 
# tamanho? Qual a área que os quadrados terão?
def loteandoFazenda(lado_a: int, lado_b: int) -> int:
    if lado_a == lado_b:
        return lado_a
    else:
        if lado_a > lado_b:
            return loteandoFazenda(lado_b, lado_a-lado_b)
        elif lado_b > lado_a:
            return loteandoFazenda(lado_a, lado_b-lado_a)

lado_a_ret = 1680
lado_b_ret = 640
lado_quadrado = loteandoFazenda(lado_a_ret, lado_b_ret)
print(f'Área dos Quadrados: {lado_quadrado**2}m^2\nQtde Lotes: {(lado_a_ret*lado_b_ret)/lado_quadrado**2}\n')

# 4.1 - Escreva o código para a função soma
def somaArray(lista: list)-> int:
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[len(lista)-1] + somaArray(lista[:len(lista)-1])

array = [2, 4, 6]
print(f'Soma: {somaArray(array)}\n')

# 4.2 - Escreva uma função recursiva que conte o número de itens em uma lista.
def contaArray(lista: list)-> int:
    if len(lista) == 1:
        return 1
    else:
        return contaArray(lista[:len(lista)-1]) + 1

array = [2, 4, 6]
print(f'Quantidade: {contaArray(array)}\n')

# 4.3 - Encontre o valor mais alto em uma lista.
def maiorValor(lista: list, num: int)-> int:
    if len(lista) == 1:
        return lista[0] if lista[0] > num else num
    else:
        prox_valor = maiorValor(lista[:len(lista)-1], lista[len(lista)-1])
        if prox_valor > num:
            return prox_valor
        else:
            return num

array = [10, 15, 7, 8]
print(f'Maior valor: {maiorValor(array, array[-1])}')