from flask import Blueprint

from ..controllers.canal_controller import CanalController

canal_bp = Blueprint('canal_bp', __name__)

canal_bp.route('/', methods=['GET'])(CanalController.traer_todos)
canal_bp.route('/<id_servidor>', methods=['GET'])(CanalController.traer_canales_servidor)

