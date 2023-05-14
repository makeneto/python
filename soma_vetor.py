n: int; soma: float = 0; media: float

n = int(input("Quantos numeros voce vai digitar? "))

vetor: [float] = [0 for x in range(n)]

for i in range(0, n):
    vetor[i] = float(input("Digite um numero: "))
    soma = soma + vetor[i]

print()
print("VALORES = ", end="")

for i in range(0, n):
    print(f"{vetor[i]} " , end="")
 
media = soma /n   
print()
print(f"SOMA = {soma:.2f}")
print(f"MEDIA = {media:.2f}")