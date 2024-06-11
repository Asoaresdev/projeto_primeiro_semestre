def initial_console():
    print("===========================================")
    print(f"SISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
    print("===========================================")
    print(f"Escolha uma opção")
    print(f"\n1 - Cadastrar Livros")
    print(f"\n2 - Todos Livros") # não consta no escopo
    print(f"\n3 - Adicionar Usuário")
    print(f"\n4 - Empréstimo Livros")
    print(f"\n5 - Devolução de Livros")
    print(f"\n6 - Consulta de Livros")
    print(f"\n7 - Relatório")
    option = input(f"\nSua opção: ")
    print("==============================")
    return option

def add_book_console ():
    title = input("Título do livro: ")
    author = input("Autor do livro: ")
    year = input("Ano da publicação do livro: ")
    number_of_copies = input("Número de cópias do livro: ")
    return (title, author, year, number_of_copies)

def add_user_console ():
    name = input("Nome: ")
    id = input("Numero identificação: ")
    contato = input("Contato: ")
    return (name, id, contato)
    
def loan_books():
    title = input( "Digite o título do livro: ")
    return title

def return_books():
    title = input( "Digite o título do livro a ser devolvido: ")
    return title

def search_book():
    print(f"\n - Consulta de Livros por:")
    print(f"\n1 - Título")
    print(f"\n2 - Ano da publicação")
    print(f"\n3 - Autor")
    option = input(f"\nSua opção: ")
    print("==============================")
    return option




 