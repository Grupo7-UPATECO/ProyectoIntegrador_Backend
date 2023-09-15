from flask import request
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
            # AGREGAR EXCEPCIONES
            return {'error': 'El servidor ya existe'},400
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
            # RAISE EXCEPTION
            return {'error': 'El servidor no existe'}, 400
        
    # DELETE
    @classmethod
    def eliminar_servidor(self,id_servidor):
        """Borra un servidor"""
        servidor = Servidor(id_servidor=id_servidor)
        # EXCEPCION EN CASO DE QUE EL SERVIDOR NO EXISTA
        Servidor.eliminar_servidor(servidor)
        return {'message': 'Servidor eliminado exitosamente'}
            
