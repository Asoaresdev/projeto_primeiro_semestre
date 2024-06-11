import sqlite3
import pandas as pd

class DatbaseManager:
    def __init__(self, db_name:str) -> None:
        self._db_name = db_name
        self._connection = None
        self._cursor = None
    # criando a conexão com o banco de dados 
    def create_connection(self) -> None:
        if not self._connection:
            self._connection = sqlite3.connect(self._db_name)
            self._cursor = self._connection.cursor()
    # fechando conexão e o cursor do banco de dados 
    def close_connection(self) -> None:
        self._cursor.close()
        self._connection.close()        
        self._connection = None
        self._cursor = None


class LibraryManager(DatbaseManager):
    def __init__(self) -> None:
        # passando o nome do banco para a super classe DatbaseManager
        super().__init__("library.db")

    # Método para obter todos os livros do banco de dados
    def get_all_books(self) -> pd.DataFrame:
        self.create_connection()
        sql = "SELECT * FROM books"  # Consulta SQL
        
        df_books = pd.read_sql_query(sql, self._connection)
        self.close_connection()

        return df_books
    
    # Metodo para adicionar livro ao banco de dados 
    def add_book(self, title, author, year, number_of_copies ):
        self.create_connection()

        sql = """
        INSERT INTO books
        (title, author, year, number_of_copies, number_copies_out) values(?, ?, ?, ?, 0)
        """
        D = [title, author, year, number_of_copies]
        
        self._cursor.execute(sql, D)
        self._connection.commit()
        self.close_connection()

    def loan_Book(self, title):
        self.create_connection()

        number_copies = """
        SELECT number_of_copies
        FROM books
        WHERE title = ?
        """
        number_copies_out = """
        SELECT number_copies_out
        FROM books
        WHERE title = ?
        """
        D = [title]
        filter_number_copies= self._cursor.execute(number_copies, D)
        data_number_copies = filter_number_copies.fetchone()
        filter_number_copies_out= self._cursor.execute(number_copies_out, D)
        data_number_copies_out = filter_number_copies_out.fetchone()

        if data_number_copies:
            data_int_number_copies = int(data_number_copies[0])
            data_int_number_copies_out = int(data_number_copies_out[0])
            if data_int_number_copies > 0:
                sql_update_books = """
                UPDATE books
                SET number_of_copies = ?,
                number_copies_out = ?
                WHERE title = ? 
                """
                E = [str(data_int_number_copies - 1), str(data_int_number_copies_out + 1), title]
                
                update_number_copies= self._cursor.execute(sql_update_books, E)
                data_number_copies = update_number_copies.fetchone()
                print("===============================")
                print(f"Titulo {title.upper()} emprestado")
                print("===============================")
                self._connection.commit()
                self.close_connection()
            else:
                print("===============================")
                print(f"Titulo {title} indisponível, no momento,  na base de dados")
                print("===============================")
        else:
            print("===============================")
            print(f"Titulo {title} não consta na base de dados")
            print("===============================")

    def add_user(self, name, id, contato):
        self.create_connection()
        sql = """
        INSERT INTO library_user
        (name, id, contato) VALUES(?, ?, ?)
        """
        D = [name, id, contato]
        self._cursor.execute(sql, D)
        self._connection.commit()
        self.close_connection()

    def return_book(self, title):
        self.create_connection()
        # busca o numero de cópias dquele título no banco de dados 
        sql_number_copies = """
        SELECT number_of_copies
        FROM books
        WHERE title = ?
        """
        sql_number_copies_out = """
        SELECT number_copies_out
        FROM books
        WHERE title = ?
        """
        D = [title]
        filter_number_copies = self._cursor.execute(sql_number_copies, D)
        data_number_copies = filter_number_copies.fetchone()
        filter_number_copies_out = self._cursor.execute(sql_number_copies_out, D)
        data_number_copies_out = filter_number_copies_out.fetchone()
       
        Update_books = """
        UPDATE books
        SET number_of_copies = ?,
        number_copies_out = ?
        WHERE title = ? 
        """
        # acrescenta, no banco de dados, + 1 ao número de cópias daquele título
        data_int_number_copies = int(data_number_copies[0])
        data_int_number_copies_out = int(data_number_copies_out[0])
      
        E = [str(data_int_number_copies + 1), str(data_int_number_copies_out - 1),title]
        
        update= self._cursor.execute(Update_books, E)
        # data_update_books = update.fetchone()
        
        self._connection.commit()
        self.close_connection()
        print("************************************************")
        print(f"Livro {title.upper()} devolvido com sucesso")
        print("************************************************")

    def search_book_title(self, title):
        self.create_connection()
        
        sql_pd = f"SELECT * FROM books"

        df_book = pd.read_sql_query(sql_pd, self._connection)
        self.close_connection()
        line_df_book = df_book[df_book["title"] == title]
        print(line_df_book)

    def search_book_year(self, year):
        self.create_connection()
        
        sql_pd = f"SELECT * FROM books"

        df_book = pd.read_sql_query(sql_pd, self._connection)
        self.close_connection()
        line_df_book = df_book[df_book["year"] == year]
        print(line_df_book)

    def search_book_author(self, author):
        self.create_connection()
        
        sql_pd = f"SELECT * FROM books"

        df_book = pd.read_sql_query(sql_pd, self._connection)
        self.close_connection()
        line_df_book = df_book[df_book["author"] == author]
        print(line_df_book)

    
       