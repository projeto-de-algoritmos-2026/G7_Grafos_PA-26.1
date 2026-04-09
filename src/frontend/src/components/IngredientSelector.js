"use client";

import styles from './IngredientSelector.module.css';

export default function IngredientSelector({ 
  ingredients, 
  selectedIds, 
  onToggleIngredient, 
  onNext,
  onBack
}) {
  return (
    <div className={`glass-panel fade-in ${styles.container}`}>
      <h2>O que você tem na geladeira?</h2>
      <p style={{marginBottom: '1rem', color: 'var(--text-muted)'}}>
        Selecione os ingredientes disponíveis. Dependendo da receita, calcularemos o que falta.
      </p>

      <div className={styles.grid}>
        {ingredients.map(ing => (
          <label key={ing.id} className={`${styles.item} ${selectedIds.includes(ing.id) ? styles.selected : ''}`}>
            <input 
              type="checkbox" 
              checked={selectedIds.includes(ing.id)}
              onChange={() => onToggleIngredient(ing.id)}
            />
            <span className={styles.name}>{ing.name}</span>
            <span className={styles.unit}>{ing.unit}</span>
          </label>
        ))}
      </div>

      <div className={styles.actions}>
        <button onClick={onBack}>Voltar</button>
        <button className="primary" onClick={onNext}>Simular Preparo</button>
      </div>
    </div>
  );
}
