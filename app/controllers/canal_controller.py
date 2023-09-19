from flask import request
from app.models.canal import Canal




class CanalController:
    
        @classmethod
        def traer_todos(self):
            """Trae todos los canales"""
            canales_obj = Canal.obtener_canales()
            canales = []
            for canal in canales_obj:
                canales.append(canal.serialize())
            return canales, 200
        
        @classmethod
        def traer_canales_servidor(self, id_servidor):
            """Devuelve los canales de un servidor"""
            canales_obj = Canal.traer_canales_servidor(id_servidor)
            canales = []
            for canal in canales_obj:
                canales.append(canal.serialize())
            return canales, 200
        
        @classmethod
        def crear_nuevo(self):
            """Crea un nuevo canal. Si el nombre ya existe, arroja un error"""
            data = request.json
            canal = Canal(**data)
    
            nombre_canal = data.get('nombre_canal')
    
            if canal.existe(nombre_canal):
                # AGREGAR EXCEPCIONES
                return {'error': 'El canal ya existe'},400
            else:
                Canal.crear_canal(canal)
            return {'message': 'canal creado exitosamente'}, 200
        
