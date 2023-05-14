N: int; a: float; b: float; c: float
media: float

N = int(input("Quantos casos voce vai digitar? "))

for i in range(0, N):
    print("Digite tres numeros: ")
    a = float(input())
    b = float(input())
    c = float(input())
    
    media = (a + b + c) / 3
    print(f"MEDIA = {media:.1f}")
    
