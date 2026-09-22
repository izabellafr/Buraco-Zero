"""
Buraco Zero - Sistema web colaborativo de registro de ocorrências
na pavimentação urbana de Campo Grande/MS.

Módulo 3: substituição do armazenamento em CSV por um banco de dados
relacional em SQLite, com operações de inserção, consulta, atualização
e remoção de dados via SQL (ver database.py).
"""

from flask import Flask, render_template, request, redirect, url_for, flash

import database

app = Flask(__name__)
app.secret_key = "buraco-zero-dev-key"

database.inicializar_banco()


@app.route("/", methods=["GET"])
def index():
    bairros = database.listar_bairros()
    ocorrencias = database.listar_ocorrencias()
    total_ocorrencias, pontuacao_total, por_gravidade = database.totais()
    return render_template(
        "index.html",
        bairros=bairros,
        gravidades=database.GRAVIDADES,
        ocorrencias=ocorrencias,
        total_ocorrencias=total_ocorrencias,
        pontuacao_total=pontuacao_total,
        por_gravidade=por_gravidade,
    )


@app.route("/registrar", methods=["POST"])
def registrar():
    bairro_id = request.form.get("bairro_id", "").strip()
    gravidade = request.form.get("gravidade", "").strip()
    descricao = request.form.get("descricao", "").strip()

    if not bairro_id or not gravidade or not descricao:
        flash("Preencha todos os campos para registrar a ocorrência.", "erro")
        return redirect(url_for("index"))

    database.inserir_ocorrencia(int(bairro_id), gravidade, descricao)
    flash("Ocorrência registrada com sucesso. Obrigado por contribuir!", "sucesso")
    return redirect(url_for("index"))


@app.route("/editar/<int:ocorrencia_id>", methods=["GET"])
def editar(ocorrencia_id):
    ocorrencia = database.obter_ocorrencia(ocorrencia_id)
    if ocorrencia is None:
        flash("Ocorrência não encontrada.", "erro")
        return redirect(url_for("index"))
    return render_template(
        "editar.html", ocorrencia=ocorrencia, gravidades=database.GRAVIDADES
    )


@app.route("/atualizar/<int:ocorrencia_id>", methods=["POST"])
def atualizar(ocorrencia_id):
    gravidade = request.form.get("gravidade", "").strip()
    descricao = request.form.get("descricao", "").strip()

    if not gravidade or not descricao:
        flash("Preencha todos os campos para atualizar a ocorrência.", "erro")
        return redirect(url_for("editar", ocorrencia_id=ocorrencia_id))

    database.atualizar_ocorrencia(ocorrencia_id, gravidade, descricao)
    flash("Ocorrência atualizada com sucesso.", "sucesso")
    return redirect(url_for("index"))


@app.route("/remover/<int:ocorrencia_id>", methods=["POST"])
def remover(ocorrencia_id):
    database.remover_ocorrencia(ocorrencia_id)
    flash("Ocorrência removida.", "sucesso")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
