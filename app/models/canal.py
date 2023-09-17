from app.database import DatabaseConnection

class Canal:


    def __init__(self, id_canal=None, nombre_canal=None, id_servidor=None ):
        self.id_canal = id_canal
        self.nombre_canal= nombre_canal
        self.id_servidor = id_servidor
    
    def serialize(self):
        """Serializa el objeto y retorna un diccionario"""
        return {
            "id_canal" : self.id_canal,
            "nombre_canal" : self.nombre_canal,
            "id_servidor" : self.id_servidor
        }
    

    @classmethod
    def obtener_canales(cls):
        """Obtiene los canales de la y los devuelve en una lista"""
        query = """SELECT * FROM discordio.canales"""
        resultados = DatabaseConnection.fetch_all(query)
        
        canales = []
        if resultados is not None:
            for resultado in resultados:
                canales.append(cls(*resultado))
        return canales
    
    @classmethod
    def traer_canales_servidor(cls, id_servidor):
        """Obtiene los canales de un servidor"""
        query = """SELECT * FROM discordio.canales WHERE id_servidor = %s"""
        params = id_servidor,
        resultados = DatabaseConnection.fetch_all(query, params=params)
        
        canales = []
        if resultados is not None:
            for resultado in resultados:
                canales.append(cls(*resultado))
        return canales
