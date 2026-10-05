"""
Etapas 2 a 7: Programação Genética.

- Representação do indivíduo (árvore de expressão)
- Função de aptidão (fitness)
- Seleção (torneio)
- Cruzamento (crossover)
- Mutação
- Loop evolutivo

Um indivíduo é uma árvore de expressão matemática:
- Folha: a variável 'x' (representa C) ou um número (constante)
- Nó interno: uma lista [operador, filho_esquerdo, filho_direito]

Exemplo: ['+', ['*', 1.8, 'x'], 32]  representa  (1.8 * x) + 32
"""
import random
import copy

random.seed(42)  # fixa a semente para resultados reproduzíveis

OPERADORES = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
}



# Etapa 2: Representação do indivíduo
def folha_aleatoria():
    """Cria uma folha: ou a variável 'x', ou uma constante aleatória."""
    if random.random() < 0.5:
        return 'x'
    return round(random.uniform(-10, 40), 2)


def gerar_arvore(profundidade):
    """Cria uma árvore de expressão aleatória."""
    if profundidade == 0 or random.random() < 0.3:
        return folha_aleatoria()
    op = random.choice(list(OPERADORES))
    return [op, gerar_arvore(profundidade - 1), gerar_arvore(profundidade - 1)]


def avaliar(no, x):
    """Calcula o valor numérico da árvore para um dado x (temperatura em C)."""
    if no == 'x':
        return x
    if isinstance(no, (int, float)):
        return no
    op, esquerda, direita = no
    return OPERADORES[op](avaliar(esquerda, x), avaliar(direita, x))


def para_texto(no):
    """Converte a árvore em uma string legível, tipo '(C * 1.8) + 32'."""
    if no == 'x':
        return 'C'
    if isinstance(no, (int, float)):
        return str(round(no, 3))
    op, esquerda, direita = no
    return f"({para_texto(esquerda)} {op} {para_texto(direita)})"


def tamanho(no):
    """Conta quantos nós a árvore tem (usado para penalizar árvores gigantes)."""
    if not isinstance(no, list):
        return 1
    return 1 + tamanho(no[1]) + tamanho(no[2])



# Etapa 3: Função de aptidão (fitness)
def aptidao(arvore, dados_treino):
    """
    Calcula o erro quadrático médio (MSE) entre o valor previsto pela árvore
    e o valor real de F, para todos os dados de treino.
    Quanto MENOR o valor retornado, melhor é o indivíduo.
    Uma pequena penalidade por tamanho evita árvores gigantes e confusas.
    """
    erro = sum((avaliar(arvore, c) - f) ** 2 for c, f in dados_treino) / len(dados_treino)
    return erro + 0.05 * tamanho(arvore)



# Funções auxiliares para cruzamento e mutação
# (trabalham com "caminhos": uma sequência de índices que localiza
#  um ponto dentro da árvore, por exemplo (1, 2) = filho direito do
#  filho esquerdo da raiz)
def todos_os_caminhos(no, caminho=()):
    """Lista o caminho até cada nó da árvore (para escolher um ponto de corte)."""
    caminhos = [caminho]
    if isinstance(no, list):
        caminhos += todos_os_caminhos(no[1], caminho + (1,))
        caminhos += todos_os_caminhos(no[2], caminho + (2,))
    return caminhos


def pegar(no, caminho):
    """Retorna a subárvore que está naquele caminho."""
    for i in caminho:
        no = no[i]
    return no


def substituir(no, caminho, novo):
    """Retorna uma NOVA árvore com a subárvore daquele caminho trocada por 'novo'."""
    if not caminho:
        return novo
    no = copy.deepcopy(no)
    alvo = no
    for i in caminho[:-1]:
        alvo = alvo[i]
    alvo[caminho[-1]] = novo
    return no



# Etapas 4, 5 e 6: Seleção, Cruzamento e Mutação
def selecao_torneio(populacao, notas, k=5):
    """Sorteia k indivíduos da população e devolve o de menor erro (melhor)."""
    competidores = random.sample(range(len(populacao)), k)
    vencedor = min(competidores, key=lambda i: notas[i])
    return populacao[vencedor]


def cruzamento(pai1, pai2):
    """Troca uma subárvore aleatória de pai1 por uma subárvore de pai2."""
    ponto1 = random.choice(todos_os_caminhos(pai1))
    ponto2 = random.choice(todos_os_caminhos(pai2))
    return substituir(pai1, ponto1, copy.deepcopy(pegar(pai2, ponto2)))


def mutacao(arvore):
    """
    Dois tipos de mutação:
    - 50% das vezes: ajusta só uma constante, com passo grande ou pequeno
      (o passo grande explora, o pequeno faz o ajuste fino)
    - nas outras: troca uma subárvore qualquer por outra nova
    """
    constantes = [c for c in todos_os_caminhos(arvore)
                  if isinstance(pegar(arvore, c), (int, float))]
    if constantes and random.random() < 0.5:
        ponto = random.choice(constantes)
        passo = random.choice([1, 0.1, 0.01])
        return substituir(arvore, ponto, pegar(arvore, ponto) + random.gauss(0, passo))
    ponto = random.choice(todos_os_caminhos(arvore))
    return substituir(arvore, ponto, gerar_arvore(2))



# Etapa 7: Loop evolutivo
def evoluir(dados_treino, tam_pop=300, geracoes=150, p_cruz=0.7, p_mut=0.25, imprimir=True):
    """
    Executa a Programação Genética:
    1. Cria população inicial aleatória
    2. Repete por várias gerações:
       - avalia a aptidão de todos
       - preserva o melhor indivíduo (elitismo)
       - gera o resto da nova população por cruzamento, mutação ou cópia
    3. Retorna o melhor indivíduo encontrado
    """
    populacao = [gerar_arvore(3) for _ in range(tam_pop)]

    for g in range(geracoes):
        notas = [aptidao(ind, dados_treino) for ind in populacao]
        melhor_i = min(range(tam_pop), key=lambda i: notas[i])
        melhor = populacao[melhor_i]

        if imprimir and g % 10 == 0:
            print(f"Geração {g:3d} | erro = {notas[melhor_i]:.4f} | {para_texto(melhor)}")

        nova_pop = [copy.deepcopy(melhor)]  # elitismo: o melhor sempre sobrevive
        while len(nova_pop) < tam_pop:
            r = random.random()
            if r < p_cruz:
                filho = cruzamento(
                    selecao_torneio(populacao, notas),
                    selecao_torneio(populacao, notas),
                )
            elif r < p_cruz + p_mut:
                filho = mutacao(selecao_torneio(populacao, notas))
            else:
                filho = copy.deepcopy(selecao_torneio(populacao, notas))

            if tamanho(filho) <= 31:  # evita árvores gigantes demais
                nova_pop.append(filho)

        populacao = nova_pop

    notas = [aptidao(ind, dados_treino) for ind in populacao]
    melhor_final = populacao[min(range(tam_pop), key=lambda i: notas[i])]
    return melhor_final



# Teste rápido deste arquivo
if __name__ == "__main__":
    from dados import gerar_dados_treino

    arvore_teste = ['+', ['*', 1.8, 'x'], 32]
    print("Árvore ideal:", para_texto(arvore_teste))
    print("Avaliando em C=0:  ", avaliar(arvore_teste, 0), "(esperado: 32.0)")
    print("Avaliando em C=100:", avaliar(arvore_teste, 100), "(esperado: 212.0)")

    dados_treino = gerar_dados_treino()
    print("\nAptidão da árvore ideal (deve ser baixa, só a penalidade de tamanho):")
    print(aptidao(arvore_teste, dados_treino))

    print("\nÁrvore aleatória gerada:")
    aleatoria = gerar_arvore(3)
    print(para_texto(aleatoria))
    print("Aptidão dela (geralmente bem maior):")
    print(aptidao(aleatoria, dados_treino))

    print("\n--- Testando o loop evolutivo com poucas gerações (20) ---")
    melhor = evoluir(dados_treino, tam_pop=100, geracoes=20)
    print("\nMelhor encontrado em 20 gerações:", para_texto(melhor))
    print("Aptidão:", aptidao(melhor, dados_treino))