"""
Buraco Zero - Módulo de acesso ao banco de dados (SQLite)

Reúne todas as operações de manipulação de dados (inserção, consulta,
atualização e remoção) usadas pela aplicação Flask em app.py.
"""

import sqlite3
from pathlib import Path
from datetime import datetime

DB_FILE = Path(__file__).parent / "buraco_zero.db"
SCHEMA_FILE = Path(__file__).parent / "schema.sql"

BAIRROS_INICIAIS = [
    "Centro", "Jardim dos Estados", "Vila Célia", "Monte Castelo",
    "Amambaí", "Tiradentes", "Jardim Aeroporto",
]
GRAVIDADES = ["Leve", "Média", "Grave"]
PONTOS_POR_REGISTRO = 10


def conectar():
    conexao = sqlite3.connect(DB_FILE)
    conexao.execute("PRAGMA foreign_keys = ON")
    conexao.row_factory = sqlite3.Row
    return conexao


def inicializar_banco():
    """Cria as tabelas (se ainda não existirem) e insere os bairros iniciais."""
    conexao = conectar()
    with open(SCHEMA_FILE, encoding="utf-8") as f:
        conexao.executescript(f.read())

    for nome in BAIRROS_INICIAIS:
        conexao.execute(
            "INSERT OR IGNORE INTO bairros (nome) VALUES (?)", (nome,)
        )
    conexao.commit()
    conexao.close()


def listar_bairros():
    conexao = conectar()
    bairros = conexao.execute(
        "SELECT id, nome FROM bairros ORDER BY nome"
    ).fetchall()
    conexao.close()
    return bairros


def inserir_ocorrencia(bairro_id: int, gravidade: str, descricao: str):
    conexao = conectar()
    conexao.execute(
        """
        INSERT INTO ocorrencias (bairro_id, gravidade, descricao, pontos, data_hora)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            bairro_id,
            gravidade,
            descricao,
            PONTOS_POR_REGISTRO,
            datetime.now().strftime("%d/%m/%Y %H:%M"),
        ),
    )
    conexao.commit()
    conexao.close()


def listar_ocorrencias():
    """Consulta todas as ocorrências, unindo (JOIN) com o nome do bairro."""
    conexao = conectar()
    ocorrencias = conexao.execute(
        """
        SELECT ocorrencias.id, bairros.nome AS bairro, ocorrencias.gravidade,
               ocorrencias.descricao, ocorrencias.pontos, ocorrencias.data_hora
        FROM ocorrencias
        JOIN bairros ON ocorrencias.bairro_id = bairros.id
        ORDER BY ocorrencias.id DESC
        """
    ).fetchall()
    conexao.close()
    return ocorrencias


def obter_ocorrencia(ocorrencia_id: int):
    conexao = conectar()
    ocorrencia = conexao.execute(
        "SELECT * FROM ocorrencias WHERE id = ?", (ocorrencia_id,)
    ).fetchone()
    conexao.close()
    return ocorrencia


def atualizar_ocorrencia(ocorrencia_id: int, gravidade: str, descricao: str):
    conexao = conectar()
    conexao.execute(
        "UPDATE ocorrencias SET gravidade = ?, descricao = ? WHERE id = ?",
        (gravidade, descricao, ocorrencia_id),
    )
    conexao.commit()
    conexao.close()


def remover_ocorrencia(ocorrencia_id: int):
    conexao = conectar()
    conexao.execute("DELETE FROM ocorrencias WHERE id = ?", (ocorrencia_id,))
    conexao.commit()
    conexao.close()


def totais():
    conexao = conectar()
    total = conexao.execute("SELECT COUNT(*) AS n FROM ocorrencias").fetchone()["n"]
    pontos = conexao.execute(
        "SELECT COALESCE(SUM(pontos), 0) AS s FROM ocorrencias"
    ).fetchone()["s"]
    por_gravidade = {
        linha["gravidade"]: linha["n"]
        for linha in conexao.execute(
            "SELECT gravidade, COUNT(*) AS n FROM ocorrencias GROUP BY gravidade"
        ).fetchall()
    }
    conexao.close()
    return total, pontos, {g: por_gravidade.get(g, 0) for g in GRAVIDADES}
