# Sistema escola

alunos = []
medias = []
pergunta = input('Deseja acessar?').lower()
while pergunta == 'sim':
    
    for i in range(3):
        senha = input('SENHA: ')
        if senha == '123':
            print('SISTEMA DE NOTAS...')
            pergunta = input('Deseja continuar?')
            nome = input('Aluno: ')
            nota1 = float(input('Nota Matematica: '))
            nota2 = float(input('Nota portugues: '))
            nota3 = float(input('Nota ingles: '))
            media = (nota1+nota2+nota3) / 3
            print('média', media, 'Aluno(a):', nome)
            alunos.append(nome)
            medias.append(media)
            pergunta = input('Deseja continuar?')
            if pergunta != 'sim':
                print('lista de alunos')
                print(alunos)
                print('médias')
                print(medias)
                print('***' * 8)
                print('MÈDIA DA SALA: ', sum(medias)/len(medias))
                print('***' * 8)
                
        else:
            print('Senha incorreta')
    else:
            print('Senha bloqueada')
            break
        
else:
    print('Até logo...')