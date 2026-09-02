# ============================================================
# PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA - PARTE 1
# ATIVIDADE 2 - DIVISIBILIDADE, MDC E MMC
# ============================================================

# ---------------------- CABEÇALHO ---------------------------

nome = input("Augusto Corrêa Silva ")
matricula = input("2612082020 ")
turno = input("Matutino ")

disciplina = "Estruturas Matemáticas para Computação"

print("\n============================================================")
print("          ATIVIDADE 2 - DIVISIBILIDADE, MDC E MMC")
print("============================================================")
print("Nome: Augusto")
print("Matrícula: 2612082020")
print("Disciplina: Matemática Discreta")
print("Turno: Matutino")
print("============================================================")


# -------------------- ENTRADA DOS NÚMEROS -------------------

print("\nDigite dois números inteiros positivos.")

while True:
    numero1 = int(input("Digite o primeiro número: "))

    if numero1 > 0:
        break
    else:
        print("Erro! O número deve ser positivo.")


while True:
    numero2 = int(input("Digite o segundo número: "))

    if numero2 > 0:
        break
    else:
        print("Erro! O número deve ser positivo.")


# ============================================================
# 1. DIVISÃO INTEIRA (DIV)
# ============================================================

div = numero1 // numero2


# ============================================================
# 2. RESTO DA DIVISÃO (MOD)
# ============================================================

mod = numero1 % numero2


# ============================================================
# 3. ALGORITMO DE EUCLIDES
# ============================================================

print("\n============================================================")
print("              ALGORITMO DE EUCLIDES")
print("============================================================")

a = numero1
b = numero2

while b != 0:

    resto = a % b

    print(a, "=", b, "x", a // b, "+", resto)

    a = b
    b = resto


# O último valor diferente de zero é o MDC.
mdc = a


# ============================================================
# 4. MDC
# ============================================================

print("\n============================================================")
print("                         MDC")
print("============================================================")

print("MDC(", numero1, ",", numero2, ") =", mdc)


# ============================================================
# 5. MMC
# ============================================================

mmc = (numero1 * numero2) // mdc

print("\n============================================================")
print("                         MMC")
print("============================================================")

print("MMC(", numero1, ",", numero2, ") =", mmc)


# ============================================================
# RESULTADOS DA DIVISIBILIDADE
# ============================================================

print("\n============================================================")
print("                    DIVISIBILIDADE")
print("============================================================")

print("\nPrimeiro número:", numero1)
print("Segundo número:", numero2)

print("\nDivisão inteira (DIV):")
print(numero1, "DIV", numero2, "=", div)

print("\nResto da divisão (MOD):")
print(numero1, "MOD", numero2, "=", mod)


if mod == 0:
    print("\n", numero1, "é divisível por", numero2)
else:
    print("\n", numero1, "não é divisível por", numero2)


if numero1 % numero2 == 0:
    print(numero2, "é divisor de", numero1)
else:
    print(numero2, "não é divisor de", numero1)


# ============================================================
# RESULTADO FINAL
# ============================================================

print("\n============================================================")
print("                    RESULTADO FINAL")
print("============================================================")

print("Números:", numero1, "e", numero2)
print("DIV =", div)
print("MOD =", mod)
print("MDC =", mdc)
print("MMC =", mmc)

print("\n============================================================")
print("                 FIM DA ATIVIDADE 2")
print("="*20)