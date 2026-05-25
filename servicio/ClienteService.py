import modelo.Cliente as c
class ClienteService:

    def __init__(self, conexion):
        db = conexion.obtener_conexion()

        self.__coleccion = db["clientes"]

    def ver_cliente(self):
        clientes_db = self.__coleccion.find(
            {},
            {"_id": 0}
        )

        clientes = []

        for cliente in clientes_db:
            direccion = cliente.get("direccion", {})
            ciudad = direccion.get("ciudad")
            pais = direccion.get("pais")

            clientes.append(
                c.Cliente(
                    cliente.get("nombre"),
                    cliente.get("email"),
                    ciudad,
                    pais,
                    cliente.get("pedidos", [])
                )
            )

        return clientes

    def crear_cliente(self, nombre, email, ciudad, pais, producto, cantidad, precio):
        pedidos = []

        if producto and cantidad and precio:
            pedidos.append({
                "producto": producto,
                "cantidad": cantidad,
                "precio": precio
            })

        cliente = c.Cliente(
            nombre,
            email,
            ciudad,
            pais,
            pedidos
        )

        return self.__coleccion.insert_one(cliente.to_dict())
    
    def agregar_producto(self, email, producto, cantidad, precio):
        pedido = {
            "producto": producto,
            "cantidad": cantidad,
            "precio": precio
        }
        return self.__coleccion.update_one(
            {"email": email},
            {"$push": {"pedidos": pedido}}
        )

    def actualizar_direccion(self, email, ciudad, pais):
        nueva_direccion = {
            "ciudad": ciudad,
            "pais": pais
        }
        return self.__coleccion.update_one(
            {"email": email},
            {"$set": {"direccion": nueva_direccion}}
        )

    def eliminar_pedido(self, email, producto):
        # Elimina todos los pedidos que coincidan con el nombre de producto
        return self.__coleccion.update_one(
            {"email": email},
            {"$pull": {"pedidos": {"producto": producto}}}
        )

    def buscar_por_ciudad(self, ciudad):
        clientes_db = self.__coleccion.find(
            {"direccion.ciudad": ciudad},
            {"_id": 0}
        )

        clientes = []
        for cliente in clientes_db:
            direccion = cliente.get("direccion", {})
            ciudad = direccion.get("ciudad")
            pais = direccion.get("pais")

            clientes.append(
                c.Cliente(
                    cliente.get("nombre"),
                    cliente.get("email"),
                    ciudad,
                    pais,
                    cliente.get("pedidos", [])
                )
            )

        return clientes
    