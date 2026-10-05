# Programação Genética: Conversão de Celsius para Fahrenheit

Trabalho acadêmico que usa **Programação Genética (PG)** em Python para descobrir a fórmula de conversão de graus Celsius para Fahrenheit a partir de dados.

> Status: implementação concluída. Os resultados estão no final deste documento.

## Integrantes

- Ana Carla Martins Teixeira
- Brunna Luyza Coelho Alves da Silva

## Objetivo

Usando Programação Genética, encontrar a função de conversão entre Celsius (C) e Fahrenheit (F).

As fórmulas conhecidas, usadas apenas para gerar os dados de treino e conferir o resultado, são:

- Celsius para Fahrenheit: `F = C × 9/5 + 32`
- Fahrenheit para Celsius: `C = (F − 32) × 5/9`

## O que é Programação Genética?

Técnica inspirada na evolução natural. Uma população de expressões matemáticas, representadas como árvores, evolui ao longo de gerações por meio de seleção, cruzamento e mutação, até que alguma delas se aproxime da solução correta.

O algoritmo não recebe a fórmula. Ele só enxerga pares (C, F) e tenta encontrar uma expressão que os reproduza.

## Estrutura do repositório

```
pg-celsius-fahrenheit/
├── dados.py       # funções de conversão e dados de treino
├── genetica.py    # tudo da PG: indivíduo, aptidão, seleção, cruzamento, mutação, evolução
├── main.py        # executa a evolução e mostra o resultado
├── README.md
└── .gitignore
```

- **`dados.py`**: implementa as duas funções de conversão (C→F e F→C) e gera os pares (Celsius, Fahrenheit) usados como dados de treino.
- **`genetica.py`**: implementa a Programação Genética em si: representação do indivíduo (expressão matemática), função de aptidão, seleção, cruzamento, mutação e o loop evolutivo.
- **`main.py`**: executa a evolução chamando `genetica.py` e imprime a melhor expressão encontrada, comparando com a fórmula real.

## Como a PG funciona (passo a passo)

### Etapa 1: Dados de treino (`dados.py`)

São gerados 21 pares (C, F), com C de -50 a 150 °C de 10 em 10, usando a fórmula real `F = C × 9/5 + 32`. Esses pares são a única informação que a PG recebe.

### Etapa 2: Representação do indivíduo (`genetica.py`)

Cada indivíduo é uma **árvore de expressão**:

- **Folhas:** a variável `x` (que representa C) ou uma constante aleatória entre -10 e 40.
- **Nós internos:** um operador (`+`, `-` ou `*`) com dois filhos.

Exemplo: `['+', ['*', 1.8, 'x'], 32]` representa `(1.8 × C) + 32`.

A população inicial é formada por árvores aleatórias de profundidade até 3.

### Etapa 3: Função de aptidão

Mede o quanto uma árvore erra. Para cada par (C, F), calcula o valor previsto pela árvore e compara com o F real. A aptidão é:

```
aptidão = erro quadrático médio (MSE) + 0,05 × número de nós
```

**Quanto menor, melhor.** A penalidade por tamanho evita árvores gigantes e difíceis de interpretar.

### Etapa 4: Seleção por torneio

Sorteia 5 indivíduos da população e escolhe o de menor aptidão. Assim, os melhores têm mais chance de gerar filhos, mas os piores ainda têm alguma chance, o que mantém a diversidade.

### Etapa 5: Cruzamento

Dados dois pais, troca-se uma subárvore sorteada do primeiro por uma subárvore sorteada do segundo, gerando um filho com características dos dois.

### Etapa 6: Mutação

Em cerca de metade das vezes, **ajusta uma constante** da árvore somando um ruído gaussiano com passo sorteado entre 1, 0,1 e 0,01 (o passo grande explora, o pequeno faz o ajuste fino). Nas demais, **troca uma subárvore** por outra aleatória nova.

### Etapa 7: Loop evolutivo

A cada geração:

1. Calcula a aptidão de todos os indivíduos.
2. Copia o melhor para a próxima geração (**elitismo**).
3. Preenche o resto da nova população por cruzamento (70%), mutação (25%) ou cópia de um selecionado (5%).
4. Descarta filhos com mais de 31 nós.

Ao final das gerações, retorna o melhor indivíduo.

### Etapa 8: Execução (`main.py`)

Gera os dados, roda a evolução, imprime a melhor expressão encontrada e compara a previsão da PG com a fórmula real em alguns valores de temperatura.

### Parâmetros usados

| Parâmetro | Valor |
|---|---|
| Tamanho da população | 300 |
| Número de gerações | 150 |
| Profundidade das árvores iniciais | até 3 |
| Operadores | `+`, `-`, `*` |
| Constantes iniciais | aleatórias entre -10 e 40 |
| Torneio | 5 indivíduos |
| Cruzamento / mutação / cópia | 70% / 25% / 5% |
| Limite de tamanho | 31 nós |
| Penalidade de tamanho | 0,05 por nó |
| Semente aleatória | 42 (resultados reproduzíveis) |

## Plano do trabalho

- [x] `dados.py`: gerar os dados de treino
- [x] `genetica.py`: representação do indivíduo (árvore de expressão)
- [x] `genetica.py`: função de aptidão
- [x] `genetica.py`: seleção, cruzamento e mutação
- [x] `genetica.py`: loop evolutivo
- [x] `main.py`: executar e exibir o resultado
- [x] Testar e documentar os resultados neste README

## Tecnologias

- Python 3 (apenas a biblioteca padrão: `random` e `copy`)

## Como executar

1. Clone o repositório e entre na pasta:

```bash
git clone https://github.com/anacarla136/pg-celsius-fahrenheit.git
cd pg-celsius-fahrenheit
```

2. Execute a evolução completa:

```bash
python main.py
```

Não há dependências externas para instalar. Os arquivos `dados.py` e `genetica.py` também podem ser executados sozinhos (`python dados.py`, `python genetica.py`) para ver testes rápidos de cada etapa.

## Resultados

Execução com os parâmetros da tabela acima (população de 300, 150 gerações, semente 42).

**Melhor expressão encontrada:**

```
F = ((31.942 + C) - (C * -0.801))
```

Simplificando, isso equivale a **F ≈ 1,801 × C + 31,942**, muito próximo da fórmula real **F = 1,8 × C + 32**. A expressão tem apenas 7 nós, e a aptidão final foi 0,3531 (MSE de aproximadamente 0,003 mais 0,35 de penalidade de tamanho).

**Comparação com a fórmula real:**

| Celsius | PG (°F) | Real (°F) |
|---:|---:|---:|
| 0 | 31,94 | 32,00 |
| 37 | 98,57 | 98,60 |
| 100 | 212,03 | 212,00 |
| -40 | -40,09 | -40,00 |
| 150 | 302,07 | 302,00 |

O maior erro nesses pontos foi de cerca de 0,09 °F.

**Evolução do erro (aptidão do melhor indivíduo):**

| Geração | Aptidão |
|---:|---:|
| 0 | 150,85 |
| 10 a 90 | ≈ 146,92 (estagnado) |
| 100 | 3,55 |
| 110 | 0,39 |
| final | 0,35 |

O erro ficou praticamente parado por boa parte da execução e despencou quando a PG encontrou a estrutura `C + constante + C × constante`, depois refinada pelas mutações de constantes.

### Observações

- A PG evolui a conversão **Celsius para Fahrenheit**. A conversão inversa está implementada em `dados.py` como função de apoio.
- Como a PG é estocástica, a expressão encontrada pode variar com a semente. Com outras sementes, as expressões também ficaram muito próximas da fórmula real, mas em formas diferentes e, às vezes, mais longas.
- Os dados de treino não têm ruído, então a solução exata `1,8 × C + 32` existe e é o alvo ideal.
