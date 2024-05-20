# Projeto_BD

##Relatório Até o Momento do Processo de Desenvolvimento do trabalho de banco de dados para GFC Veículos:

#Modelo Conceitual:

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
