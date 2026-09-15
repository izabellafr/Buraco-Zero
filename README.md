# Buraco Zero

Sistema web colaborativo para registro e acompanhamento de ocorrências na
pavimentação urbana de Campo Grande/MS (buracos, rachaduras e falhas nas vias).

Projeto de Extensão UFMS Digital (95DX7.200525) — Projeto Integrador de
Tecnologia da Informação II.

## Sobre o projeto

No **Módulo 1** (Resolução de problemas e análise de requisitos), o protótipo
foi desenvolvido em **Python + Streamlit**, priorizando velocidade de
validação da ideia sem escrever HTML/CSS.

No **Módulo 2** (Desenvolvimento web com frameworks e HTML/CSS), a aplicação
foi reconstruída em **Flask**, com páginas HTML semânticas e acessíveis e
estilização CSS responsiva escrita manualmente, atendendo aos requisitos de
estruturação, acessibilidade e responsividade do módulo.

## Tecnologias utilizadas

- **Python 3** — lógica da aplicação
- **Flask** — framework web (rotas, templates, formulários)
- **Jinja2** — motor de templates HTML
- **Pandas** — manipulação dos dados tabulares
- **CSS3** (Flexbox, Grid, media queries) — estilização responsiva, sem frameworks de CSS
- **CSV** — armazenamento local dos registros

## Estrutura de arquivos

```
buraco-zero/
├── app.py                     # aplicação Flask: rotas e lógica de dados
├── requirements.txt           # dependências do projeto
├── data/
│   └── ocorrencias.csv        # armazenamento local das ocorrências
├── templates/
│   ├── base.html               # estrutura HTML base (cabeçalho, rodapé, landmarks)
│   └── index.html              # formulário de registro + feed de ocorrências
└── static/
    └── css/
        └── style.css            # estilização responsiva
```

## Funcionalidades

- Formulário de registro de ocorrências (bairro, gravidade, descrição)
- Validação de campos obrigatórios no servidor
- Listagem das ocorrências registradas em tabela (responsiva em telas pequenas)
- Indicadores: total de ocorrências e pontuação acumulada da comunidade
- Gráfico de barras (CSS puro) por nível de gravidade
- Gamificação simples: pontuação fixa por ocorrência registrada
- HTML semântico com landmarks (`header`, `main`, `footer`), `fieldset`/`legend`,
  rótulos associados a campos, link de "pular para o conteúdo" e foco visível
  para navegação por teclado

## Como executar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/izabellafr/Buraco-Zero.git
   cd Buraco-Zero
   ```

2. (Opcional, recomendado) crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   python app.py
   ```

5. Acesse no navegador: [http://localhost:5000](http://localhost:5000)

## Próximos passos

- Upload de fotos das ocorrências
- Identificação do usuário e ranking individual de pontuação
- Geolocalização automática e mapa interativo
- Migração do armazenamento em CSV para um banco de dados relacional
