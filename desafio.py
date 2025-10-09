### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

try:
 nome = input('Informe seu nome: ')

 if nome.isdigit():
   print('Voçê digitou seu nome errado.')
 elif len(nome) == 0:
   print('Voçê não digitou nada')
 elif nome.isspace():
   print('Voçê digitou só espaço.')
except ValueError as e:
  print(e)
  exit()

try:
 salario = float(input('Informe seu salário: '))

 if salario < 0:
    print('Por favor digite um valor positivo para o salário.')
except ValueError:
  print('Entrada inválida para o salário. Por favor digite um número.')
  exit()

try:
 bonus = float(input('informe o valor do bônus recebido: '))

 if salario < 0:
    print('Por favor digite um valor positivo para o bônus.')
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()
    
comissao = salario + (salario * bonus)

print(f'\nNome: {nome}\nSalario: R$  {salario:.2f}\nNovo salário com bônus: R$ {comissao:.2f}')
