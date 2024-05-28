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

# Função para buscar todos os registros da tabela Pessoa
def fetch_all_pessoas():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Pessoa")
            rows = cursor.fetchall()
            return rows
        except Error as e:
            st.error(f"Erro ao buscar registros de Pessoa: {e}")
        finally:
            connection.close()
    return []

# Função para adicionar nova pessoa
def add_pessoa(nome, cpf, telefone, email):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Pessoa (Nome, CPF, Telefone, Email) VALUES (%s, %s, %s, %s)", (nome, cpf, telefone, email))
            connection.commit()
            st.success("Pessoa adicionada com sucesso!")
        except Error as e:
            st.error(f"Erro ao adicionar pessoa: {e}")
        finally:
            connection.close()

# Função para buscar todos os registros da tabela Cliente
def fetch_all_clientes():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Cliente")
            rows = cursor.fetchall()
            return rows
        except Error as e:
            st.error(f"Erro ao buscar registros de Cliente: {e}")
        finally:
            connection.close()
    return []

# Função para adicionar novo cliente
def add_cliente(id_pessoa):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Cliente (ID_Pessoa) VALUES (%s)", (id_pessoa,))
            connection.commit()
            st.success("Cliente adicionado com sucesso!")
        except Error as e:
            st.error(f"Erro ao adicionar cliente: {e}")
        finally:
            connection.close()

# Função para buscar todos os registros da tabela Vendedor
def fetch_all_vendedores():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Vendedor")
            rows = cursor.fetchall()
            return rows
        except Error as e:
            st.error(f"Erro ao buscar registros de Vendedor: {e}")
        finally:
            connection.close()
    return []

# Função para adicionar novo vendedor
def add_vendedor(id_pessoa, gerente_id):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Vendedor (ID_Pessoa, Gerente_ID) VALUES (%s, %s)", (id_pessoa, gerente_id))
            connection.commit()
            st.success("Vendedor adicionado com sucesso!")
        except Error as e:
            st.error(f"Erro ao adicionar vendedor: {e}")
        finally:
            connection.close()

# Título do aplicativo
st.title("Banco de Dados GFC Veículos")

# Adicionar Pessoa
st.subheader("Adicionar Nova Pessoa")
with st.form("add_pessoa_form"):
    nome = st.text_input("Nome")
    cpf = st.text_input("CPF")
    telefone = st.text_input("Telefone")
    email = st.text_input("Email")
    submit_add_pessoa = st.form_submit_button("Adicionar Pessoa")
    if submit_add_pessoa:
        add_pessoa(nome, cpf, telefone, email)

# Adicionar Cliente
st.subheader("Adicionar Novo Cliente")
with st.form("add_cliente_form"):
    id_pessoa_cliente = st.number_input("ID da Pessoa do Cliente")
    submit_add_cliente = st.form_submit_button("Adicionar Cliente")
    if submit_add_cliente:
        add_cliente(id_pessoa_cliente)

# Adicionar Vendedor
st.subheader("Adicionar Novo Vendedor")
with st.form("add_vendedor_form"):
    id_pessoa_vendedor = st.number_input("ID da Pessoa do Vendedor")
    gerente_id = st.number_input("ID do Gerente (se aplicável)")
    submit_add_vendedor = st.form_submit_button("Adicionar Vendedor")
    if submit_add_vendedor:
        add_vendedor(id_pessoa_vendedor, gerente_id)
