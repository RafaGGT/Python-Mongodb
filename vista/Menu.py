from servicio.Conexion import Conexion
from controlador.ClienteController import ClienteController

class Menu:
    def __init__(self):
        self.__conexion = Conexion()
        self.__cliente_controller = ClienteController(self.__conexion)

    def mostrar_menu(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Crear Cliente")
            print("2. Agregar Producto")
            print("3. Actualizar Dirección")
            print("4. Eliminar Pedido")
            print("5. Buscar clientes por ciudad")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_cliente()
            elif opcion == "2":
                self.agregar_producto()
            elif opcion == "3":
                self.actualizar_direccion()
            elif opcion == "4":
                self.eliminar_pedido()
            elif opcion == "5":
                self.buscar_por_ciudad()
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def crear_cliente(self):

        nombre = input("Ingrese nombre: ")
        email = input("Ingrese email: ")
        ciudad = input("Ingrese ciudad: ")
        pais = input("Ingrese país: ")
        pregunta = input("¿Desea registrar un producto para este cliente? (s/n): ")
        if pregunta.lower() != 's':
            print("Cliente registrado sin producto.")
            self.__cliente_controller.crear_cliente(nombre, email, ciudad, pais, None, None, None)
            return
        else:
            producto = input("Ingrese producto: ")
            cantidad = input("Ingrese cantidad: ")
            precio = input("Ingrese precio: ")
            self.__cliente_controller.crear_cliente(nombre, email, ciudad, pais, producto, cantidad, precio)
            print("Cliente registrado correctamente")
        
    def agregar_producto(self):
        self.__cliente_controller.ver_clientes()
        email = input("Ingrese el email del cliente: ")
        producto = input("Ingrese producto: ")
        cantidad = input("Ingrese cantidad: ")
        precio = input("Ingrese precio: ")
        self.__cliente_controller.agregar_producto(email, producto, cantidad, precio)
        print("Producto agregado correctamente")

    def actualizar_direccion(self):
        self.__cliente_controller.ver_clientes()
        email = input("Ingrese el email del cliente a actualizar: ")
        ciudad = input("Ingrese nueva ciudad: ")
        pais = input("Ingrese nuevo país: ")
        res = self.__cliente_controller.actualizar_direccion(email, ciudad, pais)
        if getattr(res, 'modified_count', 0) > 0:
            print("Dirección actualizada correctamente")
        else:
            print("No se actualizó la dirección (cliente no encontrado o mismo valor)")

    def eliminar_pedido(self):
        self.__cliente_controller.ver_clientes()
        email = input("Ingrese el email del cliente: ")
        producto = input("Ingrese el nombre del producto a eliminar del pedido: ")
        res = self.__cliente_controller.eliminar_pedido(email, producto)
        if getattr(res, 'modified_count', 0) > 0:
            print("Pedido eliminado correctamente")
        else:
            print("No se eliminó ningún pedido (cliente o producto no encontrado)")

    def buscar_por_ciudad(self):
        ciudad = input("Ingrese la ciudad a buscar: ")
        self.__cliente_controller.buscar_clientes_por_ciudad(ciudad)

    