import os
import Produto.ProdutoDAO as produ

menuProduto = '''
Escolha uma das opções:
1 - estoque
2 - Cadastrar um produto
3 - Alterar produto
4 - Excluir produto
0 - Voltar ao menu anterior
--------------------------------
'''
def show_menu_produto():

    os.system('cls')
    escolha = '9'
    while escolha != '0':
        if escolha == '1':
            print('Escolheu estoque')
            produ.listar_estoque()
        elif escolha == '2':
            print('Escolheu cadastrar um novo produto')
            produ.cadastrar_produto()
        elif escolha == '3':
            produ.alterar_produto()
            print('Escolheu cadastrar um novo cliente')
        elif escolha == '4':
            produ.excluir_produto()
            print('escolheu excluir um cliente')
        elif escolha == '9':
            pass
        else:
            print("Opção inválida. Favor escolher uma das opções do menu.")

        print(menuProduto)
        escolha = input('--->:')
        os.system('cls')