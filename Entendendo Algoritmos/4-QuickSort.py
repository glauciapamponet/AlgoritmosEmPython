# Capitulo 4. QuickSort - Algoritmo de ordenação conhecido por seu otimo desempenho, atuando junto à estratégia de 
# recursão de dividir e conquistar.

# Algoritmo de ordenação QuickSort de divisão do array em casos maiores e menores com base em um pivô - O melhor caso possui
# complexidade assintótica de O(nlog(n)), que é quando o pivô selecionado condiz com a mediana do array. Já o caso médio e 
# o pior caso possuem complexidade assintótica de O(n^2) que corresponde ao caso do pivô escolhido ser um dos máximos ou mínimos
# do array. A posição de index escolhida também pode refletir nesse desempenho.
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