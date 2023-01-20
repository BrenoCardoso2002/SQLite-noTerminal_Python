# Importações:
import os
import sqlite3

# variaveis:
dbExiste = False
path = "DataBase/DataBase_Python.db"

# verifica se o arquivo de banco de dados não existe, para que seja criada a tabela depois:
if os.path.isfile(path):
    dbExiste = True

# faz a conexão com o banco de dados, caso o banco de dados não exista ele será criado:
connection = sqlite3.connect(path)

# Cria o cursor:
cursor = connection.cursor()

if (not dbExiste):
    # Cria a tabela no banco de dados:
    # comando sql:
    Create_Table = """ CREATE TABLE TB_Users (
	"ID"	INTEGER NOT NULL,
	"FirstName"	TEXT NOT NULL,
	"LastName"	TEXT NOT NULL,
	PRIMARY KEY("ID" AUTOINCREMENT)
) """
    # executa o comando sql:
    cursor.execute(Create_Table)
    # confirma as alterações:
    connection.commit()

# obtem o primeiro nome:
fName = input("Insira o primeiro nome: ")
# obtem o sobrenome:
lName = input("Insira o sobrenome: ")

# adiciona na tabela do banco de dados:
# comando sql:
Insert_Table = "Insert into TB_Users (FirstName, LastName) values ('{}', '{}')".format(fName, lName)
# executa o comando sql:
cursor.execute(Insert_Table)
# confirma as alterações:
connection.commit()

# Exibe todos os registros da tabela:
# comando sql:
Select_All = "Select * from TB_Users"
# executa o comando sql:
cursor.execute(Select_All)
# busca todos os resultados:
resultados = cursor.fetchall()
# laço de repetição que exibe todos os resutados, linha por linha:
for linha in resultados:
    print(linha)

# fecha a conexão com banco de dados:
connection.close()