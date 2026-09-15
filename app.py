"""
Buraco Zero - Sistema web colaborativo de registro de ocorrências
na pavimentação urbana de Campo Grande/MS.

Módulo 2: reconstrução da interface com Flask + HTML semântico + CSS responsivo,
substituindo o protótipo em Streamlit do Módulo 1.
"""

from datetime import datetime
from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "buraco-zero-dev-key"  # apenas para exibir mensagens flash em dev

DATA_DIR = Path(__file__).parent / "data"
DATA_FILE = DATA_DIR / "ocorrencias.csv"
COLUNAS = ["data_hora", "bairro", "gravidade", "descricao", "pontos"]
PONTOS_POR_REGISTRO = 10

BAIRROS = [
    "Centro", "Jardim dos Estados", "Vila Célia", "Monte Castelo",
    "Amambaí", "Tiradentes", "Jardim Aeroporto", "Outro",
]
GRAVIDADES = ["Leve", "Média", "Grave"]


def carregar_dados() -> pd.DataFrame:
    """Carrega o histórico de ocorrências do arquivo CSV local."""
    if not DATA_FILE.exists():
        return pd.DataFrame(columns=COLUNAS)
    return pd.read_csv(DATA_FILE)


def salvar_ocorrencia(bairro: str, gravidade: str, descricao: str) -> None:
    """Acrescenta uma nova ocorrência ao CSV, atribuindo pontos de gamificação."""
    DATA_DIR.mkdir(exist_ok=True)
    df = carregar_dados()
    nova_linha = {
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "bairro": bairro,
        "gravidade": gravidade,
        "descricao": descricao,
        "pontos": PONTOS_POR_REGISTRO,
    }
    df = pd.concat([df, pd.DataFrame([nova_linha])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)


@app.route("/", methods=["GET"])
def index():
    df = carregar_dados()
    ocorrencias = df.sort_values("data_hora", ascending=False).to_dict("records")
    total_ocorrencias = len(df)
    pontuacao_total = int(df["pontos"].sum()) if not df.empty else 0
    por_gravidade = (
        df["gravidade"].value_counts().reindex(GRAVIDADES, fill_value=0).to_dict()
        if not df.empty
        else {g: 0 for g in GRAVIDADES}
    )
    return render_template(
        "index.html",
        bairros=BAIRROS,
        gravidades=GRAVIDADES,
        ocorrencias=ocorrencias,
        total_ocorrencias=total_ocorrencias,
        pontuacao_total=pontuacao_total,
        por_gravidade=por_gravidade,
    )


@app.route("/registrar", methods=["POST"])
def registrar():
    bairro = request.form.get("bairro", "").strip()
    gravidade = request.form.get("gravidade", "").strip()
    descricao = request.form.get("descricao", "").strip()

    if not bairro or not gravidade or not descricao:
        flash("Preencha todos os campos para registrar a ocorrência.", "erro")
        return redirect(url_for("index"))

    salvar_ocorrencia(bairro, gravidade, descricao)
    flash("Ocorrência registrada com sucesso. Obrigado por contribuir!", "sucesso")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
