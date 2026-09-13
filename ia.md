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

La implementación del Sprint 4 está en validación: las pruebas anónimas,
CSRF y migraciones pasaron; falta la prueba autenticada con el superusuario
local antes de cerrar el Sprint. No se almacenaron credenciales en Git ni se
modificó la contraseña existente. El usuario debe iniciar sesión directamente
en el navegador sin compartir sus credenciales en el chat o la documentación.
