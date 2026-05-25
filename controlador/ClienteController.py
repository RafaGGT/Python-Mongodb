from servicio.ClienteService import ClienteService    

class ClienteController:

    def __init__(self, conexion):
        self.__service = ClienteService(conexion)

    def ver_clientes(self):
        clientes = self.__service.ver_cliente()

        print("\n------------------------------\n")
        print("Clientes:")
        for cliente in clientes:
            print("Nombre: ", cliente.nombre)
            print("Email: ", cliente.email)
            print("Ciudad: ", cliente.direccion.get("ciudad"))
            print("Pais: ", cliente.direccion.get("pais"))
            # Mostrar pedidos del cliente si existen
            if cliente.pedidos:
                print("Pedidos:")
                for p in cliente.pedidos:
                    print(f"  - Producto: {p.get('producto')}, Cantidad: {p.get('cantidad')}, Precio: {p.get('precio')}")
            else:
                print("Pedidos: Ninguno")
        print("\n------------------------------\n")

    def crear_cliente(self, nombre, email, ciudad, pais, producto, cantidad, precio):
        return self.__service.crear_cliente(nombre, email, ciudad, pais, producto, cantidad, precio)
    
    def agregar_producto(self, email, producto, cantidad, precio):
        return self.__service.agregar_producto(email, producto, cantidad, precio)

    def actualizar_direccion(self, email, ciudad, pais):
        return self.__service.actualizar_direccion(email, ciudad, pais)

    def eliminar_pedido(self, email, producto):
        # Mostrar pedidos que coinciden antes de eliminar
        clientes = self.__service.ver_cliente()
        cliente = next((c for c in clientes if c.email == email), None)
        if cliente is None:
            print("Cliente no encontrado")
            return None
        pedidos_coincidentes = [p for p in cliente.pedidos if p.get("producto") == producto]
        if not pedidos_coincidentes:
            print("No se encontraron pedidos con ese producto para el cliente especificado.")
            return None

        print("\nPedidos que se eliminarán:")
        for p in pedidos_coincidentes:
            print(f"- Producto: {p.get('producto')}, Cantidad: {p.get('cantidad')}, Precio: {p.get('precio')}")

        confirmar = input("¿Confirma eliminar estos pedidos? (s/n): ")
        if confirmar.lower() != 's':
            print("Operación cancelada.")
            return None

        res = self.__service.eliminar_pedido(email, producto)
        if getattr(res, 'modified_count', 0) > 0:
            print("Pedido(s) eliminado(s) correctamente.")
        else:
            print("No se eliminaron pedidos (cliente o producto no encontrado).")

        return res

    def buscar_clientes_por_ciudad(self, ciudad):
        clientes = self.__service.buscar_por_ciudad(ciudad)

        print("\n---- Clientes en ciudad: {} ----\n".format(ciudad))
        for cliente in clientes:
            print("Nombre: ", cliente.nombre)
            print("Email: ", cliente.email)
            print("Ciudad: ", cliente.direccion.get("ciudad"))
            print("Pais: ", cliente.direccion.get("pais"))
            print("-----------------------------")

        return clientes

    