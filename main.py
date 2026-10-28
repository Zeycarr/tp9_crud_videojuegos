import mysql.connector
from conexion import obtener_conexion


def crear():
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre es obligatorio.")
        return
    pais = input("País de origen (Enter para omitir): ").strip() or None
    sitio = input("Sitio web (Enter para omitir): ").strip() or None

    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO desarrolladoras (nombre, pais_origen, sitio_web) VALUES (%s, %s, %s)",
        (nombre, pais, sitio),
    )
    conn.commit()
    print(f"Desarrolladora creada con ID {cursor.lastrowid}.")
    cursor.close()
    conn.close()


def listar():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id_desarrolladora, nombre, pais_origen, sitio_web "
        "FROM desarrolladoras ORDER BY id_desarrolladora"
    )
    filas = cursor.fetchall()
    if not filas:
        print("No hay desarrolladoras cargadas.")
    else:
        print(f"\n{'ID':<5}{'Nombre':<30}{'País':<20}{'Sitio web'}")
        print("-" * 80)
        for id_, nombre, pais, sitio in filas:
            print(f"{id_:<5}{nombre:<30}{(pais or '-'):<20}{sitio or '-'}")
    cursor.close()
    conn.close()


def actualizar():
    try:
        id_ = int(input("ID de la desarrolladora a actualizar: "))
    except ValueError:
        print("El ID debe ser un número.")
        return

    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT nombre, pais_origen, sitio_web FROM desarrolladoras WHERE id_desarrolladora = %s",
        (id_,),
    )
    actual = cursor.fetchone()
    if actual is None:
        print("No existe una desarrolladora con ese ID.")
        cursor.close()
        conn.close()
        return

    print("Dejá vacío para mantener el valor actual.")
    nombre = input(f"Nombre [{actual[0]}]: ").strip() or actual[0]
    pais = input(f"País [{actual[1] or '-'}]: ").strip() or actual[1]
    sitio = input(f"Sitio web [{actual[2] or '-'}]: ").strip() or actual[2]

    cursor.execute(
        "UPDATE desarrolladoras SET nombre = %s, pais_origen = %s, sitio_web = %s "
        "WHERE id_desarrolladora = %s",
        (nombre, pais, sitio, id_),
    )
    conn.commit()
    print("Desarrolladora actualizada.")
    cursor.close()
    conn.close()


def eliminar():
    try:
        id_ = int(input("ID de la desarrolladora a eliminar: "))
    except ValueError:
        print("El ID debe ser un número.")
        return

    if input("¿Seguro que querés eliminarla? (s/n): ").strip().lower() != "s":
        print("Operación cancelada.")
        return

    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM desarrolladoras WHERE id_desarrolladora = %s", (id_,)
        )
        conn.commit()
        if cursor.rowcount == 0:
            print("No existe una desarrolladora con ese ID.")
        else:
            print("Desarrolladora eliminada.")
    except mysql.connector.IntegrityError:
        print("No se puede eliminar: tiene videojuegos asociados.")
    finally:
        cursor.close()
        conn.close()


def menu():
    opciones = {"1": crear, "2": listar, "3": actualizar, "4": eliminar}
    while True:
        print("\n=== CRUD Desarrolladoras ===")
        print("1. Crear")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("0. Salir")
        eleccion = input("Elegí una opción: ").strip()
        if eleccion == "0":
            print("Hasta luego.")
            break
        accion = opciones.get(eleccion)
        if accion is None:
            print("Opción inválida.")
            continue
        try:
            accion()
        except mysql.connector.Error as e:
            print("Error de base de datos:", e)


if __name__ == "__main__":
    menu()