#EXERCICIO 4 CODIGO PARA "BETTER LETTERS" (Python)


from dataclasses import dataclass
from datetime import datetime

@dataclass 
class Publicacao:
    titulo: str
    descricao: str
    autor: str
    datetime: datetime
    curtidas: int = 0

lista_publicacoes = []

def Criar_publicacao():
    print("\n === Crie sua Publicação! :) ===")
    titulo = input("O que está na sua mente agora? :o ")
    descricao = input("Quer adicionar alguma legenda? | Se não quiser, agora vai querer >:( ")
    autor = input("Qual é o seu nome? :) ")
    data_hora = datetime.now()
    
    nova_publicacao = Publicacao(titulo, descricao, autor, data_hora)
    lista_publicacoes.append(nova_publicacao)
    print("Uhuu!! Publicação criada com sucesso! Aproveite e visualize os Posts de outros usuários! :D ")
    
def Curtir_publicacao():
    print(" <3 ")
    if not lista_publicacoes:
        print(" :( Nenhuma publicação disponível! :( ")
        return
    
    visualizar_feed()
    try:
        indice = int(input("Digite o numero da publicação para curtir <3 ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            lista_publicacoes[indice].curtidas += 1
            print("<3 Publicação curtida! <3 ")
        else:
             print(" :( Publicação não encontrada :( ")
    except ValueError:
        print("Número inválido. :/ ")
    
def visualizar_feed():
    print("Que tal dar uma olhada no Feed? :) ")
    if not lista_publicacoes:
        print("Não encontrei a publicação que você está procurando... tente novamente. :/ ")
        return
        
    for i, pub in enumerate(lista_publicacoes, 1):
        print(f"{i}. {pub.autor} - {pub.curtidas} curtidas")
        print(f"    {pub.titulo[:50]}...")
        print(f"    {pub.datetime.strftime('%d/%m/%Y %H:%M')}")
        print("-" * 40)
        
def visualizar_publicacao_individual():
    print("Vem ver essa publicação! :o ")
    if not lista_publicacoes:
        print("Não tem publicações! :( ")
        return
        
    visualizar_feed()
    try:
        indice = int(input("Digite o numero da publicação: ")) - 1
        if 0 <= indice < len(lista_publicacoes):
            pub = lista_publicacoes[indice]
            print(f"\nAutor: {pub.autor}")
            print(f"Data: {pub.datetime.strftime('%d/%m/%Y %H:%M')}")
            print(f"Título: {pub.titulo}")
            print(f"Descrição: {pub.descricao}")
            print(f"Curtidas: {pub.curtidas}")
        else:
            print("Não encontrei esta publicação... :( Tente novamente")
    except ValueError:
        print("Número inválido... :/ ")

def visualizar_publicacao_autor():
    print("Publicações por autor! :') ")
    if not lista_publicacoes:
        print("Não tem nenhuma publicação disponivel... :/ ")
        return
    autor = input("Digite o nome do autor:  :) ")
    publicacoes_autor = [pub for pub in lista_publicacoes if pub.autor.lower() == autor.lower()]
        
    if not publicacoes_autor:
        print(f"{autor} Não tem nenhuma publicação! :| ")
        return
        
    print(f"\nPublicações de {autor}: ")
    for pub in publicacoes_autor:
        print(f"- {pub.titulo[:50]}... ({pub.curtidas} curtidas)")
        print(f" {pub.datetime.strftime('%d/%m/%Y %H:%M')}")
        print("-" * 30)

def menu():
    while True:
        print("\n=== :) BETTER LETTERS (: ===")
        print("1. Criar Publicação")
        print("2. Curtir Publicação")
        print("3. Visualizar Publicação Individual")
        print("4. Visualizar Publicação por Autor")
        print("0. Goodbye! ")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            Criar_publicacao()
        elif opcao == "2":
            Curtir_publicacao()
        elif opcao == "3":
            visualizar_publicacao_individual()
        elif opcao == "4":
            visualizar_publicacao_autor()
        elif opcao == "0":
            print("Bye Bye! Até a proxima! :D ")
            break
        else:
            print("Opção inválida!")
    
if __name__ == "__main__":

    menu()
