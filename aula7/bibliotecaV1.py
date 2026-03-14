import mysql.connector
from datetime import date


class Biblioteca:

    def __init__(self):

        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bliotecatitov1"
        )  

        self.cursor = self.conexao.cursor()

        print("Conectado ao banco com sucesso!")

    # CLIENTES

    def cadastrar_cliente(self):

        nome = input("Nome: ")
        email = input("Email: ")
        cpf = input("CPF: ")

        sql = """
        INSERT INTO cliente
        (nome_cliente,email_cliente,cpf_cliente)
        VALUES (%s,%s,%s)
        """

        self.cursor.execute(sql, (nome, email, cpf))
        self.conexao.commit()

        print("Cliente cadastrado!")

    def listar_clientes(self):

        sql = "SELECT * FROM cliente"

        self.cursor.execute(sql)

        clientes = self.cursor.fetchall()

        print("\n--- CLIENTES ---")

        for cliente in clientes:
            print(cliente)

    # LIVROS

    def cadastrar_livro(self):

        titulo = input("Titulo: ")
        isbn = input("ISBN: ")
        editora = input("Editora: ")

        sql = """
        INSERT INTO livro
        (titulo_livro,isbn_livro,editora_livro,data_entrada_livro)
        VALUES (%s,%s,%s,CURDATE())
        """

        self.cursor.execute(sql, (titulo, isbn, editora))
        self.conexao.commit()

        print("Livro cadastrado!")

    def listar_livros(self):

        sql = "SELECT * FROM livro"

        self.cursor.execute(sql)

        livros = self.cursor.fetchall()

        print("\n--- LIVROS ---")

        for livro in livros:
            print(livro)

    # JOGOS

    def cadastrar_jogo(self):

        nome = input("Nome do jogo: ")
        categoria = input("Categoria: ")
        fornecedor = input("Fornecedor: ")

        sql = """
        INSERT INTO jogo
        (nome_jogo,categoria_jogo,fornecedor_jogo,estado_jogo)
        VALUES (%s,%s,%s,'disponivel')
        """

        self.cursor.execute(sql, (nome, categoria, fornecedor))
        self.conexao.commit()

        print("Jogo cadastrado!")

    def listar_jogos(self):

        sql = "SELECT * FROM jogo"

        self.cursor.execute(sql)

        jogos = self.cursor.fetchall()

        print("\n--- JOGOS ---")

        for jogo in jogos:
            print(jogo)

    # VERIFICAR DISPONIBILIDADE

    def verificar_livro_disponivel(self, id_livro):

        sql = """
        SELECT *
        FROM item_emprestimo ie
        JOIN emprestimo e
        ON ie.fk_emprestimo = e.id_emprestimo
        WHERE ie.fk_livro = %s
        AND e.estado_retorno_emprestimo IS NULL
        """

        self.cursor.execute(sql, (id_livro,))

        resultado = self.cursor.fetchone()

        return resultado is None

    def verificar_jogo_disponivel(self, id_jogo):

        sql = """
        SELECT *
        FROM item_emprestimo ie
        JOIN emprestimo e
        ON ie.fk_emprestimo = e.id_emprestimo
        WHERE ie.fk_jogo = %s
        AND e.estado_retorno_emprestimo IS NULL
        """

        self.cursor.execute(sql, (id_jogo,))

        resultado = self.cursor.fetchone()

        return resultado is None

    # CRIAR EMPRESTIMO

    def criar_emprestimo(self):

        print("\nCLIENTES DISPONÍVEIS")
        self.listar_clientes()

        id_cliente = input("Digite o ID do cliente: ")

        print("\n1 - Emprestar Livro")
        print("2 - Emprestar Jogo")

        tipo = input("Escolha: ")

        data_inicio = date.today()
        data_fim = input("Data de devolução (AAAA-MM-DD): ")

        sql = """
        INSERT INTO emprestimo
        (data_inicio_emprestimo,data_termino_emprestimo,
        estado_entrega_emprestimo,estado_retorno_emprestimo)
        VALUES (%s,%s,%s,%s)
        """

        valores = (data_inicio, data_fim, "emprestado", None)

        self.cursor.execute(sql, valores)

        id_emprestimo = self.cursor.lastrowid

        sql_cliente = """
        INSERT INTO realiza_emprestimo
        (fk_cliente,fk_emprestimo)
        VALUES (%s,%s)
        """

        self.cursor.execute(sql_cliente, (id_cliente, id_emprestimo))

        if tipo == "1":

            self.listar_livros()
            id_livro = input("Digite o ID do livro: ")

            if not self.verificar_livro_disponivel(id_livro):
                print("Livro já emprestado!")
                return

            sql_item = """
            INSERT INTO item_emprestimo
            (fk_emprestimo,fk_livro)
            VALUES (%s,%s)
            """

            self.cursor.execute(sql_item, (id_emprestimo, id_livro))

            item = "Livro ID " + id_livro

        elif tipo == "2":

            self.listar_jogos()
            id_jogo = input("Digite o ID do jogo: ")

            if not self.verificar_jogo_disponivel(id_jogo):
                print("Jogo já emprestado!")
                return

            sql_item = """
            INSERT INTO item_emprestimo
            (fk_emprestimo,fk_jogo)
            VALUES (%s,%s)
            """

            self.cursor.execute(sql_item, (id_emprestimo, id_jogo))

            item = "Jogo ID " + id_jogo

        else:
            print("Opção inválida")
            return

        self.conexao.commit()

        print("\n========== COMPROVANTE ==========")
        print("Empréstimo:", id_emprestimo)
        print("Cliente:", id_cliente)
        print("Item:", item)
        print("Data início:", data_inicio)
        print("Data devolução:", data_fim)
        print("Status: EMPRESTADO")
        print("=================================")

    # DEVOLUÇÃO

    def registrar_devolucao(self):

        id_emprestimo = input("Digite o ID do empréstimo: ")

        sql = """
        UPDATE emprestimo
        SET estado_retorno_emprestimo = 'devolvido'
        WHERE id_emprestimo = %s
        """

        self.cursor.execute(sql, (id_emprestimo,))
        self.conexao.commit()

        print("Devolução registrada!")

    # RELATÓRIO

    def relatorio_emprestimos(self):

        sql = """
        SELECT
        cliente.nome_cliente,
        livro.titulo_livro,
        jogo.nome_jogo,
        emprestimo.id_emprestimo,
        emprestimo.data_inicio_emprestimo,
        emprestimo.data_termino_emprestimo,
        emprestimo.estado_retorno_emprestimo

        FROM cliente

        JOIN realiza_emprestimo
        ON cliente.id_cliente = realiza_emprestimo.fk_cliente

        JOIN emprestimo
        ON emprestimo.id_emprestimo = realiza_emprestimo.fk_emprestimo

        JOIN item_emprestimo
        ON emprestimo.id_emprestimo = item_emprestimo.fk_emprestimo

        LEFT JOIN livro
        ON livro.id_livro = item_emprestimo.fk_livro

        LEFT JOIN jogo
        ON jogo.id_jogo = item_emprestimo.fk_jogo
        """

        self.cursor.execute(sql)

        resultado = self.cursor.fetchall()

        print("\n===== RELATÓRIO =====")

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
            print("5 - Cadastrar jogo")
            print("6 - Listar jogos")
            print("7 - Realizar empréstimo")
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
                self.cadastrar_jogo()

            elif opcao == "6":
                self.listar_jogos()

            elif opcao == "7":
                self.criar_emprestimo()

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