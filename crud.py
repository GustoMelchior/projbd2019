import pymysql.cursors

def mainMenu():
	print("1: Criar tabela")
	print("2: Realizar busca")
	print("3: Atualizar valor")
	print("4: Deletar")
	print("5: Sair")
	op=int(input("Escolha uma opcao: "))
	if op==1:
		createMenu()
		mainMenu()
	elif op==2:
		retrieveMenu()
		mainMenu()
	elif op==3:
		updateMenu()
		mainMenu()
	elif op==4:
		deleteMenu()
		mainMenu()
	elif op==5:
		exit
	else:
		printf("Opcao invalida.")
		mainMenu()

def createMenu():
	nome=input("Nome da nova tabela: ")
	campo1=input("Nome do primeiro argumeto: ")
	campo2=input("Nome do segundo argumento: ")
	with connection.cursor() as cursor:
		create = "create table {0}(id int not null,nome varchar(120) not null,{1} date,{2} int,primary key (id));".format(nome,campo1,campo2)
		cursor.execute(create)

	connection.commit()

def retrieveMenu():
	query=input("Entre com a busca: ")
	with connection.cursor() as cursor:
		if query == "":
			retrieve = "SELECT I.nome, C.nome FROM esdb.INSTITUICAO AS I INNER JOIN esdb.INSTITUICAO_has_CURSO AS IC ON I.idINSTITUICAO = IC.INSTITUICAO_idINSTItuiCAO INNER JOIN esdb.CURSO AS C ON C.idCURSO = IC.CURSO_idCURSO WHERE C.total_cred < 200;"
			cursor.execute(retrieve)
		else:
			cursor.execute(query)
		result = cursor.fetchone( )
		print(result)

def updateMenu():
	update=input("Entre com a busca: ")
	with connection.cursor() as cursor:
		#if update=="":
			#update = "insert into INSTITUICAO values(39012,'UnB','DF','Darcy Ribeiro',1961,load_file('C:\Users\Gabriel\Desktop\unb.png'));"
		cursor.execute(update)

def deleteMenu():
	delete=input("Entre com o comando de delecao: ")
	with connection.cursor() as cursor:
		if delete=="":
			delete = "DELETE FROM disciplina WHERE creditos='6';"
		else:
			delete="{0}".format(delete)
		cursor.execute(delete)

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='your666sql',
                             db='esdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

mainMenu()
connection.close()