from flask import Blueprint

from ..controllers.discordio_controller import UsuarioController

discordio_bp = Blueprint('discordio_bp', __name__)

discordio_bp.route('/inicio_sesion', methods=['POST'])(UsuarioController.inicio_sesion)
discordio_bp.route('/mostrar_usuario', methods=['GET'])(UsuarioController.mostrar_usuario)
discordio_bp.route('/cerrar_sesion', methods=['GET'])(UsuarioController.cerrar_sesion)