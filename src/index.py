from models.contato import Contato
from models.mensagem import Mensagem
from ui.menu import imprimirMenuPrincipal, limparTela


# FUNÇÕES
def AdicionarContato():
    # ESCREVER LÓGICA AQUI!

    # Exemplo de criação de um contato
    
    print("===== NOVO CONTATO =====\n")
    nom = str.capitalize(input('Digite o nome: '))
    num = int(input('Digite o numero: '))
    contatos.update({nom: num})
    
    print("\nContato Criado com Sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def MostrarContatos():
    # ESCREVER LÓGICA AQUI
    print("===== LISTA DE CONTATOS =====\n")
    print(contatos)
    
    input("\n[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def EditarContato():
    # ESCREVER LÓGICA AQUI
    
    print("===== OQUE GOSTARIA DE ALTERAR =====")
    escolha = input('\n1 - Nome\n2 - Número\n\n[1] [2]\nOPÇÃO: ')

    if escolha == "1":
        print('\n',contatos.keys())
        escolha_contato = str.capitalize(input('DIGITE O NOME QUE SERÁ EDITADO: '))
        for x in contatos:
            if escolha_contato in x:

                novo = str.capitalize(input('NOVO NOME: '))
                contatos[novo] = contatos.pop(x)
                print(contatos)
                print('\nNome editado com sucesso!!!')
                input("[APERTE ENTER PARA CONTINUAR]")
                limparTela()
                break
                
            else:
                print('\nNome não escontrado')
                input("[APERTE ENTER PARA CONTINUAR]")
                limparTela()

    elif escolha == "2":
        print('\n', contatos.values())
        escolha_contato = int(input('DIGITE O NÚMERO QUE SERÁ EDITADO: '))
        if escolha_contato in contatos.values():
            for x in contatos.keys():
                
                novo = int(input('NOVO NÚMERO: '))
                contatos[x] = (novo)
                print(contatos)
                print('\nNúmero editado com sucesso!!!')
                input("[APERTE ENTER PARA CONTINUAR]")
                limparTela()
            
        else:
                print('\nNúmero não escontrado')
                input("[APERTE ENTER PARA CONTINUAR]")
                limparTela()
    else:
        print('\nEscolha não acessivel...')
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()

def EscreverMensagem():
    # Exemplo de criação de uma mensagem
    destinatario = Contato("Contato para envio", "Numero para envio")
    mensagem = Mensagem(destinatario, "Mensagem", "01/01/2024")

    print("\nMensagem Criada com Sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()


# PROGRAMA PRINCIPAL

fimPrograma = False

contatos = {}

while not fimPrograma:
    imprimirMenuPrincipal()
    opcao = int(input("\n[1] [2] [3] [4]\nOPÇÃO: "))

    if opcao == 1:
        AdicionarContato()
    elif opcao == 2:
        MostrarContatos()
    elif opcao == 3:
        EditarContato()
    elif opcao == 4:
        EscreverMensagem()
    elif opcao == 0:
        fimPrograma = True
    else: 
        print("Opção Errada! Favor escolha uma opção válida")
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()

print("===== FIM DO PROGRAMA =====\n")