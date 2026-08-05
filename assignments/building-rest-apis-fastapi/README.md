# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construir uma API REST básica com FastAPI para gerenciar tarefas (to-do items), aplicando operações CRUD, validação de dados e códigos de resposta HTTP apropriados.

## 📝 Tarefas

### 🛠️ Criar a Estrutura Inicial da API

#### Descrição
Configure uma aplicação FastAPI com endpoint de saúde e uma estrutura em memória para armazenar tarefas.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI em `starter-code.py`
- Implementar o endpoint `GET /health` que retorne `{"status": "ok"}`
- Definir um modelo Pydantic `Task` com campos `id`, `title`, `completed`
- Manter uma coleção em memória para armazenar tarefas durante a execução


### 🛠️ Implementar Endpoints CRUD

#### Descrição
Implemente os endpoints para criar, listar, buscar, atualizar e remover tarefas.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para criar uma nova tarefa
- Implementar `GET /tasks` para listar todas as tarefas
- Implementar `GET /tasks/{task_id}` para retornar uma tarefa específica
- Implementar `PUT /tasks/{task_id}` para atualizar título e status
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa
- Retornar `404` quando a tarefa não existir


### 🛠️ Validar Regras e Testar Respostas

#### Descrição
Adicione validações para os dados recebidos e valide manualmente os endpoints com exemplos de requisição.

#### Requisitos
O programa concluído deve:

- Impedir criação de tarefa com `title` vazio
- Garantir que `completed` seja booleano
- Retornar `201` no cadastro e `204` na exclusão com sucesso
- Testar os endpoints com `curl` ou Swagger UI (`/docs`)
- Registrar no README exemplos de payload para criar e atualizar tarefa
