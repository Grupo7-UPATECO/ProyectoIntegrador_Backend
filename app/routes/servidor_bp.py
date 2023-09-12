from flask import Blueprint

from ..controllers.servidor_controller import ServidorController

servidor_bp = Blueprint('servidor_bp', __name__)

servidor_bp.route('/', methods=['GET'])(ServidorController.traer_todos)