Temas:
 - Grafos

# Receita Inteligente

**Conteúdo da Disciplina**: - Grafos<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 232014638  |  Caio Soares de Andrade |
| 231011408  |  Guilherme Flyan Araujo |

## Sobre 
O objetivo do TopoChef é exemplificar o uso de grafos direcionados acíclicos e o algoritmo de ordenação topológica em tarefas cotidianas do dia a dia que possuem relação de precedência ou pré requisitos.<br>
Para isso desenvolvemos uma aplicação web hospedada em nuvem, sendo que o frontend da aplicação está hospedada na Vercel e o backend no Render.

## Screenshots
![Imagem 1](/assets/Captura%20de%20tela%202026-04-13%20213946.png)<br>
![Imagem 2](/assets/Captura%20de%20tela%202026-04-13%20213957.png)<br>
![Imagem 3](/assets/Captura%20de%20tela%202026-04-13%20214202.png)<br>
![Imagem 4](/assets/Captura%20de%20tela%202026-04-13%20214219.png)<br>

## Instalação 

### Frontend
**Linguagem**: TypeScript<br>
**Framework**: Next.js<br>
**Link de Acesso**: [TopoChef](https://g7-grafos-pa-26-1.vercel.app/)<br>
**Pré-Requisitos**: Node.js v20+<br>
**Comandos**: Caso queira rodar localmente acesse a pasta src/frontend rode no terminal `npm i` e depois `npm run dev`.

### Backend
**Linguagem**: Python<br>
**Framework**: FastAPI<br>
**Link de Acesso**: [API TopoChef](https://g7-grafos-pa-26-1.onrender.com)<br>
**Pré-Requisitos**: Python v3.10+<br>
**Comandos**: Caso queira rodar localmente acesse a pasta src/backend crie um ambiente virtual python no diretório e por fim execute no terminal `pip install -r requirements` e depois `uvicorn main:app --reload` para buildar a API.

## Uso 
Caso queira rodar localmente o frontend e o backend, altere em `src/frontend/app/recipe/[id]/page.tsx` na variável `api_url` com a URL cujo backend esteja rodando localmente.

## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.




