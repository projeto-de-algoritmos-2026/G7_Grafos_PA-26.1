# feat: detecção de violações de dependência
# Analisa uma lista ordenada de passos e identifica quais
# dependências foram violadas (passo aparece antes do seu pré-requisito).
# Gera explicações pedagógicas em português para cada violação.

from recipe_models import Step, Violation


def detect_violations(
    ordered_steps: list[Step],
    adjacency_list: list[list[int]],
    all_steps: list[Step],
) -> list[Violation]:
    """
    Detecta violações de dependência em uma ordenação de passos.

    Uma violação ocorre quando um passo aparece ANTES de um passo
    do qual ele depende na lista ordenada.

    Args:
        ordered_steps: Lista de passos na ordem gerada pelo algoritmo.
        adjacency_list: Lista de adjacência do grafo (adjacency_list[i] = dependências do passo i).
        all_steps: Lista completa de passos da receita (para lookup de nomes).

    Returns:
        Lista de Violation com explicações pedagógicas.
    """
    violations: list[Violation] = []

    # Mapa: step_id -> posição na lista ordenada (0-based)
    position_map: dict[int, int] = {}
    for idx, step in enumerate(ordered_steps):
        position_map[step.id] = idx

    # Mapa: step_id -> nome do passo (para mensagens)
    name_map: dict[int, str] = {step.id: step.name for step in all_steps}

    for idx, step in enumerate(ordered_steps):
        # Verificar cada dependência deste passo
        for dep_id in adjacency_list[step.id]:
            dep_position = position_map.get(dep_id)

            if dep_position is not None and dep_position > idx:
                # Violação: a dependência aparece DEPOIS do passo atual
                dep_name = name_map.get(dep_id, f"Passo {dep_id}")

                reason = (
                    f"❌ O passo '{step.name}' aparece na posição {idx + 1}, "
                    f"mas depende de '{dep_name}' que só aparece na posição "
                    f"{dep_position + 1}. "
                    f"Ou seja, você tentaria fazer '{step.name}' sem antes "
                    f"ter completado '{dep_name}'!"
                )

                violations.append(Violation(
                    step_position=idx + 1,
                    step_name=step.name,
                    depends_on_position=dep_position + 1,
                    depends_on_name=dep_name,
                    reason=reason,
                ))

    return violations
