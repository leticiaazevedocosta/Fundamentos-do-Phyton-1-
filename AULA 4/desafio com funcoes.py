# desafio
# crie uma função de cadastro
# precisa cadastrar 2 ou mais pessoas
# e-mail, nome, idade



   
def novo_cadastro():
    pessoas_cadastradas = ['Helena', 'Davi', 'Joana', 'Marcos']
    pergunta = input('Deseja acessar o sistema?: ')
    while pergunta == 'sim':
        
         nome = input('Digite seu nome: ')
         idade = int(input('Digite sua idade: '))
         email = input('Digite seu email: ')
         pessoas_cadastradas += (nome,)
         print(pessoas_cadastradas)
         pergunta = input('Deseja continuar acessando o sistema?: ').lower
        
    else:
         print('Encerrando atendimento')
         
              
              
              
novo_cadastro()