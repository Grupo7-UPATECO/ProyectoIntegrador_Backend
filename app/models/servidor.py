from app.database import DatabaseConnection


class Servidor:
    """Modelo del Servidor"""
    def __init__(self, id_servidor=None, nombre_servidor=None, id_usuario=None ):
        self.id_servidor = id_servidor
        self.nombre_servidor= nombre_servidor
        self.id_usuario = id_usuario

    def serialize(self):
        return {
            "id_servidor" : self.id_servidor,
            "nombre_servidor" : self.nombre_servidor,
            "id_usuario" : self.id_usuario
        }
    
    # NOT TESTED
    @classmethod
    def existe(cls, nombre_servidor):
        """Verifica si un servidor con X nombre ya existe """
        servidores = cls.obtener_servidores()
        for servidor in servidores:
            if servidor.nombre_servidor == nombre_servidor:
                return True
        return False
    
    @classmethod
    def obtener_servidores(cls):
        query = """SELECT * FROM discordio.servidor"""
        servidores = DatabaseConnection.fetch_all(query)
        return servidores