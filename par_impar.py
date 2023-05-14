N: int; x: int

N = int(input("Quantos numeros voce vai digitar? "))

for i in range(0, N):
    x = int(input("Digite um numero: "))
    
    if x == 0:
        print("NULO")
    else:
        if x % 2 == 0:
            print("PAR ", end="")
        else:
            print("IMPAR ", end="")
        
        if x < 0:
            print("NEGATIVO")
        else:
            print("POSITIVO")