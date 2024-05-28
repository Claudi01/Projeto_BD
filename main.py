import mysql.connector
import streamlit as st

# Conectar ao banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bradesco01",
    database="projetoBD"
)
mycursor = mydb.cursor()

print("Connection Established")

# Criação do Trigger
try:
    mycursor.execute("DELIMITER //")
    mycursor.execute("""
        CREATE TRIGGER after_update_venda
        AFTER UPDATE ON Venda
        FOR EACH ROW
        BEGIN
            IF OLD.Valor_Total != NEW.Valor_Total THEN
                INSERT INTO Log_Alteracao_Venda (ID_Venda, Valor_Total_Antigo, Valor_Total_Novo, Data_Alteracao)
                VALUES (OLD.ID_Venda, OLD.Valor_Total, NEW.Valor_Total, NOW());
            END IF;
        END//
    """)
    mycursor.execute("DELIMITER ;")
    mydb.commit()
    print("Trigger created successfully!")
except mysql.connector.Error as err:
    print("Error creating trigger:", err)

# Função principal
def main():
    relatorio_funcionario() 
    st.sidebar.title("Menu")
    page = st.sidebar.selectbox("Selecione a Página", ["Venda", "Administrador"])
    
    if page == "Venda":
        venda_page()
    elif page == "Administrador":
        administrador_page()

# Página de Vendas
def venda_page():
    st.title("Empresa de Vendas - Venda")
    st.subheader("Página de Venda")
    tabs = ["Gerenciar Dados", "Buscar Vendas"]  
    tab = st.selectbox("Selecione uma Função", tabs)

    if tab == "Gerenciar Dados":
        manage_dados()
    elif tab == "Buscar Vendas":  
        buscar_vendas()  

# Página do Administrador
def administrador_page():
    st.title("Empresa de Vendas - Administrador")
    st.subheader("Página do Administrador")
    tabs = ["Gerenciar Vendedores", "Gerenciar Clientes", "Gerenciar Veículos", "Gerenciar Acessórios", "Relatório"]
    tab = st.selectbox("Selecione uma Função", tabs)

    if tab == "Gerenciar Vendedores":
        manage_vendedores()
    elif tab == "Gerenciar Clientes":
        manage_clientes()
    elif tab == "Gerenciar Veículos":
        manage_veiculos()
    elif tab == "Gerenciar Acessórios":
        manage_acessorios()
    elif tab == "Relatório":
        relatorio_page()

# Página de Relatório
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

# Função de Relatório no MySQL
def relatorio_funcionario_mysql(id_vendedor):
    try:
        mycursor.callproc("relatorio_funcionario")
        for result in mycursor.stored_results():
            relatorio = result.fetchall()
        return relatorio
    except mysql.connector.Error as err:
        print("Erro ao gerar o relatório:", err)
        return None

# Função de Relatório
def relatorio_funcionario():
    try:
        mycursor.execute("DELIMITER //")
        mycursor.execute("""
            CREATE FUNCTION relatorio_funcionario()
            RETURNS TEXT
            BEGIN
                DECLARE relatorio TEXT;
                SET relatorio = '';

                SELECT CONCAT('ID do Vendedor: ', ID_Vendedor, ', Total de Vendas: ', COUNT(*))
                INTO relatorio
                FROM Venda
                GROUP BY ID_Vendedor
                HAVING COUNT(*) > 0;

                IF relatorio IS NULL THEN
                    SET relatorio = 'Nenhum dado encontrado para gerar o relatório.';
                END IF;

                RETURN relatorio;
            END//
        """)
        mycursor.execute("DELIMITER ;")
        mydb.commit()
        print("Function created successfully!")
    except mysql.connector.Error as err:
        print("Error creating function:", err)

# Gerenciar Vendedores
def manage_vendedores():
    st.subheader("Gerenciar Vendedores")
    option = st.selectbox("Selecione uma operação", ("Criar", "Ler", "Atualizar", "Apagar"))

    if option == "Criar":
        st.subheader("Adicionar um Vendedor")
        id_vendedor = st.text_input("ID do Vendedor")
        id_pessoa = st.text_input("ID da Pessoa")
        gerente_id = st.text_input("ID do Gerente")
        if st.button("Adicionar"):
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
        st.subheader("Atualizar Vendedor")
        old_id = st.text_input("ID Antigo do Vendedor")
        new_id = st.text_input("Novo ID do Vendedor")
        if st.button("Atualizar"):
            sql = "UPDATE Vendedor SET ID_Vendedor=%s WHERE ID_Vendedor=%s"
            val = (new_id, old_id)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Vendedor Atualizado com Sucesso!")

    elif option == "Apagar":
        st.subheader("Apagar Vendedor")
        id_vendedor = st.text_input("ID do Vendedor")
        if st.button("Apagar"):
            sql = "DELETE FROM Vendedor WHERE ID_Vendedor=%s"
            val = (id_vendedor,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Vendedor Apagado com Sucesso!")

# Gerenciar Clientes
def manage_clientes():
    st.subheader("Gerenciar Clientes")
    option = st.selectbox("Selecione uma operação", ("Criar", "Ler", "Atualizar", "Apagar"))

    if option == "Criar":
        st.subheader("Adicionar um Cliente")
        id_cliente = st.text_input("ID do Cliente")
        id_pessoa = st.text_input("ID da Pessoa")
        
        if st.button("Adicionar"):
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
                    st.error("ID_Pessoa não existe na tabela Pessoa. Por favor, adicione primeiro essa pessoa.")
            except mysql.connector.Error as err:
                st.error(f"Erro ao verificar ID_Pessoa: {err}")

    elif option == "Ler":
        st.subheader("Ver Clientes")
        try:
            mycursor.execute("SELECT * FROM Cliente")
            result = mycursor.fetchall()
            for row in result:
                st.write(row)
        except mysql.connector.Error as err:
            st.error(f"Erro ao ler clientes: {err}")

    elif option == "Atualizar":
        st.subheader("Atualizar Cliente")
        id_cliente = st.text_input("ID do Cliente")
        campo = st.selectbox("Campo para Atualizar", ["ID_Pessoa"])
        novo_valor = st.text_input(f"Novo Valor para {campo}")
        
        if st.button("Atualizar"):
            if campo == "ID_Pessoa":
                # Verificar se novo ID_Pessoa existe na tabela Pessoa
                try:
                    mycursor.execute("SELECT COUNT(*) FROM Pessoa WHERE ID_Pessoa = %s", (novo_valor,))
                    pessoa_exists = mycursor.fetchone()[0]
                    
                    if not pessoa_exists:
                        st.error("Novo ID_Pessoa não existe na tabela Pessoa. Por favor, adicione primeiro essa pessoa.")
                        return
                except mysql.connector.Error as err:
                    st.error(f"Erro ao verificar novo ID_Pessoa: {err}")
                    return
            
            try:
                sql = f"UPDATE Cliente SET {campo}=%s WHERE ID_Cliente=%s"
                val = (novo_valor, id_cliente)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Cliente Atualizado com Sucesso!")
            except mysql.connector.Error as err:
                st.error(f"Erro ao atualizar cliente: {err}")

    elif option == "Apagar":
        st.subheader("Apagar Cliente")
        id_cliente = st.text_input("ID do Cliente")
        if st.button("Apagar"):
            try:
                sql = "DELETE FROM Cliente WHERE ID_Cliente=%s"
                val = (id_cliente,)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Cliente Apagado com Sucesso!")
            except mysql.connector.Error as err:
                st.error(f"Erro ao apagar cliente: {err}")

# Gerenciar Veículos
def manage_veiculos():
    st.subheader("Gerenciar Veículos")
    option = st.selectbox("Selecione uma operação", ("Criar", "Ler", "Atualizar", "Apagar"))

    if option == "Criar":
        st.subheader("Adicionar um Veículo")
        id_veiculo = st.text_input("ID do Veículo")
        modelo = st.text_input("Modelo")
        ano = st.text_input("Ano")
        cor = st.text_input("Cor")
        preco = st.text_input("Preço")
        if st.button("Adicionar"):
            sql = "INSERT INTO Veículo (ID_Veículo, Modelo, Ano, Cor, Preço) VALUES (%s, %s, %s, %s, %s)"
            val = (id_veiculo, modelo, ano, cor, preco)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Veículo Adicionado com Sucesso!")

    elif option == "Ler":
        st.subheader("Ver Veículos")
        mycursor.execute("SELECT * FROM Veículo")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Atualizar":
        st.subheader("Atualizar Veículo")
        id_veiculo = st.text_input("ID do Veículo")
        campo = st.selectbox("Campo para Atualizar", ["Modelo", "Ano", "Cor", "Preço"])
        novo_valor = st.text_input(f"Novo Valor para {campo}")
        if st.button("Atualizar"):
            sql = f"UPDATE Veículo SET {campo}=%s WHERE ID_Veículo=%s"
            val = (novo_valor, id_veiculo)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Veículo Atualizado com Sucesso!")

    elif option == "Apagar":
        st.subheader("Apagar Veículo")
        id_veiculo = st.text_input("ID do Veículo")
        if st.button("Apagar"):
            sql = "DELETE FROM Veículo WHERE ID_Veículo=%s"
            val = (id_veiculo,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Veículo Apagado com Sucesso!")

# Gerenciar Acessórios
def manage_acessorios():
    st.subheader("Gerenciar Acessórios")
    option = st.selectbox("Selecione uma operação", ("Criar", "Ler", "Atualizar", "Apagar"))

    if option == "Criar":
        st.subheader("Adicionar um Acessório")
        id_acessorio = st.text_input("ID do Acessório")
        preco = st.text_input("Nome")
        descricao = st.text_input("Descrição")
        if st.button("Adicionar"):
            sql = "INSERT INTO Acessório (ID_Acessório, Nome, Descrição) VALUES (%s, %s, %s)"
            val = (id_acessorio, nome, descricao)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Acessório Adicionado com Sucesso!")

    elif option == "Ler":
        st.subheader("Ver Acessórios")
        mycursor.execute("SELECT * FROM Acessório")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Atualizar":
        st.subheader("Atualizar Acessório")
        id_acessorio = st.text_input("ID do Acessório")
        campo = st.selectbox("Campo para Atualizar", ["Descrição", "Preço"])
        novo_valor = st.text_input(f"Novo Valor para {campo}")
        if st.button("Atualizar"):
            sql = f"UPDATE Acessório SET {campo}=%s WHERE ID_Acessório=%s"
            val = (novo_valor, id_acessorio)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Acessório Atualizado com Sucesso!")

    elif option == "Apagar":
        st.subheader("Apagar Acessório")
        id_acessorio = st.text_input("ID do Acessório")
        if st.button("Apagar"):
            sql = "DELETE FROM Acessório WHERE ID_Acessório=%s"
            val = (id_acessorio,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Acessório Apagado com Sucesso!")

# Buscar Vendas
def buscar_vendas():
    st.subheader("Buscar Vendas")
    id_venda = st.text_input("ID da Venda")
    if st.button("Buscar"):
        sql = "SELECT * FROM Venda WHERE ID_Venda = %s"
        val = (id_venda,)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        if result:
            for row in result:
                st.write(row)
        else:
            st.write("Nenhuma venda encontrada com o ID fornecido.")

# Gerenciar Dados da Venda
def manage_dados():
    st.subheader("Gerenciar Dados da Venda")
    option = st.selectbox("Selecione uma operação", ("Criar", "Ler", "Atualizar", "Apagar"))

    if option == "Criar":
        st.subheader("Adicionar uma Venda")
        id_venda = st.text_input("ID da Venda")
        id_vendedor = st.text_input("ID do Vendedor")
        id_cliente = st.text_input("ID do Cliente")
        data_venda = st.text_input("Data da Venda")
        valor_total = st.text_input("Valor Total")
        if st.button("Adicionar"):
            sql = "INSERT INTO Venda (ID_Venda, ID_Vendedor, ID_Cliente, Data_Venda, Valor_Total) VALUES (%s, %s, %s, %s, %s)"
            val = (id_venda, id_vendedor, id_cliente, data_venda, valor_total)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Venda Adicionada com Sucesso!")

    elif option == "Ler":
        st.subheader("Ver Vendas")
        mycursor.execute("SELECT * FROM Venda")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option == "Atualizar":
        st.subheader("Atualizar Venda")
        id_venda = st.text_input("ID da Venda")
        campo = st.selectbox("Campo para Atualizar", ["ID_Vendedor", "ID_Cliente", "Data_Venda", "Valor_Total"])
        novo_valor = st.text_input(f"Novo Valor para {campo}")
        if st.button("Atualizar"):
            sql = f"UPDATE Venda SET {campo}=%s WHERE ID_Venda=%s"
            val = (novo_valor, id_venda)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Venda Atualizada com Sucesso!")

    elif option == "Apagar":
        st.subheader("Apagar Venda")
        id_venda = st.text_input("ID da Venda")
        if st.button("Apagar"):
            sql = "DELETE FROM Venda WHERE ID_Venda=%s"
            val = (id_venda,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Venda Apagada com Sucesso!")

if __name__ == "__main__":
    main()
