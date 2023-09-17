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