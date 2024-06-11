import console
from database_manager import LibraryManager

# chamando a função com as opções do console 
option = console.initial_console()

if option == "1":
    print("Opção 1 escolhida - Cadastrar Livros")
    # Dados vindo do console 
    result_console = console.add_book_console()
    title, author, year, number_of_copies = result_console

    # Instanciando a classe 
    manager = LibraryManager()
    # Usando o método da classe 
    manager.add_book(title, author, year, number_of_copies)

elif option == "2":
    print("Opção 2 escolhida - Todos Livros")
    # Instanciando a classe 
    manager = LibraryManager()
    # Usando o método da classe 
    df_books = manager.get_all_books()
    print(df_books)
   
elif option == "3":
    print("Opção 3 escolhida - Adicionar Usuário")
    # Dados vindo do console 
    result_console = console.add_user_console()
    name, id, contato = result_console
    # Instanciando a classe 
    manager = LibraryManager()
    # Usando o método da classe 
    manager.add_user(name, id, contato)
   

elif option == "4":
    print("Opção 4 escolhida - Empréstimo Livros")
    result_console = console.loan_books()
     # Instanciando a classe 
    manager = LibraryManager()
     # Usando o método da classe 
    manager.loan_Book(result_console)
    

elif option == "5":
    print("Opção 5 escolhida - Devolução de Livros")
    result_console = console.return_books()
     # Instanciando a classe 
    manager = LibraryManager()
     # Usando o método da classe 
    manager.return_book(result_console)

elif option == "6":
    print("Opção 6 escolhida - Consulta de Livros")
    result_console = console.search_book()
    if result_console == "1":
        print("Por título")
        title = input("Digite o título: ")
        manager = LibraryManager()
        manager.search_book_title(title)
    elif result_console == "2":
        print("Por Ano da publicação")
        year = input("Digite o ano: ")
        manager = LibraryManager()
        manager.search_book_year(year)
    elif result_console == "3":
        print("Por Autor")
        author = input("Digite o autor: ")
        manager = LibraryManager()
        manager.search_book_author(author)
    else:
        print("Opção não encontrada")

elif option == "7":
    print("Opção 6 escolhida - Relatório")
else:
    print("Opção não encontrada")