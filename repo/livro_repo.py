from data.database import criar_conexao
from models.livro import Livro
from sql.livro_sql import *

def criar_tabela_livro():
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(CRIAR_TABELA_LIVRO)
    conexao.commit()
    conexao.close()
    
def inserir_livro(livro: Livro) -> Livro:
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(INSERIR_LIVRO, (livro.titulo, livro.autor, livro.ano_publicacao))
    conexao.commit()
    livro.id = cursor.lastrowid
    conexao.close()
    return livro

def listar_livros() -> list:
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(LISTAR_LIVROS)
    livros = cursor.fetchall()
    conexao.close()
    return [Livro(id=livro[0], titulo=livro[1], autor=livro[2], ano_publicacao=livro[3]) for livro in livros]

def buscar_livro_por_id(id: int) -> Livro:
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(BUSCAR_LIVRO_POR_ID, (id,))
    livro = cursor.fetchone()
    conexao.close()
    if livro:
        return Livro(id=livro[0], titulo=livro[1], autor=livro[2], ano_publicacao=livro[3])
    
def editar_livro(livro: Livro) -> bool:
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(UPDATE_LIVRO, (livro.titulo, livro.autor, livro.ano_publicacao, livro.id))
    conexao.commit()
    conexao.close()
    return cursor.rowcount > 0

def excluir_livro(id: int) -> bool:
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute(EXCLUIR_LIVRO, (id,))
    conexao.commit()
    conexao.close()
    return cursor.rowcount > 0
