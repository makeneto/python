x: int; resultado = int; i: int

x = int(
    input("Deseja a tabuada para qual valor? ")
)

for i in range(1, 11):
    resultado = x * i
    print(f"{x} x {i} = {resultado}")
    