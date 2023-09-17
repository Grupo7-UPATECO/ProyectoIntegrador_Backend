from app.database import DatabaseConnection


class Chat:
    """Modelo de chat"""
    def __init__(self, id_chat=None, chat = None, id_usuario=None, nombre_usuario = None, id_canal=None, fecha_creacion=None):
        self.id_chat = id_chat
        self.chat = chat
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.id_canal = id_canal
        self.fecha_creacion = fecha_creacion

    def serialize(self):
        """Serializa el objeto y retorna un diccionario"""
        return {
            "id_chat" : self.id_chat,
            "chat" : self.chat,
            "id_usuario" : self.id_usuario,
            "nombre_usuario" : self.nombre_usuario,
            "id_canal" : self.id_canal,
            "fecha_creacion"  : self.fecha_creacion
        }
    
    @classmethod
    def traer_chats(self, id_canal):
        """
        Obtiene los chats que los usuarios dejaron en un canal especifico
        """
        query = """SELECT discordio.chats.id_chat, discordio.chats.chat, discordio.chats.id_usuario, discordio.usuarios.nombre_usuario, discordio.chats.id_canal, discordio.chats.fecha_creacion FROM discordio.chats 
        INNER JOIN discordio.usuarios ON discordio.chats.id_usuario = discordio.usuarios.id_usuario
        WHERE discordio.chats.id_canal = %s ORDER BY fecha_creacion;"""

        params = id_canal,
        resultados = DatabaseConnection.fetch_all(query, params=params)

        chats = []
        if resultados is not None:
            for resultado in resultados:
                chats.append(self(*resultado))
        
        return chats