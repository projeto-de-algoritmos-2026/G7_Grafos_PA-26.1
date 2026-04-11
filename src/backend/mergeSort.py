def mergeSort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esquerda = mergeSort(arr[:meio])
    direita = mergeSort(arr[meio:])

    return merge(esquerda, direita)


def merge(esq, dir):
    resultado = []
    i = j = 0

    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1

    # adiciona o resto
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])

    return resultado
