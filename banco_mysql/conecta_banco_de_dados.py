import MySQLdb as mdb


def converte_para_lista_de_dicts(cursor):
    colunas = [dados_da_coluna[0] for dados_da_coluna in cursor.description]
    registros = cursor.fetchall()
    return [dict(zip(colunas, registro)) for registro in registros]


db = mdb.connect(
    host="localhost",
    user="usuario",
    passwd="senha",
    db="nome_do_banco"
)

cursor = db.cursor()
cursor.execute("SELECT id, nome, email FROM usuarios")

linhas = converte_para_lista_de_dicts(cursor)

for linha in linhas:
    print('ID: {}'.format(linha['id']))
    print('NOME: {}'.format(linha['nome']))
    print('E-MAIL: {}'.format(linha['email']))
    print('-------')
