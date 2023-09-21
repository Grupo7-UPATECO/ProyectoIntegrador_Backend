from flask import Blueprint
from app.models.exceptions import DatosInvalidos, ErrorServidor, NoAutorizado, NoEncontrado

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(DatosInvalidos)
def maneja_datos_invalidos(error):
    return error.get_response()

@errors.app_errorhandler(NoAutorizado)
def maneja_datos_invalidos(error):
    return error.get_response()

@errors.app_errorhandler(ErrorServidor)
def maneja_datos_invalidos(error):
    return error.get_response()

@errors.app_errorhandler(NoEncontrado)
def maneja_datos_invalidos(error):
    return error.get_response()