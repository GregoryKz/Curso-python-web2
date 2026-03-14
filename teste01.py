import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="127.0.0.1",   # ← importante
        user="pyuser",
        password="senac",
        database="aula1"
    )

    print("Conectado ao MySQL!")

except mysql.connector.Error as erro:
    print("Erro:", erro)

finally:
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()