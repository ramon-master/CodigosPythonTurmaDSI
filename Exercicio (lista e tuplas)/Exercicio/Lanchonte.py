cardapio = {
    "salgado", 4.90,
    "suco", 3.00,
    "refrigerente", 4.00,
    "hambuguer", 7.20,
    "Doce", 2.00,

    }

print("="*40)
print(f"{'lanchonete':^40}")
print("="*40)

for chave, valor in cardapio.items():
    print(f"{chave:.<30}R${valor:>5}")
print("="*40)