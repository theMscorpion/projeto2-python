import random
dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']
registro = [['braço', 100, 150, 'segunda'], ['perna', 100, 100, 'terça'], ['braço', 100, 150, 'quarta']]
dia = [] 


#def grafico_de_barras():
 #   if 

def cadastro_de_exercícios():
    registro_especifico = []
    nome_exercício = str(input('Digite o nome do exercício realizado: '))
    tempo_minutos = int(input('Digite o tempo gasto em minutos durante o exercício: '))
    gasto_calórico = int(input('Digite o gasto calórico do exercício em kilo calorias: '))
    dia_semana = str(input('Digite o dia da semana em que você realizou o exercicío: ')).lower()

    while dia_semana not in dias:
        print('Dia da semana inválido. Por favor, insira um dia válido.')
        print('Utilize: segunda, terça, quarta, quinta, sexta, sábado ou domingo.')
        dia_semana = str(input('Digite o dia da semana em que você realizou o exercicío: ')).lower()

    registro_especifico.append(nome_exercício)
    registro_especifico.append(tempo_minutos)
    registro_especifico.append(gasto_calórico)
    registro_especifico.append(dia_semana)

    registro.append(registro_especifico)

    print('Cadastro Concluído!')
    print(registro)
   



def relatório_diário():
    tempo_total = 0
    calorias_total = 0
    encontrou = False

    dia_escolhido = str(input('Informe o dia do relatório que você deseja obter: ')).lower()
    
    while dia_escolhido not in dias:
        print('Dia da semana inválido. Por favor, insira um dia válido.')
        print('Utilize: segunda, terça, quarta, quinta, sexta, sábado ou domingo.')
        dia_escolhido = str(input('Digite o dia da semana em que você realizou o exercicío: ')).lower()


    if not encontrou:
        print('Nenhum exercício encontrado para o dia informado.')
        print('Cadastre um exercício selecionando a opção 1 do menu.')
    else:
        if dia_escolhido in ['sábado','domingo']:
            print(f'No {dia_escolhido}, você treinou por {tempo_total} minutos e gastou {calorias_total} calorias.')
        else:
            print(f'Na {dia_escolhido}-feira, você treinou por {tempo_total} minutos e gastou {calorias_total} calorias.')
        
def calcular_imc ():
    peso = float(input('Digite seu peso em Kg: '))
    altura = float(input('Digite sua altura em metros: '))
    imc = peso/altura**2

    if imc < 18.5:
        print('Você está abaixo do peso ideal!')
    elif imc < 25:
        print('Você está com o peso adequado!')
    elif imc < 30:
        print('Você está sobrepeso!')
    else:
        print('Você está obeso!')

def meta_semanal():
    meta = int(input('Digite sua meta semanal de calorias: '))
    calorias_total = 0
    for i in range(len(calorias)):
        calorias_total += calorias[i]
    if calorias_total >= meta:
        print(f'Parabéns! Você atingiu sua meta semanal de {meta} calorias!')
    else:
        print(f'Você não atingiu sua meta semanal de {meta} calorias. Você consumiu apenas {calorias_total} calorias.')
    
def frases_motivacionais():
    frases_motivacionais = ['Hoje é um novo dia, bora pra luta!','Só você pode fazer acontecer!','Você não precisa ser o melhor, só precisa ser melhor do que ontem','Desistir não é uma opção','Bora tirar o monstro da jaula!','Deixa de ser frango e vai treinar!']
    print(random.choice(frases_motivacionais))

def média_calorias():
    registro_de_calorias = []
    registro_de_tempo = []
    nome_dos_exercicios = []
    calorias = 0
    tempo = 0
    media_de_calorias = 0

    def valor_em_lista(x, lista):
        for i in lista:
            if x == i:
                return False
        return True

    if len(registro) == 0:
        print('Nenhum exercício cadastrado.')
        print('Cadastre um exercício selecionando a opção 1 do menu.')
    else:
        for sublista in range(len(registro)):
            nome_do_exercicio = registro[sublista][0]

            if valor_em_lista(nome_do_exercicio, nome_dos_exercicios):
                soma_da_caloria = 0
                soma_do_tempo = 0

                for i in range(len(registro)):
                    if registro[i][0] == nome_do_exercicio:
                        caloria = int(registro[i][2])
                        tempo = int(registro[i][1])
                        soma_da_caloria += caloria
                        soma_do_tempo += tempo

                nome_dos_exercicios.append(nome_do_exercicio)
                registro_de_calorias.append(soma_da_caloria)
                registro_de_tempo.append(soma_do_tempo)
    for i in range(len(nome_dos_exercicios)):
        calorias = registro_de_calorias[i]
        nome_do_exercicio_e = nome_dos_exercicios[i]
        tempo = registro_de_tempo[i]
        media_de_calorias= calorias / tempo
        print(f"O media de calorias gasta pelo exercicio {nome_do_exercicio_e} foi de {media_de_calorias}K calorias")

               
def valor_em_lista(x, lista):
    for i in lista:
        if x == i:
            return False
    return True            

    
            
 
def gráfico_de_calorias():
    registro_de_calorias = []
    registro_de_tempo = []
    nome_dos_exercicios = []

    if len(registro) == 0:
        print('Nenhum exercício cadastrado.')
        print('Cadastre um exercício selecionando a opção 1 do menu.')
    else:
        for sublista in range(len(registro)):
            nome_do_exercicio = registro[sublista][0]

            if valor_em_lista(nome_do_exercicio, nome_dos_exercicios):
                soma_da_caloria = 0

                for i in range(len(registro)):
                    if registro[i][0] == nome_do_exercicio:
                        caloria = int(registro[i][2])
                        soma_da_caloria += caloria

                nome_dos_exercicios.append(nome_do_exercicio)
                registro_de_calorias.append(soma_da_caloria)

        print("---------------------------------------------Gráfico de calorias------------------------------------------------------------")
        print("        0----------------------250-------------------------500-----------------------750--------------------1000")

        for i in range(len(nome_dos_exercicios)):
            nome = nome_dos_exercicios[i]
            calorias = registro_de_calorias[i]

            traços = int((calorias / 1000) * 100)
            barra = '-' * traços
            print(f"{nome:<5} | {barra} {calorias}Kcal")






def menu():
    print('''---------------MENU---------------
[1] Cadastro de Exercícios
[2] Relatório Diário
[3] Calculo de IMC
[4] Meta Semanal
[5] Frases Motivacionais
[6] Média de Calorias por Exercício
[7] Código de barras no terminal
[0] Encerrar Programa''')
    
    return int(input('Selecione uma opção: '))

opção = 1

while opção != 0:
    opção = menu()
    if opção == 1:
        cadastro_de_exercícios()
    if opção == 2:
        relatório_diário()
    if opção == 3:
        calcular_imc()
    if opção == 4:
        meta_semanal()
    if opção == 5:
        frases_motivacionais()
    if opção == 6:
        média_calorias()
    if opção == 7:
        gráfico_de_calorias()
    if opção <0 or opção > 7:
        print('Opção inválida...\nEscolha uma opção do menu')