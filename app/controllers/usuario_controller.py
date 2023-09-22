from app.models.exceptions import DatosInvalidos, NoAutorizado, NoEncontrado
from ..models.usuario import Usuario

from flask import request, session

class UsuarioController:

    @classmethod
    def inicio_sesion(cls):
        """Inicia sesion"""
        data = request.json
        usuario = Usuario(
            nombre_usuario = data.get('nombre_usuario'),
            contrasena = data.get('contrasena')
        )
        
        if Usuario.existe(usuario):
            session['nombre_usuario'] = data.get('nombre_usuario')
            return {"message": "Sesion iniciada"}, 200
        else:
            return {"message": "Usuario o contraseña incorrectos"}, 401
    
   
    @classmethod
    def mostrar_usuario(cls):
        """Devuelve los datos del usuario logueado"""
        nombre_usuario = session.get('nombre_usuario')
        if nombre_usuario:
            usuario_logeado = Usuario(nombre_usuario=nombre_usuario)
            resultado = Usuario.obtener_usuario(usuario_logeado)
            if resultado is None:
                # return {"message": "Usuario no encontrado"}, 404
                raise NoEncontrado(404, "No encontrado", f"El usuario {nombre_usuario} no ha sido encontrado")
            return resultado.serialize(), 200
        else:
            return {"message": "Usuario no encontrado"}, 400
    
    @classmethod
    def cerrar_sesion(cls):
        """Destruye la sesion"""
        session.pop('nombre_usuario', None)
        return {"message": "Sesion cerrada"}, 200
    

    @classmethod
    def crear_cuenta(cls):
        """Recibe los datos del formulario de registro y envia a la base de datos"""
        data = request.json
        usuario = Usuario(**data)
        nombre_usuario = data.get('nombre_usuario')
        if usuario.obtener_usuario(usuario) is None:
            Usuario.registrar_nuevo(usuario)
            return {"message": "Usuario creado exitosamente."}
        else:
            raise DatosInvalidos(400, "Petición invalida", f"El usuario {nombre_usuario} ya existe. Elije otro nombre de usuario.")
           
        