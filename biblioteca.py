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
    

# ── LIBRO ───────────────────────────────────────────────────
class Libro(metaclass=MiMeta):
    def __init__(self, titulo, autor, isbn, anio, paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.anio = anio
        self.paginas = paginas
        self.disponible = True

    def mostrar(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"  [{estado}] {self.titulo} - {self.autor} | ISBN: {self.isbn} | {self.anio} | {self.paginas} págs.")


# ── PRESTAMO (composición: usa Libro y Usuario) ─────────────
class Prestamo(metaclass=MiMeta):
    def __init__(self, libro, usuario):
        self.libro = libro          # composición con Libro
        self.usuario = usuario      # agregación con Usuario
        self.fecha_prestamo = datetime.now().strftime("%d/%m/%Y")
        self.fecha_devolucion = None
        self.activo = True
        self.libro.disponible = False

    def devolver(self):
        self.activo = False
        self.fecha_devolucion = datetime.now().strftime("%d/%m/%Y")
        self.libro.disponible = True

    def mostrar(self):
        estado = "ACTIVO" if self.activo else "DEVUELTO"
        devuelto = self.fecha_devolucion if self.fecha_devolucion else "---"
        print(f"  [{estado}] '{self.libro.titulo}' → {self.usuario.nombre} {self.usuario.apellido} | Prestado: {self.fecha_prestamo} | Devuelto: {devuelto}")

# ── LISTAS GLOBALES (almacenamiento simple) ─────────────────
libros = []
usuarios = []
prestamos = []


# ── FUNCIONES DE LIBROS ─────────────────────────────────────
@registrar_accion
def agregar_libro():
    titulo  = input("  Título: ")
    autor   = input("  Autor: ")
    isbn    = input("  ISBN: ")
    anio    = input("  Año: ")
    paginas = input("  Páginas: ")
    libros.append(Libro(titulo, autor, isbn, anio, paginas))
    print("  ✅ Libro agregado.")

@registrar_accion
def modificar_libro():
    isbn = input("  ISBN del libro a modificar: ")
    libro = buscar_libro(isbn)
    if libro:
        libro.titulo  = input(f"  Nuevo título ({libro.titulo}): ") or libro.titulo
        libro.autor   = input(f"  Nuevo autor ({libro.autor}): ") or libro.autor
        libro.anio    = input(f"  Nuevo año ({libro.anio}): ") or libro.anio
        libro.paginas = input(f"  Nuevas páginas ({libro.paginas}): ") or libro.paginas
        print("  ✅ Libro modificado.")
    else:
        print("  ❌ Libro no encontrado.")

@registrar_accion
def eliminar_libro():
    isbn = input("  ISBN del libro a eliminar: ")
    libro = buscar_libro(isbn)
    if libro:
        if not libro.disponible:
            print("  ❌ No se puede eliminar un libro prestado.")
        else:
            libros.remove(libro)
            print("  ✅ Libro eliminado.")
    else:
        print("  ❌ Libro no encontrado.")

def listar_libros():
    if not libros:
        print("  (No hay libros registrados)")
    for l in libros:
        l.mostrar()

def buscar_libro(isbn):
    for l in libros:
        if l.isbn == isbn:
            return l
    return None
