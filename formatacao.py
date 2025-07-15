nome = 'alice'
altura = 1.68
peso = 100
idade = 1.68
IMC = peso / altura **2

print(nome, "possui", altura, 'm', 'pesa', peso, 'kg', 'e seu IMIC é: ',IMC)

# F-string
#quando for imprimir variavel precisa de chave{} 
#quando quiser menos casas decimais colocar o .2F por exemplo
print(f'{nome} tem {altura}m e pesa {peso}k\nE seu IMC é: {IMC:.1f}')

