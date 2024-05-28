# Projeto_BD: GFC Veículos

# Relatório Até o Momento do Processo de Desenvolvimento do trabalho de banco de dados para GFC Veículos:

## Mini Mundo da GFC Veículos: 

![Captura de tela 2024-05-22 172448](https://github.com/Craudi01/Projeto_BD/assets/152215002/56f89e30-8933-47eb-8518-d6b5e74643d1)

A GFC Veículos é uma empresa especializada na comercialização de veículos novos e usados. Além das vendas, a empresa oferece serviços de financiamento e manutenção para os seus clientes. A empresa possui uma equipe de vendedores responsáveis por conduzir as transações e manter o relacionamento com os clientes. A GFC Veículos mantém registros detalhados de clientes, vendedores, veículos, vendas, financiamentos, manutenções, acessórios e endereços

## Modelo Conceitual:

1. Identificação das Entidades Principais
Etapa: Identificamos os principais objetos do sistema que possuem existência própria e são relevantes para o negócio.
Entidades:

Pessoa
Cliente
Vendedor
Endereço
Veículo
Venda
Financiamento
Manutenção
Acessório
2. Definição dos Atributos das Entidades
Etapa: Para cada entidade, atribuímos características específicas que as definem.
Atributos:

Pessoa: ID_Pessoa, Nome, CPF, Telefone, Email
Cliente: ID_Cliente, ID_Pessoa
Vendedor: ID_Vendedor, ID_Pessoa, Gerente_ID
Endereço: ID_Endereço, Rua, Número, Cidade, Estado, CEP, ID_Cliente
Veículo: ID_Veículo, Modelo, Ano, Cor, Preço
Venda: ID_Venda, Data_Venda, Valor_Total, Forma_Pagamento, ID_Cliente, ID_Vendedor
Financiamento: ID_Financiamento, ID_Venda, Instituição_Financeira, Número_Parcelas, Valor_Parcela
Manutenção: ID_Manutenção, Data_Manutenção, Tipo_Manutenção, Custo, ID_Veículo, ID_Cliente
Acessório: ID_Acessório, Nome, Descrição
3. Identificação dos Relacionamentos Entre Entidades
Etapa: Determinamos como as entidades se relacionam entre si.
Relacionamentos:

Cliente - Venda: Realiza vendas (1:N)
Vendedor - Venda: Faz vendas (1:N)
Venda - Veículo: Inclui veículos (N:N)
Venda - Financiamento: Tem financiamento (1:1)
Veículo - Manutenção: Recebe manutenções (1:N)
Cliente - Endereço: Tem endereços (1:N)
Veículo - Acessório: Possui acessórios (N:N)
Vendedor - Vendedor: Gerencia vendedores (1:N)
4. Definição das Cardinalidades
Etapa: Especificamos as regras de quantidade nos relacionamentos.
Cardinalidades:

Cliente - Venda: 1 Cliente : N Vendas
Vendedor - Venda: 1 Vendedor : N Vendas
Venda - Veículo: N Vendas : N Veículos
Venda - Financiamento: 1 Venda : 1 Financiamento
Veículo - Manutenção: 1 Veículo : N Manutenções
Cliente - Endereço: 1 Cliente : N Endereços
Veículo - Acessório: N Veículos : N Acessórios
Vendedor - Vendedor: 1 Vendedor : N Vendedores gerenciados
5. Identificação de Heranças
Etapa: Definimos as relações de herança (superclasse/subclasse).
Heranças:

Pessoa como superclasse de Cliente e Vendedor
6. Identificação de Entidades Fracas e Auto-relacionamentos
Etapa: Identificamos entidades que dependem de outras e auto-relacionamentos.
Entidade Fraca:

Endereço depende de Cliente
Auto-relacionamento:
Vendedor gerencia outros Vendedores
7. Ilustração do Diagrama ER
Etapa: Visualizamos o modelo conceitual com entidades, atributos, e relacionamentos em um diagrama ER.

Entidades representadas por retângulos.
Atributos representados por elipses conectadas aos retângulos.
Relacionamentos representados por losangos conectando as entidades.
Cardinalidades indicadas ao lado das linhas de relacionamento.
Chaves Primárias (PK) e Chaves Estrangeiras (FK) anotadas nas entidades.
Entidades fracas e heranças visualizadas adequadamente.
Resumo dos Relacionamentos
Cliente - Venda: Realiza vendas (1:N)
Vendedor - Venda: Faz vendas (1:N)
Venda - Veículo: Inclui veículos (N:N)
Venda - Financiamento: Tem financiamento (1:1)
Veículo - Manutenção: Recebe manutenções (1:N)
Cliente - Endereço: Tem endereços (1:N)
Veículo - Acessório: Possui acessórios (N:N)
Vendedor - Vendedor: Gerencia vendedores (1:N)


## Imagem Modelo Conceitual:

![Trabalho_bd](https://github.com/Craudi01/Projeto_BD/assets/152215002/9ae01cbf-d01d-4ad9-858c-af358b98779f)


## Modelo Lógico:

1. Transformação das Entidades em Tabelas
Etapa: Convertendo entidades do modelo conceitual para tabelas no modelo lógico, incluindo os atributos e identificando as chaves primárias (PK) e estrangeiras (FK).

Tabelas e Atributos:

Pessoa:
Atributos: ID_Pessoa (PK), Nome, CPF, Telefone, Email
Cliente:
Atributos: ID_Cliente (PK), ID_Pessoa (FK)
Vendedor:
Atributos: ID_Vendedor (PK), ID_Pessoa (FK), Gerente_ID (FK)
Endereço:
Atributos: ID_Endereço (PK), Rua, Número, Cidade, Estado, CEP, ID_Cliente (FK)
Veículo:
Atributos: ID_Veículo (PK), Modelo, Ano, Cor, Preço
Venda:
Atributos: ID_Venda (PK), Data_Venda, Valor_Total, Forma_Pagamento, ID_Cliente (FK), ID_Vendedor (FK)
Financiamento:
Atributos: ID_Financiamento (PK), ID_Venda (FK), Instituição_Financeira, Número_Parcelas, Valor_Parcela
Manutenção:
Atributos: ID_Manutenção (PK), Data_Manutenção, Tipo_Manutenção, Custo, ID_Veículo (FK), ID_Cliente (FK)
Acessório:
Atributos: ID_Acessório (PK), Nome, Descrição
2. Definição dos Relacionamentos
Etapa: Definimos os relacionamentos entre as tabelas usando chaves estrangeiras (FK) e asseguramos a integridade referencial.

Relacionamentos e Cardinalidades:

Cliente - Venda:
Descrição: Realiza vendas.
Cardinalidade: 1:N
Chave Estrangeira: ID_Cliente em Venda.
Vendedor - Venda:
Descrição: Faz vendas.
Cardinalidade: 1:N
Chave Estrangeira: ID_Vendedor em Venda.
Venda - Veículo:
Descrição: Inclui veículos.
Cardinalidade: N:N
Tabela Associativa: Venda_Veículo com ID_Venda (FK), ID_Veículo (FK).
Venda - Financiamento:
Descrição: Tem financiamento.
Cardinalidade: 1:1
Chave Estrangeira: ID_Venda em Financiamento.
Veículo - Manutenção:
Descrição: Recebe manutenções.
Cardinalidade: 1:N
Chave Estrangeira: ID_Veículo em Manutenção.
Cliente - Endereço:
Descrição: Tem endereços.
Cardinalidade: 1:N
Chave Estrangeira: ID_Cliente em Endereço.
Veículo - Acessório:
Descrição: Possui acessórios.
Cardinalidade: N:N
Tabela Associativa: Veículo_Acessório com ID_Veículo (FK), ID_Acessório (FK).
Vendedor - Vendedor:
Descrição: Gerencia vendedores.
Cardinalidade: 1:N
Chave Estrangeira: Gerente_ID em Vendedor.
3. Aplicação de Restrições e Regras de Integridade
Etapa: Definimos restrições para garantir a integridade dos dados e regras específicas para atributos.

Restrições:

Pessoa:
CPF: UNIQUE
Email: UNIQUE
Cliente:
ID_Pessoa: FK
Vendedor:
ID_Pessoa: FK
Gerente_ID: FK
Endereço:
ID_Cliente: FK
Venda:
ID_Cliente: FK
ID_Vendedor: FK
Financiamento:
ID_Venda: FK
Manutenção:
ID_Veículo: FK
ID_Cliente: FK
Venda_Veículo:
ID_Venda: FK
ID_Veículo: FK
Veículo_Acessório:
ID_Veículo: FK
ID_Acessório: FK
4. Criação de Tabelas Associativas para Relacionamentos N:N
Etapa: Implementamos tabelas associativas para representar relacionamentos muitos-para-muitos.

Tabelas Associativas:

Venda_Veículo:
Atributos: ID_Venda (FK), ID_Veículo (FK)
Veículo_Acessório:
Atributos: ID_Veículo (FK), ID_Acessório (FK)
Resumo dos Relacionamentos e Cardinalidades
Cliente - Venda:

Realiza vendas: 1:N
Chave Estrangeira: ID_Cliente em Venda.
Vendedor - Venda:

Faz vendas: 1:N
Chave Estrangeira: ID_Vendedor em Venda.
Venda - Veículo:

Inclui veículos: N:N
Tabela Associativa: Venda_Veículo com ID_Venda (FK), ID_Veículo (FK).
Venda - Financiamento:

Tem financiamento: 1:1
Chave Estrangeira: ID_Venda em Financiamento.
Veículo - Manutenção:

Recebe manutenções: 1:N
Chave Estrangeira: ID_Veículo em Manutenção.
Cliente - Endereço:

Tem endereços: 1:N
Chave Estrangeira: ID_Cliente em Endereço.
Veículo - Acessório:

Possui acessórios: N:N
Tabela Associativa: Veículo_Acessório com ID_Veículo (FK), ID_Acessório (FK).
Vendedor - Vendedor:

Gerencia vendedores: 1:N
Chave Estrangeira: Gerente_ID em Vendedor.



## Imagem Modelo Lógico:

![Trabalho_bd_Logico](https://github.com/Craudi01/Projeto_BD/assets/152215002/d97cc1cb-f111-4171-b457-5a43730ef310)



## Codigo do Banco de dados: 

CREATE DATABASE projetoBD;

USE projetoBD;
CREATE TABLE Pessoa (
    ID_Pessoa INT PRIMARY KEY,
    Nome VARCHAR(100),
    CPF CHAR(11) UNIQUE,
    Telefone VARCHAR(15),
    Email VARCHAR(100)
);

CREATE TABLE Cliente (
    ID_Cliente INT PRIMARY KEY,
    ID_Pessoa INT,
    FOREIGN KEY (ID_Pessoa) REFERENCES Pessoa(ID_Pessoa)
);

CREATE TABLE Vendedor (
    ID_Vendedor INT PRIMARY KEY,
    ID_Pessoa INT,
    Gerente_ID INT,
    FOREIGN KEY (ID_Pessoa) REFERENCES Pessoa(ID_Pessoa),
    FOREIGN KEY (Gerente_ID) REFERENCES Vendedor(ID_Vendedor)
);

CREATE TABLE Endereço (
    ID_Endereço INT PRIMARY KEY,
    Rua VARCHAR(100),
    Número INT,
    Cidade VARCHAR(50),
    Estado CHAR(2),
    CEP CHAR(8),
    ID_Cliente INT,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente)
);

CREATE TABLE Veículo (
    ID_Veículo INT PRIMARY KEY,
    Modelo VARCHAR(50),
    Ano YEAR,
    Cor VARCHAR(20),
    Preço DECIMAL(10, 2)
);

CREATE TABLE Venda (
    ID_Venda INT PRIMARY KEY,
    Data_Venda DATE,
    Valor_Total DECIMAL(10, 2),
    Forma_Pagamento VARCHAR(20),
    ID_Cliente INT,
    ID_Vendedor INT,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente),
    FOREIGN KEY (ID_Vendedor) REFERENCES Vendedor(ID_Vendedor)
);

CREATE TABLE Financiamento (
    ID_Financiamento INT PRIMARY KEY,
    ID_Venda INT,
    Instituição_Financeira VARCHAR(100),
    Número_Parcelas INT,
    Valor_Parcela DECIMAL(10, 2),
    FOREIGN KEY (ID_Venda) REFERENCES Venda(ID_Venda)
);

CREATE TABLE Manutenção (
    ID_Manutenção INT PRIMARY KEY,
    Data_Manutenção DATE,
    Tipo_Manutenção VARCHAR(50),
    Custo DECIMAL(10, 2),
    ID_Veículo INT,
    ID_Cliente INT,
    FOREIGN KEY (ID_Veículo) REFERENCES Veículo(ID_Veículo),
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente)
);

CREATE TABLE Acessório (
    ID_Acessório INT PRIMARY KEY,
    Nome VARCHAR(50),
    Descrição TEXT
);

CREATE TABLE Veículo_Acessório (
    ID_Veículo INT,
    ID_Acessório INT,
    PRIMARY KEY (ID_Veículo, ID_Acessório),
    FOREIGN KEY (ID_Veículo) REFERENCES Veículo(ID_Veículo),
    FOREIGN KEY (ID_Acessório) REFERENCES Acessório(ID_Acessório)
);

CREATE TABLE Venda_Veículo (
    ID_Venda INT,
    ID_Veículo INT,
    PRIMARY KEY (ID_Venda, ID_Veículo),
    FOREIGN KEY (ID_Venda) REFERENCES Venda(ID_Venda),
    FOREIGN KEY (ID_Veículo) REFERENCES Veículo(ID_Veículo)
);

