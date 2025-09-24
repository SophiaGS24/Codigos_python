#EXERCICIO2 (cadastro paciente)

def menu():
    print("\n--- Hospital ---")
    print("1 - Cadastrar paciente")
    print("2 - Atender paciente X")
    print("3 - Fila/Sala de Espera.")
    print("4 - Sair")
    return input("Escolha uma opção: ")


lista_paciente = []

while True:
    opcao = menu()

    if opcao == "1":

        nome = input("Nome completo do paciente: ")
        idade = input("Idade do paciente: ")
        sintomas = input("Sintomas apresentados pelo paciente: ")

        paciente = {
            "nome": nome,
            "idade": idade,
            "sintomas": sintomas,        
            
            }
        
        lista_paciente.append(paciente)
        print(f"Paciente {nome}, {idade} anos, apresenta {sintomas}. /Registrado com sucesso.")

    elif opcao == "2":
        if lista_paciente:
            paciente_atendido = lista_paciente.pop(0)
            print(f"\n Atendendo paciente: {paciente_atendido['nome']}")
            print(f"Idade: {paciente_atendido['idade']}")
            print(f"Sintomas: {paciente_atendido['sintomas']}")
        
        else:
            print("Nenhum paciente na lista de atendimento.")
            
    elif opcao == "3":
        print(f"Pacientes atualmente na sala de espera: {len(lista_paciente)}")
        
    elif opcao == "4":
        print("Encerrando sistema")
        break
    
    else:

        print("Opção inválida. Tente novamente mais tarde.")
