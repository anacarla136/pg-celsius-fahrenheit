"""
Etapa 8: Execução principal.

Junta os dados de treino (dados.py) com a Programação Genética
(genetica.py), roda a evolução completa e mostra o resultado final
comparado com a fórmula real de conversão.
"""
from dados import gerar_dados_treino, celsius_para_fahrenheit
from genetica import evoluir, para_texto, avaliar


def main():
    print("=" * 60)
    print("Programação Genética: Celsius -> Fahrenheit")
    print("=" * 60)
    print("Fórmula real: F = C * 9/5 + 32\n")

    dados_treino = gerar_dados_treino()

    print("Evoluindo a população ao longo das gerações...\n")
    melhor = evoluir(dados_treino, tam_pop=300, geracoes=150)

    print("\n" + "=" * 60)
    print("Melhor expressão encontrada pela PG:")
    print("F =", para_texto(melhor))
    print("=" * 60)

    print("\nComparação com a fórmula real:")
    print(f"{'Celsius':>10} {'PG (°F)':>12} {'Real (°F)':>12}")
    for c in (0, 37, 100, -40, 150):
        previsto = avaliar(melhor, c)
        real = celsius_para_fahrenheit(c)
        print(f"{c:>10} {previsto:>12.2f} {real:>12.2f}")


if __name__ == "__main__":
    main()