# Módulo de serviço: Lógica de negócio para receitas
# Fornece abstrações para listar, buscar e calcular viabilidade de receitas.

from recipe_models import (
    Recipe,
    RecipeSummary,
    Ingredient,
    MissingResponse,
)
from recipe_loader import get_all_recipes, get_recipe


def list_recipes() -> list[RecipeSummary]:
    """Retorna resumo de todas as receitas disponíveis."""
    recipes = get_all_recipes()
    summaries: list[RecipeSummary] = []

    for recipe in recipes.values():
        summaries.append(RecipeSummary(
            id=recipe.id,
            name=recipe.name,
            description=recipe.description,
            ingredient_count=len(recipe.ingredients),
            step_count=len(recipe.steps),
        ))

    return summaries


def get_recipe_detail(recipe_id: str) -> Recipe | None:
    """Retorna os detalhes completos de uma receita."""
    return get_recipe(recipe_id)


def list_all_ingredients() -> list[Ingredient]:
    """
    Retorna uma lista contendo todos os ingredientes únicos disponíveis.
    """
    recipes = get_all_recipes()
    seen_ids: set[str] = set()
    ingredients: list[Ingredient] = []

    for recipe in recipes.values():
        for ingredient in recipe.ingredients:
            if ingredient.id not in seen_ids:
                seen_ids.add(ingredient.id)
                ingredients.append(ingredient)

    # Ordenar por categoria, depois por nome
    ingredients.sort(key=lambda i: (i.category, i.name))
    return ingredients


def calculate_missing(recipe_id: str, available_ids: list[str]) -> MissingResponse | None:
    """
    Calcula a diferença entre os ingredientes da receita e os fornecidos pelo usuário.
    """
    recipe = get_recipe(recipe_id)
    if recipe is None:
        return None

    available_set = set(available_ids)

    available: list[Ingredient] = []
    missing: list[Ingredient] = []

    for ingredient in recipe.ingredients:
        if ingredient.id in available_set:
            available.append(ingredient)
        else:
            missing.append(ingredient)

    return MissingResponse(
        recipe_id=recipe.id,
        available=available,
        missing=missing,
        can_make=len(missing) == 0,
    )
