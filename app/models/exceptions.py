from flask import jsonify

class CustomException(Exception):
    def __init__(self, status_code, name= 'Custom error', description = 'Error' ):
        super().__init__()
             
        self.status_code = status_code
        self.name = name
        self.description = description
        
    def get_response(self):
        response = jsonify({
            'error': {
                'code' : self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })

        response.status_code = self.status_code
        return response
    

class DatosInvalidos(CustomException):
    def __init__(self, status_code, name, description):
        super().__init__(status_code, name, description)
        self.status_code = 400
        self.name = self.name
        self.description = self.description

    def get_response(self):
        response = jsonify({
            'error': {
                'status_code': self.status_code,
                'name': self.name,
                'description': self.description
            }
        })
        response.status_code = self.status_code
        return response
     # Ejemplo en controller: raise DatosInvalidos(400, "Peticion invalida", "El servidor ya existe")
    

class NoAutorizado(CustomException):
    def __init__(self, status_code, name, description):
        super().__init__(status_code, name, description)
        self.status_code = 403
        self.name = self.name
        self.description = self.description

    def get_response(self):
        response = jsonify({
            'error': {
                'status_code': self.status_code,
                'name': self.name,
                'description': self.description
            }
        })
        response.status_code = self.status_code
        return response
    # Ejemplo: raise NoAutorizado(403, "No autorizado", "No tienes los permisos necesarios para realizar esta accion")

class ErrorServidor(CustomException):
    def __init__(self, status_code, name, description):
        super().__init__(status_code, name, description)
        self.status_code = 500
        self.name = self.name
        self.description = self.description

    def get_response(self):
        response = jsonify({
            'error': {
                'status_code': self.status_code,
                'name': self.name,
                'description': self.description
            }
        })
        response.status_code = self.status_code
        return response
    # Ejemplo: raise ErrorServidor(500, "Error de servidor", "Se ha producido un error inesperado")

class NoEncontrado(CustomException):
    def __init__(self, status_code, name, description):
        super().__init__(status_code, name, description)
        self.status_code = 404
        self.name = self.name
        self.description = self.description

    def get_response(self):
        response = jsonify({
            'error': {
                'status_code': self.status_code,
                'name': self.name,
                'description': self.description
            }
        })
        response.status_code = self.status_code
        return response
    # Ejemplo: raise NoEncontrado(400, "No encontrado", f"El servidor {nombre_servidor} no ha sido encontrado")

