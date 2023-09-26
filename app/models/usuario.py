from app.database import DatabaseConnection


class Usuario:
    def __init__(self, id_usuario = None, nombre_usuario = None, nombre = None, apellido = None, email = None, contrasena = None, imagen_perfil=None):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasena = contrasena
        self.imagen_perfil = imagen_perfil

    def serialize(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre_usuario": self.nombre_usuario,
            "nombre" : self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "contrasena": self.contrasena,
            "imagen_perfil": self.imagen_perfil
        }
        
    @classmethod
    def existe(self, usuario):
        """Verifica si hay un usuario y contraseña registrados en la base de datos"""
        query = """SELECT id_usuario FROM discordio.usuarios WHERE nombre_usuario = %s AND contrasena = %s"""
        params = (usuario.nombre_usuario, usuario.contrasena)
        resultado = DatabaseConnection.fetch_one(query, params=params)
        return resultado
    
    @classmethod
    def obtener_usuario(self, usuario):
        """Obtiene la todos los datos de un usuario segun su nombre de usuario"""
        query = """SELECT * FROM discordio.usuarios WHERE nombre_usuario = %s;"""
        params = usuario.nombre_usuario,
        print(params)
        resultado = DatabaseConnection.fetch_one(query, params=params)
        if resultado is not None:
            return self(*resultado)
   
        return None

    @classmethod
    def registrar_nuevo(self, usuario):
        """Registra en la base de datos un nuevo usuario"""
        query = """INSERT INTO discordio.usuarios (nombre_usuario, nombre, apellido, email, contrasena) VALUES (%s, %s, %s, %s, %s)"""
        params = usuario.nombre_usuario, usuario.nombre, usuario.apellido, usuario.email, usuario.contrasena
        result = DatabaseConnection.execute_query(query, params=params)
        return result
    
    # UPDATE `discordio`.`usuarios` SET `nombre_usuario` = 'marpe' WHERE (`id_usuario` = '7');
    @classmethod
    def modificar_datos(cls, usuario):
        """Modifica la informacion de un usuario en la base de datos"""
        columnas = {"nombre_usuario", "nombre", "apellido", "email"}
        query_list = []
        params = []

        for clave, valor in usuario.__dict__.items():
            if clave in columnas and valor is not None:
                query_list.append(f"{clave} = %s")
                params.append(valor)
        params.append(usuario.id_usuario)

        query = "UPDATE discordio.usuarios SET "+",".join(query_list) + " WHERE id_usuario = %s"
        result = DatabaseConnection.execute_query(query, params=params)

        if result:
            return usuario
        else:
            return None