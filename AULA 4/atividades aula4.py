#Atividade 1 - Verificação de numero positivo
#Escreva um programa em python que solicite ao usuario um numero inteiro e verifique se o número é positivo, negativo ou zero.
#Em seguida, exiba uma mensagem apropriada de acordo com o resultado da verificação.

numero = int(input('Digite um numero: '))
if numero > 0:
    print('numero positivo')
elif numero == 0:
    print ('numero 0')
elif numero < 0:
    print ('numero negativo')
print()

#Atividade 2 - Classificação de triangulos
#Escreva um programa em Python que receba tres comprimentos de lados de um triangulo e determine se o triangulo é equilátero, isóseles ou escaleno.

lado1 = int(input('Digite o primeiro lado do seu triangulo: '))
lado2 = int(input('Digite o segundo lado do seu triangulo: ' ))
lado3 = int(input('Digite o terceiro lado do seu tringulo: '))
    
if lado1 == lado2 == lado3:
    print('O seu triangulo é equilátero')
elif lado1 == lado2 != lado3:
    print('O seu triangulo é isóseles')
elif lado1 != lado2 == lado3:
    print('O seu triangulo é isóseles')
elif lado1 != lado2 != lado3:
    print('O seu triangulo é escaleno')

print()



#Atividade 3
#Verifique se o usuario é maior de idade e pode entrar no show, escreva um programa que peça a idade e decida se ele pode entrar no show.

idade = int(input('Digite sua idade: '))
if idade >= 16:
    print('Acesso liberado')
else:
    print('Acesso negado! Somente maiores de 16 anos')