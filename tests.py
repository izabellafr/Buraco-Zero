"""
Buraco Zero - Suite de testes automatizados

Contém dois tipos de teste, usando o módulo unittest, nativo do Python:

1. Testes unitários: testam as funções de database.py isoladamente,
   sem passar pelas rotas do Flask.
2. Testes de integração: testam as rotas de app.py de ponta a ponta,
   exercitando a integração entre Flask, database.py e o banco SQLite.

Ambos os tipos de teste usam um banco de dados SQLite temporário e
separado do banco de dados real (buraco_zero.db), para não misturar
dados de teste com dados de uso real da aplicação.

Para rodar: python -m unittest tests.py -v
"""

import unittest
import tempfile
import sqlite3
from pathlib import Path

import database


class TestesUnitariosDatabase(unittest.TestCase):
    """Testes unitários: cada função de database.py testada isoladamente."""

    def setUp(self):
        # Cria um arquivo de banco de dados temporário só para este teste
        self.arquivo_temporario = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.arquivo_temporario.close()
        database.DB_FILE = Path(self.arquivo_temporario.name)
        database.inicializar_banco()
        self.bairro_id = database.listar_bairros()[0]["id"]

    def tearDown(self):
        Path(self.arquivo_temporario.name).unlink(missing_ok=True)

    def test_inserir_ocorrencia_cria_registro(self):
        database.inserir_ocorrencia(self.bairro_id, "Grave", "Buraco de teste")
        ocorrencias = database.listar_ocorrencias()
        self.assertEqual(len(ocorrencias), 1)
        self.assertEqual(ocorrencias[0]["descricao"], "Buraco de teste")
        self.assertEqual(ocorrencias[0]["pontos"], 10)

    def test_listar_ocorrencias_traz_nome_do_bairro_via_join(self):
        database.inserir_ocorrencia(self.bairro_id, "Leve", "Teste de JOIN")
        ocorrencias = database.listar_ocorrencias()
        self.assertIn("bairro", ocorrencias[0].keys())
        self.assertIsInstance(ocorrencias[0]["bairro"], str)

    def test_atualizar_ocorrencia_altera_gravidade_e_descricao(self):
        database.inserir_ocorrencia(self.bairro_id, "Leve", "Descrição original")
        ocorrencia_id = database.listar_ocorrencias()[0]["id"]
        database.atualizar_ocorrencia(ocorrencia_id, "Grave", "Descrição corrigida")
        atualizada = database.obter_ocorrencia(ocorrencia_id)
        self.assertEqual(atualizada["gravidade"], "Grave")
        self.assertEqual(atualizada["descricao"], "Descrição corrigida")

    def test_remover_ocorrencia_exclui_registro(self):
        database.inserir_ocorrencia(self.bairro_id, "Média", "Será removida")
        ocorrencia_id = database.listar_ocorrencias()[0]["id"]
        database.remover_ocorrencia(ocorrencia_id)
        self.assertIsNone(database.obter_ocorrencia(ocorrencia_id))

    def test_totais_conta_ocorrencias_e_soma_pontos(self):
        database.inserir_ocorrencia(self.bairro_id, "Leve", "Um")
        database.inserir_ocorrencia(self.bairro_id, "Grave", "Dois")
        total, pontos, por_gravidade = database.totais()
        self.assertEqual(total, 2)
        self.assertEqual(pontos, 20)
        self.assertEqual(por_gravidade["Leve"], 1)
        self.assertEqual(por_gravidade["Grave"], 1)

    def test_chave_estrangeira_bloqueia_bairro_inexistente(self):
        """Verificação: a restrição FOREIGN KEY deve impedir um bairro_id inválido."""
        with self.assertRaises(sqlite3.IntegrityError):
            database.inserir_ocorrencia(9999, "Grave", "Bairro que não existe")

    def test_check_bloqueia_gravidade_invalida(self):
        """Verificação: a restrição CHECK deve impedir uma gravidade fora da lista."""
        conexao = database.conectar()
        with self.assertRaises(sqlite3.IntegrityError):
            conexao.execute(
                "INSERT INTO ocorrencias (bairro_id, gravidade, descricao, pontos, data_hora) "
                "VALUES (?, ?, ?, ?, ?)",
                (self.bairro_id, "Gravissima", "Valor de gravidade inválido", 10, "01/01/2026 00:00"),
            )
        conexao.close()


class TestesIntegracaoRotas(unittest.TestCase):
    """Testes de integração: exercitam as rotas do Flask de ponta a ponta."""

    def setUp(self):
        self.arquivo_temporario = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
        self.arquivo_temporario.close()
        database.DB_FILE = Path(self.arquivo_temporario.name)
        database.inicializar_banco()

        import app as app_module
        app_module.app.config["TESTING"] = True
        self.app_module = app_module
        self.client = app_module.app.test_client()

        self.bairro_id = database.listar_bairros()[0]["id"]

    def tearDown(self):
        Path(self.arquivo_temporario.name).unlink(missing_ok=True)

    def test_pagina_inicial_carrega(self):
        resposta = self.client.get("/")
        self.assertEqual(resposta.status_code, 200)
        self.assertIn(b"Buraco Zero", resposta.data)

    def test_registrar_ocorrencia_via_post(self):
        resposta = self.client.post("/registrar", data={
            "bairro_id": str(self.bairro_id),
            "gravidade": "Grave",
            "descricao": "Ocorrência via teste de integração",
        }, follow_redirects=True)
        self.assertEqual(resposta.status_code, 200)
        self.assertIn("Ocorrência via teste de integração".encode(), resposta.data)

    def test_registrar_com_campo_vazio_nao_salva(self):
        resposta = self.client.post("/registrar", data={
            "bairro_id": str(self.bairro_id),
            "gravidade": "",
            "descricao": "",
        }, follow_redirects=True)
        total, _, _ = database.totais()
        self.assertEqual(total, 0)
        self.assertIn("Preencha todos os campos".encode(), resposta.data)

    def test_editar_e_remover_ocorrencia_via_rotas(self):
        database.inserir_ocorrencia(self.bairro_id, "Leve", "Original")
        ocorrencia_id = database.listar_ocorrencias()[0]["id"]

        resposta_editar = self.client.get(f"/editar/{ocorrencia_id}")
        self.assertEqual(resposta_editar.status_code, 200)

        self.client.post(f"/atualizar/{ocorrencia_id}", data={
            "gravidade": "Grave", "descricao": "Editada via teste",
        })
        self.assertEqual(database.obter_ocorrencia(ocorrencia_id)["gravidade"], "Grave")

        self.client.post(f"/remover/{ocorrencia_id}")
        self.assertIsNone(database.obter_ocorrencia(ocorrencia_id))


if __name__ == "__main__":
    unittest.main()
