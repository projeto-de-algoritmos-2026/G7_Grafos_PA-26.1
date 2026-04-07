# Configuração CORS e registro de rotas da API
# Importa a instância original do FastAPI (main.py) e integra os novos routers.
#
# Inicialização local:
#   uvicorn app_setup:app --reload

from fastapi.middleware.cors import CORSMiddleware

# Importar o app existente do colega
from main import app

# Importar os novos routers
from recipe_router import router as recipe_router
from ingredient_router import router as ingredient_router


# --- CORS ---
# Permite que o frontend Next.js (localhost:3000) acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Next.js dev server
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Registrar routers ---
app.include_router(recipe_router)
app.include_router(ingredient_router)
