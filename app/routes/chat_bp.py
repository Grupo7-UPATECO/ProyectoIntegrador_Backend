from flask import Blueprint

from app.controllers.chats_controller import ChatController



chat_bp = Blueprint('chat_bp', __name__)

chat_bp.route('/<int:id_canal>', methods=['GET'])(ChatController.traer_chats_canal)
chat_bp.route('/<int:id_canal>/', methods=['POST'])(ChatController.publicar)