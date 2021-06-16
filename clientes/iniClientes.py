import os
import clientes.clienteDAO as cliente
    
menuClientes = '''
Escolha uma das opções:
1 - Listar os clientes
2 - Cadastrar um novo cliente
3 - Alterar cliente
4 - Excluir um cliente
0 - Voltar ao menu anterior
--------------------------------
'''

def show_menu_clientes():

    os.system('cls')
    escolha = '9'
    while escolha != '0':
        if escolha == '1':
            print('Escolheu listar os clientes')
            cliente.listar_clientes()
        elif escolha == '2':
            print('Escolheu cadastrar um novo cliente')
            cliente.cadastrar_cliente()
        elif escolha == '3':
            cliente.alterar_cliente()
        elif escolha == '4':
            print('escolheu excluir um cliente')
            cliente.excluir_cliente()
        elif escolha == '9':
            pass
        else:
            print("Opção inválida. Favor escolher uma das opções do menu.")

        print(menuClientes)
        escolha = input('--->:')
        os.system('cls')