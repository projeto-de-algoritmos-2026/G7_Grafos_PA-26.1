# feat: endpoints REST de ingredientes
# Router FastAPI para listagem de todos os ingredientes únicos
# disponíveis no sistema (consolidados de todas as receitas).

from fastapi import APIRouter
from recipe_models import Ingredient
from recipe_service import list_all_ingredients

router = APIRouter(prefix="/api/v1/ingredients", tags=["ingredients"])


@router.get("/", response_model=list[Ingredient])
def get_all_ingredients():
    """
    Lista todos os ingredientes únicos de todas as receitas.
    Ordenados por categoria e nome.
    Útil para o seletor de ingredientes no frontend.
    """
    return list_all_ingredients()
