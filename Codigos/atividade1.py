# ============================================================
# PORTFÓLIO DE PROGRAMAÇÃO MATEMÁTICA - PARTE 1
# ATIVIDADE 1 - TEORIA DOS CONJUNTOS
# ============================================================

# ---------------------- CABEÇALHO ---------------------------

nome = input("Augusto Corrêa Silva ")
matricula = input("2612082020")
turno = input("Matutino ")

disciplina = "Estruturas Matemáticas para Computação"

print("\n============================================================")
print("             ATIVIDADE 1 - TEORIA DOS CONJUNTOS")
print("============================================================")
print("Nome: Augusto")
print("Matrícula: 2612082020")
print("Disciplina: Matemática Discreta")
print("Turno: Matutino")
print("============================================================")


# -------------------- ENTRADA DOS CONJUNTOS -----------------

print("\nDigite os elementos dos conjuntos separados por espaço.")
print("Exemplo: 1 2 3 4 5")

entrada_a = input("Digite os elementos do conjunto A: ")
entrada_b = input("Digite os elementos do conjunto B: ")

A = set()

for valor in entrada_a.split():
    A.add(int(valor))

B = set()

for valor in entrada_b.split():
    B.add(int(valor))


# ------------------------- UNIÃO ----------------------------

uniao = A | B


# ---------------------- INTERSEÇÃO ---------------------------

intersecao = A & B


# ---------------------- DIFERENÇAS ---------------------------

diferenca_A_B = A - B
diferenca_B_A = B - A


# --------------------- CARDINALIDADES ------------------------

card_A = len(A)
card_B = len(B)
card_uniao = len(uniao)
card_intersecao = len(intersecao)


# --------------------- CONJUNTO DAS PARTES -------------------

def conjunto_das_partes(conjunto):
    partes = [set()]

    for elemento in conjunto:
        novas_partes = []

        for subconjunto in partes:
            novo_subconjunto = subconjunto.copy()
            novo_subconjunto.add(elemento)
            novas_partes.append(novo_subconjunto)

        partes = partes + novas_partes

    return partes


partes_A = conjunto_das_partes(A)
partes_B = conjunto_das_partes(B)


# ----------------------- PARTIÇÃO ----------------------------

pares_A = set()
impares_A = set()

for elemento in A:
    if elemento % 2 == 0:
        pares_A.add(elemento)
    else:
        impares_A.add(elemento)


# ------------------- PRODUTO CARTESIANO ----------------------

produto_cartesiano = []

for elemento_A in A:
    for elemento_B in B:
        produto_cartesiano.append((elemento_A, elemento_B))


# ---------------------- INCLUSÃO -----------------------------

A_esta_contido_em_B = A <= B
B_esta_contido_em_A = B <= A


# ============================================================
#                         RESULTADOS
# ============================================================

print("\n\n============================================================")
print("                       RESULTADOS")
print("============================================================")

print("\nConjunto A:", A)
print("Conjunto B:", B)

print("\n1. UNIÃO")
print("A ∪ B =", uniao)

print("\n2. INTERSEÇÃO")
print("A ∩ B =", intersecao)

print("\n3. DIFERENÇAS")
print("A - B =", diferenca_A_B)
print("B - A =", diferenca_B_A)

print("\n4. CARDINALIDADES")
print("|A| =", card_A)
print("|B| =", card_B)
print("|A ∪ B| =", card_uniao)
print("|A ∩ B| =", card_intersecao)

print("\n5. CONJUNTO DAS PARTES DE A")
print("P(A) = {")

for subconjunto in partes_A:
    print("  ", subconjunto)

print("}")

print("\nConjunto das partes de B")
print("P(B) = {")

for subconjunto in partes_B:
    print("  ", subconjunto)

print("}")

print("\n6. CARDINALIDADE DOS CONJUNTOS DAS PARTES")
print("|P(A)| =", len(partes_A))
print("|P(B)| =", len(partes_B))

print("\n7. EXEMPLO DE PARTIÇÃO DO CONJUNTO A")

print("Parte dos elementos pares:", pares_A)
print("Parte dos elementos ímpares:", impares_A)

print("A partição é formada por:")
print("{", pares_A, ",", impares_A, "}")


print("\n8. PRODUTO CARTESIANO A × B")
print("A × B = {")

for par in produto_cartesiano:
    print("  ", par)

print("}")


print("\n9. RELAÇÃO DE INCLUSÃO")

if A_esta_contido_em_B:
    print("A está contido em B: A ⊆ B")
else:
    print("A NÃO está contido em B: A ⊄ B")

if B_esta_contido_em_A:
    print("B está contido em A: B ⊆ A")
else:
    print("B NÃO está contido em A: B ⊄ A")


print("\n============================================================")
print("                 FIM DA ATIVIDADE 1")
print("============================================================")