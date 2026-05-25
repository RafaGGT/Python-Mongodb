class Cliente:

    def __init__(self, nombre, email, ciudad, pais, pedidos=None):
        self.__nombre = nombre
        self.__email = email

        self.__direccion = {
            "ciudad": ciudad,
            "pais": pais
        }

        self.__pedidos = pedidos if pedidos else []

    def to_dict(self):
        return {
            "nombre": self.__nombre,
            "email": self.__email,
            "direccion": self.__direccion,
            "pedidos": self.__pedidos
        }

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    @property
    def pedidos(self):
        return self.__pedidos
    
    @pedidos.setter
    def pedidos(self, pedidos):
        self.__pedidos = pedidos

    