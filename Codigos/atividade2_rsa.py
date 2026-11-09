
# ATIVIDADE 2 — CRIPTOGRAFIA RSA
# Primalidade, construção de chaves, cifragem, decifragem
# e demonstrações dos Teoremas de Euler e Fermat.


def ler_inteiro(mensagem):
    """Lê um número inteiro e trata entradas inválidas."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: digite um número inteiro válido.")


def mdc(a, b):
    """Calcula o máximo divisor comum pelo algoritmo de Euclides."""
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a


def euclides_estendido(a, b):
    """
    Calcula:
        mdc(a, b)
        e os coeficientes x e y tais que:
        a*x + b*y = mdc(a, b)
    """
    if b == 0:
        return a, 1, 0

    divisor, x1, y1 = euclides_estendido(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return divisor, x, y


def eh_primo(numero):
    """Verifica se um número inteiro é primo."""
    if numero < 2:
        return False

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    divisor = 3

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False

        divisor += 2

    return True


def inverso_modular(a, modulo):
    """
    Calcula o inverso modular de a módulo modulo.

    O inverso existe quando:
        mdc(a, modulo) = 1
    """

    a = a % modulo

    divisor, x, _ = euclides_estendido(a, modulo)

    if divisor != 1:
        return None

    return x % modulo


def potencia_modular(base, expoente, modulo, mostrar=False):
    """
    Calcula:
        base^expoente mod modulo

    utilizando exponenciação rápida por quadrados sucessivos.
    """

    if modulo <= 0:
        raise ValueError("O módulo deve ser positivo.")

    if expoente < 0:
        raise ValueError("O expoente deve ser não negativo.")

    resultado = 1
    base = base % modulo
    passo = 1

    if mostrar:
        print(
            f"\nCalculando {base}^{expoente} mod {modulo}"
            " por quadrados sucessivos:"
        )

    while expoente > 0:

        if mostrar:
            print(
                f"Etapa {passo}: "
                f"resultado = {resultado}, "
                f"base = {base}, "
                f"expoente = {expoente}"
            )

        if expoente % 2 == 1:
            resultado = (resultado * base) % modulo

            if mostrar:
                print(
                    f"  Expoente ímpar → "
                    f"resultado = {resultado}"
                )

        base = (base * base) % modulo
        expoente //= 2
        passo += 1

    if mostrar:
        print(f"Resultado final = {resultado}")

    return resultado


def obter_primos():
    """Obtém os números primos p e q e calcula os parâmetros RSA."""

    print("\n=== PARTE A: PRIMALIDADE E PARÂMETROS RSA ===")

    while True:

        p = ler_inteiro("Digite o número primo p: ")
        q = ler_inteiro("Digite o número primo q: ")

        if p <= 1 or q <= 1:
            print("p e q devem ser maiores que 1.")

        elif p == q:
            print("p e q devem ser diferentes.")

        elif not eh_primo(p) or not eh_primo(q):
            print("p e q precisam ser números primos.")

        else:
            break

    # Cálculo de n
    n = p * q

    # Função totiente de Euler para p e q primos
    phi = (p - 1) * (q - 1)

    print("\n=== PARÂMETROS RSA ===")

    print(f"p = {p}")
    print(f"q = {q}")

    print(
        f"\nn = p × q"
        f"\nn = {p} × {q}"
        f"\nn = {n}"
    )

    print(
        f"\nφ(n) = (p - 1)(q - 1)"
        f"\nφ(n) = ({p} - 1) × ({q} - 1)"
        f"\nφ(n) = {phi}"
    )

    # Escolha do expoente público
    while True:

        e = ler_inteiro(
            f"\nEscolha o expoente público e "
            f"(1 < e < {phi}): "
        )

        if e <= 1 or e >= phi:
            print(
                f"e deve satisfazer "
                f"1 < e < {phi}."
            )

        elif mdc(e, phi) != 1:
            print(
                f"mdc({e}, {phi}) = "
                f"{mdc(e, phi)}."
            )
            print(
                "e e φ(n) precisam ser coprimos."
            )

        else:
            print(
                f"mdc({e}, {phi}) = 1."
            )
            print("Expoente público válido.")
            break

    print("\nParâmetros escolhidos:")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"n = {n}")
    print(f"φ(n) = {phi}")
    print(f"e = {e}")

    return p, q, n, phi, e


def construir_chaves(n, phi, e):
    """Constrói a chave pública e a chave privada."""

    print("\n=== PARTE B: CONSTRUÇÃO DAS CHAVES ===")

    # d é o inverso de e módulo phi
    d = inverso_modular(e, phi)

    if d is None:
        print(
            "Não foi possível calcular o inverso modular."
        )
        return None

    print(
        f"\nPrecisamos encontrar d tal que:"
        f"\n{e} × d ≡ 1 (mod {phi})"
    )

    print(
        f"\nValor encontrado:"
        f"\nd = {d}"
    )

    print(
        f"\nVerificação:"
        f"\n{e} × {d} = {e * d}"
    )

    print(
        f"{e * d} mod {phi} = "
        f"{(e * d) % phi}"
    )

    if (e * d) % phi == 1:
        print("Inverso modular confirmado!")
    else:
        print("Erro no cálculo do inverso modular.")
        return None

    print(
        f"\nChave pública: (e, n) = ({e}, {n})"
    )

    print(
        f"Chave privada: (d, n) = ({d}, {n})"
    )

    return d


def cifrar_decifrar(n, e, d):
    """Realiza a cifragem e a decifragem de uma mensagem numérica."""

    print("\n=== PARTE C: CIFRAGEM E DECIFRAGEM ===")

    while True:

        M = ler_inteiro(
            f"Digite o número inteiro M "
            f"(0 ≤ M < {n}): "
        )

        if 0 <= M < n:
            break

        print(
            f"Valor inválido."
            f"\nM deve estar entre 0 e {n - 1}."
        )

    print(f"\nMensagem original:")
    print(f"M = {M}")

    # Cifragem
    C = potencia_modular(
        M,
        e,
        n,
        mostrar=True
    )

    print(
        f"\n=== CIFRAGEM ==="
        f"\nC ≡ M^e (mod n)"
        f"\nC ≡ {M}^{e} (mod {n})"
        f"\nC = {C}"
    )

    # Decifragem
    M_linha = potencia_modular(
        C,
        d,
        n,
        mostrar=True
    )

    print(
        f"\n=== DECIFRAGEM ==="
        f"\nM' ≡ C^d (mod n)"
        f"\nM' ≡ {C}^{d} (mod {n})"
        f"\nM' = {M_linha}"
    )

    # Comparação
    print("\n=== RESULTADO ===")

    print(f"Mensagem original: {M}")
    print(f"Mensagem decifrada: {M_linha}")

    if M_linha == M:
        print(
            "\n✓ Decifragem correta!"
            "\nA mensagem original foi recuperada."
        )
    else:
        print(
            "\n✗ A decifragem não recuperou a mensagem."
        )


def demonstrar_euler_fermat():
    """Menu para demonstração dos Teoremas de Euler e Fermat."""

    while True:

        print("\n" + "=" * 58)
        print("PARTE D — TEOREMAS DE EULER E FERMAT")
        print("=" * 58)

        print("1 - Demonstrar Teorema de Euler")
        print("2 - Demonstrar Pequeno Teorema de Fermat")
        print("0 - Voltar")

        opcao = input("Escolha: ").strip()

        if opcao == "1":

            print("\n=== TEOREMA DE EULER ===")

            base = ler_inteiro(
                "Digite a base: "
            )

            modulo = ler_inteiro(
                "Digite o módulo n (> 1): "
            )

            while modulo <= 1:
                print("O módulo deve ser maior que 1.")

                modulo = ler_inteiro(
                    "Digite o módulo novamente: "
                )

            divisor = mdc(base, modulo)

            print(
                f"\nmdc({base}, {modulo}) = "
                f"{divisor}"
            )

            if divisor != 1:

                print(
                    "\nO Teorema de Euler não pode "
                    "ser aplicado diretamente."
                )

                print(
                    "A base e o módulo precisam ser coprimos."
                )

                expoente = ler_inteiro(
                    "\nDigite um expoente não negativo: "
                )

                while expoente < 0:
                    print(
                        "O expoente deve ser não negativo."
                    )

                    expoente = ler_inteiro(
                        "Digite novamente: "
                    )

                resultado = potencia_modular(
                    base,
                    expoente,
                    modulo,
                    mostrar=True
                )

                print(
                    f"\nResultado:"
                    f"\n{base}^{expoente} mod {modulo}"
                    f" = {resultado}"
                )

            else:

                # Calcula φ(n)
                phi_modulo = 0
                coprimos = []

                for candidato in range(1, modulo):

                    if mdc(candidato, modulo) == 1:
                        phi_modulo += 1
                        coprimos.append(candidato)

                print(
                    f"\nNúmeros de 1 até {modulo - 1}"
                    " coprimos com o módulo:"
                )

                print(coprimos)

                print(
                    f"\nφ({modulo}) = "
                    f"{phi_modulo}"
                )

                resultado = potencia_modular(
                    base,
                    phi_modulo,
                    modulo,
                    mostrar=True
                )

                print(
                    f"\nVerificação:"
                    f"\n{base}^{phi_modulo}"
                    f" mod {modulo} = {resultado}"
                )

                if resultado == 1:
                    print(
                        "\n✓ Teorema de Euler confirmado!"
                    )
                else:
                    print(
                        "\n✗ O resultado não foi 1."
                    )

        elif opcao == "2":

            print(
                "\n=== PEQUENO TEOREMA DE FERMAT ==="
            )

            primo = ler_inteiro(
                "Digite um número primo p: "
            )

            while not eh_primo(primo):

                print(
                    "O número informado não é primo."
                )

                primo = ler_inteiro(
                    "Digite outro número primo: "
                )

            a = ler_inteiro(
                f"Digite uma base a "
                f"que não seja divisível por {primo}: "
            )

            while a % primo == 0:

                print(
                    f"{a} é divisível por {primo}."
                )

                a = ler_inteiro(
                    "Digite outra base: "
                )

            print(
                f"\nPrimo escolhido: p = {primo}"
            )

            print(
                f"Base escolhida: a = {a}"
            )

            print(
                f"a mod p = "
                f"{a % primo}"
            )

            resultado = potencia_modular(
                a,
                primo - 1,
                primo,
                mostrar=True
            )

            print(
                f"\nVerificação de Fermat:"
                f"\n{a}^{primo - 1}"
                f" mod {primo} = {resultado}"
            )

            if resultado == 1:
                print(
                    "\n✓ Pequeno Teorema de Fermat confirmado!"
                )
            else:
                print(
                    "\n✗ O resultado não foi 1."
                )

            print(
                "\nObservação:"
                "\nO Pequeno Teorema de Fermat "
                "é aplicado quando o módulo é primo."
            )

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def main():

    # Obtém os parâmetros RSA
    p, q, n, phi, e = obter_primos()

    # Constrói a chave privada
    d = construir_chaves(
        n,
        phi,
        e
    )

    if d is None:
        return

    while True:

        print("\n" + "=" * 58)
        print("ATIVIDADE 2 — CRIPTOGRAFIA RSA")
        print("=" * 58)

        print("1 - Cifrar e decifrar um número")
        print("2 - Demonstrar Teoremas de Euler/Fermat")
        print("3 - Mostrar parâmetros e chaves")
        print("0 - Encerrar")

        opcao = input("Escolha: ").strip()

        if opcao == "1":

            cifrar_decifrar(
                n,
                e,
                d
            )

        elif opcao == "2":

            demonstrar_euler_fermat()

        elif opcao == "3":

            print("\n=== PARÂMETROS RSA ===")

            print(f"p = {p}")
            print(f"q = {q}")
            print(f"n = {n}")
            print(f"φ(n) = {phi}")
            print(f"e = {e}")
            print(f"d = {d}")

            print(
                f"\nChave pública: "
                f"({e}, {n})"
            )

            print(
                f"Chave privada: "
                f"({d}, {n})"
            )

        elif opcao == "0":

            print("\nPrograma encerrado.")
            break

        else:

            print(
                "\nOpção inválida."
            )


if __name__ == "__main__":
    main()