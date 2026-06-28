# trabajo-practico-final.
biblioteca 
# Consigna General
Desarrollar una aplicación en Python denominada Sistema de Gestión de Biblioteca Digital. El
sistema deberá permitir administrar libros, usuarios y préstamos utilizando Programación
Orientada a Objetos.

# Requerimientos Funcionales
Gestión de Libros
Datos mínimos: Título, Autor, ISBN, Año de publicación y Cantidad de páginas.
Operaciones mínimas: Alta, Modificación, Baja y Listado.
Gestión de Usuarios
Datos mínimos: Nombre, Apellido, DNI y Correo electrónico.
Operaciones mínimas: Alta, Modificación, Baja y Listado.
Gestión de Préstamos
Registrar préstamos, devoluciones y consultar préstamos activos.
Un libro no podrá prestarse si ya posee un préstamo activo.
Se deberá registrar fecha de préstamo y devolución.
Requerimientos Técnicos
• Implementar al menos una jerarquía de herencia.
• Implementar al menos un comportamiento polimórfico.
• Implementar al menos una relación de agregación.
• Implementar al menos una relación de composición.

• Implementar al menos un decorador propio e integrarlo dentro del sistema.
• Implementar una metaclase utilizando type o una clase derivada de type.
• Implementar al menos un patrón de diseño, debidamente justificado.

## Integrantes del grupo

- (Julian TTito)
- (Javier Lopez Acuña)

## Conceptos implementados

- **Herencia**: `Usuario` hereda de `Persona`
- **Polimorfismo**: el método `mostrar()` se comporta distinto en cada clase
- **Composición**: `Prestamo` usa `Libro` y `Usuario` directamente
- **Agregación**: `Usuario` puede existir sin un préstamo
- **Decorador propio**: `@registrar_accion` muestra cada acción ejecutada
- **Metaclase**: `MiMeta` cuenta las instancias creadas de cada clase
- **Patrón de diseño**: no se usan clases externas, todo está en un solo archivo (simplicidad intencional)

## Cómo ejecutar

Requiere Python 3.10 o superior.

```bash
python main.py
```
