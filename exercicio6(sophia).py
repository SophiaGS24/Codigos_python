
#exercicio 6 (loja de informática)


servicos = {
    "formatação": 80,
    "limpeza geral": 50,
    "remoção de vírus": 60,
    "instalação de programas": 40
}

estoque = {
    "memória RAM": 10,
    "HD": 5,
    "SSD": 7,
    "fonte": 4,
    "placa de vídeo": 3
}

reparos = []

def listar_servicos():
    print("\n--- Nossos Serviços! ---")
    for nome, preco in servicos.items():
        print(f"{nome} - R$ {preco}")
    print("-------------------------")

def adicionar_reparo():
    cliente = input("Nome do cliente: ")
    descricao = input("Descrição do reparo: ")
    preco = float(input("Valor do serviço: "))
    tecnico = input("Técnico responsável pelo reparo: ")
    reparo = {
        "cliente": cliente,
        "descricao": descricao,
        "preco": preco,
        "tecnico": tecnico,
        "status": "Estamos analisando sua máquina!"
    }
    reparos.append(reparo)
    print(f"\n[OK] Reparo adicionado para {cliente}.")

def atualizar_status():
    cliente = input("Nome do cliente: ")
    novo_status = input("Status: ")
    for r in reparos:
        if r["cliente"] == cliente:
            r["status"] = novo_status
            print(f"[OK] Status atualizado para '{novo_status}'.")
            return
    print("[ERRO] Cliente não encontrado.")

def consultar_status():
    cliente = input("Nome do cliente: ")
    for r in reparos:
        if r["cliente"] == cliente:
            print(f"O computador de {cliente} está: {r['status']}")
            return
    print("[ERRO] Cliente não encontrado.")

def vender_peca():
    nome_peca = input("Nome da peça: ")
    quantidade = int(input("Quantidade: "))
    if nome_peca in estoque:
        if estoque[nome_peca] >= quantidade:
            estoque[nome_peca] -= quantidade
            print(f"[OK] {quantidade}x {nome_peca} vendida(s). Restam {estoque[nome_peca]}.")
            if estoque[nome_peca] <= 2:
                print(">>> Atenção: estoque baixo, faça reposição!")
        else:
            print("[ERRO] Quantidade maior do que no estoque.")
    else:
        print("[ERRO] Peça não encontrada.")

def gerar_relatorio():
    print("\n--- Relatório ---")
    print(f"Total de reparos: {len(reparos)}")
    tecnicos = {}
    for r in reparos:
        t = r["tecnico"]
        tecnicos[t] = tecnicos.get(t, 0) + 1
    print("Serviços por técnico:")
    for t, qtd in tecnicos.items():
        print(f" - {t}: {qtd} serviços")
    print("-----------------")

def menu():
    while True:
        print("\n--- TechFix ---")
        print("1. Nossos serviços!")
        print("2. Precisa reparar algo? Clique aqui!")
        print("3. Atualizar status de reparo:")
        print("4. Consultar status de reparo:")
        print("5. Vender uma peça.")
        print("6. Gerar relatório. ")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_servicos()
        elif opcao == "2":
            adicionar_reparo()
        elif opcao == "3":
            atualizar_status()
        elif opcao == "4":
            consultar_status()
        elif opcao == "5":
            vender_peca()
        elif opcao == "6":
            gerar_relatorio()
        elif opcao == "0":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("ERRO!! Tente novamente...")

menu()
