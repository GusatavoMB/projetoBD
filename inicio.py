import conexao.connection as conn
import os
import clientes.iniClientes as cli
import Produto.iniProduto as prod
import Venda.IniVenda as ven

menu_ini = '''
Escolha uma opção: 
1 - Menu de Clientes
2 - Menu de Produtos
3 - Menu de Vendas
-----------------------
0 - Sair do sistema
'''
""" 
def buscar_clientes():
    sql = "SELECT * from tb_cliente;"
    cnx = conn.get_connection()
    cur = None
    clientes = None
    if cnx:
        cur = cnx.cursor()
        cur.execute(sql)
        clientes = cur.fetchall()
        cur.close()

    if clientes:
        for cli in clientes:
            print(cli[1])
 """

os.system('cls')
print(menu_ini)
escolha = input('--->:')
while escolha != '0':
    if escolha == '1': # Escolheu o menu de clientes. Vá ao início dos clientes.
        cli.show_menu_clientes()
    elif escolha == '2':
        prod.show_menu_produto()
        print('Escolheu 2')
    elif escolha == '3':
        ven.show_menu_venda()
        print("Escolheu 3")
    elif escolha == '0':
        pass
    else:
        print("Escolheu qualquer coisa.....")

    print(menu_ini)
    escolha = input('--->:')
    os.system('cls')