#EXERCÍCIO 5

#1. Requisitos funcionais:

#1. Requisitos funcionais:

#	1- sistema precisa ter opçao para 'informar o problema' para manutenção
#	2- sistema precisa ter cadastro de nome do cliente
#	3- precisa ter cadastro do serviço (formatação: 80, limpeza geral: 50, remoção de vírus: 60, instalação de programas: 40)
#	4- precisa ter o adicional de 30% pela 'mão de obra'
#	5- precisa ter 'catálogo' para 
# ---------------------------

# anotações pessoais:

#agendamento:

#cliente
#data
#hora
#valor
#serviço
#barbeiro


#agenda_barbeiro:

#barbeiro
#dias_semana
#comissão
#faturamanto
#serviço


#catalogo:

#corte_simples = 25,00
#corte_barba = 35,00
#barba_completa = 20,00
#corte_social = 30,00

#- lembrete numero/email no dia anterior
#- histórico dos clientes (lista)
#- reagendamento


#CODIGO:


from decimal import Decimal 

class Agendamento:
    cliente: str
    data: str
    hora: st
    servico: str
    barbeiro: str
    custo: int

lista_agendamento = []

def Menu():
    input("Olá! O ue você quer fazer? 1- Agendar Corte/ 2- fazer Login (Empresa) ")
    if opcao == "1":
        agendar()
    elif opcao == "2":
        login()
    
def Login():
    input("digite o seu nome: ")
    if opcao == "Barbearia015"
        Barbeiro()
    
    
#agendamento de horario (clientes)
def Agendar(): 
    print("Olá! Vamos agendar seu horário!")
    cliente = input("Primeiro, qual é o seu nome?")
    corte = input("dentre os serviços disponíveis, qual você gostaria? A- corte simples/ B- corte barba/ C- barba completa/ D-corte social")
    if opcao == "a":
        custo = 25
    elif opcao == "b": 
        custo = 35
    elif opcao == "c": 
        custo = 20
    elif opcao == "d":
        custo = 30
    break
    
    else:
        print("opção inválida!")
    
    data = input(f"Ok {cliente}, qual dia fica melhor para você?")
    hora = input("Belezaa! Nessa data temos os seguintes horários:(digite 'Horarios disponiveis')")
    print(f"Este é o valor total: {custo}") 
novo_horario = Agendamento(cliente, data, hora)
lista_agendamento.append(novo_horario)
print(f"Marca aí! Seu novo horário é: {lista_agendamento}!")

Agendar()

class Barbeiro:
    nome: str
    dias: str
    faturamento: Decimal
    comissao: int
    
    
def Barbeiro():
    barbeiro = input("Digite o nome do Barbeiro: ")
    dias = input("quantos serviços ele fez essa semana? ")
  
    faturamento = 0
    for agenda in lista_agendamento:
        if barbeiro == agenda.barbeiro:
            faturamento = agenda.custo + faturamento
    comissao = faturamento * 0.3
    print(f"o total do salário mensal dele este mês é: {faturamento}")
    print(f"O salario dele será de ->{comissao} ")
    

Barbeiro()

