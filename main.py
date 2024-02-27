import sqlite3
from tabulate import tabulate

# Crear o conectar a la base de datos SQLite
conn = sqlite3.connect('inventario.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        cantidad INTEGER,
        precio INTEGER,
        descripcion TEXT,
        rubro TEXT
    )
''')
conn.commit()

print("Bienvenidos al control de inventarios".center(60, "-"))

while True:
    print("""
    (1) Añadir producto
    (2) Buscar productos
    (3) Modificar productos
    (4) Ver productos
    (5) Salir
    """)

    respuesta = int(input("Ingrese su opción: "))
    
    if respuesta == 1:
        ap = input("Ingrese el nombre del producto: ")
        ac = int(input("Ingrese la cantidad de su producto: "))
        apre = int(input("Ingrese el precio del su producto: "))
        descripcion = input("Ingrese la descripción del producto: ")
        rubro = input("Ingrese el rubro del producto (limpieza, comida, varios): ")

        # Insertar datos en la base de datos
        cursor.execute('''
            INSERT INTO productos (nombre, cantidad, precio, descripcion, rubro)
            VALUES (?, ?, ?, ?, ?)
        ''', (ap, ac, apre, descripcion, rubro))
        conn.commit()

    elif respuesta == 2:
        buscador = input("Ingrese el nombre del producto que quiere buscar: ")
        cursor.execute('SELECT * FROM productos WHERE nombre = ?', (buscador,))
        resultado = cursor.fetchone()

        if resultado:
            print("El nombre del producto es:", resultado[1])
            print("La cantidad del producto es:", resultado[2])
            print("El precio del producto es:", resultado[3])
            print("La descripción del producto es:", resultado[4])
            print("El rubro del producto es:", resultado[5])
        else:
            print("Producto no encontrado")

    elif respuesta == 3:
        buscador = input("Ingrese el nombre del producto que quiere modificar: ")
        cursor.execute('SELECT * FROM productos WHERE nombre = ?', (buscador,))
        resultado = cursor.fetchone()

        if resultado:
            ap = input("Ingrese el nombre del producto: ")
            ac = int(input("Ingrese la cantidad de su producto: "))
            apre = int(input("Ingrese el precio del su producto: "))
            descripcion = input("Ingrese la descripción del producto: ")
            rubro = input("Ingrese el rubro del producto (limpieza, comida, varios): ")

            # Actualizar datos en la base de datos
            cursor.execute('''
                UPDATE productos
                SET nombre = ?, cantidad = ?, precio = ?, descripcion = ?, rubro = ?
                WHERE id = ?
            ''', (ap, ac, apre, descripcion, rubro, resultado[0]))

            conn.commit()
        else:
            print("Producto no encontrado")

    elif respuesta == 4:
        # Mostrar todos los productos en forma de tabla
        cursor.execute('SELECT * FROM productos')
        productos = cursor.fetchall()

        if productos:
            headers = ["ID", "Nombre", "Cantidad", "Precio", "Descripción", "Rubro"]
            table_data = [[producto[0], producto[1], producto[2], producto[3], producto[4], producto[5]] for producto in productos]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        else:
            print("No hay productos registrados")

    elif respuesta == 5:
        break

# Cerrar la conexión a la base de datos al salir del bucle
conn.close()