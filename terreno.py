largura: float; comprimento: float; metroQ: float; area: float; preco: float

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite a comprimento do terreno: "))
metroQ = float(input("Digite a valor do metro quadrado: "))

area = largura * comprimento
preco = area * metroQ

print(f"Area do terreno = {area:.2f}")
print(f"Preco do terreno = {preco:.2f}")