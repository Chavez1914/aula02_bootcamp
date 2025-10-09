# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))
# soma = n1 + n2
# print(f'A soma  de {n1} + {n2} é = {soma}')

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# n1 = int(input('Informe um número: '))
# resto_divisao = n1 % 5
# print(f'o resto da divisão de {n1} por 5 é: {resto_divisao}')


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# n1 = int(input('Informe um número: '))
# n2 = int(input('Informe outro número: '))
# divisao = n1 * n2
# print(f'O resultado de {n1} x {n2} = {divisao} ')

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# n1 = int(input('Informe um número: '))
# n2 =int(input('Informe ouro número: '))
# divisao = n1 // n2
# print(f'O resultado da divisão inteira de {n1} / {n2} = {divisao}')

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# n1 = int(input('Digite um número: '))
# raiz = n1 ** 2
# print(f'A raiz qudrada de {n1} é:{raiz}')


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

#nf1 = float(input('Digite um número com decimal: '))
#nf2 = float(input('Digite outro número: '))
#soma = nf2 + nf1
# print(f'A soma de {nf1} + {nf2} = {soma}')

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

#nf1 = float(input('Digite um número com decimal: '))
#nf2 = float(input('Digite outro número: '))

#media = float(nf1 + nf2)/2
#print(f'A média dos números fornecidos é: {media:.2f}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

#base = float(input('Digite um número para calcular sua potência: '))
#expoente = float(input('Digite outro número: '))
#potencia = base ** expoente
#print(f'O resultado da potência é: {potencia:.1f}')

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

#celsius = float(input('Digite a temperatura da sua cidade em: '))
#fahrenheit = (celsius * 9/5) + 32
#print(f"{celsius}°C é igual a {fahrenheit}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

#raio = float(input("Digite o raio do círculo: "))
#area = 3.14159 * raio ** 2
#print(f"A área do círculo é: {area:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

#frase = input('Escrva uma frase: ')
#print(frase.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

#nome = input('Escreva seu nome completo: ')
#print(nome.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

#frase = input('Escreva uma frase: ')
#print(frase.strip())

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

#data = input('Digite a data de hoje no format dd/mm/aaaa: ')
#data_formatada = data.split('/')
#print(f'Dia: {data_formatada[0]}')
#print(f'Mês: {data_formatada[1]}')
#print(f'Ano: {data_formatada[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

#nome = input('Informe se primeiro nome: ')
#sobre_nome = input('Informe seu sobre nome: ')
#nome_completo = nome + sobre_nome
#print(f'Nome completo: {nome_completo}')

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

#valor1 = True
#valor2 = False
#resultado_and = valor1 and valor2
#print(f"Resultado do AND lógico:, {resultado_and}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

#valor1 = True
#valor2 = False
#resultado_or = valor1 or valor2
#print("Resultado do OR lógico:", resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

#valor1 = True
#valor2 = False
#resultado_not = not valor1
#print("Resultado do NOT lógico:", resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

#n1 = int(input('Informe um número: '))
#n2 = int(input('Informe outro número: '))
#resultado = n1 == n2
#print(f'Resultado de igualdade: {resultado}')

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

#n1 = int(input('Informe um número: '))
#n2 = int(input('Informe outro número: '))
#resultado = n1 != n2
#print(f'Resultado de diferença: {resultado}')

# #### try-except e if

# 21: Conversor de Temperatura

#try:
#    celsius = float(input("Digite a temperatura em Celsius: "))
#    fahrenheit = (celsius * 9/5) + 32
#    print(f"{celsius}°C é igual a {fahrenheit}°F.")
#except ValueError:
#    print("Por favor, digite um número válido para a temperatura.")

# 22: Verificador de Palíndromo

#entrada = input("Digite uma palavra ou frase: ")
#if isinstance(entrada, str):
 #   formatado = entrada.replace(" ", "").lower()
  #  if formatado == formatado[::-1]:
   #     print("É um palíndromo.")
    #else:
     #   print("Não é um palíndromo.")
#else:
 #   print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# 23: Calculadora Simples
try:
   num1 = float(input('Digite um número: '))
   num2 = float(input('Digite mais um número: '))
   operador = input('Escolha um operador: (+, -, *, /): ')
   if operador == '+':
      resultado = num1 + num2
   elif operador =='-':
      resultado = num1 - num2
   elif operador == '*':
      resultado = num1 * num2
   elif operador == '/':
      resultado = num1 / num2
   else:
      print('Operador invalido ou divisão por zero.')
   print('resultado: ', resultado )
except ValueError:
    print('Erro: Entrada inválida. certifique-se de inserir números.')

# 24: Classificador de Números

try:
   num = int(input('Digite um número: '))
   if num > 0:
      print('Positivo')
   elif num < 0:
      print('Negativo')
   else:
      print('Zero')
   if num % 2 == 0:
      print('Par')
   else:
      print('Impar')
except ValueError:
   print('Por favor, digite um número inteiro válido.')

# 25: Conversão de Tipo com Validação