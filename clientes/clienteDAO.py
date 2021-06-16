import datetime
import conexao.connection as conn

nome = None
cpf = None
nascimento = None
mensagem_cliente = 'Cliente a ser salvo: \n'
'Nome: ' + str(nome) + '\n'
'CPF: ' + str(cpf) + '\n'
'nascimento: ' + str(nascimento) + '\n'
'------------------------------------\n'
'1 - Digitar o nome \n'
'2 - Digitar o CPF \n'
'3 - Digitar a data de nascimento \n'
'5 - Salvar \n'
'0 - Voltar \n'


def _salvar_cliente( *args ):
    if len(args) > 3:
        sql = """UPDATE tbcliente set nome = %s, cpf = %s, nascimento = %s
        where id_cliente = %s
        """
        data = (args[1], args[2], args[3], args[0])
    else:
        sql = """INSERT INTO tbcliente(nome, cpf, nascimento)
            values(%s, %s, %s)
        """
        data = (args[0], args[1], args[2],)
    connection = conn.get_connection()
    cursor = connection.cursor()
    cursor.execute(sql, data)
    connection.commit()
    cursor.close()

def cadastrar_cliente():

    nome = input('Digite o nome do cliente: ')
    cpf = input('Digite o CPF do cliente: ')
    nascimento = input('Digite a data de nascimento do cliente (dd/mm/yyyy):')

    _salvar_cliente(nome, cpf, nascimento)

def listar_clientes():
    cnx = conn.get_connection()
    cursor = cnx.cursor()
    sql = "select * from tbcliente"
    cursor.execute(sql)
    clientes = cursor.fetchall()
    cursor.close()

    if clientes:
        for cli in clientes:
            print(str(cli[0]) + " - " + cli[1])
    else:
        print('Nenhum cliente cadastrado.')
        
def alterar_cliente():
    cli = input('Digite o código do cliente a ser alterado: ')
    sql = "select * from tbcliente where id_cliente = %s"
    data = (cli,)
    connection = conn.get_connection()
    cursor = connection.cursor()
    cursor.execute(sql, data)
    cliente = cursor.fetchone()
    if cliente:
        print('Existe um cliente...')
        print(cliente)
        nome = input("Digite o novo nome do cliente: ")
        cpf = input("Digite o novo cpf do cliente: ")
        nascimento = input("Digite a nova data de nascimento (dd/mm/yyyy)")
        id_cliente = cliente[0]
        _salvar_cliente(id_cliente, nome, cpf, nascimento)
        
    else:
        print("Cliente não encontrado.")

def excluir_cliente():
    idcliente = input("informe o id do cliente que sera excluido ou 0 para voltar:")
    if idcliente != "0":
        sql = "Delete from tbcliente where id_cliente = %s"
        data = (idcliente)
        connection = conn.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        cursor.close()