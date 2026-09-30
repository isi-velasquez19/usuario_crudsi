from config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, datos):
        query = "INSERT INTO usuarios (nombre, apellido, email) VALUES(%(nombre)s, %(apellido)s, %(email)s);"
        return connectToMySQL('usuarios_crud').query_db(query, datos)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        usuario_en_db = connectToMySQL('usuarios_crud').query_db(query)
        usuarios = []
        for usuario in usuario_en_db:
            usuarios.append(cls(usuario))
        return usuarios
    
    @classmethod
    def get_one(cls,datos):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        usuario_en_db = connectToMySQL('usuarios_crud').query_db(query,datos)

        return cls(usuario_en_db[0])
    
    @classmethod
    def update(cls, datos):
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL('usuarios_crud').query_db(query, datos)
    
    @classmethod
    def delete(cls, datos):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL('usuarios_crud').query_db(query, datos)

