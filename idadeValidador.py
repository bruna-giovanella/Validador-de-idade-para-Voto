
#Verificador se a age do usuário se encaixa como a de um eleitor

from datetime import date

def validatorData(birth_date):
    c = 0
    c1 = 0
    for i in birth_date:
        if i in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            c += 1
        if i in '/':
            c1 += 1
    if (c == 8 and len(birth_date) == 10 and c1 == 2) or (c == 7 and len(birth_date) == 9 and c1 == 2) or (c == 6 and len(birth_date) == 8 and c1 == 2):
        birth(birth_date)
    else:
        print('Data informada é inválida\nInforme sua data de nascimento no formato dd/mm/aaaa')
        birth_date = input('Nova data: ')
        validatorData(birth_date)


def birth(birth_date):
    birth_date = birth_date.split('/')
    birth_year = [year for year in birth_date if len(year) == 4]
    birth_year = int(birth_year[0])
    age(birth_year)


def age(birth_year):
    year = int(date.today().year)
    age = year - birth_year

    if age >= 18 and age <= 70:
        print('Você está apto a participar das eleições!\nSeu voto é obrigatório.')
    elif age >= 16 or age > 70:
        print('Você está apto a participar das eleições!\nMas seu voto não é obrigatório.')
    else:
        print('Você não está apto a participar das eleições.')



print('Informe sua data de nascimento no formato dd/mm/aaaa')
birth_date = input('data: ')

validatorData(birth_date)

