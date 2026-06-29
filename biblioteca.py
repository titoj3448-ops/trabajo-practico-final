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

# ── FUNCIONES DE USUARIOS ───────────────────────────────────
@registrar_accion
def agregar_usuario():
    nombre   = input("  Nombre: ")
    apellido = input("  Apellido: ")
    dni      = input("  DNI: ")
    email    = input("  Email: ")
    usuarios.append(Usuario(nombre, apellido, dni, email))
    print("  ✅ Usuario agregado.")

@registrar_accion
def modificar_usuario():
    dni = input("  DNI del usuario a modificar: ")
    usuario = buscar_usuario(dni)
    if usuario:
        usuario.nombre   = input(f"  Nuevo nombre ({usuario.nombre}): ") or usuario.nombre
        usuario.apellido = input(f"  Nuevo apellido ({usuario.apellido}): ") or usuario.apellido
        usuario.email    = input(f"  Nuevo email ({usuario.email}): ") or usuario.email
        print("  ✅ Usuario modificado.")
    else:
        print("  ❌ Usuario no encontrado.")

@registrar_accion
def eliminar_usuario():
    dni = input("  DNI del usuario a eliminar: ")
    usuario = buscar_usuario(dni)
    if usuario:
        usuarios.remove(usuario)
        print("  ✅ Usuario eliminado.")
    else:
        print("  ❌ Usuario no encontrado.")

def listar_usuarios():
    if not usuarios:
        print("  (No hay usuarios registrados)")
    for u in usuarios:
        u.mostrar()

def buscar_usuario(dni):
    for u in usuarios:
        if u.dni == dni:
            return u
    return None

# ── FUNCIONES DE PRÉSTAMOS ──────────────────────────────────
@registrar_accion
def registrar_prestamo():
    isbn = input("  ISBN del libro: ")
    dni  = input("  DNI del usuario: ")
    libro   = buscar_libro(isbn)
    usuario = buscar_usuario(dni)
    if not libro:
        print("  ❌ Libro no encontrado.")
    elif not usuario:
        print("  ❌ Usuario no encontrado.")
    elif not libro.disponible:
        print("  ❌ El libro ya está prestado.")
    else:
        prestamos.append(Prestamo(libro, usuario))
        print("  ✅ Préstamo registrado.")

@registrar_accion
def registrar_devolucion():
    isbn = input("  ISBN del libro a devolver: ")
    for p in prestamos:
        if p.libro.isbn == isbn and p.activo:
            p.devolver()
            print("  ✅ Devolución registrada.")
            return
    print("  ❌ No hay préstamo activo para ese libro.")

def listar_prestamos_activos():
    activos = [p for p in prestamos if p.activo]
    if not activos:
        print("  (No hay préstamos activos)")
    for p in activos:
        p.mostrar()

def listar_todos_prestamos():
    if not prestamos:
        print("  (No hay préstamos registrados)")
    for p in prestamos:
        p.mostrar()

# ── MENÚS ────────────────────────────────────────────────────
def menu_libros():
    while True:
        print("\n--- GESTIÓN DE LIBROS ---")
        print("1. Agregar libro")
        print("2. Modificar libro")
        print("3. Eliminar libro")
        print("4. Listar libros")
        print("0. Volver")
        op = input("Opción: ")
        if op == "1": agregar_libro()
        elif op == "2": modificar_libro()
        elif op == "3": eliminar_libro()
        elif op == "4": listar_libros()
        elif op == "0": break
        else: print("Opción inválida.")

def menu_usuarios():
    while True:
        print("\n--- GESTIÓN DE USUARIOS ---")
        print("1. Agregar usuario")
        print("2. Modificar usuario")
        print("3. Eliminar usuario")
        print("4. Listar usuarios")
        print("0. Volver")
        op = input("Opción: ")
        if op == "1": agregar_usuario()
        elif op == "2": modificar_usuario()
        elif op == "3": eliminar_usuario()
        elif op == "4": listar_usuarios()
        elif op == "0": break
        else: print("Opción inválida.")

def menu_prestamos():
    while True:
        print("\n--- GESTIÓN DE PRÉSTAMOS ---")
        print("1. Registrar préstamo")
        print("2. Registrar devolución")
        print("3. Ver préstamos activos")
        print("4. Ver todos los préstamos")
        print("0. Volver")
        op = input("Opción: ")
        if op == "1": registrar_prestamo()
        elif op == "2": registrar_devolucion()
        elif op == "3": listar_prestamos_activos()
        elif op == "4": listar_todos_prestamos()
        elif op == "0": break
        else: print("Opción inválida.")

def main():
    while True:
        print("\n=== SISTEMA DE BIBLIOTECA DIGITAL ===")
        print("1. Libros")
        print("2. Usuarios")
        print("3. Préstamos")
        print("0. Salir")
        op = input("Opción: ")
        if op == "1": menu_libros()
        elif op == "2": menu_usuarios()
        elif op == "3": menu_prestamos()
        elif op == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
