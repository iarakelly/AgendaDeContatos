
lista = []

def CriarContato():
    # fazer verificação se o contato já existe
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    email = input('email:')

    contato = {
    "nome" : nome, "telefone" : telefone, "email" : email
    }

    lista.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")

def menu ():
    print('''
==============Agenda de Contatos==============
[1]Adicionar
[2]Listar
[3]Buscar
[4]Atualizar
[5]Exluir
==============================================''')
    opc = input("Selecione uma opeção: ")
    if opc == "1":
        #criar contato
        pass
    elif opc == "2":
        #listar contatos
        pass
    elif opc == "3":
        #buscar contatos
        pass
    elif opc == "4":
        #att contato
        pass
    elif opc == "5":
        #delete contato
        pass
    
def main():
    menu()
main()