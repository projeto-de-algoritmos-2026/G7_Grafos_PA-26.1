# feat: endpoints REST de receitas
# Router FastAPI com todos os endpoints de receitas:
# listagem, detalhes, ingredientes faltantes, ordenação e comparação.

from fastapi import APIRouter, HTTPException
from recipe_models import (
    Recipe,
    RecipeSummary,
    AvailableIngredientsRequest,
    MissingResponse,
    SortRequest,
    SortResult,
    CompareResponse,
)
from recipe_service import list_recipes, get_recipe_detail, calculate_missing
from algorithm_service import sort_by_algorithm, compare_all_algorithms

router = APIRouter(prefix="/api/v1/recipes", tags=["recipes"])


@router.get("/", response_model=list[RecipeSummary])
def get_recipes():
    """Lista resumo de todas as receitas disponíveis."""
    return list_recipes()


@router.get("/{recipe_id}", response_model=Recipe)
def get_recipe(recipe_id: str):
    """Retorna detalhes completos de uma receita."""
    recipe = get_recipe_detail(recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail=f"Receita '{recipe_id}' não encontrada.")
    return recipe


@router.post("/{recipe_id}/missing", response_model=MissingResponse)
def get_missing_ingredients(recipe_id: str, body: AvailableIngredientsRequest):
    """
    Calcula ingredientes faltantes para uma receita,
    dado os ingredientes disponíveis do usuário.
    """
    result = calculate_missing(recipe_id, body.available)
    if result is None:
        raise HTTPException(status_code=404, detail=f"Receita '{recipe_id}' não encontrada.")
    return result


@router.post("/{recipe_id}/sort", response_model=SortResult)
def sort_recipe_steps(recipe_id: str, body: SortRequest):
    """
    Ordena os passos da receita usando o algoritmo escolhido.
    Algoritmos: "topological", "mergesort", "quicksort".
    """
    recipe = get_recipe_detail(recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail=f"Receita '{recipe_id}' não encontrada.")

    try:
        return sort_by_algorithm(recipe, body.algorithm)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/{recipe_id}/compare", response_model=CompareResponse)
def compare_algorithms(recipe_id: str):
    """Compara os 3 algoritmos (TopSort, MergeSort, QuickSort) lado a lado."""
    recipe = get_recipe_detail(recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail=f"Receita '{recipe_id}' não encontrada.")

    results = compare_all_algorithms(recipe)
    return CompareResponse(
        recipe_id=recipe.id,
        recipe_name=recipe.name,
        results=results,
    )
