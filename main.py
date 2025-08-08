import os
import time
import requests
from models.livro import Livro
from repo.livro_repo import buscar_livro_por_id, criar_tabela_livro, editar_livro, excluir_livro, inserir_livro, listar_livros
import salvar_livro

criar_tabela_livro()

def buscar_livros(palavra_chave):
    url = f"https://www.googleapis.com/books/v1/volumes?q={palavra_chave}"
    response = requests.get(url)
    if response.status_code == 200:
        livros = response.json().get('items', [])
        for livro in livros:
            titulo = livro['volumeInfo'].get('title', 'Título não disponível')
            autores = livro['volumeInfo'].get('authors', ['Autor desconhecido'])
            print(f"Título: {titulo}, Autores: {', '.join(autores)}")
    else:
        print(f"Erro ao buscar livros: {response.status_code}")
        
def main():
    while True:
        os.system("cls")
        print("\nMenu:")
        print("Bem-vindo ao sistema de gerenciamento de livros!")
        print("Escolha uma opção:")
        print("1. Buscar livros")
        print("2. Cadastrar livro")
        print("3. ver livros salvos")
        print("4. Inserir dados no banco")
        print("5. Gerenciar banco (pesquisar, editar, excluir, etc.)")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        try:
            inteiro = int(opcao)
        
            if inteiro == 1:
                os.system("cls")
                palavra_chave = input("Digite uma palavra-chave para buscar livros: ")
                print("Buscando livros...")
                time.sleep(4)
                if not palavra_chave:
                    print("Nenhuma palavra-chave fornecida.")
                    continue
                else:
                    buscar_livros(palavra_chave)
                    print("Pressione Enter para continuar...", end="")
                    input()
                    os.system("cls")
                    print("Voltando ao menu principal...")
                    time.sleep(4)
                    continue
                    
            
            elif inteiro == 2:
                os.system("cls")
                print("Cadastro de livro")
                titulo = input("Digite o título do livro: ")
                autor = input("Digite o autor do livro: ")
                ano_publicacao = input("Digite o ano de publicação: ")
                if not titulo or not autor or not ano_publicacao:
                    print("Todos os campos são obrigatórios. Tente novamente.")
                    continue
                else:
                    salvar_livro.salvar_livro_txt(titulo, autor, ano_publicacao)
                    print("Livro cadastrado com sucesso!")
                    print("Pressione Enter para continuar...", end="")
                    input()
                    os.system("cls")
                    print("Voltando ao menu principal...")
                    time.sleep(4)
                    continue
            
            elif inteiro == 3:
                os.system("cls")
                salvar_livro.ler_livros_salvos()
                print("Pressione Enter para continuar...", end="")
                input()
                os.system("cls")
                print("Voltando ao menu principal...")
                time.sleep(4)
                continue
            
            elif inteiro == 4: 
                os.system("cls")
                print("Inserindo dados no banco de dados...") 
                titulo = input("Digite o título do livro: ")
                autor = input("Digite o autor do livro: ")
                ano_publicacao = input("Digite o ano de publicação: ")
                dados = Livro(titulo=titulo, autor=autor, ano_publicacao=ano_publicacao)
                inserir_livro(dados)
                print("Livro inserido com sucesso!")
                print("Pressione Enter para continuar...", end="")
                input()
                os.system("cls")
                print("Voltando ao menu principal...")
                time.sleep(4)
                continue
            
            elif inteiro == 5:
                os.system("cls")
                print("Gerenciando banco de dados...")
                print("1. Listar livros")
                print("2. Editar livro")
                print("3. Excluir livro")
                print("0. Voltar")
                sub_opcao = int(input("Escolha uma opção: "))
                if sub_opcao == 1:
                    os.system("cls")
                    livro = int(input("Digite o ID do livro a ser listado: "))
                    os.system("cls")
                    dados = buscar_livro_por_id(livro)
                    print("Listando livros...")
                    time.sleep(2)
                    if dados:
                        print("Livro encontrado:")
                        print(f"ID: {dados.id}")
                        print(f"titulo do livro: {dados.titulo}")
                        print(f"Autor: {dados.autor}")
                        print(f"Ano de publicação: {dados.ano_publicacao}")
                        print("Pressione Enter para continuar...", end="")
                        input()
                        os.system("cls")
                        print("Voltando ao menu principal...")
                        time.sleep(4)
                        continue
                    
                    else:
                        print("ID inválido.")
                        continue
                
                elif sub_opcao == 2:
                    os.system("cls")
                    print("Editando livro...")
                    print("Para editar um livro, você precisa saber o ID dele.")
                    listar_livros()
                    id_livro = int(input("Digite o ID do livro a ser editado: "))
                    if id_livro is None:
                        print("ID inválido.")
                        continue
                    else:
                        buscar_livro_por_id(id_livro)
                        titulo = input("Digite o novo título do livro: ")
                        autor = input("Digite o novo autor do livro: ")
                        ano_publicacao = input("Digite o novo ano de publicação: ")
                        dados = Livro(id=id_livro, titulo=titulo, autor=autor, ano_publicacao=ano_publicacao)
                        editar_livro(dados)
                        print("Livro editado com sucesso!")
                        print("Pressione Enter para continuar...", end="")
                        input()
                        os.system("cls")
                        print("Voltando ao menu principal...")
                        time.sleep(4)
                        continue
                
                elif sub_opcao == 3:
                    id_livro = int(input("Digite o ID do livro a ser excluído: "))
                    if id_livro is None:
                        print("ID inválido.")
                        continue
                    else:
                        excluir_livro(id_livro)
                        print("Livro excluído com sucesso!")
                
                elif sub_opcao == 0:
                    continue
                else:
                    print("Opção inválida. Tente novamente.")
            
            elif inteiro == 0:
                print("Saindo do programa...")
                time.sleep(2)
                break
        except ValueError:
            os.system("cls")
            print("Erro, nao deve ser letra ou caractere especial, tente novamente.")
            time.sleep(3)
            continue
            
        
if __name__ == "__main__":
    main()
    