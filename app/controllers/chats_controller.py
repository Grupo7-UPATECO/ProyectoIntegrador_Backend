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
    
    @classmethod
    def eliminar(self,id_canal, id_chat):
        """Borra un chat con id X de un canal de id X"""
        chats_obj = Chat.traer_chats(id_canal)
        msj_a_borrar = Chat(id_chat=id_chat)
        for chat in chats_obj:
            if chat.id_chat == msj_a_borrar.id_chat:
                Chat.eliminar_mensaje(msj_a_borrar)
       
        # TODO EXCEPTION EN CASO QUE EL MENSAJE NO EXISTA / 
        # TODO el usuario que euire eliminar el mensaje debe ser el autor
        
        return {'message': 'Mensaje eliminado exitosamente'}