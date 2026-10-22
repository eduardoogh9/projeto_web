"""print("ola, eduardo")
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
altura = float(input("digite sua altura: "))

print("########dados de cadastro########")
print()
print(f"nome completo: {nome}")
print(f"sua idade: {idade}")
print(f"sua altura: {altura}")"""


produto =input("digite o nome do produto: ")
preco = float(input("digite o preço do produto: "))

desconto = preco * 0.10
preco_final = preco - desconto
print("/n----RESUMO DA COMPRA----")

print(f"produto: {produto}")
print(f"preço original: R$ {preco:.2f}")
print(f"desconto: R$ {desconto:.2f}")
print(f"preço final a pagar: R$ {preco_final:.2f}")
