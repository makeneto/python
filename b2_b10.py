x: int; n: int; operacao = int; soma: int = 0

n = int(input("Quantos numeros serao digitados: "))

for i in range(0, n):
    x = int(input())
    operacao = (2 ** i) * x
    soma = soma + operacao
  
print()  
print(f"Resultado = {soma}")
print()

