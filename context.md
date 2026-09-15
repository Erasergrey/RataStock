# Contexto del proyecto

## Proyecto

RataStock ES2

## Objetivo

Desarrollar una aplicación web Django que permita administrar productos almacenados en una base de datos mediante operaciones CRUD.

## Problema

La versión anterior de RataStock evaluaba solicitudes utilizando un stock ingresado manualmente. En esta nueva versión los productos existirán realmente en una base de datos y cada producto tendrá información persistente.

## Requisitos académicos

- 2.1.1 Configurar conexión a base de datos.
- 2.1.2 Utilizar Django Admin.
- 2.1.3 Implementar operaciones CRUD.
- 2.1.4 Implementar una aplicación back end con acceso a base de datos, seguridad y manejo de sesiones utilizando IA como apoyo.

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

## Estado actual

Sprints 1, 2, 3, 4 y 5 completados.

Sprint 5 cerró el rediseño visual y QA final. La aplicación conserva Django,
SQLite, ORM, Auth y Sessions; no se incorporaron React, Vite ni Firebase.

Django:

- proyecto `ratastock` creado;
- aplicación `inventario` creada.

Base de datos:

- SQLite3;
- gestionada con Django ORM;
- `db.sqlite3` local e ignorada por Git.

## Modelo implementado

Producto:

- `id` automático
- `nombre`
- `descripcion`
- `stock`
- `precio`
- `activo`
- `fecha_creacion`

Migración: `inventario/migrations/0001_initial.py`.

Seguridad: `SECRET_KEY` se carga mediante `.env` y `python-decouple`.

Django Admin:

- `Producto` registrado en `inventario/admin.py`;
- listado administrativo con campos relevantes;
- búsqueda por nombre;
- filtro por estado activo;
- ordenamiento por nombre;
- superusuario local creado;
- acceso a `/admin/` validado.

Pruebas realizadas desde Django Admin:

- crear un producto;
- consultar y listar;
- buscar por nombre;
- filtrar por estado activo;
- editar el stock;
- eliminar el producto temporal.

Estas operaciones administrativas no reemplazan el CRUD propio requerido en
el Sprint 3.

CRUD propio:

- CREATE: `crear_producto()`;
- READ: `lista_productos()`;
- UPDATE: `editar_producto()`;
- DELETE: `eliminar_producto()`.

Formularios: `ProductoForm` basado en `ModelForm`.

Templates:

- `base.html`;
- `lista_productos.html`;
- `formulario_producto.html`;
- `confirmar_eliminar.html`.

Rutas:

- `/productos/`;
- `/productos/nuevo/`;
- `/productos/<id>/editar/`;
- `/productos/<id>/eliminar/`.

Persistencia: Django ORM → SQLite3.

Seguridad actual:

- Django Auth y Django Sessions nativos;
- `LoginView` en `/login/` con conservación de `next`;
- `LogoutView` en `/logout/` exclusivamente mediante POST;
- las cuatro vistas CRUD protegidas con `login_required`;
- navegación condicionada por `user.is_authenticated`;
- CSRF activo en login, formularios CRUD y logout;
- DELETE requiere confirmación y POST.

Flujo implementado:

Usuario sin sesión → login → autenticación → sesión Django → CRUD → logout
→ sesión finalizada.

Validaciones realizadas del Sprint 4:

- `manage.py check`: sin incidencias;
- login anónimo: HTTP 200;
- cuatro rutas CRUD anónimas: HTTP 302 al login conservando `next`;
- credenciales inválidas: errores visibles y sin autenticación;
- logout GET: HTTP 405;
- POST sin CSRF: HTTP 403;
- `makemigrations --check --dry-run`: sin cambios;
- migración `sessions.0001_initial` aplicada;
- modelo, migración inicial y configuración del Admin sin cambios;
- `.env`, SQLite y entorno virtual siguen ignorados por Git.

Pruebas manuales autenticadas confirmadas por el usuario:

- login correcto y listado accesible con sesión;
- sesión persistente durante la navegación;
- CREATE, READ y UPDATE autenticados correctos;
- DELETE mediante POST correcto;
- Django Admin funcionando;
- logout mediante POST correcto;
- acceso a `/productos/` después del logout redirige nuevamente al login.

Verificación final de cierre:

- `manage.py check`: sin incidencias;
- `makemigrations --check --dry-run`: `No changes detected`;
- `sessions.0001_initial`: aplicada;
- el producto original conserva todos sus campos respecto de la referencia previa;
- se detectó y eliminó exclusivamente el registro temporal de autenticación
  todavía presente al verificar la base local; queda 1 producto legítimo y
  ningún producto temporal del Sprint 4;
- `.env` y `db.sqlite3` no están versionados;
- revisión de código y documentación sin credenciales detectadas;
- sin cambios en modelo, migración inicial ni `admin.py`.

Sprint 5 — interfaz, QA y cierre:

- rediseño navy/azul propio inspirado únicamente en principios visuales de
  MyCodeBank, un proyecto previo del estudiante;
- dashboard de inventario en /productos/ con métricas de lectura obtenidas
  desde Producto: total, activos, sin stock y stock total;
- formato CLP mediante el filtro clp, sin cambiar DecimalField ni datos;
- tabla con badges, indicador de sin stock, acciones compactas y
  desplazamiento horizontal accesible;
- formularios, confirmación de eliminación y login rediseñados;
- checkbox Activo alineado con su etiqueta;
- sidebar de escritorio y navegación compacta bajo 980 px; tarjetas a dos
  columnas bajo 1200 px y a una bajo 600 px;
- QA funcional final: check y migraciones correctos; rutas anónimas,
  Auth/Sessions, CRUD, Admin y logout verificados; temporal eliminado y
  producto original intacto.

## Alcance

Incluye posteriormente:

- base de datos;
- productos persistentes;
- Django Admin;
- listado de productos;
- creación;
- edición;
- eliminación;
- login;
- logout;
- sesiones;
- protección de rutas;
- CSRF.

No incluye:

- API REST;
- React;
- carrito;
- checkout;
- pagos;
- ERP;
- CRM;
- e-commerce completo.

## Regla para futuros Sprints

Antes de realizar cualquier cambio:

1. leer `context.md`;
2. leer `README.md`;
3. leer `plan.md`;
4. leer `SPRINTS.md`;
5. revisar `git status`;
6. revisar últimos commits;
7. entender el código existente;
8. modificar únicamente el alcance del Sprint actual.

# EVA3

## Objetivo

RataStock ES3 extiende la versión final de EVA2 mediante una API RESTful. La
rama `eva3` parte exactamente de `eva2` en el commit `72b1c20`, mientras la
rama y el tag de entrega de EVA2 permanecen congelados.

La aplicación conserva:

- el modelo `Producto` existente;
- SQLite local y Django ORM;
- Django Admin;
- el CRUD HTML;
- `LoginView` y `LogoutView`;
- Django Sessions;
- el dashboard de inventario.

El Sprint 1 incorporó:

- Django REST Framework 3.18.1;
- las aplicaciones `rest_framework` y `rest_framework.authtoken`;
- autenticación global mediante `TokenAuthentication`;
- permisos globales mediante `IsAuthenticated`;
- paginación global `PageNumberPagination` con 10 elementos por página;
- las cuatro migraciones oficiales de `authtoken`.

Queda para el Sprint final:

- QA final y evidencias de entrega.

El Sprint 2 incorporó `ProductoSerializer`, `ProductoViewSet` y un
`DefaultRouter`. La API está disponible en `/api/productos/` y
`/api/productos/<id>/`, con las acciones CRUD estándar de `ModelViewSet`. Las
pantallas HTML y la API trabajan sobre el mismo modelo `Producto`, sin duplicar
la lógica CRUD manual ni crear un modelo adicional.

El Sprint 3 validó las respuestas JSON reales mediante `APIClient` y
`force_authenticate`: 200 para listado, detalle y actualizaciones; 201 para
creación; 204 para eliminación; 400 ante stock negativo; 401 sin autenticación;
y 404 para un recurso inexistente. El listado devuelve JSON paginado. Las
pruebas utilizaron un producto temporal, eliminado al finalizar, y conservaron
intacto el producto original. La evidencia se guarda en
`pruebas/sprint3_api.txt`.

El Sprint 4 reemplazó la autenticación por token permanente por JWT mediante
Simple JWT 5.5.1. `/api/token/` entrega el par access/refresh y
`/api/token/refresh/` renueva el token de acceso. La API mantiene
`IsAuthenticated`: usuarios autenticados pueden consultar, crear y actualizar,
pero DELETE requiere `is_staff`. Se comprobaron 401 sin JWT o con JWT inválido,
403 al eliminar como usuario no staff y 204 al eliminar como staff. La
evidencia sin credenciales ni tokens se guarda en
`pruebas/sprint4_seguridad.txt`.

El Sprint 5 incorporó drf-spectacular 0.30.0 y `AutoSchema`. El esquema OpenAPI
está disponible en `/api/schema/` y la interfaz Swagger en `/api/docs/`; ambas
rutas respondieron 200 y Swagger cargó correctamente. README documenta los
endpoints, JWT access/refresh, el encabezado Bearer, permisos, paginación y
códigos HTTP. La evidencia se guarda en `pruebas/sprint5_documentacion.txt` sin
credenciales ni tokens.

El Sprint 6 preparó el proyecto para Render sin realizar todavía un despliegue.
La configuración usa PostgreSQL mediante `DATABASE_URL` cuando la variable
existe y conserva SQLite como respaldo local. `DEBUG` y `SECRET_KEY` continúan
obteniéndose del entorno; `ALLOWED_HOSTS` admite una lista desde el entorno y
`RENDER_EXTERNAL_HOSTNAME` agrega el host permitido de Render. WhiteNoise sirve
los archivos estáticos recopilados en `STATIC_ROOT`.
El script `build.sh` instala dependencias, ejecuta `collectstatic` y aplica las
migraciones. El comando de inicio previsto es `gunicorn ratastock.wsgi:application`.

El QA local del Sprint 6 confirmó `manage.py check`, ausencia de migraciones
nuevas, recopilación de estáticos, login, listado HTML, Admin, Swagger y API con
JWT. También se comprobó la selección de PostgreSQL con variables ficticias,
sin conectarse a un servicio externo ni exponer secretos. El producto original
quedó intacto y el usuario temporal fue eliminado.

PostgreSQL local también fue validado sobre PostgreSQL 18.6 en Windows. Se
creó la base `ratastock`, se aplicaron todas las migraciones existentes y el
ORM confirmó conexión, lectura y escritura. Login, listado HTML, Admin,
Swagger y API JWT funcionaron sobre PostgreSQL. Los temporales se revirtieron
en una transacción: quedaron cero productos y cero usuarios en esa base.
SQLite conserva su producto legítimo y su archivo no cambió; no se migraron
datos entre motores. `DATABASE_URL` se utilizó sólo en el entorno del proceso,
sin guardar ni mostrar la credencial. Sin esa variable, SQLite continúa como
respaldo local. README documenta el inicio local mediante entrada oculta.

La configuración segura se definió antes de exponer recursos: no se utilizó
`AllowAny` global y los endpoints de productos requieren autenticación JWT.
No existen acciones API adicionales.

El recurso REST implementado es `productos`, con endpoint principal
`/api/productos/`, reutilizando el modelo `Producto` sin crear un modelo nuevo.
El serializer declara explícitamente los campos `id`, `nombre`,
`descripcion`, `stock`, `precio`, `activo` y `fecha_creacion`. Los campos `id`
y `fecha_creacion` son de solo lectura porque identifican el recurso y son
generados por Django, respectivamente. No se utilizará `fields = "__all__"`.

## Criterios académicos EVA3

- **3.1.1 — Configuración de Django REST Framework:** settings, serializer,
  ViewSet, router y paginación.
- **3.1.2 — Autenticación y permisos:** token o JWT, endpoints protegidos,
  permisos diferenciados y credenciales protegidas.
- **3.1.3 — JSON y códigos HTTP:** validación de 200, 201, 204, 400, 401, 403
  y 404 mediante un cliente HTTP.
- **3.1.4 — API RESTful:** recursos en plural, verbos HTTP, documentación,
  README, evidencias y uso crítico de IA.

## Arquitectura prevista

```text
                    RataStock
                        |
             +----------+----------+
             |                     |
          HTML ES2              API ES3
             |                     |
       Django Views           DRF ViewSet
       ModelForm              Serializer
             |                     |
             +----------+----------+
                        |
                     Producto
                        |
                   Django ORM
                        |
                     SQLite
```

Las vistas HTML existentes no se eliminarán y la API vivirá bajo `/api/`.

## Regla para los siguientes Sprints EVA3

Antes de cada Sprint futuro:

1. leer `context.md`;
2. leer `README.md`;
3. leer `plan.md`;
4. leer `SPRINTS.md`;
5. leer `ia.md`;
6. revisar `git status`;
7. revisar los últimos commits;
8. comprobar que la rama activa sea `eva3`;
9. modificar únicamente el alcance del Sprint actual.
