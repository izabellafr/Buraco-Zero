"""
Buraco Zero - Sistema web simplificado para registro de ocorrências
de buracos e falhas na pavimentação urbana.

Projeto Integrador de Tecnologia da Informação II
Programa de Extensão UFMS Digital (95DX7.200525)
"""

import os
from datetime import datetime

import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# Configurações gerais
# ---------------------------------------------------------------------------
DATA_FILE = "ocorrencias.csv"
PONTOS_POR_REGISTRO = 10
COLUNAS = ["data_hora", "bairro", "gravidade", "descricao", "pontos"]

st.set_page_config(
    page_title="Buraco Zero",
    page_icon="🕳️",
    layout="wide",
)


# ---------------------------------------------------------------------------
# Funções auxiliares
# ---------------------------------------------------------------------------
def carregar_dados() -> pd.DataFrame:
    """Carrega o histórico de ocorrências salvo em CSV.
    Caso o arquivo ainda não exista, retorna um DataFrame vazio."""
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame(columns=COLUNAS)


def salvar_ocorrencia(bairro: str, gravidade: str, descricao: str) -> pd.DataFrame:
    """Adiciona uma nova ocorrência ao arquivo CSV e retorna os dados atualizados."""
    dados = carregar_dados()
    nova_ocorrencia = {
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "bairro": bairro.strip(),
        "gravidade": gravidade,
        "descricao": descricao.strip(),
        "pontos": PONTOS_POR_REGISTRO,
    }
    dados = pd.concat([dados, pd.DataFrame([nova_ocorrencia])], ignore_index=True)
    dados.to_csv(DATA_FILE, index=False)
    return dados


# ---------------------------------------------------------------------------
# Cabeçalho
# ---------------------------------------------------------------------------
st.title("🕳️ Buraco Zero")
st.caption(
    "Sistema colaborativo e gamificado para registro de ocorrências "
    "na pavimentação das vias públicas de Campo Grande/MS."
)

coluna_formulario, coluna_dados = st.columns([1, 2])

# ---------------------------------------------------------------------------
# Formulário de registro (coluna esquerda)
# ---------------------------------------------------------------------------
with coluna_formulario:
    st.subheader("Registrar ocorrência")

    with st.form("form_ocorrencia", clear_on_submit=True):
        bairro = st.text_input("Bairro ou endereço aproximado")
        gravidade = st.selectbox("Nível de gravidade", ["Leve", "Média", "Grave"])
        descricao = st.text_area("Descrição do problema")
        enviado = st.form_submit_button("Registrar ocorrência")

    if enviado:
        if not bairro.strip() or not descricao.strip():
            st.warning("Preencha o bairro e a descrição antes de enviar.")
        else:
            salvar_ocorrencia(bairro, gravidade, descricao)
            st.success(
                f"Ocorrência registrada com sucesso! "
                f"Você ganhou {PONTOS_POR_REGISTRO} pontos."
            )
            st.rerun()

# ---------------------------------------------------------------------------
# Visualização dos dados (coluna direita)
# ---------------------------------------------------------------------------
with coluna_dados:
    st.subheader("Ocorrências registradas")
    dados = carregar_dados()

    if dados.empty:
        st.info("Nenhuma ocorrência registrada até o momento.")
    else:
        st.dataframe(dados, use_container_width=True, hide_index=True)

        total_pontos = int(dados["pontos"].sum())
        total_ocorrencias = len(dados)

        metrica1, metrica2 = st.columns(2)
        metrica1.metric("Ocorrências registradas", total_ocorrencias)
        metrica2.metric("Pontuação total da comunidade", total_pontos)

        st.markdown("**Ocorrências por gravidade**")
        st.bar_chart(dados["gravidade"].value_counts())

