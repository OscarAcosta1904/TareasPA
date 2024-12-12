from tienda.tienda import Tienda

tienda = Tienda()

print("Hola")

for producto in Tienda.lista_productos:
    print(f"ID: {producto.ide}, Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}")