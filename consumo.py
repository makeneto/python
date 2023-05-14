distancia: int
combustivel: float; consumo_medio: float

distancia = int(input("Distancia percorrida: "))
combustivel = float(input("Combustivel gasto: "))

consumo_medio = distancia / combustivel

print(f"Consumo medio = {consumo_medio:.3f}")