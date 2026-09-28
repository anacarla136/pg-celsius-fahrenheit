# Programação Genética: Conversão de Celsius para Fahrenheit

Trabalho acadêmico que vai usar **Programação Genética (PG)** em Python para descobrir a fórmula de conversão de graus Celsius para Fahrenheit a partir de dados.

>  Projeto em desenvolvimento.

## Integrantes

- Ana Carla Martins Teixeira
- Brunna Luyza Coelho Alves da Silva


## Objetivo
 
Usando Programação Genética, encontrar a função de conversão entre Celsius (C) e Fahrenheit (F).
 
As fórmulas conhecidas, usadas apenas para gerar os dados de treino e conferir o resultado, são:
 
- Celsius para Fahrenheit: `F = C × 9/5 + 32`
- Fahrenheit para Celsius: `C = (F − 32) × 5/9`
## O que é Programação Genética?
 
Técnica inspirada na evolução natural. Uma população de expressões matemáticas evolui ao longo de gerações por meio de seleção, cruzamento e mutação, até que alguma delas se aproxime da solução correta.
 
## Estrutura do repositório
 
```
pg-celsius-fahrenheit/
├── dados.py        # dados de treino
├── genetica.py       # tudo da PG: indivíduo, aptidão, seleção, cruzamento, mutação, evolução
├── main.py             # executa e mostra o resultado
├── README.md
└── .gitignore
```
 
- **`dados.py`** — implementa as duas funções de conversão (C→F e F→C) e gera os pares (Celsius, Fahrenheit) usados como dados de treino.
- **`genetica.py`** — implementa a Programação Genética em si: como um indivíduo (expressão matemática) é representado, a função de aptidão (erro entre o valor previsto e o real), seleção, cruzamento, mutação e o loop evolutivo.
- **`main.py`** — executa a evolução chamando `genetica.py` e imprime a melhor expressão encontrada, comparando com a fórmula real.
## Plano do trabalho
 
- [ ] `dados.py` — gerar os dados de treino
- [ ] `genetica.py` — representação do indivíduo (árvore de expressão)
- [ ] `genetica.py` — função de aptidão
- [ ] `genetica.py` — seleção, cruzamento e mutação
- [ ] `genetica.py` — loop evolutivo
- [ ] `main.py` — executar e exibir o resultado
- [ ] Testar e documentar os resultados neste README
## Tecnologias
 
- Python 3
## Como executar
 
_A ser preenchido quando o código estiver pronto._
 
## Resultados
 
_A ser preenchido após os testes._
 
