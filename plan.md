# 1. Problema

Se necesita administrar productos e inventario de forma persistente. El registro manual o temporal dificulta consultar, actualizar y mantener información consistente sobre los productos disponibles.

# 2. Solución

RataStock ES2 utilizará Django y una base de datos para registrar productos y permitir operaciones CRUD.

# 3. Objetivo general

Implementar una aplicación back end con base de datos, Django Admin, CRUD y manejo seguro de sesiones.

# 4. Objetivos específicos

- Configurar una base de datos mediante Django.
- Crear un modelo Producto.
- Gestionarlo mediante Django Admin.
- Implementar Create, Read, Update y Delete.
- Incorporar login, logout y sesiones.
- Proteger las operaciones que requieran autenticación.
- Utilizar IA como apoyo documentado.

# 5. Alcance

Incluye:

- productos;
- base de datos;
- CRUD;
- Admin;
- autenticación;
- sesiones;
- interfaz HTML/CSS.

Excluye:

- API;
- React;
- pagos;
- carrito;
- ERP;
- CRM.

# 6. Arquitectura prevista

```text
Usuario
  ↓
Templates
  ↓
Views Django
  ↓
Django ORM
  ↓
Base de datos SQLite

Administrador
  ↓
Django Admin
  ↓
Django ORM
  ↓
Base de datos
```

# 7. Seguridad prevista

- Django Auth;
- Django Sessions;
- `login_required`;
- CSRF;
- `SECRET_KEY` mediante variables de entorno.

Estas medidas todavía no se implementan en el Sprint 0.

# EVA3

## Problema

La aplicación actual responde a usuarios humanos mediante páginas HTML. EVA3
debe permitir que otros programas consulten y modifiquen productos mediante
JSON sin reemplazar la interfaz existente.

## Solución

Agregar una API RESTful con Django REST Framework sobre el modelo `Producto`
existente, conservando el CRUD HTML, Django Admin, autenticación y sesiones de
EVA2.

```text
Persona  → HTML
Programa → API JSON
             ↓
          Producto
             ↓
        Django ORM
             ↓
           SQLite
```

El desarrollo se realizará por etapas en la rama `eva3`. El Sprint 0 define
solamente el alcance y el versionado; Django REST Framework y la API se
implementarán desde el Sprint 1.
