# ordenar_bois.py
# 🐂 Ordenador de Bois da Fazenda - Projeto simples em Python
# Autor: Seu Nome
# Licença: MIT

# --- Entrada de dados ---
print("🐂 Bem-vindo ao Ordenador de Bois da Fazenda Rio Claro!\n")

bois = []

# Lê nome e peso de 3 bois
for i in range(1, 4):
    nome = input(f"Nome do boi {i}: ")
    peso = float(input(f"Peso de {nome} (kg, use ponto, ex.: 485.7): "))
    bois.append((nome, peso))  # armazena como tupla (nome, peso)

# --- Processamento: ordenação decrescente pelo peso ---
bois_ordenados = sorted(bois, key=lambda x: x[1], reverse=True)

# --- Saída formatada ---
print("\n=== Ranking (mais pesado → mais leve) ===")
for posicao, (nome, peso) in enumerate(bois_ordenados, start=1):
    print(f"{posicao}) {nome} — {peso:.2f} kg")

