from flask import request
from app.models.chat import Chat


class ChatController:

    @classmethod
    def traer_chats_canal(self, id_canal):
        """Obtiene una lista de chats de un canal especifico, ordenado de los mas antiguos a los mas recientes """
        chats_obj = Chat.traer_chats(id_canal)
        chats = []
        for chat in chats_obj:
            chats.append(chat.serialize())
        return chats, 200
    
    @classmethod
    def publicar(self, id_canal):
        """Publica un mensaje en el chat"""
        data = request.json
        chat = Chat(**data)

        chat.id_canal = id_canal
        
        Chat.crear_mensaje(chat)
        return {"message": "Mensaje publicado exitosamente"}