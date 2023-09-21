from flask import Blueprint

from ..controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint('usuario_bp', __name__)

usuario_bp.route('/inicio_sesion', methods=['POST'])(UsuarioController.inicio_sesion)
usuario_bp.route('/perfil', methods=['GET'])(UsuarioController.mostrar_usuario)
usuario_bp.route('/cerrar_sesion', methods=['GET'])(UsuarioController.cerrar_sesion)
