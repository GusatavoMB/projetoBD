import conexao.connection as conn

menu_venda = '''
Escolha uma opção: 
1 - Menu de Clientes
2 - Menu de Produtos
3 - Menu de Vendas
-----------------------
0 - Sair do sistema
'''

def salvar_venda(*args):

    sql = """insert into venda (data_venda, id_cliente)
        values(current_date, %s)"""
    data = (args[0])
    connection = conn.get_connection()
    cursor = connection.cursor()
    cursor.execute(sql, data)
    connection.commit()
    cursor.close()

def salvar_produtos(*args):

    cnx = conn.get_connection()
    cursor = cnx.cursor()
    sql = "select max(id_venda) from venda"
    cursor.execute(sql)
    venda = cursor.fetchall()
    cursor.close()
    if venda:
        for v in venda:
            v_id = v[0]

    sql = """insert into item_venda (id_venda, id_produto, quantidade)
            values(%s,%s, %s)"""
    data = (v_id, args[0], args[1])
    connection = conn.get_connection()
    cursor = connection.cursor()
    cursor.execute(sql, data)
    connection.commit()
    cursor.close()

def cadastrar_venda():
    cnx = conn.get_connection()
    cursor = cnx.cursor()
    sql = "select * from tbcliente"
    cursor.execute(sql)
    cliente = cursor.fetchall()
    cursor.close()

    if cliente:
        for cli in cliente:
            print(str(cli[0]) + " - " + cli[1])
    else:
        print('Nenhum cliente cadastrado.')

    id_cliente = input("informe o id do cliente para a venda:")

    salvar_venda(id_cliente)

    aux = '1'
    while aux == '1':
        aux = input("1 - para adicionar produto:\n"
                    "0 - para sair:")
        if aux == '1':
            cnx = conn.get_connection()
            cursor = cnx.cursor()
            sql = "select * from tbproduto"
            cursor.execute(sql)
            produto = cursor.fetchall()
            cursor.close()

            if produto:
                for prod in produto:
                    print(str(prod[0]) + " - " + prod[1] + " / R$:" + str(prod[2]))
            else:
                print('Nenhum Produto cadastrado.')

            id_produto = input("informe o id do produto para a venda:")
            qtd = input("informe a quantidade:")
            salvar_produtos(id_produto, qtd)

def listar_venda():
    cnx = conn.get_connection()
    cursor = cnx.cursor()
    sql = "select v.id_venda,v.data_venda from venda v"
    cursor.execute(sql)
    vendas = cursor.fetchall()
    cursor.close()

    if vendas:
        for ven in vendas:
            print(str(ven[0]) + " - " + str(ven[1]))
    else:
        print('Nenhuma venda cadastrada.')

def excluir_venda():
    listar_venda()
    idvenda = input("informe o id da venda que sera excluido ou 0 para voltar:")
    if idvenda != "0":
        sql = "Delete from item_venda where id_venda = %s"
        data = (idvenda)
        connection = conn.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (data,))
        connection.commit()
        cursor.close()

        sql = "Delete from venda where id_venda = %s"
        data = (idvenda)
        connection = conn.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (data,))
        connection.commit()
        cursor.close()