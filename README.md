# Superstore - ETL
O Superstore.csv é um dos conjuntos de dados mais populares do Kaggle para treinamento em análise de dados, visualização e Business Intelligence (BI). Ele simula as operações de uma rede varejista e contém informações sobre vendas, clientes, produtos, pedidos, descontos e lucros.

### Principais características
- 9.994 registros (linhas) de transações de vendas.
- 21 colunas com informações comerciais e logísticas.
- Cobertura de pedidos realizados entre 2014 e 2017.
- Base amplamente utilizada para análises de performance de vendas e lucratividade.
- Informações disponíveis

### O dataset inclui campos como:
- Pedido: Order ID, Order Date, Ship Date, Ship Mode
- Cliente: Customer ID, Customer Name, Segment
- Localização: Country, City, State, Postal Code, Region
- Produto: Product ID, Product Name, Category, Sub-Category
- Métricas de negócio: Sales, Quantity, Discount, Profit

### Diagrama de Classes
<img width="899" height="459" alt="image" src="https://github.com/user-attachments/assets/02546249-2c7d-4888-b980-5a0bb1f5910f" />

### Objetivo do projeto
Pipeline ETL modular para ingestão e tratamento de dados de vendas do Superstore, com automação, testes e persistência em banco de dados.

1. **Extrair dados do arquivo CSV**
- Ler os dados do Superstore.csv.
- Validar a estrutura do arquivo.
- Garantir que os dados sejam carregados corretamente.
2. **Transformar e limpar os dados**
- Tratar valores nulos.
- Padronizar formatos de datas.
- Corrigir inconsistências.
- Normalizar campos para facilitar análises.
3. **Carregar dados em banco de dados**
- Inserir os registros em tabelas estruturadas.
- Garantir integridade e consistência dos dados.
- Evitar duplicidades.
4. **Automatizar o processo ETL**
- Executar o fluxo de forma repetível.
- Reduzir atividades manuais.
- Permitir execução automática via GitHub Actions.
5. **Garantir qualidade do código**
- Implementar testes unitários com Pytest.
- Aplicar padrões de código com Flake8.
- Validar componentes críticos do pipeline.

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/75d200c9-042e-4782-9583-2be43c4abd25" />

