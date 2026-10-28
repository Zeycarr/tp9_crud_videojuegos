import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def obtener_conexion():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", 3306)),
    )


if __name__ == "__main__":
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        print("Conexión exitosa. Tablas encontradas:")
        for (tabla,) in cursor:
            print(" -", tabla)
        cursor.close()
        conn.close()
    except Exception as e:
        print("Error de conexión:", e)