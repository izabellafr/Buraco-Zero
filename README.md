# Buraco Zero

Sistema web colaborativo para registro e acompanhamento de ocorrências na
pavimentação urbana de Campo Grande/MS (buracos, rachaduras e falhas nas vias).

Projeto de Extensão UFMS Digital (95DX7.200525) — Projeto Integrador de
Tecnologia da Informação II.

## Sobre o projeto

- **Módulo 1** (Resolução de problemas e análise de requisitos): protótipo em
  **Python + Streamlit**, sem controle sobre HTML/CSS, dados salvos em CSV.
- **Módulo 2** (Desenvolvimento web com frameworks e HTML/CSS): reconstrução
  em **Flask**, com HTML semântico e CSS responsivo, dados ainda em CSV.
- **Módulo 3** (Banco de Dados e Controle de versão): o armazenamento em CSV
  foi substituído por um **banco de dados relacional SQLite**, com duas
  entidades (`bairros` e `ocorrencias`) relacionadas por chave estrangeira,
  e a aplicação passou a suportar inserção, consulta, atualização e remoção
  de ocorrências via SQL. O código foi versionado com **Git** e publicado
  no GitHub com commits organizados e descritivos.

## Tecnologias utilizadas

- **Python 3** e **Flask** — lógica da aplicação e rotas
- **SQLite** — banco de dados relacional (via módulo `sqlite3`, nativo do Python)
- **SQL** — criação do esquema e manipulação de dados (`CREATE TABLE`, `INSERT`,
  `SELECT` com `JOIN`, `UPDATE`, `DELETE`)
- **Jinja2** — templates HTML
- **CSS3** — estilização responsiva
- **Git e GitHub** — controle de versão

## Estrutura de arquivos

```
buraco-zero/
├── app.py             # rotas Flask (registrar, editar, atualizar, remover)
├── database.py         # todas as operações SQL (inserção, consulta, atualização, remoção)
├── schema.sql           # definição das tabelas, chaves primárias e estrangeiras
├── requirements.txt
├── buraco_zero.db        # arquivo do banco SQLite (gerado automaticamente na 1ª execução)
├── templates/
│   ├── base.html
│   ├── index.html          # formulário de registro + listagem de ocorrências
│   └── editar.html          # formulário de edição de uma ocorrência
└── static/
    └── css/
        └── style.css
```

## Modelo de dados

Duas entidades relacionadas (relacionamento um-para-muitos):

- **bairros**: `id` (chave primária), `nome` (único, obrigatório)
- **ocorrencias**: `id` (chave primária), `bairro_id` (chave estrangeira para
  `bairros.id`), `gravidade`, `descricao`, `pontos`, `data_hora`

## Funcionalidades

- Registro de ocorrências associadas a um bairro cadastrado
- Listagem das ocorrências com indicadores (total e pontuação da comunidade)
- Gráfico por nível de gravidade
- **Edição** de uma ocorrência já registrada (gravidade e descrição)
- **Remoção** de uma ocorrência, com confirmação
- Validação de campos obrigatórios e uso de parâmetros SQL (proteção contra injeção de SQL)

## Como executar localmente

```bash
git clone https://github.com/izabellafr/Buraco-Zero.git
cd Buraco-Zero
pip install -r requirements.txt
python app.py
```

Acesse [http://localhost:5000](http://localhost:5000). O banco de dados
(`buraco_zero.db`) e os bairros iniciais são criados automaticamente na
primeira execução.

## Próximos passos

- Upload de fotos das ocorrências
- Identificação do usuário e ranking individual de pontuação
- Geolocalização automática e mapa interativo
- Migração para um banco de dados em nuvem (PostgreSQL) caso o projeto escale
