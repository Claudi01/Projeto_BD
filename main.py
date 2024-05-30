import mysql.connector
import streamlit as st


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="GabrielRoma4215!",
    database="projetoBD"
)
mycursor = mydb.cursor()

print("Connection Established")


try:
    mycursor.execute("""
        CREATE TRIGGER after_update_venda
        AFTER UPDATE ON Venda
        FOR EACH ROW
        BEGIN
            IF OLD.Valor_Total != NEW.Valor_Total THEN
                INSERT INTO Log_Alteracao_Venda (ID_Venda, Valor_Total_Antigo, Valor_Total_Novo, Data_Alteracao)
                VALUES (OLD.ID_Venda, OLD.Valor_Total, NEW.Valor_Total, NOW());
            END IF;
        END;
    """)
    mydb.commit()
    print("Trigger created successfully!")
except mysql.connector.Error as err:
    print("Error creating trigger:", err)


def main():
    st.sidebar.title("Menu")
    page = st.sidebar.selectbox("Selecione a Página", ["Venda", "Administrador"])
    
    if page == "Venda":
        venda_page()
    elif page == "Administrador":
        administrador_page()


def venda_page():
    st.title("GFC Veículos - Venda")
    st.subheader("Página de Venda")
    tabs = st.tabs(["Gerenciar Dados", "Buscar Vendas"])
    
    with tabs[0]:
        manage_dados()
    with tabs[1]:
        buscar_vendas()


def administrador_page():
    st.title("GFC Veículos - Administrador")
    st.subheader("Página do Administrador")
    tabs = st.tabs(["Gerenciar Pessoas", "Gerenciar Vendedores", "Gerenciar Clientes", "Gerenciar Veículos", "Gerenciar Acessórios", "Relatório"])
    
    with tabs[0]:
        manage_pessoas()
    with tabs[1]:
        manage_vendedores()
    with tabs[2]:
        manage_clientes()
    with tabs[3]:
        manage_veiculos()
    with tabs[4]:
        manage_acessorios()
    with tabs[5]:
        relatorio_page()


def relatorio_page():
    st.subheader("Relatório")
    st.write("Insira o ID do vendedor para gerar o relatório:")
    id_vendedor = st.text_input("ID do Vendedor")

    if st.button("Gerar Relatório"):
        relatorio = relatorio_funcionario_mysql(id_vendedor)
        if relatorio:
            st.write(relatorio)
        else:
            st.write("Nenhum dado encontrado para gerar o relatório.")


def relatorio_funcionario_mysql(id_vendedor):
    try:
        mycursor.callproc("relatorio_funcionario")
        for result in mycursor.stored_results():
            relatorio = result.fetchall()
        return relatorio
    except mysql.connector.Error as err:
        print("Erro ao gerar o relatório:", err)
        return None


def manage_pessoas():
    st.subheader("Gerenciar Pessoas")
    option = st.selectbox("Selecione uma operação", ("Criar", "Ler", "Atualizar", "Apagar"), key="pessoas_selectbox")

    if option == "Criar":
        with st.form(key="criar_pessoa"):
            st.subheader("Adicionar uma Pessoa")
            id_pessoa = st.text_input("ID da Pessoa")
            nome = st.text_input("Nome")
            cpf = st.text_input("CPF")
            telefone = st.text_input("Telefone")
            email = st.text_input("Email")
            submit_button = st.form_submit_button(label="Adicionar")
            
            if submit_button:
                sql = "INSERT INTO Pessoa (ID_Pessoa, Nome, CPF, Telefone, Email) VALUES (%s, %s, %s, %s, %s)"
                val = (id_pessoa, nome, cpf, telefone, email)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Pessoa Adicionada com Sucesso!")

    elif option == "Ler":
        st.subheader("Ver Pessoas")
        mycursor.execute("SELECT * FROM Pessoa")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Atualizar":
        with st.form(key="atualizar_pessoa"):
            st.subheader("Atualizar Pessoa")
            id_pessoa = st.text_input("ID da Pessoa")
            campo = st.selectbox("Campo para Atualizar", ["Nome", "CPF", "Telefone", "Email"], key="pessoa_update_selectbox")
            novo_valor = st.text_input(f"Novo Valor para {campo}")
            submit_button = st.form_submit_button(label="Atualizar")
            
            if submit_button:
                sql = f"UPDATE Pessoa SET {campo}=%s WHERE ID_Pessoa=%s"
                val = (novo_valor, id_pessoa)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Pessoa Atualizada com Sucesso!")

    elif option == "Apagar":
        with st.form(key="apagar_pessoa"):
            st.subheader("Apagar Pessoa")
            id_pessoa = st.text_input("ID da Pessoa")
            submit_button = st.form_submit_button(label="Apagar")
            
            if submit_button:
                sql = "DELETE FROM Pessoa WHERE ID_Pessoa=%s"
                val = (id_pessoa,)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Pessoa Apagada com Sucesso!")


def manage_vendedores():
    st.subheader("Gerenciar Vendedores")
    option = st.selectbox("Selecione uma operação", ("Criar", "Ler", "Atualizar", "Apagar"), key="vendedores_selectbox")

    if option == "Criar":
        with st.form(key="criar_vendedor"):
            st.subheader("Adicionar um Vendedor")
            id_vendedor = st.text_input("ID do Vendedor")
            id_pessoa = st.text_input("ID da Pessoa")
            gerente_id = st.text_input("ID do Gerente")
            submit_button = st.form_submit_button(label="Adicionar")
            
            if submit_button:
                sql = "INSERT INTO Vendedor (ID_Vendedor, ID_Pessoa, Gerente_ID) VALUES (%s, %s, %s)"
                val = (id_vendedor, id_pessoa, gerente_id)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Vendedor Adicionado com Sucesso!")

    elif option == "Ler":
        st.subheader("Ver Vendedores")
        mycursor.execute("SELECT * FROM Vendedor")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Atualizar":
        with st.form(key="atualizar_vendedor"):
            st.subheader("Atualizar Vendedor")
            old_id = st.text_input("ID Antigo do Vendedor")
            new_id = st.text_input("Novo ID do Vendedor")
            submit_button = st.form_submit_button(label="Atualizar")
            
            if submit_button:
                sql = "UPDATE Vendedor SET ID_Vendedor=%s WHERE ID_Vendedor=%s"
                val = (new_id, old_id)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Vendedor Atualizado com Sucesso!")

    elif option == "Apagar":
        with st.form(key="apagar_vendedor"):
            st.subheader("Apagar Vendedor")
            id_vendedor = st.text_input("ID do Vendedor")
            submit_button = st.form_submit_button(label="Apagar")
            
            if submit_button:
                sql = "DELETE FROM Vendedor WHERE ID_Vendedor=%s"
                val = (id_vendedor,)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Vendedor Apagado com Sucesso!")


def manage_clientes():
    st.subheader("Gerenciar Clientes")
    option = st.selectbox("Selecione uma operação", ("Criar", "Ler", "Atualizar", "Apagar"), key="clientes_selectbox")

    if option == "Criar":
        with st.form(key="criar_cliente"):
            st.subheader("Adicionar um Cliente")
            id_cliente = st.text_input("ID do Cliente")
            id_pessoa = st.text_input("ID da Pessoa")
            submit_button = st.form_submit_button(label="Adicionar")
            
            if submit_button:
                # Verificar se ID_Pessoa existe na tabela Pessoa
                try:
                    mycursor.execute("SELECT COUNT(*) FROM Pessoa WHERE ID_Pessoa = %s", (id_pessoa,))
                    pessoa_exists = mycursor.fetchone()[0]
                    
                    if pessoa_exists > 0:
                        try:
                            sql = "INSERT INTO Cliente (ID_Cliente, ID_Pessoa) VALUES (%s, %s)"
                            val = (id_cliente, id_pessoa)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            st.success("Cliente Adicionado com Sucesso!")
                        except mysql.connector.Error as err:
                            st.error(f"Erro ao adicionar cliente: {err}")
                    else:
                        st.error("ID_Pessoa não existe na tabela Pessoa.")
                except mysql.connector.Error as err:
                    st.error(f"Erro ao verificar existência da pessoa: {err}")

    elif option == "Ler":
        st.subheader("Ver Clientes")
        mycursor.execute("SELECT * FROM Cliente")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Atualizar":
        with st.form(key="atualizar_cliente"):
            st.subheader("Atualizar Cliente")
            id_cliente = st.text_input("ID do Cliente")
            campo = st.selectbox("Campo para Atualizar", ["ID_Pessoa"], key="cliente_update_selectbox")
            novo_valor = st.text_input(f"Novo Valor para {campo}")
            submit_button = st.form_submit_button(label="Atualizar")
            
            if submit_button:
                sql = f"UPDATE Cliente SET {campo}=%s WHERE ID_Cliente=%s"
                val = (novo_valor, id_cliente)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Cliente Atualizado com Sucesso!")

    elif option == "Apagar":
        with st.form(key="apagar_cliente"):
            st.subheader("Apagar Cliente")
            id_cliente = st.text_input("ID do Cliente")
            submit_button = st.form_submit_button(label="Apagar")
            
            if submit_button:
                sql = "DELETE FROM Cliente WHERE ID_Cliente=%s"
                val = (id_cliente,)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Cliente Apagado com Sucesso!")


def manage_veiculos():
    st.subheader("Gerenciar Veículos")
    option = st.selectbox("Selecione uma operação", ("Criar", "Ler", "Atualizar", "Apagar"), key="veiculos_selectbox")

    if option == "Criar":
        with st.form(key="criar_veiculo"):
            st.subheader("Adicionar um Veículo")
            id_veiculo = st.text_input("ID do Veículo")
            modelo = st.text_input("Modelo")
            marca = st.text_input("Marca")
            ano = st.text_input("Ano")
            preco = st.text_input("Preço")
            submit_button = st.form_submit_button(label="Adicionar")
            
            if submit_button:
                sql = "INSERT INTO Veiculo (ID_Veiculo, Modelo, Marca, Ano, Preco) VALUES (%s, %s, %s, %s, %s)"
                val = (id_veiculo, modelo, marca, ano, preco)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Veículo Adicionado com Sucesso!")

    elif option == "Ler":
        st.subheader("Ver Veículos")
        mycursor.execute("SELECT * FROM Veiculo")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Atualizar":
        with st.form(key="atualizar_veiculo"):
            st.subheader("Atualizar Veículo")
            id_veiculo = st.text_input("ID do Veículo")
            campo = st.selectbox("Campo para Atualizar", ["Modelo", "Marca", "Ano", "Preço"], key="veiculo_update_selectbox")
            novo_valor = st.text_input(f"Novo Valor para {campo}")
            submit_button = st.form_submit_button(label="Atualizar")
            
            if submit_button:
                sql = f"UPDATE Veiculo SET {campo}=%s WHERE ID_Veiculo=%s"
                val = (novo_valor, id_veiculo)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Veículo Atualizado com Sucesso!")

    elif option == "Apagar":
        with st.form(key="apagar_veiculo"):
            st.subheader("Apagar Veículo")
            id_veiculo = st.text_input("ID do Veículo")
            submit_button = st.form_submit_button(label="Apagar")
            
            if submit_button:
                sql = "DELETE FROM Veiculo WHERE ID_Veiculo=%s"
                val = (id_veiculo,)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Veículo Apagado com Sucesso!")


def manage_acessorios():
    st.subheader("Gerenciar Acessórios")
    option = st.selectbox("Selecione uma operação", ("Criar", "Ler", "Atualizar", "Apagar"), key="acessorios_selectbox")

    if option == "Criar":
        with st.form(key="criar_acessorio"):
            st.subheader("Adicionar um Acessório")
            id_acessorio = st.text_input("ID do Acessório")
            descricao = st.text_input("Descrição")
            preco = st.text_input("Preço")
            submit_button = st.form_submit_button(label="Adicionar")
            
            if submit_button:
                sql = "INSERT INTO Acessorio (ID_Acessorio, Descricao, Preco) VALUES (%s, %s, %s)"
                val = (id_acessorio, descricao, preco)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Acessório Adicionado com Sucesso!")

    elif option == "Ler":
        st.subheader("Ver Acessórios")
        mycursor.execute("SELECT * FROM Acessorio")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Atualizar":
        with st.form(key="atualizar_acessorio"):
            st.subheader("Atualizar Acessório")
            id_acessorio = st.text_input("ID do Acessório")
            campo = st.selectbox("Campo para Atualizar", ["Descrição", "Preço"], key="acessorio_update_selectbox")
            novo_valor = st.text_input(f"Novo Valor para {campo}")
            submit_button = st.form_submit_button(label="Atualizar")
            
            if submit_button:
                sql = f"UPDATE Acessorio SET {campo}=%s WHERE ID_Acessorio=%s"
                val = (novo_valor, id_acessorio)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Acessório Atualizado com Sucesso!")

    elif option == "Apagar":
        with st.form(key="apagar_acessorio"):
            st.subheader("Apagar Acessório")
            id_acessorio = st.text_input("ID do Acessório")
            submit_button = st.form_submit_button(label="Apagar")
            
            if submit_button:
                sql = "DELETE FROM Acessorio WHERE ID_Acessorio=%s"
                val = (id_acessorio,)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Acessório Apagado com Sucesso!")


def manage_dados():
    st.subheader("Gerenciar Dados")
    st.write("Funções para criar, ler, atualizar e apagar dados no banco de dados.")


def buscar_vendas():
    st.subheader("Buscar Vendas")
    st.write("Insira o ID da venda que deseja buscar:")
    id_venda = st.text_input("ID da Venda")

    if st.button("Buscar"):
        mycursor.execute("SELECT * FROM Venda WHERE ID_Venda = %s", (id_venda,))
        result = mycursor.fetchone()
        if result:
            st.write(result)
        else:
            st.write("Nenhuma venda encontrada com esse ID.")

if __name__ == '__main__':
    main()
