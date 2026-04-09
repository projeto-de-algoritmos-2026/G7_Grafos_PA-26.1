"use client";

import styles from './AlgorithmComparison.module.css';

export default function AlgorithmComparison({ comparisonData, onReset }) {
  if (!comparisonData || !comparisonData.results) return null;

  return (
    <div className={`fadeIn ${styles.container}`}>
      <div className={styles.header}>
        <h2>Comparação de Algoritmos</h2>
        <button onClick={onReset} className="primary">Escolher Nova Receita</button>
      </div>

      <p style={{marginBottom: '2rem', color: 'var(--text-muted)'}}>
        Veja o que acontece quando tentamos ordenar os passos da receita <strong>"{comparisonData.recipe_name}"</strong> com diferentes algoritmos.
      </p>

      <div className={styles.grid}>
        {comparisonData.results.map(result => (
          <div key={result.algorithm} className={`glass-panel ${styles.algoColumn} ${result.is_valid ? styles.validBorder : styles.invalidBorder}`}>
            <h3 className={result.is_valid ? styles.validText : styles.invalidText}>
              {result.algorithm_label}
            </h3>
            
            <p className={styles.explanation}>{result.explanation}</p>

            <div className={styles.statusBadge}>
              {result.is_valid ? "✅ Ordem Válida" : "❌ Violações Encontradas"}
            </div>

            {result.violations.length > 0 && (
              <div className={styles.violationsBox}>
                <h4>Erros de Dependência:</h4>
                <ul>
                  {result.violations.map((v, i) => (
                    <li key={i}>
                      Passo {v.step_position} ("{v.step_name}") executado antes da sua dependência "{v.depends_on_name}".
                    </li>
                  ))}
                </ul>
              </div>
            )}

            <div className={styles.stepsList}>
              <h4>Ordem Resultante:</h4>
              <ol>
                {result.ordered_steps.map((step, idx) => {
                  const isViolating = result.violations.some(v => v.step_name === step.name);
                  return (
                    <li key={idx} className={`${styles.stepItem} ${isViolating ? styles.stepError : ''}`}>
                      <span className={styles.stepNum}>{idx + 1}</span>
                      <span className={styles.stepName}>{step.name}</span>
                    </li>
                  );
                })}
              </ol>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
