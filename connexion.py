import mysql.connector
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if connection.is_connected():
        print(f"✅ Connexion réussie à {database} pour {user}")
except mysql.connector.Error as err:
    print(" Erreur de connexion :", err)
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
