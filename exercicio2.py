#EXERCICIO1
evento = "Taylor Swift, Eras Tour"
Ingresso = 500 
quantidade = 80

print(f"Escolha o evento: {evento}")
print(f"O valor unitário do ingresso é {ingresso}")
print(f"Deseja prosseguir?")
print(f"1- sim")
print(f"2- não")

opcao = input("Digite a opção: ")

if opcao == "1":
    print(f"Digite o numero de ingressos: {quantidade}")
if quantidade < "80":
    print(f"O total a ser pago é: {total + quantidade}")
else: 
    print(f"Número de ingressos indisponível no momento")
    

#EXERCICIO2
lista_de_numeros = [9, 20, 40]
print(lista_de_numeros)
numero_digitado = int(input("Digite o numero: "))
lista_de_numeros.append(numero_digitado)
print(f"Lista após inserir o numero 20 --> {lista_de_numeros}")

a = ["Joao","Maria"]
a.insert(0, input("Qual o nome: "))
print(a)

#EXERCICIO3
paciente = ["Joao","Maria"]
paciente.insert(0, input("Qual o nome do paciente: "))
print(paciente)

paciente(input("paciente atendido: "))
   