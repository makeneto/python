n1: float; n2: float; nota_final: float
soma: int = 0

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

soma = n1 + n2

print(f"NOTA FINAL = {soma:.1f}")

if soma < 60.00:
    print("REPROVADO")