from flask import request
from app.models.exceptions import DatosInvalidos, NoEncontrado
from app.models.servidor import Servidor


class ServidorController:
#  CREATE
    @classmethod
    def crear_nuevo(self):
        """Crea un nuevo servidor. Si el nombre ya existe, arroja un error"""
        data = request.json
        servidor = Servidor(**data)

        nombre_servidor = data.get('nombre_servidor')

        if servidor.existe(nombre_servidor):
            raise DatosInvalidos(400, "Petición invalida", f"El servidor {nombre_servidor} ya existe")
            
        else:
            Servidor.crear_servidor(servidor)
            return {'message': 'servidor creado exitosamente'}, 200
    
# READ

    @classmethod
    def traer_todos(self):
        """Trae todos los servidores"""
        servidores_obj = Servidor.obtener_servidores()
        servidores = []
        for servidor in servidores_obj:
            servidores.append(servidor.serialize())
        return servidores, 200
    
    @classmethod
    def traer_servidor(self, id_servidor):
        """Devuelve un servidor"""
        servidor = Servidor(id_servidor=id_servidor)
        resultado = Servidor.obtener_servidor(servidor)
        if resultado is not None:
            return resultado.serialize(), 200
        else:
            raise NoEncontrado(404, "No encontrado", "El servidor no existe")
        
    # DELETE
    @classmethod
    def eliminar_servidor(self,id_servidor):
        """Borra un servidor"""
        servidor = Servidor(id_servidor=id_servidor)
        # EXCEPCION EN CASO DE QUE EL SERVIDOR NO EXISTA
        print(servidor.id_servidor)
        if servidor.obtener_servidor(servidor) is None:
            raise NoEncontrado(404, "No encontrado", "El servidor no existe")
        else:
            Servidor.eliminar_servidor(servidor)
            return {'message': 'Servidor eliminado exitosamente'}
            
    @classmethod
    def traer_servidores_por_usuario(self, nombre_usuario):
        """Trae los servidores a los que pertenece un usuario, si un usuario no pertenece a ningun servidor, se produce un error"""
        # nombre_usuario = Usuario(nombre_usuario=nombre_usuario)
        resultado = Servidor.traer_servidores_de_un_usuario(nombre_usuario=nombre_usuario)
        servidores = []
        if len(resultado) > 0:
            for servidor in resultado:
                servidores.append(servidor.serialize())
            return servidores, 200
        else:
            raise DatosInvalidos(400, "Peticion invalida", f"El usuario {nombre_usuario} no se ha unido a ningun servidor")
        
    
    #buscador
    @classmethod
    def traer_servidor_por_nombre(self, nombre_servidor):
        """Devuelve un servidor"""
        servidor = Servidor(nombre_servidor=nombre_servidor)
        resultado = Servidor.obtener_servidor_por_nombre(servidor)
        if resultado is not None:
            return resultado.serialize(), 200
        else:
            raise NoEncontrado(404, "No encontrado", "El servidor no existe")
        


    @classmethod
    def traer_servidores_por_id_usuario(cls, id_usuario):
        """Trae los nombre_servidor con el mismo id_usuario"""
        resultado = Servidor.obtener_nombre_servidores_por_id_usuario(id_usuario)
        nombres_servidores = []
        if len(resultado) > 0:
            for nombre_servidor in resultado:
                nombres_servidores.append(nombre_servidor)
            return {'nombre_servidores': nombres_servidores}, 200
        else:
            raise NoEncontrado(404, "No encontrado", f"No hay servidores para el usuario con id {id_usuario}")
