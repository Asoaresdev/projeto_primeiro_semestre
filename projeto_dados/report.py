import sqlite3
import pandas as pd

# buscando os dados no banco de dados
connection = sqlite3.connect("library.db")

sql_books = "SELECT * FROM books"  # Consulta SQL
sql_users = "SELECT * FROM library_user"  # Consulta SQL
# criando os dataframes
df_books = pd.read_sql_query(sql_books, connection)
df_users = pd.read_sql_query(sql_users, connection)

connection.close()

# tratando dados
df_books['number_of_copies'] = df_books['number_of_copies'].astype(int)
df_books['number_copies_out'] = df_books['number_copies_out'].astype(int)
# somando dados para relatorio
sum_number_of_copies = df_books['number_of_copies'].sum() 
sum_number_copies_out = df_books['number_copies_out'].sum() 
sum_all_books = sum_number_of_copies + sum_number_copies_out

total_titles = len(df_books)
total_users = len(df_users)
# mostrando os dados
print(df_books)
print("****************************************************")
print(df_users)
print("====================================================")
print("Soma de todos os livros a disposição: ", sum_number_of_copies)
print("Soma de todos os livros fora: ", sum_number_copies_out)
print("Soma de todos os livros : ", sum_all_books)
print("Total de títulos : ", total_titles)
print("Total de usuários : ", total_users)