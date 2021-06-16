import datetime
import conexao.connection as conn

def _salvar_produto( *args ):
    if len(args) > 2:
        sql = """UPDATE tbproduto set descricao = %s, preco = %s
        where id_produto = %s
        """
        data = (args[1], args[2], args[0])
    else:
        sql = """INSERT INTO tbproduto(descricao, preco)
            values(%s, %s)
        """
        data = (args[0], args[1])
    connection = conn.get_connection()
    cursor = connection.cursor()
    cursor.execute(sql, data)
    connection.commit()
    cursor.close()

def cadastrar_produto(): # Define os processos para o cadastramento do cliente.

    descricao = input('digite uma descricao do produto: ')
    preco = input('Digite o preco do produto: ')

    # Aqui se valida os dados que vão ser inseridos no banco

    # Aqui se salva os dados do cliente no banco.
    _salvar_produto(descricao, preco)

def listar_estoque():
    cnx = conn.get_connection()
    cursor = cnx.cursor()
    sql = "select * from tbproduto"
    cursor.execute(sql)
    produto = cursor.fetchall()
    cursor.close()

    if produto:
        for produ in produto:
            print(str(produ[0]) + " - " + produ[1])
    else:
            print('Nenhum produto cadastrado.')


def alterar_produto():
    produ = input('Digite o código do produto a ser alterado: ')
    sql = "select * from tbproduto where id_produto = %s"
    data = (produ,)
    connection = conn.get_connection()
    cursor = connection.cursor()
    cursor.execute(sql, data)
    produto = cursor.fetchone()
    if produto:
        print('Existe um produto...')
        print(produto)
        descricao = input("Digite a descricao do produto: ")
        preco = input("Digite preco ")
        id_produto = produto[0]
        _salvar_produto(id_produto, descricao, preco)

    else:
        print("produto não encontrado.")

def excluir_produto():
    idproduto = input("informe o id do produto que sera excluido ou 0 para voltar:")
    if idproduto != "0":
        sql = "Delete from tbproduto where id_produto = %s"
        data = (idproduto)
        connection = conn.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        cursor.close()
