dardo1: float; dardo2: float; dardo3: float; maior: float = 0;

print("Digite as tres distancias:")
dardo1 = float(input())
dardo2 = float(input())
dardo3 = float(input())

if dardo1 > dardo2 and dardo1 > dardo3:
    maior = dardo1
elif dardo2 > dardo1 and dardo2 > dardo3:
    maior = dardo2
else:
    maior = dardo3
print(f"MAIOR DISTANCIA = {maior}")