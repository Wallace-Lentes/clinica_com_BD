import mysql.connector

def criar_conexao():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="clinica"
    )
    return conn
