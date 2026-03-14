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
        print ("Conectado...")
        
    def cadastrar_cliente(self):
        
        nome = input("Digite o nome do cliente:")
        email = input("Digite o emial do cliente:")
        cpf = input ("Digite o cpf do cliente:")
        
        sql = """ 
            INSERT INTO cliente (nome_cliente, email_cliente, cpf_cliente)
            VALUES (%s,%s,%s)
        """
        self.cursor.execute(sql, (nome, email,cpf))
        self.conexao.commit()
        print ("Cliente foi cadastrado")
    
    def listar_cliente(self):
        sql = " SELECT  * FROM cliente"
        self.cursor.execute(sql)
        clientes = self.cursor.fetchall()
        for cliente in clientes:
            print(cliente)2
    
    def menu(self):
        while True:
            print("1- Cadastrar Cliente")
            print("2- Listar Cliente")
            print("0 - sair")
            
            retorno = input("Opção:")
            
            if retorno == "1":
                self.cadastrar_cliente()
            elif retorno == "2":
                self.listar_cliente()
            elif retorno == "0":
                print("Saida")
                break
            else:
                print("Opção invalida")
        
sistema= Biblioteca()
sistema.menu()
            
            
            
        

    
    

        
        

        
        