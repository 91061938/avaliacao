senha_correta = "Proz@2023"
tentativas = 0 

while tentativas < 3:
    senha_digitada = input ("usuario, digite a senha")
    if senha_digitada == senha_correta:
        print("Acesso liberado!")
        break
    elif tentativas == 2:
        print("conta bloqueada:")
        break
    else:
        print("\nSenha incorreta!")
        tentativas = tentativas + 1