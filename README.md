# RataStock ES2

RataStock ES2 es una aplicación académica desarrollada con Django para gestionar productos mediante una base de datos, Django Admin, operaciones CRUD, autenticación y sesiones.

## Evaluación

- 2.1.1 Base de datos.
- 2.1.2 Django Admin.
- 2.1.3 CRUD.
- 2.1.4 Backend, base de datos, seguridad e IA.

## Stack previsto

- Python
- Django
- SQLite
- Django ORM
- Django Admin
- Django Auth
- Django Sessions
- HTML
- CSS
- Git
- GitHub
- Inteligencia artificial como apoyo

## Estado

Sprint 5 completado.

Django y SQLite están configurados, el modelo `Producto` está implementado y
puede administrarse desde Django Admin mediante un superusuario local. La
aplicación permite listar, crear, editar y eliminar productos mediante vistas y
templates propios mediante Django ORM y el modelo `Producto`.

El Sprint 4 incorpora login y logout propios con las vistas nativas de Django,
sesiones, protección de las cuatro vistas CRUD y CSRF. El login está en
`/login/` y el logout requiere POST a `/logout/`. Las credenciales se ingresan
directamente en la aplicación y no deben almacenarse en Git.

El usuario confirmó las pruebas manuales de login, persistencia de sesión,
CRUD autenticado, Django Admin y logout POST con bloqueo posterior del CRUD.
Las validaciones técnicas finales pasaron, sin migraciones nuevas y con
Sessions aplicada. El producto original permanece intacto y no quedan
productos temporales del Sprint 4.

## Interfaz y dashboard

La interfaz propia se implementa con HTML/CSS mediante Django Templates. El
listado /productos/ funciona como dashboard de inventario y presenta total de
productos, activos, sin stock y stock total calculados desde el modelo
existente. Los precios se muestran en CLP con separador de miles.

El diseño usa una paleta navy/azul, sidebar adaptativa, tarjetas, tabla
responsive, badges de estado y formularios coherentes. Django, SQLite, ORM,
Auth, Sessions, Admin y la semántica del CRUD se mantienen sin cambios de
arquitectura.

MyCodeBank se usó únicamente como referencia visual de un proyecto previo del
estudiante. RataStock no incorpora React, Vite, Firebase ni lógica bancaria.

## EVA3 — En desarrollo

RataStock será extendido mediante Django REST Framework para exponer el recurso
Producto como API RESTful, conservando las pantallas HTML y funcionalidades de
EVA2.

Rama de desarrollo: `eva3`.

Sprint 1 completado: Django REST Framework 3.18.1 y `authtoken` están
configurados con `TokenAuthentication`, `IsAuthenticated` y paginación de 10
elementos.

Sprint 2 completado: `ProductoSerializer` y `ProductoViewSet` exponen el modelo
existente mediante `/api/productos/` y `/api/productos/<id>/`. La API requiere
autenticación y convive con el CRUD HTML y Django Admin, que permanecen
operativos. El endpoint para obtener tokens todavía no está implementado.

### Respuestas HTTP comprobadas

| Código | Caso validado |
|---|---|
| 200 | Listado y detalle; actualización mediante PUT y PATCH |
| 201 | Creación válida de un producto temporal |
| 204 | Eliminación del producto temporal |
| 400 | Rechazo de un producto con stock negativo y error en `stock` |
| 401 | Solicitud a la API sin autenticación |
| 404 | Consulta de un ID inexistente |

Las pruebas usan JSON paginado, no desactivan validaciones y eliminan sus datos
temporales al finalizar. La evidencia de Sprint 3 está en
`pruebas/sprint3_api.txt`.

### Seguridad JWT

La API usa JWT mediante Simple JWT 5.5.1:

- `POST /api/token/` obtiene los tokens access y refresh;
- `POST /api/token/refresh/` renueva el token access;
- todas las operaciones de productos requieren autenticación;
- GET, POST, PUT y PATCH están disponibles para usuarios autenticados;
- DELETE está restringido a usuarios staff.

Se comprobaron respuestas 401 para ausencia o invalidez del JWT, 403 para
DELETE no staff y 204 para DELETE staff. La evidencia está en
`pruebas/sprint4_seguridad.txt` y no contiene credenciales ni tokens.
