def calcular_preco_final(preco_produto):
    imposto = 0.12
    preco_com_imposto = preco_produto + (preco_produto * imposto)
    return preco_com_imposto

preco_produto = float(input("Digite o preço do produto: R$ "))

preco_final = calcular_preco_final(preco_produto)

print(f"O preço final do produto com imposto é: R$ {preco_final:.2f}")