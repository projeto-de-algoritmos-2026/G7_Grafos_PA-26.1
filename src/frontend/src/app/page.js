"use client";

import { useState, useEffect } from 'react';
import RecipeList from '@/components/RecipeList';
import IngredientSelector from '@/components/IngredientSelector';
import AlgorithmComparison from '@/components/AlgorithmComparison';
import { fetchRecipes, fetchIngredients, compareAlgorithms } from '@/lib/api';

export default function Home() {
  const [step, setStep] = useState(1);
  const [recipes, setRecipes] = useState([]);
  const [allIngredients, setAllIngredients] = useState([]);
  
  const [selectedRecipeId, setSelectedRecipeId] = useState(null);
  const [selectedIngredientIds, setSelectedIngredientIds] = useState([]);
  const [comparisonData, setComparisonData] = useState(null);
  const [loadingMsg, setLoadingMsg] = useState('');

  useEffect(() => {
    async function loadInitialData() {
      const [recs, ings] = await Promise.all([fetchRecipes(), fetchIngredients()]);
      setRecipes(recs);
      setAllIngredients(ings);
    }
    loadInitialData();
  }, []);

  const handleSelectRecipe = (id) => {
    setSelectedRecipeId(id);
    setSelectedIngredientIds([]); // reseta ingredientes
    setStep(2);
  };

  const handleToggleIngredient = (id) => {
    setSelectedIngredientIds(prev => 
      prev.includes(id) ? prev.filter(i => i !== id) : [...prev, id]
    );
  };

  const handleSimulate = async () => {
    setLoadingMsg('Simulando o preparo nos bastidores e ordenando os grafos...');
    setStep(0); // Loading state
    
    // Na nossa simulação, pulamos a checagem de "missing ingredients" para ser direto,
    // e focamos na comparação dos algoritmos ensinando grafos.
    const cmpData = await compareAlgorithms(selectedRecipeId);
    
    setComparisonData(cmpData);
    setLoadingMsg('');
    setStep(3);
  };

  const reset = () => {
    setSelectedRecipeId(null);
    setComparisonData(null);
    setStep(1);
  };

  return (
    <main style={{ padding: '2rem' }}>
      <header style={{ marginBottom: '3rem', textAlign: 'center' }}>
        <h1 className="title-gradient" style={{ fontSize: '2.5rem' }}>Ordene a sua Receita (DAGs)</h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Aprenda como Grafos Direcionados Acíclicos são essenciais para evitar pratos desastrosos.
        </p>
      </header>

      {step === 0 && (
        <div style={{ textAlign: 'center', marginTop: '4rem' }}>
          <div className="spinner" style={{ margin: '0 auto 1rem', width: '40px', height: '40px' }}></div>
          <p>{loadingMsg}</p>
        </div>
      )}

      {step === 1 && (
        <RecipeList recipes={recipes} onSelectRecipe={handleSelectRecipe} />
      )}

      {step === 2 && (
        <IngredientSelector 
          ingredients={allIngredients} 
          selectedIds={selectedIngredientIds}
          onToggleIngredient={handleToggleIngredient}
          onNext={handleSimulate}
          onBack={() => setStep(1)}
        />
      )}

      {step === 3 && (
        <AlgorithmComparison 
          comparisonData={comparisonData} 
          onReset={reset}
        />
      )}
    </main>
  );
}
