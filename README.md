# PROJ_VENDAS_ESTOQUE

Sistema de vendas e estoque com backend em Flask e frontend em React.

## Visão geral (explicação simples)

Imagine uma lojinha:

- O frontend é o balcão (tela onde a pessoa clica).
- O backend é o atendente (entende pedidos e aplica regras).
- O banco de dados é o caderno (guarda tudo).

Quando acontece uma venda, o sistema faz isso:

1. Recebe os itens da compra.
2. Verifica se existe estoque.
3. Diminui o estoque.
4. Salva a venda.
5. Mostra o faturamento no relatório.

## O que já foi feito até agora

- Login com JWT.
- Perfis de usuário: admin e vendedor.
- Cadastro de produtos protegido para admin.
- Registro de venda com baixa automática de estoque.
- Relatório de faturamento diário para dashboard.
- Ambiente Docker com app + PostgreSQL.
- Seed para criar/atualizar usuário admin.

## Estrutura principal

- estoquevendaspython/
  - app/auth_routes.py: login e rota protegida de admin.
  - app/routes.py: produtos, vendas e relatório.
  - app/models.py: tabelas do banco.
  - app/**init**.py: criação do app e registro de rotas.
  - config.py: variáveis de configuração e segredos.
  - run.py: inicialização do servidor.
  - seed.py: criação de usuário admin.
  - docker-compose.yml e Dockerfile: ambiente em container.
- src/
  - pages/Login.js: tela de login.
  - pages/Dashboard.js: gráfico de faturamento.
  - pages/Venda.js: envio da venda.
  - services/api.js: cliente Axios com token automático.

## First principles (princípios fundamentais)

Para entender qualquer sistema, quebre em partes pequenas:

1. Entrada
   - Alguém envia dados (login, senha, itens da venda).

2. Regras
   - O sistema decide se pode ou não pode (ex.: sem estoque, não vende).

3. Memória
   - O banco guarda o histórico (usuários, produtos, vendas).

4. Permissão
   - Nem todo usuário pode tudo.

5. Visualização
   - Os dados viram gráfico para facilitar decisão.

Se você entende esses 5 blocos, entende o projeto inteiro.

## Como rodar o backend

### Opção A: Docker

Na pasta estoquevendaspython:

- docker compose up --build

Depois, se necessário:

- python seed.py

API em:

- http://localhost:5000

### Opção B: Local

Na pasta estoquevendaspython:

- pip install -r requirements.txt
- python run.py
- python seed.py

## Endpoints principais

- POST /login
- GET /admin/dashboard
- POST /produtos
- POST /registrar_venda
- GET /relatorio/faturamento

## Limitações atuais

- package.json do frontend não foi encontrado nesta workspace.
- POST /registrar_venda está sem proteção JWT no código atual.
- Existem segredos padrão que devem ser trocados em produção.

## Guia completo

Veja explicação detalhada em:

- docs/guia-projeto.md
