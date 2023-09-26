from flask import Blueprint

from ..controllers.servidor_controller import ServidorController

servidor_bp = Blueprint('servidor_bp', __name__)

servidor_bp.route('/', methods=['GET'])(ServidorController.traer_todos)
servidor_bp.route('/<int:id_servidor>', methods=['GET'])(ServidorController.traer_servidor)
servidor_bp.route('/<string:nombre_usuario>', methods=['GET'])(ServidorController.traer_servidores_por_usuario)
servidor_bp.route('/', methods=['POST'])(ServidorController.crear_nuevo)
servidor_bp.route('/<int:id_servidor>', methods=['DELETE'])(ServidorController.eliminar_servidor)
# buscar un servidor por nombre
servidor_bp.route('/buscar/<string:nombre_servidor>', methods=['GET'])(ServidorController.traer_servidor_por_nombre)


servidor_bp.route('/usuario/<int:id_usuario>', methods=['GET'])(ServidorController.traer_servidores_por_id_usuario)
