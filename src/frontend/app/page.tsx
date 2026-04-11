"use client";

import Link from "next/link";
import {ingredients} from "../data/ingredients.json";
import {recipes} from "../data/recipes.json";
import { useState } from "react";


export default function Home() {
  const [selectedIngredients, setSelectedIngredients] = useState<string[]>([]);
  const [selectedRecipe, setSelectedRecipe] = useState<string>();

  const toggleRecipe = (recipeId: string) => {
    setSelectedRecipe((prev) => (prev === recipeId ? undefined : recipeId));
  }

  const checkIngredientSelected = (ingredientId: string) => {
    return selectedIngredients.includes(ingredientId);
  };

  const checkRecipeSelected = (recipeId: string) => {
    return selectedRecipe === recipeId;
  }

    const toggleIngredient = (ingredientId: string) => {
    setSelectedIngredients((prev) =>
      prev.includes(ingredientId)
        ? prev.filter((id) => id !== ingredientId)
        : [...prev, ingredientId]
    );
    setSelectedRecipe(undefined);
  };

  const recipeIsAvailable = (recipeId: string, ingredients: string[]) => {
    const recipe = recipes.find((r) => r.id === recipeId);
    if (!recipe) return false;
    
    if (recipe.ingredients.every((ingredient) =>
      ingredients.includes(ingredient.id)
    )) {
      return true;
    }
    return false;
  };

  console.log(selectedIngredients);

  return (
    <>
        <section className="w-full flex flex-col justify-center items-center gap-10 lg:px-15">
          <h3 className="text-2xl font-bold">Selecione os Ingredientes</h3>
          <ul className=" w-full flex flex-wrap items-center justify-center lg:grid lg:grid-cols-6 gap-5 lg:gap-20">
            {ingredients.map((ingredient) => (
              <li key={ingredient.id} className={checkIngredientSelected(ingredient.id) ? "w-[150px] h-[100px] bg-blue-950 flex justify-center items-center hover:cursor-pointer scale-[1.1] rounded-xl brightness-150 border border-gray-600" : " w-[150px] h-[100px] bg-blue-950 flex justify-center items-center hover:cursor-pointer hover:scale-[1.1] hover:brightness-150 transition rounded-xl border border-gray-600"} onClick={()=>(toggleIngredient(ingredient.id))} >
                <p>{ingredient.id}</p>
              </li>
            ))}
          </ul>
        </section>

        <section className="w-full flex flex-col justify-center items-center px-5 lg:px-15">
          <h2 className="text-2xl font-bold">Receitas Disponíveis</h2>
          <ul className="w-full flex flex-wrap justify-center items-center gap-5 lg:gap-20 pt-10">
            {recipes.map((recipe)=>(
              <li key={recipe.id} className={recipeIsAvailable(recipe.id, selectedIngredients) ? (checkRecipeSelected(recipe.id) ? "w-[500px] h-[200px] lg:h-[150px] bg-blue-950 flex flex-col justify-center items-center hover:cursor-pointer scale-[1.1] rounded-xl brightness-150 border border-gray-600 gap-5 p-10" : " w-[500px] h-[200px] lg:h-[150px] bg-blue-950 flex flex-col justify-center items-center hover:cursor-pointer hover:scale-[1.1] hover:brightness-150 transition rounded-xl border border-gray-600 gap-5 p-10") : " w-[500px] h-[200px] lg:h-[150px] bg-blue-950 flex flex-col justify-center items-center hover:cursor-not-allowed opacity-50 rounded-xl border border-gray-600 gap-5 p-10"} onClick={()=>{if(recipeIsAvailable(recipe.id, selectedIngredients))toggleRecipe(recipe.id)}}>
                <h3 className="text-xl font-bold">{recipe.name}</h3>
                <p className="text-center">{recipe.description}</p>
              </li>
            ))}
          </ul>
        </section>
        <Link href={`/recipe/${selectedRecipe}`}>
          <button className={selectedRecipe ? "w-[200px] h-[50px] bg-green-600 flex justify-center items-center hover:cursor-pointer hover:scale-[1.1] hover:brightness-150 transition rounded-xl border border-gray-600" : "w-[200px] h-[50px] bg-green-600 flex justify-center items-center hover:cursor-not-allowed opacity-50 rounded-xl border border-gray-600"} disabled={!selectedRecipe}>
            Confirmar Receita
        </button>
        </Link>
    </>
  );
}
