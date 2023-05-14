N: int; x: int; dentro: int = 0; fora: int = 0

N = int(input("Quantos numeros voce vai digitar? "))

for i in range(0, N):
    x = int(input("Digite um numero: "))
    
    if  x > 10 and x < 20:
        dentro = dentro + 1        
    elif x < 10 or x > 20:
        fora = fora + 1
        
print(f"{dentro} DENTRO")
print(f"{fora} FORA")
