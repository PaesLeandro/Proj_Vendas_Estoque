# Guia do Projeto (5ª série + First Principles)

Este guia explica o projeto de um jeito simples, como aula prática.

## 1) O que este sistema faz?

Pense em uma loja:

- alguém entra e compra produtos;
- o sistema registra a venda;
- o estoque diminui;
- o dono vê o faturamento em gráfico.

Ou seja: o sistema ajuda a vender melhor e não perder controle do estoque.

## 2) First Principles (princípios fundamentais)

First principles significa: quebrar algo grande em partes pequenas e básicas.

### A. Entrada

Toda ação começa com entrada de dados.

Exemplos neste projeto:

- login e senha na tela de login;
- lista de itens na venda.

Sem entrada, não existe processo.

### B. Processamento e Regras

Depois que entra dado, o sistema aplica regras.

Exemplos:

- senha correta? cria token;
- perfil é admin? pode cadastrar produto;
- tem estoque suficiente? permite vender.

Sem regra, o sistema vira bagunça.

### C. Memória (Banco de dados)

O sistema precisa lembrar o que aconteceu.

Ele guarda:

- usuários;
- produtos;
- clientes;
- vendas;
- itens de cada venda.

Sem memória, tudo some quando o programa fecha.

### D. Segurança e Permissão

Nem todo usuário deve fazer tudo.

No projeto:

- token JWT identifica quem está logado;
- perfil admin tem mais poder.

Sem permissão, qualquer pessoa pode fazer ação crítica.

### E. Saída e Visualização

No final, os dados precisam virar informação útil.

No projeto:

- o backend calcula faturamento por dia;
- o frontend mostra em gráfico.

Sem visualização, fica difícil decidir.

Resumo mental:
Entrada -> Regra -> Memória -> Permissão -> Visualização

## 3) Arquitetura do projeto

### Backend (Flask)

Pasta: estoquevendaspython

Arquivos importantes:

- app/**init**.py
  - cria o app e registra as rotas;
- app/auth_routes.py
  - login e rota administrativa protegida;
- app/routes.py
  - registrar venda, cadastrar produto e relatório;
- app/models.py
  - tabelas do banco;
- run.py
  - sobe servidor;
- seed.py
  - cria/atualiza usuário admin.

### Frontend (React)

Pasta: src

Arquivos importantes:

- pages/Login.js
- pages/Dashboard.js
- pages/Venda.js
- services/api.js

O api.js adiciona token automaticamente nas requisições.

## 4) O que foi implementado até agora

1. Login com JWT.
2. Perfis de usuário (admin e vendedor).
3. Cadastro de produto com proteção por perfil admin.
4. Registro de venda com:
   - validação de estoque,
   - cálculo de subtotal e total,
   - baixa automática do estoque.
5. Relatório de faturamento diário.
6. Dashboard com gráfico de linha.
7. Ambiente com Docker + PostgreSQL.
8. Script para garantir usuário admin.

## 5) Fluxo completo (passo a passo)

### Fluxo de login

1. Usuário digita login/senha.
2. Frontend chama POST /login.
3. Backend valida no banco.
4. Se ok, devolve access_token.
5. Front salva token no localStorage.
6. Próximas requisições vão com Authorization Bearer.

### Fluxo de venda

1. Front manda cliente_id e itens para POST /registrar_venda.
2. Backend busca produto por produto.
3. Se faltar estoque, retorna erro.
4. Se tiver estoque, calcula subtotais e total.
5. Diminui quantidades do estoque.
6. Salva venda e itens.
7. Retorna sucesso.

### Fluxo de relatório

1. Backend lê vendas.
2. Agrupa faturamento por dia (pandas).
3. Retorna JSON.
4. Dashboard desenha o gráfico.

## 6) Modelo de dados em palavras simples

- Usuario: quem usa o sistema.
- Produto: item que pode ser vendido.
- Cliente: pessoa/empresa compradora.
- Venda: compra feita em uma data.
- ItemVenda: cada linha da venda (produto + quantidade + subtotal).

Relações:

- uma venda tem vários itens;
- cada item aponta para um produto;
- cada venda pertence a um cliente.

## 7) Como rodar

### Com Docker

Entrar em estoquevendaspython e executar:

- docker compose up --build

Depois, se necessário:

- python seed.py

### Sem Docker

Entrar em estoquevendaspython e executar:

- pip install -r requirements.txt
- python run.py
- python seed.py

API padrão:

- http://localhost:5000

## 8) Endpoints principais

- POST /login
- GET /admin/dashboard
- POST /produtos
- POST /registrar_venda
- GET /relatorio/faturamento

## 9) Limitações e atenção

1. package.json do frontend não foi encontrado nesta workspace.
2. POST /registrar_venda está sem JWT obrigatório no código atual.
3. Segredos padrão devem ser alterados para produção.

## 10) Glossário simples

- API: porta de comunicação entre frontend e backend.
- JWT: crachá digital temporário.
- Banco de dados: caderno organizado e permanente.
- ORM: tradutor entre Python e SQL.
- Docker: caixa padronizada para rodar o sistema igual em várias máquinas.

## 11) Próximos passos sugeridos

1. Proteger /registrar_venda com JWT.
2. Criar documentação de setup do frontend quando os arquivos de build estiverem no repositório.
3. Mover segredos para variáveis seguras de ambiente.
4. Criar testes automatizados para login e venda.
