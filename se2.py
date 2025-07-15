entrada = input('Voce quer[entrar ou sair]?')
entrada = entrada.lower()
print(entrada)
if entrada == 'entrar':
    print('Seja bem-vindo!')
elif entrada == 'sair':
    print('Até mais')
else:
    print('Você errou')