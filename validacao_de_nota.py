n1: float
n2: float
media: float

n1 = float(input("Digite a primeira nota: "))

while n1 < 0 or n1 > 10:
    n1 = float(input("Valor invalido! Tente novamente: "))
    

n2 = float(input("Digite a segunda nota: "))
while n2 < 0 or n2 > 10:
    n2 = float(input("Valor invalido! Tente novamente: "))

media = (n1 + n2) / 2

print(f"MEDIA = {media:.2f}")