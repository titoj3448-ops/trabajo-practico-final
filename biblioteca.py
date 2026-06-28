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
