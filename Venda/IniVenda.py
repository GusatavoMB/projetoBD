import os
import Venda.vendaDAO as vend

menuVenda = '''
Escolha uma das opções:
1 - Listar vendas
2 - Cadastrar vendas
3 - excluir uma venda
0 - Voltar ao menu anterior
--------------------------------
'''


def show_menu_venda():
    os.system('cls')
    escolha = '9'
    while escolha != '0':
        if escolha == '1':
            print('Escolheu listar vendas')
            vend.listar_venda()
        elif escolha == '2':
            print('Escolheu cadastrar venda')
            vend.cadastrar_venda()
        elif escolha == '3':
            print('Escolheu excluir uma venda')
            vend.excluir_venda()
        elif escolha == '9':
            pass
        else:
            print("Opção inválida. Favor escolher uma das opções do menu.")

        print(menuVenda)
        escolha = input('--->:')
        os.system('cls')