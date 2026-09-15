# Uso de Inteligencia Artificial

## Herramientas

ChatGPT y Codex.

## Propósito

Se utilizarán como apoyo para:

- analizar requisitos;
- planificar el proyecto;
- revisar la arquitectura Django;
- apoyar la codificación;
- diseñar interfaces;
- detectar errores;
- revisar seguridad;
- preparar pruebas.

## Responsabilidad del estudiante

Las sugerencias de IA deberán ser revisadas, comprendidas y probadas antes de incorporarse. La responsabilidad sobre las decisiones y la entrega final corresponde al estudiante.

## Primera decisión apoyada por IA

Se analizó el enunciado y se decidió mantener un proyecto pequeño centrado en base de datos, Django Admin, CRUD, autenticación y sesiones. Se descartaron API REST, React, pagos y carrito porque no son necesarios para los criterios entregados.

## Registro de consultas

| Sprint | Consulta realizada | Propuesta de IA | Decisión/corrección del estudiante |
|---|---|---|---|
| 0 | ¿Qué alcance corresponde a ES2? | Priorizar base de datos, Admin, CRUD, autenticación y sesiones. | Mantener un proyecto pequeño y excluir API, React, pagos y carrito. |
| 1 | ¿Qué estructura mínima debería tener un modelo Producto para demostrar persistencia mediante Django ORM sin agregar funcionalidades innecesarias? | Usar un único modelo con nombre, descripción, stock, precio, estado y fecha de creación; configurar SQLite y ordenar el flujo de migraciones. | Mantener solamente Producto, descartar categorías, proveedores y pedidos, y proteger `SECRET_KEY` desde el primer commit de Django. |
| 2 | ¿Qué configuración mínima de Django Admin permite demostrar correctamente la administración de un modelo Producto sin agregar funciones innecesarias? | Registrar Producto, mostrar campos relevantes, permitir búsqueda por nombre y filtro por estado activo. | Usar una configuración básica y descartar acciones personalizadas, exportaciones y dashboards. Las credenciales del superusuario permanecen locales y no se documentan ni versionan. |
| 3 | ¿Cuál es la estructura mínima para implementar un CRUD de Producto en Django mediante vistas basadas en funciones y ModelForm? | Crear un `ModelForm`, cuatro vistas, URLs y templates conectados al ORM. | Usar vistas basadas en funciones para hacer explícitas las operaciones CRUD y descartar DRF, ViewSets, API, JavaScript y clases genéricas. DELETE requiere confirmación y POST. |
| 4 | ¿Cuál es la forma más simple y segura de proteger un CRUD Django mediante autenticación y sesiones nativas sin implementar un sistema de usuarios personalizado? | Utilizar Django Auth, Django Sessions, LoginView, LogoutView, login_required y CSRF. | Se utilizaron las herramientas nativas de Django para evitar implementar manualmente contraseñas, sesiones o autenticación. Se descartaron JWT, OAuth, API tokens, usuario personalizado y roles complejos por ser innecesarios. |
| 5 | ¿Cómo adaptar el lenguaje visual de un dashboard React existente (MyCodeBank) a una aplicación Django CRUD sin reutilizar su arquitectura frontend? | Reutilizar principios visuales: sidebar, tarjetas, paleta navy/azul, dashboard de métricas, responsive y tabla mejorada; no copiar React ni Firebase. | Se reutilizó únicamente la referencia de diseño de un proyecto previo del estudiante. RataStock mantuvo Django Templates, Django ORM, SQLite, Auth y Sessions. Se descartaron React, Vite, Firebase, lógica financiera y transacciones. |

Sprint 4 completado: las pruebas anónimas, CSRF y migraciones pasaron. El
usuario confirmó las pruebas manuales de login, sesión, CRUD autenticado,
Django Admin y logout POST con bloqueo posterior del CRUD. En la verificación
final se limpió exclusivamente el producto temporal de autenticación que aún
permanecía en la base local, preservando el producto original.

No se almacenaron credenciales en Git ni se modificó la contraseña existente.
Las credenciales se ingresan directamente en la aplicación, sin compartirlas
en el chat o la documentación.

Sprint 5 completado: MyCodeBank fue utilizado exclusivamente como referencia
visual de un proyecto previo del estudiante. Se añadió una interfaz propia en
HTML/CSS con dashboard, métricas de lectura, formato CLP y responsive; no se
incorporaron su arquitectura React, Firebase, hooks, servicios ni lógica
bancaria.

# EVA3

## Herramientas

ChatGPT y Codex.

## Primer uso de IA en EVA3

Se utilizó IA para analizar la pauta, planificar la extensión REST, mantener
separadas la interfaz HTML y la futura API JSON, y definir un orden incremental
de implementación que preserve la entrega final de EVA2.

## Registro crítico obligatorio

Durante EVA3, cada consulta relevante deberá documentar:

- qué se preguntó;
- qué recomendó la IA;
- qué recomendación se descartó;
- por qué se descartó;
- qué solución decidió implementar el estudiante.

| Sprint | Consulta realizada | Recomendación de IA | Recomendación descartada y motivo | Decisión del estudiante |
|---|---|---|---|---|
| 0 | ¿Cómo extender RataStock con una API REST sin afectar las pantallas HTML de EVA2? | Reutilizar el modelo `Producto`, mantener las vistas Django existentes y construir la API en `/api/` mediante Sprints separados. | Reemplazar el CRUD HTML por una SPA, porque eliminaría evidencia funcional de EVA2 y ampliaría innecesariamente el alcance. | Conservar ambos consumidores: personas mediante HTML y programas mediante JSON. |
| 1 | ¿Qué configuración inicial de DRF permite preparar una API segura antes de crear endpoints? | Registrar DRF y `authtoken`, usar autenticación por token, exigir autenticación por defecto y configurar paginación. | La IA pudo sugerir `AllowAny` para facilitar pruebas, pero se descartó porque dejaría la API pública. | Mantener `IsAuthenticated` como permiso global, `TokenAuthentication` y páginas de 10 elementos. |
| 2 | ¿Cómo exponer `Producto` como recurso REST sin duplicar el CRUD HTML? | Crear un `ModelSerializer`, un `ModelViewSet` y registrarlo con `DefaultRouter`. | Crear vistas API manuales separadas para cada verbo, porque duplicaría comportamiento que DRF ya resuelve y aumentaría el mantenimiento. | Reutilizar el modelo `Producto`, declarar los campos explícitamente y conservar `id` y `fecha_creacion` como solo lectura. |
| 3 | ¿Cómo comprobar respuestas JSON y errores reales antes de habilitar un endpoint de tokens? | Usar `APIClient` con `force_authenticate`, datos temporales y aserciones sobre códigos y cuerpos JSON. | Desactivar validaciones o usar `@csrf_exempt`/`AllowAny` para evitar errores, porque reduciría la seguridad y ocultaría el comportamiento real de DRF. | Mantener validaciones y autenticación activas; comprobar 200, 201, 204, 400, 401 y 404 y eliminar los temporales. |
| 4 | ¿Qué autenticación y permisos permiten proteger la API y diferenciar una operación destructiva? | Usar JWT con access/refresh y combinar `IsAuthenticated` con un permiso específico para DELETE. | Se descartó dejar `TokenAuthentication` permanente porque el token estándar no expira. | Implementar Simple JWT y permitir DELETE únicamente a usuarios staff; mantener GET, POST, PUT y PATCH para usuarios autenticados. |
| 5 | ¿Cómo generar documentación verificable sin mantener manualmente un esquema separado del código? | Integrar drf-spectacular para generar OpenAPI y Swagger desde las rutas y serializers reales. | Escribir un esquema estático independiente, porque podría quedar desactualizado respecto de la implementación. | Usar `AutoSchema`, publicar `/api/schema/` y `/api/docs/`, y guardar evidencia sin secretos. |

## Decisiones críticas de EVA3

- Se rechazó `AllowAny` global porque expondría la API de productos.
- Se descartaron tokens permanentes y se eligió JWT con access/refresh.
- DELETE quedó reservado a usuarios staff; las demás acciones requieren un
  usuario autenticado.
- `ProductoSerializer` usa campos explícitos y no `fields = "__all__"`;
  `id` y `fecha_creacion` son de solo lectura.
- Las pruebas conservaron validaciones y permisos reales, sin usar
  `@csrf_exempt` como atajo.

Consulta específica de seguridad resuelta en el Sprint 4:

> ¿Qué mecanismo de autenticación y qué permisos diferenciados debe usar la
> API de RataStock para proteger escritura y lectura sin exponer credenciales?
