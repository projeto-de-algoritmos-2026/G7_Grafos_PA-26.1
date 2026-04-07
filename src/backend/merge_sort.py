# feat: simulação MergeSort para passos de receita
# Ordena os passos por ID numérico usando MergeSort real.
# Preserva parcialmente a ordem original (IDs tendem a ser sequenciais),
# mas falha em receitas com ramos paralelos no DAG.

from recipe_models import Step


def merge(left: list[Step], right: list[Step]) -> list[Step]:
    """Merge de duas sublistas ordenadas por Step.id."""
    result: list[Step] = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i].id <= right[j].id:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_steps(steps: list[Step]) -> list[Step]:
    """
    Ordena passos por ID usando MergeSort.

    Para fins pedagógicos: o MergeSort preserva parcialmente a ordem
    porque os IDs foram atribuídos em sequência lógica. Porém, ele
    NÃO respeita dependências do grafo — apenas ordena numericamente.

    Em receitas com ramos paralelos (ex: guanciale + espaguete + molho),
    a ordem por ID pode violar dependências quando um passo de um ramo
    paralelo tem ID menor que um passo de outro ramo do qual depende.
    """
    if len(steps) <= 1:
        return list(steps)

    mid = len(steps) // 2
    left = merge_sort_steps(steps[:mid])
    right = merge_sort_steps(steps[mid:])
    return merge(left, right)
