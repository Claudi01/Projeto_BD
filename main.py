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

# Funções de CRUD para Pessoa
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

def add_pessoa(nome, cpf, telefone, email):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Pessoa (Nome, CPF, Telefone, Email) VALUES (%s, %s, %s, %s)", 
                           (nome, cpf, telefone, email))
            connection.commit()
            st.success("Pessoa adicionada com sucesso!")
        except Error as e:
            st.error(f"Erro ao adicionar pessoa: {e}")
        finally:
            connection.close()

def delete_pessoa(id_pessoa):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Pessoa WHERE ID_Pessoa = %s", (id_pessoa,))
            connection.commit()
            st.success("Pessoa deletada com sucesso!")
        except Error as e:
            st.error(f"Erro ao deletar pessoa: {e}")
        finally:
            connection.close()

def update_pessoa(id_pessoa, nome, cpf, telefone, email):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE Pessoa SET Nome = %s, CPF = %s, Telefone = %s, Email = %s WHERE ID_Pessoa = %s", 
                           (nome, cpf, telefone, email, id_pessoa))
            connection.commit()
            st.success("Pessoa atualizada com sucesso!")
        except Error as e:
            st.error(f"Erro ao atualizar pessoa: {e}")
        finally:
            connection.close()

# Funções de CRUD para Cliente
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

def delete_cliente(id_cliente):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Cliente WHERE ID_Cliente = %s", (id_cliente,))
            connection.commit()
            st.success("Cliente deletado com sucesso!")
        except Error as e:
            st.error(f"Erro ao deletar cliente: {e}")
        finally:
            connection.close()

def update_cliente(id_cliente, id_pessoa):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE Cliente SET ID_Pessoa = %s WHERE ID_Cliente = %s", 
                           (id_pessoa, id_cliente))
            connection.commit()
            st.success("Cliente atualizado com sucesso!")
        except Error as e:
            st.error(f"Erro ao atualizar cliente: {e}")
        finally:
            connection.close()

# Funções de CRUD para Vendedor
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

def delete_vendedor(id_vendedor):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Vendedor WHERE ID_Vendedor = %s", (id_vendedor,))
            connection.commit()
            st.success("Vendedor deletado com sucesso!")
        except Error as e:
            st.error(f"Erro ao deletar vendedor: {e}")
        finally:
            connection.close()

def update_vendedor(id_vendedor, id_pessoa, gerente_id):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE Vendedor SET ID_Pessoa = %s, Gerente_ID = %s WHERE ID_Vendedor = %s", 
                           (id_pessoa, gerente_id, id_vendedor))
            connection.commit()
            st.success("Vendedor atualizado com sucesso!")
        except Error as e:
            st.error(f"Erro ao atualizar vendedor: {e}")
        finally:
            connection.close()

# Funções de CRUD para Endereço
def fetch_all_enderecos():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Endereço")
            rows = cursor.fetchall()
            return rows
        except Error as e:
            st.error(f"Erro ao buscar registros de Endereço: {e}")
        finally:
            connection.close()
    return []

def add_endereco(rua, numero, cidade, estado, cep, id_cliente):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Endereço (Rua, Número, Cidade, Estado, CEP, ID_Cliente) VALUES (%s, %s, %s, %s, %s, %s)", 
                           (rua, numero, cidade, estado, cep, id_cliente))
            connection.commit()
            st.success("Endereço adicionado com sucesso!")
        except Error as e:
            st.error(f"Erro ao adicionar endereço: {e}")
        finally:
            connection.close()

def delete_endereco(id_endereco):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM Endereço WHERE ID_Endereço = %s", (id_endereco,))
            connection.commit()
            st.success("Endereço deletado com sucesso!")
        except Error as e:
            st.error(f"Erro ao deletar endereço: {e}")
        finally:
            connection.close()

def update_endereco(id_endereco, rua, numero, cidade, estado, cep, id_cliente):
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE Endereço SET Rua = %s, Número = %s, Cidade = %s, Estado = %s, CEP = %s, ID_Cliente = %s WHERE ID_Endereço = %s", 
                           (rua, numero, cidade, estado, cep, id_cliente, id_endereco))
            connection.commit()
            st.success("Endereço atualizado com sucesso!")
        except Error as e:
            st.error(f"Erro ao atualizar endereço: {e}")
        finally:
            connection.close()

# Interface Streamlit
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

# Deletar Pessoa
st.subheader("Deletar Pessoa")
with st.form("delete_pessoa_form"):
    id_pessoa_del = st.number_input("ID da Pessoa", min_value=1, step=1)
    submit_delete_pessoa = st.form_submit_button("Deletar Pessoa")
    if submit_delete_pessoa:
        delete_pessoa(id_pessoa_del)

# Atualizar Pessoa
st.subheader("Atualizar Pessoa")
with st.form("update_pessoa_form"):
    id_pessoa_upd = st.number_input("ID da Pessoa", min_value=1, step=1, key="id_pessoa_upd")
    nome_upd = st.text_input("Nome", key="nome_upd")
    cpf_upd = st.text_input("CPF", key="cpf_upd")
    telefone_upd = st.text_input("Telefone", key="telefone_upd")
    email_upd = st.text_input("Email", key="email_upd")
    submit_update_pessoa = st.form_submit_button("Atualizar Pessoa")
    if submit_update_pessoa:
        update_pessoa(id_pessoa_upd, nome_upd, cpf_upd, telefone_upd, email_upd)

# Adicionar Cliente
st.subheader("Adicionar Novo Cliente")
with st.form("add_cliente_form"):
    id_pessoa_cliente = st.number_input("ID da Pessoa do Cliente", min_value=1, step=1)
    submit_add_cliente = st.form_submit_button("Adicionar Cliente")
    if submit_add_cliente:
        add_cliente(id_pessoa_cliente)

# Deletar Cliente
st.subheader("Deletar Cliente")
with st.form("delete_cliente_form"):
    id_cliente_del = st.number_input("ID do Cliente", min_value=1, step=1)
    submit_delete_cliente = st.form_submit_button("Deletar Cliente")
    if submit_delete_cliente:
        delete_cliente(id_cliente_del)

# Atualizar Cliente
st.subheader("Atualizar Cliente")
with st.form("update_cliente_form"):
    id_cliente_upd = st.number_input("ID do Cliente", min_value=1, step=1, key="id_cliente_upd")
    id_pessoa_upd = st.number_input("ID da Pessoa", min_value=1, step=1, key="id_pessoa_cliente_upd")
    submit_update_cliente = st.form_submit_button("Atualizar Cliente")
    if submit_update_cliente:
        update_cliente(id_cliente_upd, id_pessoa_upd)

# Adicionar Vendedor
st.subheader("Adicionar Novo Vendedor")
with st.form("add_vendedor_form"):
    id_pessoa_vendedor = st.number_input("ID da Pessoa do Vendedor", min_value=1, step=1)
    gerente_id = st.number_input("ID do Gerente (se aplicável)", min_value=0, step=1)
    submit_add_vendedor = st.form_submit_button("Adicionar Vendedor")
    if submit_add_vendedor:
        add_vendedor(id_pessoa_vendedor, gerente_id)

# Deletar Vendedor
st.subheader("Deletar Vendedor")
with st.form("delete_vendedor_form"):
    id_vendedor_del = st.number_input("ID do Vendedor", min_value=1, step=1)
    submit_delete_vendedor = st.form_submit_button("Deletar Vendedor")
    if submit_delete_vendedor:
        delete_vendedor(id_vendedor_del)

# Atualizar Vendedor
st.subheader("Atualizar Vendedor")
with st.form("update_vendedor_form"):
    id_vendedor_upd = st.number_input("ID do Vendedor", min_value=1, step=1, key="id_vendedor_upd")
    id_pessoa_vendedor_upd = st.number_input("ID da Pessoa do Vendedor", min_value=1, step=1, key="id_pessoa_vendedor_upd")
    gerente_id_upd = st.number_input("ID do Gerente (se aplicável)", min_value=0, step=1, key="gerente_id_upd")
    submit_update_vendedor = st.form_submit_button("Atualizar Vendedor")
    if submit_update_vendedor:
        update_vendedor(id_vendedor_upd, id_pessoa_vendedor_upd, gerente_id_upd)

# Adicionar Endereço
st.subheader("Adicionar Novo Endereço")
with st.form("add_endereco_form"):
    rua = st.text_input("Rua")
    numero = st.number_input("Número", min_value=1, step=1)
    cidade = st.text_input("Cidade")
    estado = st.text_input("Estado")
    cep = st.text_input("CEP")
    id_cliente = st.number_input("ID do Cliente", min_value=1, step=1)
    submit_add_endereco = st.form_submit_button("Adicionar Endereço")
    if submit_add_endereco:
        add_endereco(rua, numero, cidade, estado, cep, id_cliente)

# Deletar Endereço
st.subheader("Deletar Endereço")
with st.form("delete_endereco_form"):
    id_endereco_del = st.number_input("ID do Endereço", min_value=1, step=1)
    submit_delete_endereco = st.form_submit_button("Deletar Endereço")
    if submit_delete_endereco:
        delete_endereco(id_endereco_del)

# Atualizar Endereço
st.subheader("Atualizar Endereço")
with st.form("update_endereco_form"):
    id_endereco_upd = st.number_input("ID do Endereço", min_value=1, step=1, key="id_endereco_upd")
    rua_upd = st.text_input("Rua", key="rua_upd")
    numero_upd = st.number_input("Número", min_value=1, step=1, key="numero_upd")
    cidade_upd = st.text_input("Cidade", key="cidade_upd")
    estado_upd = st.text_input("Estado", key="estado_upd")
    cep_upd = st.text_input("CEP", key="cep_upd")
    id_cliente_upd = st.number_input("ID do Cliente", min_value=1, step=1, key="id_cliente_upd")
    submit_update_endereco = st.form_submit_button("Atualizar Endereço")
    if submit_update_endereco:
        update_endereco(id_endereco_upd, rua_upd, numero_upd, cidade_upd, estado_upd, cep_upd, id_cliente_upd)

# Exibição de Dados
st.subheader("Lista de Pessoas")
pessoas = fetch_all_pessoas()
if pessoas:
    st.table(pessoas)
else:
    st.write("Nenhuma pessoa encontrada.")

st.subheader("Lista de Clientes")
clientes = fetch_all_clientes()
if clientes:
    st.table(clientes)
else:
    st.write("Nenhum cliente encontrado.")

st.subheader("Lista de Vendedores")
vendedores = fetch_all_vendedores()
if vendedores:
    st.table(vendedores)
else:
    st.write("Nenhum vendedor encontrado.")

st.subheader("Lista de Endereços")
enderecos = fetch_all_enderecos()
if enderecos:
    st.table(enderecos)
else:
    st.write("Nenhum endereço encontrado.")
