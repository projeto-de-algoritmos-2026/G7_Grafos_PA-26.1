# feat: modelos Pydantic de receita
# Modelos de dados para o sistema de receitas inteligentes.
# Estes modelos complementam o Graph existente em models.py,
# adicionando representações de Ingredient, Step e Recipe.

from pydantic import BaseModel


class Ingredient(BaseModel):
    """Ingrediente de uma receita."""
    id: str            # ex: "guanciale"
    name: str          # ex: "Guanciale (200g)"
    category: str      # ex: "proteina", "massa", "tempero", "laticinio", "base"


class Step(BaseModel):
    """Passo de uma receita — vértice do grafo."""
    id: int            # índice do vértice (1-based)
    name: str          # ex: "Cortar o guanciale"
    description: str   # instrução detalhada
    dependencies: list[int]  # IDs dos passos pré-requisitos


class Recipe(BaseModel):
    """Receita completa com grafo de dependências."""
    id: str
    name: str
    description: str
    ingredients: list[Ingredient]
    steps: list[Step]
    adjacency_list: list[list[int]]
    # adjacency_list[i] = vértices dos quais o passo i depende
    # índice 0 = sentinela (vazio), passos começam em 1


class RecipeSummary(BaseModel):
    """Resumo de uma receita para listagem."""
    id: str
    name: str
    description: str
    ingredient_count: int
    step_count: int


class AvailableIngredientsRequest(BaseModel):
    """Request body para verificar ingredientes disponíveis."""
    available: list[str]  # lista de IDs de ingredientes


class MissingResponse(BaseModel):
    """Resposta com ingredientes faltantes."""
    recipe_id: str
    available: list[Ingredient]
    missing: list[Ingredient]
    can_make: bool


class SortRequest(BaseModel):
    """Request body para ordenar passos."""
    algorithm: str  # "topological" | "mergesort" | "quicksort"


class Violation(BaseModel):
    """Uma violação de dependência detectada na ordenação."""
    step_position: int       # posição na lista ordenada (1-based)
    step_name: str
    depends_on_position: int  # posição da dependência (1-based)
    depends_on_name: str
    reason: str              # explicação pedagógica


class SortResult(BaseModel):
    """Resultado de uma ordenação com detecção de violações."""
    algorithm: str           # "topological" | "mergesort" | "quicksort"
    algorithm_label: str     # "Topological Sort" | "MergeSort" | "QuickSort"
    ordered_steps: list[Step]
    is_valid: bool
    violations: list[Violation]
    explanation: str         # texto pedagógico sobre o resultado


class CompareResponse(BaseModel):
    """Comparação dos 3 algoritmos lado a lado."""
    recipe_id: str
    recipe_name: str
    results: list[SortResult]
