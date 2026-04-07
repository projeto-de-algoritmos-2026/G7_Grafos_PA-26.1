from recipe_models import Recipe, Step, SortResult, Violation
from topologicalSort import main as topological_sort_main
from merge_sort import merge_sort_steps
from quick_sort import quick_sort_steps
from violation_detector import detect_violations




EXPLANATION_TOPOLOGICAL = (
    "✅ O Topological Sort (DFS) respeita as dependências do grafo, garantindo que "
    "nenhum passo seja executado antes de seus pré-requisitos. Esta é a abordagem "
    "correta para ordenação de tarefas dependentes."
)

EXPLANATION_MERGESORT = (
    "⚠️ O MergeSort realizou ordenação numérica estável baseada em IDs. "
    "Embora preserve parcialmente a sequência lógica natural, ele falha em "
    "grafos compostos (ramos paralelos) ao ignorar as relações de dependência."
)

EXPLANATION_QUICKSORT = (
    "❌ O QuickSort realizou ordenação lexicográfica pelo nome. "
    "Esta abordagem é totalmente inadequada para grafos acíclicos dirigidos (DAGs), "
    "resultando em uma matriz de execução caótica."
)

EXPLANATION_CYCLE = (
    "🔄 ERRO: Ciclo detectado no grafo de dependências. "
    "A presença de uma dependência circular torna impossível realizar a ordenação. "
    "Topological Sort exige um DAG (Grafo Acíclico Dirigido)."
)


def _steps_by_id(steps: list[Step]) -> dict[int, Step]:
    """Cria um mapa step_id -> Step para lookup rápido."""
    return {step.id: step for step in steps}


def sort_topological(recipe: Recipe) -> SortResult:
    """
    Aplica o Topological Sort usando a implementação de referência existente.
    Reutiliza o topologicalSort.py do colega sem modificação.
    """
    # Chamar a implementação de referência
    sorted_ids: list[int] = topological_sort_main(recipe.adjacency_list)

    step_map = _steps_by_id(recipe.steps)

    # Detectar ciclo (lista vazia = ciclo detectado)
    if len(sorted_ids) == 0 and len(recipe.steps) > 0:
        return SortResult(
            algorithm="topological",
            algorithm_label="Topological Sort (DFS)",
            ordered_steps=[],
            is_valid=False,
            violations=[],
            explanation=EXPLANATION_CYCLE,
        )

    ordered_steps = [step_map[sid] for sid in sorted_ids if sid in step_map]
    violations = detect_violations(ordered_steps, recipe.adjacency_list, recipe.steps)

    return SortResult(
        algorithm="topological",
        algorithm_label="Topological Sort (DFS)",
        ordered_steps=ordered_steps,
        is_valid=len(violations) == 0,
        violations=violations,
        explanation=EXPLANATION_TOPOLOGICAL,
    )


def sort_mergesort(recipe: Recipe) -> SortResult:
    """Aplica MergeSort (por ID numérico) e detecta violações."""
    ordered_steps = merge_sort_steps(list(recipe.steps))
    violations = detect_violations(ordered_steps, recipe.adjacency_list, recipe.steps)

    return SortResult(
        algorithm="mergesort",
        algorithm_label="MergeSort (por ID numérico)",
        ordered_steps=ordered_steps,
        is_valid=len(violations) == 0,
        violations=violations,
        explanation=EXPLANATION_MERGESORT,
    )


def sort_quicksort(recipe: Recipe) -> SortResult:
    """Aplica QuickSort (por nome A-Z) e detecta violações."""
    ordered_steps = quick_sort_steps(list(recipe.steps))
    violations = detect_violations(ordered_steps, recipe.adjacency_list, recipe.steps)

    return SortResult(
        algorithm="quicksort",
        algorithm_label="QuickSort (por nome A→Z)",
        ordered_steps=ordered_steps,
        is_valid=len(violations) == 0,
        violations=violations,
        explanation=EXPLANATION_QUICKSORT,
    )


def sort_by_algorithm(recipe: Recipe, algorithm: str) -> SortResult:
    """Ordena pelos passos da receita usando o algoritmo escolhido."""
    sorters = {
        "topological": sort_topological,
        "mergesort": sort_mergesort,
        "quicksort": sort_quicksort,
    }

    sorter = sorters.get(algorithm)
    if sorter is None:
        raise ValueError(
            f"Algoritmo '{algorithm}' não reconhecido. "
            f"Use: {', '.join(sorters.keys())}"
        )

    return sorter(recipe)


def compare_all_algorithms(recipe: Recipe) -> list[SortResult]:
    """Executa os 3 algoritmos e retorna os resultados para comparação."""
    return [
        sort_topological(recipe),
        sort_mergesort(recipe),
        sort_quicksort(recipe),
    ]
