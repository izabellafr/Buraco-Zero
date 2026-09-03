# 🕳️ Buraco Zero — Comunidade Ativa, Ruas Melhores!

> **Sistema web colaborativo e gamificado** para mapeamento e registro inteligente de ocorrências na pavimentação urbana de **Campo Grande/MS**.

---

## 🎯 Sobre o Projeto

O **Buraco Zero** conecta o cidadão à gestão urbana de forma simples e divertida. Desenvolvido no âmbito acadêmico para a disciplina **Projeto Integrador de Tecnologia da Informação II**, o projeto é vinculado ao **Programa de Extensão UFMS Digital** *(Código: 95DX7.200525)*.

### 💡 Como Funciona?
1. **Registre:** Viu um buraco? Preencha um formulário rápido informando o bairro, a gravidade e uma breve descrição.
2. **Acompanhe:** Todos os dados ficam disponíveis instantaneamente em um painel público e interativo.
3. **Ganhe Pontos (Gamificação):** Cada colaboração soma pontos para o ranking e engajamento da comunidade!

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído prezando pela leveza, eficiência e facilidade de execução:

| Tecnologia | Finalidade |
| :--- | :--- |
| **Python 3** | Linguagem principal de desenvolvimento |
| **Streamlit** | Criação da interface web interativa |
| **Pandas** | Manipulação, análise e persistência de dados |
| **CSV** | Armazenamento local leve (sem necessidade de banco complexo) |

---

## 🚀 Guia de Instalação e Execução

Siga os passos abaixo para rodar o projeto localmente em poucos minutos:

### 1. Clone o repositório
```bash
git clone [https://github.com/](https://github.com/)<seu-usuario>/buraco-zero.git
cd buraco-zero

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

* ✨ Funcionalidades Atuais
  
📝 Formulário Dinâmico: Cadastro intuitivo com campos de bairro, nível de gravidade e descrição.

📈 Painel de Indicadores: Métricas em tempo real do total de ocorrências e pontuação coletiva.

📊 Gráficos Analíticos: Visualização imediata da distribuição de buracos por nível de gravidade.

💾 Persistência Local: Salvamento automático das informações em arquivo CSV.


* 🔮 Próximos Passos
  
📍 Geolocalización Automática (GPS): Captura precisa da localização do usuário.

🗺️ Mapa Interativo: Visualização geográfica dos pontos críticos da cidade via mapas.

🔐 Autenticação e Nuvem: Sistema de login para usuários e migração para banco de dados remoto.

👍 Validação Colaborativa: Sistema onde vizinhos podem confirmar ou atualizar o status dos buracos registrados.

## Autor

Izabella Francisca Lages da Silva — Tecnologia da Informação (UFMS)
