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
        
