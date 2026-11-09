
# ATIVIDADE 1 — CONGRUÊNCIA MODULAR E TEOREMA CHINÊS DO RESTO
# Disciplina: Estruturas Matemáticas para Computação
# Professor(a): Cristiane Loesch de Souza Costa


def ler_inteiro(mensagem):
    """Solicita um número inteiro e valida a entrada."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido.")


def mdc(a, b):
    """Calcula o máximo divisor comum pelo algoritmo de Euclides."""
    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b

    return a


def euclides_estendido(a, b):
    """Calcula o MDC e os coeficientes de Bezout."""
    if b == 0:
        return a, 1, 0

    divisor, x1, y1 = euclides_estendido(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return divisor, x, y


def inverso_modular(a, modulo):
    """Calcula o inverso modular usando Euclides Estendido."""
    if modulo <= 1:
        return None

    divisor, x, _ = euclides_estendido(a, modulo)

    if divisor != 1:
        return None

    return x % modulo


def verificar_congruencia():
    print("\n=== PARTE A: VERIFICAÇÃO DE CONGRUÊNCIA ===")

    a = ler_inteiro("Digite o inteiro a: ")
    b = ler_inteiro("Digite o inteiro b: ")

    n = ler_inteiro("Digite o módulo n (positivo): ")

    while n <= 0:
        print("O módulo precisa ser maior que zero.")
        n = ler_inteiro("Digite o módulo n: ")

    diferenca = a - b
    resto = diferenca % n

    print(f"\nCálculo: a - b = {a} - ({b}) = {diferenca}")
    print(f"Resto de {diferenca} por {n}: {resto}")

    if resto == 0:
        print(f"\n{a} ≡ {b} (mod {n})")
        print("Os números são congruentes.")
        print(f"Justificativa: {diferenca} é divisível por {n}.")
    else:
        print(f"\n{a} não é congruente a {b} módulo {n}.")
        print(f"Justificativa: o resto da divisão é {resto}.")


def teorema_chines_resto():
    print("\n=== PARTE B: TEOREMA CHINÊS DO RESTO ===")

    quantidade = ler_inteiro(
        "Quantas congruências deseja resolver? "
    )

    while quantidade < 1:
        print("É necessário informar pelo menos uma congruência.")
        quantidade = ler_inteiro("Quantidade: ")

    restos = []
    modulos = []

    # Entrada das congruências
    for i in range(quantidade):
        print(f"\nCongruência {i + 1}: x ≡ a (mod n)")

        a = ler_inteiro("Digite o resto a: ")
        n = ler_inteiro("Digite o módulo n (positivo): ")

        while n <= 0:
            print("O módulo precisa ser positivo.")
            n = ler_inteiro("Digite o módulo n: ")

        restos.append(a)
        modulos.append(n)

    # Verificação dos MDCs entre os módulos
    print("\n=== VERIFICAÇÃO DOS MÓDULOS ===")

    for i in range(quantidade):
        for j in range(i + 1, quantidade):
            divisor = mdc(modulos[i], modulos[j])

            print(
                f"mdc({modulos[i]}, {modulos[j]}) = {divisor}"
            )

    # Inicialização com a primeira congruência
    x = restos[0] % modulos[0]
    N = modulos[0]

    print("\n=== RESOLUÇÃO DO SISTEMA ===")
    print(f"Congruência inicial: x ≡ {x} (mod {N})")

    # Combinação das demais congruências
    for i in range(1, quantidade):

        a = restos[i]
        n = modulos[i]

        print(f"\nCombinando com x ≡ {a} (mod {n})")

        divisor = mdc(N, n)

        print(f"mdc({N}, {n}) = {divisor}")

        diferenca = a - x

        # Verifica a compatibilidade do sistema
        if diferenca % divisor != 0:
            print("\nNão existe solução para esse sistema.")
            print(
                f"Pois {diferenca} não é divisível por {divisor}."
            )
            return

        # Redução dos módulos
        N_reduzido = N // divisor
        n_reduzido = n // divisor

        # Calcula o valor de k
        if n_reduzido == 1:
            k = 0
        else:
            inverso = inverso_modular(
                N_reduzido, n_reduzido
            )

            if inverso is None:
                print("Não foi possível calcular o inverso modular.")
                return

            k = (
                (diferenca // divisor) * inverso
            ) % n_reduzido

        print(f"Diferença: {a} - {x} = {diferenca}")
        print(f"N reduzido = {N} / {divisor} = {N_reduzido}")
        print(f"n reduzido = {n} / {divisor} = {n_reduzido}")
        print(f"Valor de k = {k}")

        # Atualiza a solução e o módulo
        x = (x + N * k) % (N * n_reduzido)
        N = N * n_reduzido

        print(f"Nova solução: x ≡ {x} (mod {N})")

    # Resultado final
    print("\n" + "=" * 50)
    print("RESULTADO FINAL")
    print("=" * 50)

    print(f"\nSolução mínima: x = {x}")
    print(f"Módulo geral: N = {N}")

    print(f"\nSolução geral: x = {x} + t × {N}, com t ∈ ℤ.")

    # Verificação de todas as congruências
    print("\n=== VERIFICAÇÃO DAS CONGRUÊNCIAS ===")

    tudo_correto = True

    for a, n in zip(restos, modulos):

        resto_calculado = x % n
        resto_esperado = a % n

        correto = resto_calculado == resto_esperado

        print(
            f"{x} mod {n} = {resto_calculado}; "
            f"esperado {resto_esperado}: "
            f"{'OK' if correto else 'ERRO'}"
        )

        if not correto:
            tudo_correto = False

    if tudo_correto:
        print("\nTodas as congruências foram verificadas!")
    else:
        print("\nErro na verificação dos resultados.")


def main():
    while True:

        print("\n" + "=" * 58)
        print("ATIVIDADE 1 — CONGRUÊNCIA MODULAR E TCR")
        print("=" * 58)

        print("1 - Verificar congruência modular")
        print("2 - Resolver sistema pelo Teorema Chinês do Resto")
        print("0 - Sair")

        opcao = input("\nEscolha: ").strip()

        if opcao == "1":
            verificar_congruencia()

        elif opcao == "2":
            teorema_chines_resto()

        elif opcao == "0":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
