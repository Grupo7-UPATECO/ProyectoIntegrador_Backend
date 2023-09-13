from app.models.servidor import Servidor


class ServidorController:
    @classmethod
    def traer_todos(cls):
        servidores = Servidor.obtener_servidores()
        return servidores, 200