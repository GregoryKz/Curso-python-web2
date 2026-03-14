import mysql.connector
from datetime import date


class Biblioteca:

    def __init__(self):
        """
        Conecta ao banco de dados
        """

        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bliotecatitov1"
        )

        self.cursor = self.conexao.cursor()

        print("Conectado ao banco com sucesso!")

        # CLIENTE
    
    def cadastrar_cliente(self):

        nome = input("Nome: ")
        email = input("Email: ")
        cpf = input("CPF: ")

        sql = """
        INSERT INTO cliente
        (nome_cliente, email_cliente, cpf_cliente)
        VALUES (%s,%s,%s)
        """

        valores = (nome, email, cpf)

        self.cursor.execute(sql, valores)
        self.conexao.commit()

        print("Cliente cadastrado!")

    def listar_clientes(self):

        sql = "SELECT * FROM cliente"

        self.cursor.execute(sql)

        resultado = self.cursor.fetchall()

        print("\n--- CLIENTES ---")

        for cliente in resultado:
            print(cliente)

        # LIVROS
    
    def cadastrar_livro(self):

        titulo = input("Titulo: ")
        isbn = input("ISBN: ")
        editora = input("Editora: ")

        sql = """
        INSERT INTO livro
        (titulo_livro, isbn_livro, editora_livro, data_entrada_livro)
        VALUES (%s,%s,%s,CURDATE())
        """

        valores = (titulo, isbn, editora)

        self.cursor.execute(sql, valores)
        self.conexao.commit()

        print("Livro cadastrado!")

    def listar_livros(self):

        sql = "SELECT * FROM livro"

        self.cursor.execute(sql)

        livros = self.cursor.fetchall()

        print("\n--- LIVROS ---")

        for livro in livros:
            print(livro)

        # EMPRESTIMO
    
    def criar_emprestimo(self):

        data_inicio = date.today()

        data_fim = input("Data de devolução (AAAA-MM-DD): ")

        sql = """
        INSERT INTO emprestimo
        (data_inicio_emprestimo,
        data_termino_emprestimo,
        estado_entrega_emprestimo)
        VALUES (%s,%s,%s)
        """

        valores = (data_inicio, data_fim, "emprestado")

        self.cursor.execute(sql, valores)
        self.conexao.commit()

        print("Empréstimo criado!")

        # VINCULAR CLIENTE AO EMPRESTIMO
    
    def vincular_cliente_emprestimo(self):

        cliente = input("ID do cliente: ")
        emprestimo = input("ID do emprestimo: ")

        sql = """
        INSERT INTO realiza_emprestimo
        (fk_cliente,fk_emprestimo)
        VALUES (%s,%s)
        """

        valores = (cliente, emprestimo)

        self.cursor.execute(sql, valores)
        self.conexao.commit()

        print("Cliente vinculado ao empréstimo!")

        # REGISTRAR ITEM EMPRESTADO
    
    def registrar_item_livro(self):

        emprestimo = input("ID do emprestimo: ")
        livro = input("ID do livro: ")

        sql = """
        INSERT INTO item_emprestimo
        (fk_emprestimo,fk_livro)
        VALUES (%s,%s)
        """

        valores = (emprestimo, livro)

        self.cursor.execute(sql, valores)
        self.conexao.commit()

        print("Livro adicionado ao empréstimo!")

        # DEVOLUÇÃO
    
    def registrar_devolucao(self):

        emprestimo = input("ID do emprestimo: ")

        sql = """
        UPDATE emprestimo
        SET estado_retorno_emprestimo = 'devolvido'
        WHERE id_emprestimo = %s
        """

        valores = (emprestimo,)

        self.cursor.execute(sql, valores)
        self.conexao.commit()

        print("Devolução registrada!")

        # RELATÓRIO COM JOIN
    
    def relatorio_emprestimos(self):

        sql = """
        SELECT
        cliente.nome_cliente,
        livro.titulo_livro,
        emprestimo.data_inicio_emprestimo,
        emprestimo.data_termino_emprestimo

        FROM cliente

        JOIN realiza_emprestimo
        ON cliente.id_cliente = realiza_emprestimo.fk_cliente

        JOIN emprestimo
        ON emprestimo.id_emprestimo = realiza_emprestimo.fk_emprestimo

        JOIN item_emprestimo
        ON emprestimo.id_emprestimo = item_emprestimo.fk_emprestimo

        JOIN livro
        ON livro.id_livro = item_emprestimo.fk_livro
        """

        self.cursor.execute(sql)

        resultado = self.cursor.fetchall()

        print("\n--- RELATÓRIO DE EMPRÉSTIMOS ---")

        for linha in resultado:
            print(linha)

        # MENU
    
    def menu(self):

        while True:

            print("\n===== SISTEMA BIBLIOTECA =====")
            print("1 - Cadastrar cliente")
            print("2 - Listar clientes")
            print("3 - Cadastrar livro")
            print("4 - Listar livros")
            print("5 - Criar empréstimo")
            print("6 - Vincular cliente ao empréstimo")
            print("7 - Registrar livro no empréstimo")
            print("8 - Registrar devolução")
            print("9 - Relatório de empréstimos")
            print("0 - Sair")

            opcao = input("Escolha: ")

            if opcao == "1":
                self.cadastrar_cliente()

            elif opcao == "2":
                self.listar_clientes()

            elif opcao == "3":
                self.cadastrar_livro()

            elif opcao == "4":
                self.listar_livros()

            elif opcao == "5":
                self.criar_emprestimo()

            elif opcao == "6":
                self.vincular_cliente_emprestimo()

            elif opcao == "7":
                self.registrar_item_livro()

            elif opcao == "8":
                self.registrar_devolucao()

            elif opcao == "9":
                self.relatorio_emprestimos()

            elif opcao == "0":
                print("Sistema encerrado.")
                break

            else:
                print("Opção inválida!")


# EXECUÇÃO

sistema = Biblioteca()
sistema.menu()