# feat: loader com auto-discovery de receitas
# Carrega automaticamente todos os arquivos JSON em data/
# Para adicionar uma nova receita, basta criar um novo .json — zero mudança de código.

import json
import os
from glob import glob
from recipe_models import Recipe


def _get_data_dir() -> str:
    """Retorna o caminho absoluto da pasta data/."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def load_recipe(filepath: str) -> Recipe:
    """Carrega uma receita de um arquivo JSON."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return Recipe(**data)


def load_all_recipes() -> dict[str, Recipe]:
    """
    Descobre e carrega todas as receitas da pasta data/.
    Retorna um dicionário {recipe_id: Recipe}.
    """
    data_dir = _get_data_dir()
    recipes: dict[str, Recipe] = {}

    pattern = os.path.join(data_dir, "*.json")
    for filepath in sorted(glob(pattern)):
        recipe = load_recipe(filepath)
        recipes[recipe.id] = recipe

    return recipes


# Cache global — carregado uma vez na inicialização
_recipes_cache: dict[str, Recipe] | None = None


def get_all_recipes() -> dict[str, Recipe]:
    """Retorna todas as receitas (com cache)."""
    global _recipes_cache
    if _recipes_cache is None:
        _recipes_cache = load_all_recipes()
    return _recipes_cache


def get_recipe(recipe_id: str) -> Recipe | None:
    """Retorna uma receita pelo ID, ou None se não existir."""
    return get_all_recipes().get(recipe_id)


def reload_recipes() -> dict[str, Recipe]:
    """Força recarregamento das receitas (útil para desenvolvimento)."""
    global _recipes_cache
    _recipes_cache = None
    return get_all_recipes()
