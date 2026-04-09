const API_BASE = 'http://127.0.0.1:8000/api/v1';

export async function fetchIngredients() {
  try {
    const res = await fetch(`${API_BASE}/ingredients/`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Falha ao buscar ingredientes');
    return await res.json();
  } catch (error) {
    console.error(error);
    return [];
  }
}

export async function fetchRecipes() {
  try {
    const res = await fetch(`${API_BASE}/recipes/`, { cache: 'no-store' });
    if (!res.ok) throw new Error('Falha ao buscar receitas');
    return await res.json();
  } catch (error) {
    console.error(error);
    return [];
  }
}

export async function fetchRecipeDetails(id) {
  try {
    const res = await fetch(`${API_BASE}/recipes/${id}`, { cache: 'no-store' });
    if (!res.ok) throw new Error(`Falha ao buscar detalhes da receita ${id}`);
    return await res.json();
  } catch (error) {
    console.error(error);
    return null;
  }
}

export async function fetchMissingIngredients(recipeId, availableIngredients) {
  try {
    const res = await fetch(`${API_BASE}/recipes/${recipeId}/missing`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ available: availableIngredients }),
      cache: 'no-store'
    });
    if (!res.ok) throw new Error('Falha ao calcular ingredientes faltantes');
    return await res.json();
  } catch (error) {
    console.error(error);
    return null;
  }
}

export async function sortRecipe(recipeId, algorithm) {
  try {
    const res = await fetch(`${API_BASE}/recipes/${recipeId}/sort`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ algorithm: algorithm }),
      cache: 'no-store'
    });
    if (!res.ok) throw new Error('Falha ao ordenar receita');
    return await res.json();
  } catch (error) {
    console.error(error);
    return null;
  }
}

export async function compareAlgorithms(recipeId) {
  try {
    const res = await fetch(`${API_BASE}/recipes/${recipeId}/compare`, { 
      method: 'POST', 
      cache: 'no-store' 
    });
    if (!res.ok) throw new Error('Falha ao comparar os algoritmos');
    return await res.json();
  } catch (error) {
    console.error(error);
    return null;
  }
}
