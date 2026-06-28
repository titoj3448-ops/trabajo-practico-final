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
