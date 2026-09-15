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

Sprint 1 completado: Django REST Framework 3.18.1 y `authtoken` fueron
configurados inicialmente con `TokenAuthentication`, `IsAuthenticated` y
paginación de 10 elementos. Sprint 4 reemplazó esa autenticación por JWT.

Sprint 2 completado: `ProductoSerializer` y `ProductoViewSet` exponen el modelo
existente mediante `/api/productos/` y `/api/productos/<id>/`. La API requiere
autenticación y convive con el CRUD HTML y Django Admin, que permanecen
operativos.

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
- el token access se envía como `Authorization: Bearer <token>`;
- todas las operaciones de productos requieren autenticación;
- GET, POST, PUT y PATCH están disponibles para usuarios autenticados;
- DELETE está restringido a usuarios staff.

Se comprobaron respuestas 401 para ausencia o invalidez del JWT, 403 para
DELETE no staff y 204 para DELETE staff. La evidencia está en
`pruebas/sprint4_seguridad.txt` y no contiene credenciales ni tokens.

### Endpoints de la API

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/api/productos/` | Lista paginada de productos |
| POST | `/api/productos/` | Crea un producto |
| GET | `/api/productos/<id>/` | Obtiene un producto |
| PUT | `/api/productos/<id>/` | Reemplaza un producto |
| PATCH | `/api/productos/<id>/` | Actualiza parcialmente un producto |
| DELETE | `/api/productos/<id>/` | Elimina un producto; solo staff |
| POST | `/api/token/` | Obtiene access y refresh |
| POST | `/api/token/refresh/` | Renueva el token access |
| GET | `/api/schema/` | Genera el esquema OpenAPI |
| GET | `/api/docs/` | Abre la documentación Swagger |

El listado usa paginación de 10 elementos. Se comprobaron los códigos 200,
201, 204, 400, 401, 403 y 404. Nunca se deben guardar tokens reales ni
contraseñas en código, documentación o evidencias.

## PostgreSQL local

PostgreSQL 18.6 está disponible en Windows y la base local `ratastock` fue
creada y validada con Django. El driver `psycopg[binary]==3.3.5` ya está
incluido en `requirements.txt`. Se aplicaron las migraciones existentes sin
cambiar `Producto` ni generar migraciones nuevas de inventario.

SQLite sigue siendo el respaldo cuando `DATABASE_URL` está vacía o no existe.
Una URL PostgreSQL definida en el entorno selecciona esa base tanto en local
como en Render. El formato de referencia, sin valores reales, es
`postgresql://<usuario>:<clave-codificada>@<host>:<puerto>/ratastock`.
Los caracteres especiales de usuario y clave deben codificarse para una URL.

Para no guardar la credencial ni escribirla en el historial de PowerShell,
introducir la URL mediante una entrada oculta y usarla sólo durante el proceso:

```powershell
$pgLocalUrl = Read-Host "DATABASE_URL de PostgreSQL local" -AsSecureString
$env:DATABASE_URL = [System.Net.NetworkCredential]::new("", $pgLocalUrl).Password
$env:DEBUG = "True"
try {
    .\.venv\Scripts\python.exe manage.py check
    .\.venv\Scripts\python.exe manage.py migrate
    .\.venv\Scripts\python.exe manage.py runserver
} finally {
    Remove-Item Env:DATABASE_URL -ErrorAction SilentlyContinue
    $pgLocalUrl.Dispose()
    Remove-Variable pgLocalUrl
}
```

La prueba de ORM, login, listado HTML, Admin y API JWT pasó sobre PostgreSQL.
Los datos temporales se revirtieron; la base quedó con cero productos y cero
usuarios. No se copiaron productos ni cuentas desde SQLite y `db.sqlite3`
permanece intacta. Para acceso persistente al Admin de PostgreSQL, crear un
superusuario mediante `manage.py createsuperuser` en ese entorno.

## Preparación para Render

El proyecto está preparado para ejecutarse en Render, pero la creación y
configuración del servicio se realizan por separado. No se afirma todavía un
despliegue exitoso.

La base de datos se selecciona mediante el entorno:

- sin `DATABASE_URL`, el desarrollo local continúa usando `db.sqlite3`;
- con `DATABASE_URL`, Render usa PostgreSQL mediante `dj-database-url` y
  `psycopg`.

Variables de entorno requeridas en Render:

| Variable | Configuración |
|---|---|
| `SECRET_KEY` | Valor secreto generado para producción |
| `DATABASE_URL` | URL interna de la base PostgreSQL de Render |
| `DEBUG` | `False` |

Render proporciona `RENDER_EXTERNAL_HOSTNAME`, que se agrega a
`ALLOWED_HOSTS`. No se deben guardar valores reales en Git ni en evidencias.

Comando de construcción:

```bash
./build.sh
```

El script instala `requirements.txt`, recopila archivos estáticos y aplica las
migraciones. WhiteNoise sirve los archivos generados en `STATIC_ROOT`.

Comando de inicio:

```bash
python -m gunicorn ratastock.asgi:application -k uvicorn.workers.UvicornWorker
```
