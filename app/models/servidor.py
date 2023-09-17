from app.database import DatabaseConnection


class Servidor:
    """Modelo del Servidor"""
    def __init__(self, id_servidor=None, nombre_servidor=None, id_usuario=None ):
        self.id_servidor = id_servidor
        self.nombre_servidor= nombre_servidor
        self.id_usuario = id_usuario

    def serialize(self):
        """Serializa el objeto y retorna un diccionario"""
        return {
            "id_servidor" : self.id_servidor,
            "nombre_servidor" : self.nombre_servidor,
            "id_usuario" : self.id_usuario
        }
    
    @classmethod
    def existe(self, nombre_servidor):
        """Verifica si un servidor con X nombre ya existe """
        servidores = self.obtener_servidores()
        for servidor in servidores:
            if servidor.nombre_servidor == nombre_servidor:
                return True
        return False
    
    # CREATE
    @classmethod
    def crear_servidor(self, servidor):
        """Crea un nuevo servidor"""
        query = """INSERT INTO discordio.servidor (id_servidor, nombre_servidor, id_usuario) VALUES (%s,%s,%s)"""
        params = servidor.id_servidor, servidor.nombre_servidor, servidor.id_usuario
        DatabaseConnection.execute_query(query, params=params)

    # READ
    @classmethod
    def obtener_servidores(self):
        """Obtiene los servidores de la y los devuelve en una lista"""
        query = """SELECT * FROM discordio.servidor"""
        resultados = DatabaseConnection.fetch_all(query)
        
        servidores = []
        if resultados is not None:
            for resultado in resultados:
                servidores.append(self(*resultado))
        return servidores
    
    @classmethod
    def obtener_servidor(self, servidor):
        """Obtiene un servidor segun su id"""
        query = """SELECT id_servidor, nombre_servidor, id_usuario FROM discordio.servidor WHERE id_servidor = %s"""
        params = servidor.id_servidor,
        resultado = DatabaseConnection.fetch_one(query, params=params)
        if resultado is not None:
            return self(*resultado)
   
        return None

    # DELETE
    @classmethod
    def eliminar_servidor(self, servidor):
        """Elimina un servidor con X id"""
        query = """DELETE FROM discordio.servidor WHERE id_servidor = %s"""
        params = servidor.id_servidor,
        DatabaseConnection.execute_query(query, params=params)

    
    # READ
    # Traer los servidores a los que pertenezca un usuario
    @classmethod
    def traer_servidores_de_un_usuario(self, nombre_usuario):
        """
        Traer los servidores a los que pertenezca un usuario
        """
        query = """SELECT discordio.servidor.id_servidor, discordio.servidor.nombre_servidor, discordio.usuarios_servidor.id_usuario FROM discordio.servidor 
        INNER JOIN discordio.usuarios_servidor ON discordio.servidor.id_servidor = discordio.usuarios_servidor.id_servidor
        INNER JOIN discordio.usuarios ON discordio.usuarios_servidor.id_usuario = discordio.usuarios.id_usuario
        WHERE usuarios.nombre_usuario = %s;"""

        params = (nombre_usuario,)
        resultados = DatabaseConnection.fetch_all(query, params=params)

        servidores = []
        if resultados is not None:
            for resultado in resultados:
                servidores.append(self(*resultado))
                
        return servidores