# Control_Inventario_SQLite
 Este código es un programa de control de inventario que utiliza una base de datos SQLite para almacenar información sobre los productos.Este programa proporciona una forma básica de gestionar un inventario utilizando una base de datos SQLite y la entrada del usuario desde la línea de comandos.
 
Importa los módulos sqlite3 y tabulate. sqlite3 es un módulo de Python que permite interactuar con bases de datos SQLite, mientras que tabulate es un módulo que ayuda a mostrar los datos en forma de tabla.

Establece una conexión con la base de datos SQLite llamada inventario.db y crea un cursor para ejecutar comandos SQL.

Crea una tabla llamada productos si no existe. Esta tabla tiene columnas para el ID (clave primaria), nombre del producto, cantidad, precio, descripción y rubro.

Muestra un mensaje de bienvenida al usuario y entra en un bucle while que permite al usuario elegir entre varias opciones:

Añadir un producto.
Buscar productos por nombre.
Modificar productos existentes.
Ver todos los productos almacenados.
Salir del programa.
Dependiendo de la opción elegida por el usuario, el programa realiza diferentes acciones:

Para añadir un producto, solicita al usuario que ingrese información sobre el producto y lo inserta en la base de datos.
Para buscar un producto, permite al usuario buscar productos por su nombre en la base de datos y muestra la información si se encuentra.
Para modificar un producto, permite al usuario buscar un producto por su nombre, actualizar la información y guardar los cambios en la base de datos.
Para ver todos los productos, recupera todos los registros de la tabla productos y los muestra en forma de tabla utilizando el módulo tabulate.
Para salir del programa, rompe el bucle while y cierra la conexión a la base de datos.
