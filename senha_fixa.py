senha: int

senha = int(input("Digite a senha: "))

while senha != 2002200:
    senha = int(input("Senha Invalida! Tente novamente: "))
    
print("Acesso permitido!")