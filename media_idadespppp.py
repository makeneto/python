x: int; soma: int = 0; count: int = 0
media: float

print("Digite as idades:")
x = int(input())

if x < 0:
    print("IMPOSSIVEL CALCULAR")
else:
    while x > 0:
        x = int(input())
        soma = soma + x
        count = count + 1
    
media = soma / count

print(f"MEDIA = {media:.2f}")