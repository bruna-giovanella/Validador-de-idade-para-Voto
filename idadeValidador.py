#Verificador se a idade do usuário se encaixa como a de um eleitor

from datetime import date

def validadorData(data_nascimento):
    c = 0
    c1 = 0
    for i in data_nascimento:
        if i in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            c += 1
        if i in '/':
            c1 += 1
    if (c == 8 and len(data_nascimento) == 10 and c1 == 2) or (c == 7 and len(data_nascimento) == 9 and c1 == 2) or (c == 6 and len(data_nascimento) == 8 and c1 == 2):
        nascimento(data_nascimento)
    else:
        print('Data informada é inválida\nInforme sua data de nascimento no formato dd/mm/aaaa')
        data_nascimento = input('Nova data: ')
        validadorData(data_nascimento)


def nascimento(data_nascimento):
    data_nascimento = data_nascimento.split('/')
    ano_nascimento = [year for year in data_nascimento if len(year) == 4]
    ano_nascimento = int(ano_nascimento[0])
    idade(ano_nascimento)


def idade(ano_nascimento):
    ano = int(date.today().year)
    idade = ano - ano_nascimento
    
    if idade >= 18 and idade <= 70:
        print('Você está apto a participar das eleições!\nSeu voto é obrigatório.')
    elif idade >= 16 or idade > 70:
        print('Você está apto a participar das eleições!\nMas seu voto não é obrigatório.')
    else:
        print('Você não está apto a participar das eleições.')



print('Informe sua data de nascimento no formato dd/mm/aaaa')
data_nascimento = input('data: ')

validadorData(data_nascimento)

