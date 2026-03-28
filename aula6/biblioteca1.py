<<<<<<< HEAD
import mysql.connector

def conectar():

 conexao = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="biblioteca_tito"
 )

 return conexao
def cadastrar_livro():

 conn = conectar()
 cursor = conn.cursor()

 titulo = input("Titulo: ")
 isbn = input("ISBN: ")
 editora = input("Editora: ")

 sql = """
 INSERT INTO livro (titulo,isbn,editora)
 VALUES (%s,%s,%s)
 """
 
 cursor.execute(sql,(titulo,isbn,editora))

 conn.commit()

 print("Livro cadastrado!")

 cursor.close()
 conn.close()

def listar_livros():

 conn = conectar()
 cursor = conn.cursor()

 cursor.execute("SELECT * FROM livro")

 livros = cursor.fetchall()

 print("\nCATÁLOGO DE LIVROS\n")

 for livro in livros:

    print("ID:",livro[0])
    print("Titulo:",livro[1])
    print("ISBN:",livro[2])
    print("Editora:",livro[3])
    print("------------------")

 cursor.close()
 conn.close()

def emprestar_livro():

 conn = conectar()
 cursor = conn.cursor()

 cliente = input("ID do cliente: ")
 livro = input("ID do livro: ")

 sql = """
 INSERT INTO emprestimo
 (fk_cliente,fk_livro,data_inicio,data_devolucao,status_emprestimo)
 VALUES
 (%s,%s,CURDATE(),DATE_ADD(CURDATE(),INTERVAL 7 DAY),'emprestado')
 """
 cursor.execute(sql,(cliente,livro))

 conn.commit()

 print("Empréstimo realizado!")

 cursor.close()
 conn.close()

def menu():

 while True:

    print("\nBIBLIOTECA TITO")
    print("1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Emprestar Livro")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        listar_livros()
    elif opcao == "0":
        break
menu()
=======
import mysql.connector

def conectar():

 conexao = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="biblioteca_tito"
 )

 return conexao
def cadastrar_livro():

 conn = conectar()
 cursor = conn.cursor()

 titulo = input("Titulo: ")
 isbn = input("ISBN: ")
 editora = input("Editora: ")

 sql = """
 INSERT INTO livro (titulo,isbn,editora)
 VALUES (%s,%s,%s)
 """
 
 cursor.execute(sql,(titulo,isbn,editora))

 conn.commit()

 print("Livro cadastrado!")

 cursor.close()
 conn.close()

def listar_livros():

 conn = conectar()
 cursor = conn.cursor()

 cursor.execute("SELECT * FROM livro")

 livros = cursor.fetchall()

 print("\nCATÁLOGO DE LIVROS\n")

 for livro in livros:

    print("ID:",livro[0])
    print("Titulo:",livro[1])
    print("ISBN:",livro[2])
    print("Editora:",livro[3])
    print("------------------")

 cursor.close()
 conn.close()

def emprestar_livro():

 conn = conectar()
 cursor = conn.cursor()

 cliente = input("ID do cliente: ")
 livro = input("ID do livro: ")

 sql = """
 INSERT INTO emprestimo
 (fk_cliente,fk_livro,data_inicio,data_devolucao,status_emprestimo)
 VALUES
 (%s,%s,CURDATE(),DATE_ADD(CURDATE(),INTERVAL 7 DAY),'emprestado')
 """
 cursor.execute(sql,(cliente,livro))

 conn.commit()

 print("Empréstimo realizado!")

 cursor.close()
 conn.close()

def menu():

 while True:

    print("\nBIBLIOTECA TITO")
    print("1 - Cadastrar Livro")
    print("2 - Listar Livros")
    print("3 - Emprestar Livro")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        listar_livros()
    elif opcao == "0":
        break
menu()
>>>>>>> d43bcf0 (sistema completo com banco de dados)
