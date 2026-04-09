"use client";

import styles from './RecipeList.module.css';

export default function RecipeList({ recipes, onSelectRecipe }) {
  if (!recipes || recipes.length === 0) {
    return <div className="glass-panel"><div className="spinner"></div></div>;
  }

  return (
    <div className={styles.grid}>
      {recipes.map(recipe => (
        <div key={recipe.id} className={`glass-panel ${styles.card} fade-in`} onClick={() => onSelectRecipe(recipe.id)}>
          <h3>{recipe.name}</h3>
          <p className={styles.meta}>
            ⏱ {recipe.prep_time_minutes} min | 📊 {recipe.difficulty}
          </p>
          <p className={styles.desc}>{recipe.description}</p>
          <button className="primary" style={{marginTop: '1rem', width: '100%'}}>
            Selecionar Receita
          </button>
        </div>
      ))}
    </div>
  );
}
