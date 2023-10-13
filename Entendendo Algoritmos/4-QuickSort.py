# Capitulo 4. QuickSort - Algoritmo de ordenação conhecido por seu otimo desempenho, atuando junto à estratégia de 
# recursão de dividir e conquistar.

# Algoritmo de ordenação QuickSort de divisão do array em casos maiores e menores com base em um pivô 
# A complexidade assintótica varia entre 2 resultados:
# 1. Médio e melhor caso: O(nlog(n)) - pivô no meio do array produz O(log(n)) em pilhas e O(n) em loop
# 2. Pior caso: O(n^2) - pivô nas extremidades do array produz O(n) em pilhas e O(n) em loop

# o resultado 2 acontece porque quando um pivô está na extremidade, ele concentra todo o array em apenas um
# lado da divisão, então as recursões serão executadas n vezes para a ordenação.

def quickSort(lista: list)->list:
    # no caso do array ter apenas 1 elemento, ele já está ordenado
    if len(lista) < 2:
        return lista
    
    # senão, escolhe-se o pivô para dividir o array
    idx_pivo = int(len(lista)/2)
    # correndo o array, separa-se os maiores que o pivô dos menors que o pivô
    lista_dir = [lista[item] for item in range(0, len(lista)) if lista[item] >= lista[idx_pivo] and idx_pivo != item]
    lista_esq = [lista[item] for item in range(0, len(lista)) if lista[item] < lista[idx_pivo] and idx_pivo != item]

    # é feita então a recursão usando os menores, o pivô e os maiores
    return quickSort(lista_esq) + [lista[idx_pivo]] + quickSort(lista_dir)


array = [5, 4, 9, 6, 7, 3, 8, 4]
print(f'Array ordenado: {quickSort(array)}')