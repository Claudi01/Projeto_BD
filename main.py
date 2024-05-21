import streamlit as st
import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='projetoBD',
            user='root',
            password='Bradesco01'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

st.title("Projeto de Banco de Dados")

connection = get_connection()
if connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sua_tabela")
    rows = cursor.fetchall()
    connection.close()

    for row in rows:
        st.write(row)
