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
