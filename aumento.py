salario_antigo: float; novo_salario: float; aumento: float; porcentual: float


salario_antigo = float(input("Digite o salario da pessoa: "))

if salario_antigo <= 1000.00:
    porcentual = 20
    aumento = salario_antigo * porcentual / 100
    novo_salario = novo_salario + aumento
elif salario_antigo <= 3000.00:
    porcentual = 15
    aumento = salario_antigo * porcentual / 100
    novo_salario = novo_salario + aumento
elif salario_antigo <= 8000.00:
    porcentual = 10
    aumento = salario_antigo * porcentual / 100
    novo_salario = novo_salario + aumento
else:
    porcentual = 5
    aumento = salario_antigo * porcentual / 100
    novo_salario = novo_salario + aumento


print(f"Novo salario = {novo_salario}")
print(f"Aumento = {aumento}")
print(f"Porcentual = {porcentual} %")