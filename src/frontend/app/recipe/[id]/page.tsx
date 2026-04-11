import { Suspense } from "react";
import Link from "next/link";
import {recipes} from "../../../data/recipes.json";

export default async function Recipe({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const recipe = recipes.find((r: any) => r.id === id);
  const graph = recipe?.adjacency_list;
  const api_url = "https://g7-grafos-pa-26-1.onrender.com"
  
  let topologicalSortSteps = await fetch(`${api_url}/topologicalSort`, {
                                        method: "POST",
                                        headers: {
                                          "Content-Type": "application/json",
                                        },
                                        body: JSON.stringify({ graph }),
                                      });
  let mergeSortSteps = await fetch(`${api_url}/mergeSort`, {
                                  method: "POST",
                                  headers: {
                                    "Content-Type": "application/json",
                                  },
                                  body: JSON.stringify({ graph }),
                                });
  let quickSortSteps = await fetch(`${api_url}/quickSort`, {
                                  method: "POST",
                                  headers: {
                                    "Content-Type": "application/json",
                                  },
                                  body: JSON.stringify({ graph }),
                                });

  const dataTopologicalSortSteps = await topologicalSortSteps.json();
  const dataMergeSortSteps = await mergeSortSteps.json();
  const dataQuickSortSteps = await quickSortSteps.json();

  return (
    <>
      <Suspense fallback={<p>Carregando receita... 
                            <br /><br />
                              O servidor hospedado no Render pode demorar até 5 minutos para acordar...
                          </p>}>
        <div className="flex flex-col items-center justify-center items-center gap-6">
          <h3 className="text-2xl font-bold">Receita de {recipe?.name}</h3>
          <div className="mx-5 lg:mx-10 bg-blue-950 rounded-xl p-10">
            <p className="">Foram aplicados diferentes algoritmos de ordenação para testar a combinação que satisfaça a ordem necessária da receita, como a receita foi modelada através de um grafo direcionado acíclico é possível notar que o algoritmo Topological Sort é mais adequado que o Merge Sort e Quick Sort para organizar o passo a passo por ser um algoritmo que lida com precedências!
              <br />
              <br />
              O Merge e o Quick desempenham um papel bastante errado principalmente por se basear nos valores numéricos dos IDs dos passos, que foram numerados de forma aleatória, e não levam em consideração as dependências entre os passos, o que pode resultar em uma ordem de execução incorreta da receita. 
            </p>
          </div>

          <section className="flex flex-wrap justify-center items-center lg:flex-row gap-10 px-5 lg:px-0 pt-5">
            <article className="rounded-xl border-t-[7.5px] border-x-[1px] border-b-[1px] border-green-600 min-h-[400px] max-w-screen lg:min-w-[400px] lg:max-w-[400px] p-4">
              <h4 className="text-xl font-semibold text-center">Topological Sort</h4>
              <ul className="flex flex-col gap-5 mt-5">
                {dataTopologicalSortSteps.map((id: number) => (
                  <li key={id} className="bg-blue-950 rounded-xl p-4">          
                    <h5 className="font-bold">{recipe?.steps.find((i) => i.id === id)?.name}</h5>
                    <p className="">{recipe?.steps.find((i) => i.id === id)?.description}</p>
                  </li>
                ))}
              </ul>
              
            </article>
            <article className="rounded-xl border-t-[7.5px] border-x-[1px] border-b-[1px] border-red-600 min-h-[400px] max-w-screen lg:min-w-[400px] lg:max-w-[400px] p-4"> 
              <h4 className="text-xl font-semibold text-center">Merge Sort</h4>
                <ul className="flex flex-col gap-5 mt-5">
                  {dataMergeSortSteps.map((id: number) => (
                    <li key={id} className="bg-blue-950 rounded-xl p-4">          
                      <h5 className="font-bold">{recipe?.steps.find((i) => i.id === id)?.name}</h5>
                      <p className="">{recipe?.steps.find((i) => i.id === id)?.description}</p>
                    </li>
                  ))}
              </ul>
            </article>
            <article className="rounded-xl border-t-[7.5px] border-x-[1px] border-b-[1px] border-red-600 min-h-[400px] max-w-screen lg:min-w-[400px] lg:max-w-[400px] p-4">
              <h4 className="text-xl font-semibold text-center">Quick Sort</h4>
              <ul className="flex flex-col gap-5 mt-5">
                {dataQuickSortSteps.map((id: number) => (
                  <li key={id} className="bg-blue-950 rounded-xl p-4">          
                    <h5 className="font-bold">{recipe?.steps.find((i) => i.id === id)?.name}</h5>
                    <p className="">{recipe?.steps.find((i) => i.id === id)?.description}</p>
                  </li>
                ))}
              </ul>
            </article>
          </section>
          <Link href="/">
            <button className="bg-blue-900 text-white font-bold py-4 px-6 mt-5 rounded-xl cursor-pointer transition hover:scale-105 hover:brightness-125">
              Voltar para a lista de receitas
            </button>
          </Link>
        </div>
      </Suspense>
     
    </>
  );
}