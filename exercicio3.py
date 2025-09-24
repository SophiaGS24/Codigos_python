#exercicio 3 (sistema de login)

#cadastra novo email
class Usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"Email: {self.email}"

#sistema de usuario/cadastre-se
class SistemaUsuarios:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self):
        print("\n--- CADASTRE-SE ---")
        email = input("Digite o seu email: ")
        senha = input("Crie a sua senha: // não vai esquecer ela, heim! ")

        # Verificando se o email ja foi cadastrado
        for usuario in self.usuarios:
            if usuario.email == email:
                print("ERRO: Esse e-mail já está cadastrado... Tem certeza que não tem conta aqui?\n")
                return

        novo_usuario = Usuario(email, senha)
        self.usuarios.append(novo_usuario)
        print("Ebaaa!! Sua conta foi cadastrada com suceso!!\n")

    def listar_usuarios(self):
        print("\n--- Usuários ---")
        if not self.usuarios:
            print("Este usuário não existe!\n")
            return

        for i, usuario in enumerate(self.usuarios, start=1):
            print(f"{i}. {usuario}")
        print()

    def buscar_usuario(self):
        print("\n--- Buscar Usuário ---")
        email = input("Digite o e-mail do seu amiguinho: //exemplo: usuario123@email ")

        for usuario in self.usuarios:
            if usuario.email == email:
                print(f"Usuário encontrado: {usuario}\n")
                return
        print("Seu amigo não está aqui! Aproveite e convide ele para se cadastrar! \n")
#fazer login
    def login(self):
        print("\n--- Login ---")
        email = input("Digite o seu email: ")
        senha = input("Digite a sua senha: ")

        for usuario in self.usuarios:
            if usuario.email == email and usuario.senha == senha:
                print(f"Login realizado com sucesso! Bem-vindo {usuario.email} ! :D \n")
                return
        print("Email ou senha incorretos... // Você não se esqueceu da sua senha, né? :/ \n")
#menu do sistema de login
    def menu(self):
        while True:
            print("===== Sistema Login =====")
            print("1. Cadastre-se! :D ")
            print("2. Listar usuários :o ")
            print("3. Busque seu 'amiguinho@email'! :D ")
            print("4. Fazer login! ")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_usuario()
            elif opcao == "2":
                self.listar_usuarios()
            elif opcao == "3":
                self.buscar_usuario()
            elif opcao == "4":
                self.login()
            elif opcao == "5":
                print("Ahh :( Já vai? Até mais!")
                break
            else:
                print("ERRO: Essa opção não existe!! Tente novamente.\n")

# Iniciar o sistema
sistema = SistemaUsuarios()
sistema.menu()
