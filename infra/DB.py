import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

conexao = mysql.connector.connect(
    host=os.getenv("DATABASE_HOST"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    database=os.getenv("DATABASE_NAME")
)

cursor = conexao.cursor()

cursor.execute("select @@version")
version = cursor.fetchone()
if version:
    print('Conectado com sucesso')