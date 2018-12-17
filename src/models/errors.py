class InternoError(Exception):
    def __init__(self, message="Internal server Error.", status_code=500):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
    def __str__(self):
        return "Error: "+self.message
    def to_dic(self):
        return {'message':self.message,'status_code':self.status_code}

class LoginError(Exception):
    def __init__(self, message="Error al iniciar sesión.", status_code=404):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
    def __str__(self):
        return "Error: "+self.message
    def to_dic(self):
        return {'message':self.message,'status_code':self.status_code}

class LoginUserError(Exception):
    def __init__(self, message="El usuario no existe.", status_code=404):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
    def __str__(self):
        return "Error: "+self.message
    def to_dic(self):
        return {'message':self.message,'status_code':self.status_code}

class LoginPasswordError(Exception):
    def __init__(self, message="Contraseña incorrecta.", status_code=404):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
    def __str__(self):
        return "Error: "+self.message
    def to_dic(self):
        return {'message':self.message,'status_code':self.status_code}

class NoExistenUsuariosError(Exception):
    def __init__(self, message="No se han ingresado usuarios.", status_code=404):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
    def __str__(self):
        return "Error: "+self.message
    def to_dic(self):
        return {'message':self.message,'status_code':self.status_code}

class YaExisteUsuarioError(Exception):
    def __init__(self, message="El usuario ya existe!.", status_code=409):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
    def __str__(self):
        return "Error: "+self.message
    def to_dic(self):
        return {'message':self.message,'status_code':self.status_code}

class YaExisteEmailError(Exception):
    def __init__(self, message="Este email ya se encuentra registrado!.", status_code=409):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
    def __str__(self):
        return "Error: "+self.message
    def to_dic(self):
        return {'message':self.message,'status_code':self.status_code}

class UsuarioInvalidoError(Exception):
    def __init__(self, message="El usuario no es válido!.", status_code=400):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
    def __str__(self):
        return "Error: "+self.message
    def to_dic(self):
        return {'message':self.message,'status_code':self.status_code}

class UserNameError(Exception):
    def __init__(self, message="Nombre de usuario no válido, debe contener por lo menos 4 letras y/o números.", status_code=400):
        self.message=message
        self.status_code=status_code
    def __str__(self):
        return "Error: "+self.message
    def to_dic(self):
        return {'message':self.message,'status_code':self.status_code}

class EmailError(Exception):
    def __init__(self, message="Email no válido.", status_code=400):
        self.message=message
        self.status_code=status_code
    def __str__(self):
        return "Error: "+self.message
    def to_dic(self):
        return {'message':self.message,'status_code':self.status_code}

class PasswordInvalidaError(Exception):
    def __init__(self,message="Contraseña no válida, debe contener al menos 6 caracteres.", status_code=400):
        self.message=message
        self.status_code=status_code
    def __str__(self):
        return "Error: "+self.message
    def to_dic(self):
        return {'message':self.message,'status_code':self.status_code}

class TriviasGanadasError(Exception):
    def __init__(self,message="Valor no válido. Debe ser int.", status_code=500):
        self.message=message
        self.status_code=status_code
    def __str__(self):
        return "Error: "+self.message
    def to_dic(self):
        return {'message':self.message,'status_code':self.status_code}
    
class TiempoInvalidoError(Exception):
    def __init__(self,message="Valor no válido. Debe ser float.", status_code=500):
        self.message=message
        self.status_code=status_code
    def __str__(self):
        return "Error: "+self.message
    def to_dic(self):
        return {'message':self.message,'status_code':self.status_code}