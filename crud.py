import psycopg2
connection = psycopg2.connect(user = "postgres",
									password = "",
									host = "127.0.0.1",
									port = "5432",
									database = "esdb")

cursor = connection.cursor( )

try:
create = '''create table fomento
                (
				  agencia_id int not null,
                  nome varchar(120) not null,
                  data_contrato date,
                  numero_bolsas int,
                  primary key (agencia_id)
				);'''

    cursor.execute(create)
    connection.commit( )
    print("CREATE sucedeu")
except (Exception, psycopg2.Error) as error :
    print ("Erro ao criar tabela", error)

try:
retrieve = '''SELECT I.nome, C.nome FROM esdb.INSTITUICAO AS I INNER JOIN esdb.INSTITUICAO_has_CURSO AS IC ON
	I.idINSTITUICAO = IC.INSTITUICAO_idINSTItuiCAO INNER JOIN esdb.CURSO AS C ON C.idCURSO = IC.CURSO_idCURSO
	WHERE C.total_cred < 200;'''

    cursor.execute(retrieve)
    connection.commit( )
    print("RETRIEVE sucedeu")
except (Exception, psycopg2.Error) as error :
    print ("Erro ao buscar tabela", error)

try:
update = '''insert into INSTITUICAO values(39012,'UnB','DF','Darcy Ribeiro',1961,lo_import('C:\unb.jpg'));'''

    cursor.execute(update)
    connection.commit( )
    print("UPDATE sucedeu")
except (Exception, psycopg2.Error) as error :
    print ("Erro ao inserir imagem", error)

try:
delete = '''DELETE FROM disciplina
	WHERE creditos='6';'''

    cursor.execute(delete)
    connection.commit( )
    print("RETRIEVE delete")
except (Exception, psycopg2.Error) as error :
    print ("Erro ao deletar dados", error)

finally:
    if(connection):
		cursor.close()
        connection.close()