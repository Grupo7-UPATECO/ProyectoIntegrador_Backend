class Chat:
    """Modelo de chat"""
    def __init__(self, id_chat=None, chat = None, id_usuario=None, id_canal=None, fecha_creacion=None):
        self.id_chat = id_chat
        self.chat = chat
        self.id_usuario = id_usuario
        self.id_canal = id_canal
        self.fecha_creacion = fecha_creacion