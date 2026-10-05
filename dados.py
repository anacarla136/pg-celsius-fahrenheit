"""
Etapa 1: Dados de treino.

Aqui ficam as duas funções de conversão (usadas para gerar os dados
e conferir o resultado da PG) e a lista de pares (Celsius, Fahrenheit)
que servirá de dados de treino para o algoritmo genético.
"""

def celsius_para_fahrenheit(c):
    """Converte Celsius para Fahrenheit: F = C * 9/5 + 32"""
    return c * 9 / 5 + 32


def fahrenheit_para_celsius(f):
    """Converte Fahrenheit para Celsius: C = (F - 32) * 5/9"""
    return (f - 32) * 5 / 9


def gerar_dados_treino():
    """
    Gera uma lista de pares (C, F) usando a função real de conversão.
    Esses pares serão usados pela Programação Genética para avaliar
    o quão boa é cada expressão candidata.
    """
    return [(c, celsius_para_fahrenheit(c)) for c in range(-50, 151, 10)]


# Esse bloco só roda quando executamos "python dados.py" diretamente,
# servindo como um teste rápido deste arquivo.
if __name__ == "__main__":
    print("Teste das funções de conversão:")
    print("0°C  ->", celsius_para_fahrenheit(0), "°F  (esperado: 32.0)")
    print("100°C ->", celsius_para_fahrenheit(100), "°F  (esperado: 212.0)")
    print("32°F ->", fahrenheit_para_celsius(32), "°C  (esperado: 0.0)")

    print("\nDados de treino gerados:")
    for c, f in gerar_dados_treino():
        print(f"  {c:>4} °C -> {f:>6.1f} °F")