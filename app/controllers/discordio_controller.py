from ..models.usuario import Usuario

from flask import request, session

class UsuarioController:

    @classmethod
    def inicio_seccion(cls):
        data = request.json
        usuario = Usuario(
            nombre_usuario = data.get('nombre_usuario'),
            contraseña = data.get('contraseña')
        )
        
        if Usuario.is_registered(usuario):
            session['nombre_usuario'] = data.get('nombre_usuario')
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401
    
   
    @classmethod
    def mostrar_usuario(cls):
        nombre_usuario = session.get('username')
        usuario = Usuario.get(Usuario(nombre_usuario = nombre_usuario))
        if usuario is None:
            return {"message": "Usuario no encontrado"}, 404
        else:
            return usuario.serialize(), 200
    
    @classmethod
    def cerrar_seccion(cls):
        session.pop('nombre_usuario', None)
        return {"message": "Sesion cerrada"}, 200