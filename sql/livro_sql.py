CRIAR_TABELA_LIVRO = """
CREATE TABLE IF NOT EXISTS livro (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano_publicacao INTEGER NOT NULL
);
"""

INSERIR_LIVRO = """
INSERT INTO livro (titulo, autor, ano_publicacao)
VALUES (?, ?, ?);
"""

LISTAR_LIVROS = """
SELECT * FROM livro;
"""

BUSCAR_LIVRO_POR_ID = """
SELECT * FROM livro WHERE id = ?;
"""

UPDATE_LIVRO = """
UPDATE livro
SET titulo = ?, autor = ?, ano_publicacao = ?
WHERE id = ?;
"""

EXCLUIR_LIVRO = """
DELETE FROM livro WHERE id = ?;
"""