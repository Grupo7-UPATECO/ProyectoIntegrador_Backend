from flask import Blueprint

from ..controllers.servidor_controller import ServidorController

servidor_bp = Blueprint('servidor_bp', __name__)

servidor_bp.route('/', methods=['GET'])(ServidorController.traer_todos)
servidor_bp.route('/<int:id_servidor>', methods=['GET'])(ServidorController.traer_servidor)
servidor_bp.route('/', methods=['POST'])(ServidorController.crear_nuevo)
servidor_bp.route('/<int:id_servidor>', methods=['DELETE'])(ServidorController.eliminar_servidor)