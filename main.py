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
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

def fetch_all():
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sua_tabela")
        rows = cursor.fetchall()
        connection.close()
        return rows
    return []

st.title("Projeto de Banco de Dados")

# Read
rows = fetch_all()
st.subheader("Registros Atuais")
for row in rows:
    st.write(row)

# Create
st.subheader("Adicionar Novo Registro")
novo_dado = st.text_input("Digite o novo dado")
if st.button("Adicionar"):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO sua_tabela (coluna) VALUES (%s)", (novo_dado,))
        connection.commit()
        connection.close()
        st.success("Registro adicionado com sucesso!")
        st.experimental_rerun()

# Update
st.subheader("Atualizar Registro")
id_registro = st.number_input("ID do Registro a ser atualizado", min_value=0)
novo_valor = st.text_input("Novo valor")
if st.button("Atualizar"):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE sua_tabela SET coluna = %s WHERE id = %s", (novo_valor, id_registro))
        connection.commit()
        connection.close()
        st.success("Registro atualizado com sucesso!")
        st.experimental_rerun()

# Delete
st.subheader("Excluir Registro")
id_excluir = st.number_input("ID do Registro a ser excluído", min_value=0)
if st.button("Excluir"):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM sua_tabela WHERE id = %s", (id_excluir,))
        connection.commit()
        connection.close()
        st.success("Registro excluído com sucesso!")
        st.experimental_rerun()
