n: int; x:int; soma: int = 0; operacao: int

n = int(input("Digite a quantidade de numeros: "))

for i in range(0, n):
    x = int(input())
    
    operacao = (8 ** i) * x
    soma = soma + operacao
    
print()
print(f"RESULTADO {soma}")