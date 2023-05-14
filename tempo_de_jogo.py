Hora_inicial: int; Hora_final: int; duracao: int

Hora_inicial = int(input("Hora inicial: "))
Hora_final = int(input("Hora final: "))

if Hora_final > Hora_inicial:
    duracao = Hora_final - Hora_inicial
else:
    duracao = 24 - (Hora_inicial - Hora_final)
    
print(f"O JOGO DUROU {duracao} HORA(S)")