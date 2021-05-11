def menu():
    opcao= input('''
    =====================================================
    -------------------- PROJETO AGENDA EM PYTHON ------------------
MENU:

[1]CADASTRAR CONTATO
[2]LISTAR CONTATO
[3]DELETAR CONTATO
[4]BUSCAR CONTATO PELO NOME
=========================================================
    
ESCOLHA UMA OPÇÃO ACIMA:
''')
    if opcao =="1": 
        cadastrarContato()
    elif opcao =="2":
        listarContato()
    elif opcao =="3":
        deletarContato()
    else:
        BuscarContatoPeloNome()

def cadastrarContato():
    idContato = input('Escolha o Id do seu contato: ')
    nome = input('Escreva o nome do seu contato: ')
    telefone = input('Escreva o telefone do contato: ')
    email = input('Escreva o email do contato: ')
    try:
        agenda = open("agenda.txt","a")
        dados = f'{idContato};{nome};{telefone};{email} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso !!!')
    except: 
        print(f'ERRO na gravação de contato')

def listarContato():
    agenda = open("agenda.txt","r")
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarContato():
    print(f'Deletar Contato')

def BuscarContatoPeloNome():
    nome=input(f'Digite um nome a ser procurado: ')
    agenda = open('agenda.txt','r')
    for contato in agenda:
        if nome in contato.split(";")[1]:
            print(contato)
    agenda.close()

def main():
    menu()

main()
