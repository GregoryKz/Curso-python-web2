import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",      # Host do XAMPP/MariaDB
            port=3306,            # Porta padrão do MySQL no XAMPP
            user="pyuser",        # Usuário criado no phpMyAdmin
            password="SenhaSegura!123",  # Senha definida no usuário pyuser
            database="teste",     # Banco criado no phpMyAdmin
            connection_timeout=10
        )
        
        if conexao.is_connected():
            print("Conexão estabelecida com sucesso!")
            print(f"Host: {conexao.get_host_info()}")
            print(f"Database: {conexao.database}")
            cursor = conexao.cursor()
            cursor.close()
            conexao.close()
            print("Conexão encerrada com sucesso!")

    except Error as e:
        print("Erro ao conectar ao banco:", e)

if __name__ == "__main__":
    conectar()
