# Sprint 0 — Planificación e inicialización

**Estado:** COMPLETADO

**Objetivo:** documentación, contexto, Git y planificación.

# Sprint 1 — Base Django y base de datos

**Estado:** COMPLETADO

**Objetivo:** crear proyecto Django, configurar base de datos y modelo Producto.

# Sprint 2 — Django Admin

**Estado:** COMPLETADO

**Objetivo:** registrar y gestionar Producto mediante Django Admin.

# Sprint 3 — CRUD

**Estado:** COMPLETADO

**Objetivo:** crear listado, alta, edición y eliminación de productos.

# Sprint 4 — Autenticación, sesiones y seguridad

**Estado:** COMPLETADO

**Objetivo:** login, logout, sesiones, CSRF y protección de vistas.

Implementación y pruebas anónimas completadas. El usuario confirmó las pruebas
manuales de login, sesión, CRUD autenticado, Admin y logout. Validaciones
técnicas finales superadas y datos temporales eliminados, conservando el
producto original.

# Sprint 5 — Interfaz, pruebas y entrega

**Estado:** COMPLETADO

**Objetivo:** mejoras visuales, QA, documentación, GitHub y entrega.

Rediseño propio HTML/CSS completado: dashboard de inventario, métricas de
lectura, formato CLP, tabla responsive, formularios, login y confirmación de
eliminación. QA funcional, Auth/Sessions, Admin y limpieza del producto
temporal verificados. Sin React, Vite ni Firebase.

# EVA3

## Sprint 0 — Preparación y versionado

**Estado:** COMPLETADO

**Objetivo:** preservar EVA2, crear y publicar la rama `eva3`, verificar la
aplicación existente y definir el alcance REST sin implementar la API.

## Sprint 1 — Configuración DRF

**Estado:** COMPLETADO

**Objetivo:** instalar Django REST Framework, registrarlo en `settings.py` y
configurar `REST_FRAMEWORK`.

DRF 3.18.1 y `rest_framework.authtoken` configurados. La política global usa
`TokenAuthentication`, `IsAuthenticated` y paginación de 10 elementos. Las
migraciones de `authtoken` están aplicadas; todavía no existen endpoints.

## Sprint 2 — Serializer, ViewSet y Router

**Estado:** COMPLETADO

**Objetivo:** crear `ProductoSerializer`, `ProductoViewSet` y
`/api/productos/`.

El serializer declara explícitamente los siete campos de `Producto`, con `id`
y `fecha_creacion` de solo lectura. `ProductoViewSet` reutiliza el modelo con
orden estable y el router genera las rutas de colección y detalle. HTML y API
trabajan sobre el mismo modelo; todavía no existe endpoint de tokens.

## Sprint 3 — JSON y códigos HTTP

**Estado:** COMPLETADO

**Objetivo:** probar GET, POST, PUT/PATCH, DELETE y las respuestas 200, 201,
204, 400 y 404.

Se validaron además 401 sin autenticación, JSON paginado y errores entendibles
para stock negativo. La prueba controlada cubrió colección y detalle mediante
`APIClient`, eliminó todos los datos temporales y dejó evidencia en
`pruebas/sprint3_api.txt`.

## Sprint 4 — Autenticación y permisos

**Estado:** COMPLETADO

**Objetivo:** proteger la API mediante token o JWT y permisos diferenciados;
probar las respuestas 401 y 403.

Simple JWT 5.5.1 configurado con endpoints de access/refresh. La API exige JWT
y el permiso personalizado restringe DELETE a staff, manteniendo el resto del
CRUD para usuarios autenticados. Se validaron 401, 403 y DELETE staff 204, se
eliminaron todos los temporales y se guardó evidencia en
`pruebas/sprint4_seguridad.txt`.

## Sprint 5 — Documentación, Swagger, IA y evidencias

**Estado:** COMPLETADO

**Objetivo:** documentar la API y actualizar README e `ia.md`, incluyendo una
carpeta `pruebas/` con evidencias.

drf-spectacular 0.30.0 configurado con esquema OpenAPI en `/api/schema/` y
Swagger en `/api/docs/`. README documenta endpoints, JWT, permisos, paginación
y códigos HTTP; `ia.md` consolida las decisiones críticas. Schema y Swagger
respondieron 200 y la evidencia quedó en `pruebas/sprint5_documentacion.txt`.

## Sprint 6 — Render

**Estado:** COMPLETADO

**Objetivo:** preparar el despliegue de producción sin afectar el
funcionamiento local.

Se agregaron las dependencias de producción, PostgreSQL condicionado por
`DATABASE_URL` con SQLite como respaldo local, WhiteNoise y `STATIC_ROOT`.
`build.sh` instala dependencias, recopila estáticos y ejecuta migraciones; el
inicio previsto usa `gunicorn ratastock.wsgi:application`. `ALLOWED_HOSTS`
admite una lista de entorno y suma `RENDER_EXTERNAL_HOSTNAME`. El QA local
pasó sin migraciones nuevas y mantuvo operativos HTML, Admin, Swagger y JWT.
El código está preparado, pero el servicio de Render todavía debe configurarse;
no se declara un despliegue exitoso.

## Sprint 7 — QA y entrega

**Estado:** PENDIENTE

**Objetivo:** realizar la auditoría final, pruebas, revisión de seguridad y ZIP
de EVA3.
