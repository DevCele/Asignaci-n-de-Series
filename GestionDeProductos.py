import os

productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            cantidad = int(input("Introduce la cantidad disponible: "))
            break
        except ValueError:
            print("Por favor, introduce valores numéricos válidos para el precio y la cantidad.")
    
    producto = {
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    
    productos.append(producto)
    print(f"Producto '{nombre}' añadido con éxito.")

def ver_productos():
    if not productos:
        print("No hay productos en la lista.")
        return
    
    print("Productos disponibles:")
    for idx, producto in enumerate(productos, start=1):
        print(f"{idx}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            while True:
                try:
                    nuevo_nombre = input("Introduce el nuevo nombre del producto (dejar en blanco para no cambiar): ")
                    if nuevo_nombre:
                        producto['nombre'] = nuevo_nombre
                    nuevo_precio = input("Introduce el nuevo precio del producto (dejar en blanco para no cambiar): ")
                    if nuevo_precio:
                        producto['precio'] = float(nuevo_precio)
                    nueva_cantidad = input("Introduce la nueva cantidad del producto (dejar en blanco para no cambiar): ")
                    if nueva_cantidad:
                        producto['cantidad'] = int(nueva_cantidad)
                    print(f"Producto '{nombre}' actualizado con éxito.")
                    return
                except ValueError:
                    print("Por favor, introduce valores numéricos válidos para el precio y la cantidad.")
    
    print(f"No se encontró el producto '{nombre}'.")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado con éxito.")
            return
    
    print(f"No se encontró el producto '{nombre}'.")

def guardar_datos():
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados en 'productos.txt'.")

def cargar_datos():
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(',')
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })
        print("Datos cargados desde 'productos.txt'.")

def menu():
    cargar_datos()
    
    while True:
        print("\nMenu:")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()