import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Chargement des infos de connexion à MariaDB depuis le fichier .env
load_dotenv()
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME", "botroot_db")

# Connexion à la base de données
def connect():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except Error as e:
        print(f"❌ Erreur de connexion à MariaDB : {e}")
        return None

# Création de la table (si elle n’existe pas)
def init_db():
    conn = connect()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS images (
            id INT AUTO_INCREMENT PRIMARY KEY,
            filename VARCHAR(255) NOT NULL,
            type ENUM('before', 'after') NOT NULL,
            x INT NOT NULL,
            y INT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Enregistre les métadonnées d'une image
def log_image_metadata(filename, type, x, y):
    conn = connect()
    if conn is None:
        return
    cursor = conn.cursor()
    query = "INSERT INTO images (filename, type, x, y) VALUES (%s, %s, %s, %s)"
    values = (filename, type, x, y)
    try:
        cursor.execute(query, values)
        conn.commit()
    except Error as e:
        print(f"❌ Erreur d’insertion de métadonnées : {e}")
    finally:
        cursor.close()
        conn.close()