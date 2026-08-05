# 📘 Assignment: Data Cleaning and Quality in Python

## 🎯 Objective

Learn how to improve dataset reliability before analysis by handling missing values, inconsistent text formats, duplicates, and outliers using Python and pandas.

## 📝 Tasks

### 🛠️ Load and Audit Raw Data

#### Descrição
Carregue o arquivo CSV fornecido e faça uma auditoria inicial para entender os principais problemas de qualidade presentes nos dados.

#### Requisitos
O programa concluído deve:

- Carregar `data.csv` com pandas.
- Exibir o total de linhas e colunas.
- Identificar valores ausentes por coluna.
- Mostrar quantas linhas duplicadas existem.
- Listar pelo menos 3 possíveis problemas de qualidade detectados (exemplo: capitalizacao inconsistente, idades invalidas, notas fora da faixa esperada).

### 🛠️ Clean and Standardize the Dataset

#### Descrição
Aplique regras de limpeza para corrigir problemas comuns e padronizar os dados para que fiquem prontos para analise.

#### Requisitos
O programa concluído deve:

- Remover linhas duplicadas.
- Tratar valores ausentes em pelo menos 2 colunas com regras claras.
- Padronizar texto da coluna `city` (exemplo: tudo em Title Case e sem espacos extras).
- Corrigir ou remover registros com `score` fora do intervalo de 0 a 100.
- Salvar o resultado em `clean_data.csv`.

### 🛠️ Validate Data Quality and Report Changes

#### Descrição
Compare os dados antes e depois da limpeza para comprovar o impacto das transformacoes.

#### Requisitos
O programa concluído deve:

- Exibir um resumo com quantidade de linhas antes e depois da limpeza.
- Mostrar quantos valores ausentes foram resolvidos por coluna.
- Confirmar que nao ha mais duplicatas.
- Gerar um pequeno relatorio em texto no terminal com as decisoes de limpeza aplicadas.
