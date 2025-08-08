def salvar_livro_txt(titulo, autor, ano_publicacao):
    with open('livros.txt', 'a') as arquivo:
        arquivo.write(f"{titulo} - {autor} ({ano_publicacao})\n")
    print(f"Livro '{titulo}' salvo com sucesso!")
    
def ler_livros_salvos():
    try:
        with open('livros.txt', 'r') as arquivo:
            livros = arquivo.readlines()
        if livros:
            print("Livros salvos:")
            for livro in livros:
                print(livro.strip())
        else:
            print("Nenhum livro salvo.")
    except FileNotFoundError:
        print("Nenhum livro salvo ainda. O arquivo 'livros.txt' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler os livros salvos: {e}")
        
