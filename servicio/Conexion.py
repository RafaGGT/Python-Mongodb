from pymongo import MongoClient
from pymongo.errors import PyMongoError

class Conexion:
    # Crea la conexión a MongoDB
    def __init__(self, uri="mongodb://localhost:27017/", database="tiendadb"):
        try:
            self.client = MongoClient(uri)
            self.db = self.client[database]

            # Verifica conexión
            self.client.admin.command("ping")

        except PyMongoError as error:
            raise ConnectionError(f"No fue posible conectar con MongoDB: {error}")

    # Retorna la base de datos
    def obtener_conexion(self):
        return self.db

    # Cierra conexión
    def cerrar_conexion(self):
        try:
            self.client.close()
        except PyMongoError:
            pass