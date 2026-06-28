from datetime import datetime


# ── METACLASE ──────────────────────────────────────────────
# Registra cuántas instancias se crean de cada clase
class MiMeta(type):
    def __init__(cls, nombre, bases, dic):
        super().__init__(nombre, bases, dic)
        cls.total = 0

    def __call__(cls, *args, **kwargs):
        cls.total += 1
        return super().__call__(*args, **kwargs)


# ── DECORADOR PROPIO ────────────────────────────────────────
# Muestra un mensaje cada vez que se llama a una función
def registrar_accion(func):
    def wrapper(*args, **kwargs):
        print(f"[Acción] Se ejecutó: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# ── CLASE BASE (herencia) ───────────────────────────────────
class Persona(metaclass=MiMeta):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar(self):
        pass  # polimorfismo: cada subclase lo implementa distinto


# ── USUARIO hereda de Persona ───────────────────────────────
class Usuario(Persona):
    def __init__(self, nombre, apellido, dni, email):
        super().__init__(nombre, apellido)
        self.dni = dni
        self.email = email

    def mostrar(self):
        print(f"  Usuario: {self.nombre} {self.apellido} | DNI: {self.dni} | Email: {self.email}")
