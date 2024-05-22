import streamlit as st
import mysql.connector
from mysql.connector import Error

# Função para conectar ao banco de dados
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

# Função para buscar todos os registros
def fetch_all():
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sua_tabela")
        rows = cursor.fetchall()
        connection.close()
        return rows
    return []

# Título do aplicativo
st.title("Projeto de Banco de Dados")

# Leitura (Read)
st.subheader("Registros Atuais")
rows = fetch_all()
if rows:
    for row in rows:
        st.write(row)
else:
    st.write("Nenhum registro encontrado.")

# Criação (Create)
st.subheader("Adicionar Novo Registro")
with st.form("create_form"):
    novo_dado = st.text_input("Digite o novo dado")
    submit_create = st.form_submit_button("Adicionar")
    if submit_create:
        if not novo_dado:
            st.error("O campo não pode estar vazio.")
        else:
            connection = get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO sua_tabela (coluna) VALUES (%s)", (novo_dado,))
                connection.commit()
                connection.close()
                st.success("Registro adicionado com sucesso!")
                st.experimental_rerun()

# Atualização (Update)
st.subheader("Atualizar Registro")
with st.form("update_form"):
    id_registro = st.number_input("ID do Registro a ser atualizado", min_value=0, step=1)
    novo_valor = st.text_input("Novo valor")
    submit_update = st.form_submit_button("Atualizar")
    if submit_update:
        if id_registro == 0 or not novo_valor:
            st.error("Todos os campos devem ser preenchidos.")
        else:
            connection = get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute("UPDATE sua_tabela SET coluna = %s WHERE id = %s", (novo_valor, id_registro))
                if cursor.rowcount == 0:
                    st.error("ID não encontrado.")
                else:
                    connection.commit()
                    st.success("Registro atualizado com sucesso!")
                connection.close()
                st.experimental_rerun()

# Exclusão (Delete)
st.subheader("Excluir Registro")
with st.form("delete_form"):
    id_excluir = st.number_input("ID do Registro a ser excluído", min_value=0, step=1)
    submit_delete = st.form_submit_button("Excluir")
    if submit_delete:
        if id_excluir == 0:
            st.error("O campo ID deve ser preenchido.")
        else:
            connection = get_connection()
            if connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM sua_tabela WHERE id = %s", (id_excluir,))
                if cursor.rowcount == 0:
                    st.error("ID não encontrado.")
                else:
                    connection.commit()
                    st.success("Registro excluído com sucesso!")
                connection.close()
                st.experimental_rerun()
