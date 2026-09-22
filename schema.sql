-- Buraco Zero - Módulo 3
-- Esquema do banco de dados relacional (SQLite)

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS bairros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS ocorrencias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bairro_id INTEGER NOT NULL,
    gravidade TEXT NOT NULL CHECK (gravidade IN ('Leve', 'Média', 'Grave')),
    descricao TEXT NOT NULL,
    pontos INTEGER NOT NULL DEFAULT 10,
    data_hora TEXT NOT NULL,
    FOREIGN KEY (bairro_id) REFERENCES bairros (id)
);
