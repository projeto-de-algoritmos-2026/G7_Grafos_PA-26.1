# Simulação QuickSort para ordenação de passos
# Ordena por nome (ordem alfabética) para demonstrar a inadequação
# de métodos de ordenação comparativa em estruturas DAG.

from recipe_models import Step


def quick_sort_steps(steps: list[Step]) -> list[Step]:
    """
    Ordena passos lexicograficamente por nome usando QuickSort.
    Demonstração pedagógica da falha sistêmica ao ignorar dependências.
    """
    if len(steps) <= 1:
        return list(steps)

    pivot = steps[len(steps) // 2]
    left = [s for s in steps if s.name < pivot.name]
    middle = [s for s in steps if s.name == pivot.name]
    right = [s for s in steps if s.name > pivot.name]

    return quick_sort_steps(left) + middle + quick_sort_steps(right)
