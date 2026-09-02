# Buraco Zero 🕳️

Sistema web simplificado, colaborativo e gamificado para registro de ocorrências
de buracos e falhas na pavimentação das vias públicas de Campo Grande/MS.

Projeto desenvolvido para a disciplina **Projeto Integrador de Tecnologia da
Informação II**, vinculado ao Programa de Extensão UFMS Digital (95DX7.200525).

## Sobre o projeto

O Buraco Zero permite que qualquer cidadão registre, por meio de um formulário
simples, a ocorrência de um buraco em uma via pública, informando o bairro, o
nível de gravidade e uma descrição do problema. Todos os registros ficam
disponíveis em uma tabela pública, junto com indicadores simples (total de
ocorrências e pontuação acumulada pela comunidade). Para incentivar a
participação, o sistema aplica uma estratégia básica de **gamificação**: cada
ocorrência registrada gera pontos para a comunidade.

## Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — framework para criação da interface web
- [Pandas](https://pandas.pydata.org/) — manipulação e armazenamento dos dados
- Armazenamento local em arquivo `.csv` (sem necessidade de banco de dados)

## Como instalar e executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/<seu-usuario>/buraco-zero.git
   cd buraco-zero
   ```

2. (Opcional, mas recomendado) crie um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```

5. O navegador abrirá automaticamente em `http://localhost:8501`.

## Estrutura do projeto

```
buraco-zero/
├── app.py              # Código principal da aplicação Streamlit
├── requirements.txt    # Dependências do projeto
├── ocorrencias.csv     # Base de dados local (gerada automaticamente)
└── README.md           # Este arquivo
```

## Funcionalidades

- [x] Formulário para registro de ocorrências (bairro, gravidade, descrição)
- [x] Armazenamento local dos registros em CSV
- [x] Listagem de todas as ocorrências registradas
- [x] Pontuação simples por ocorrência registrada (gamificação)
- [x] Indicadores de total de ocorrências e pontuação da comunidade
- [x] Gráfico de ocorrências por nível de gravidade

## Melhorias futuras

- Geolocalização automática (GPS) para o registro das ocorrências
- Mapa interativo com a localização dos buracos
- Banco de dados remoto e autenticação de usuários
- Validação colaborativa das ocorrências registradas por outros usuários

## Autor

Izabella Francisca Lages da Silva — Tecnologia da Informação (UFMS)
