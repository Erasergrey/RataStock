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

Sprint 3 completado. Sprint 4 implementado, pendiente de validación autenticada
con el superusuario local antes de su cierre. Sprint 5 pendiente.

Django y SQLite están configurados, el modelo `Producto` está implementado y
puede administrarse desde Django Admin mediante un superusuario local. La
aplicación permite listar, crear, editar y eliminar productos mediante vistas y
templates propios mediante Django ORM y el modelo `Producto`.

El Sprint 4 incorpora login y logout propios con las vistas nativas de Django,
sesiones, protección de las cuatro vistas CRUD y CSRF. El login está en
`/login/` y el logout requiere POST a `/logout/`. Las credenciales se ingresan
directamente en la aplicación y no deben almacenarse en Git.

Falta verificar el login real, la navegación autenticada, el CRUD temporal,
Django Admin y el logout antes de marcar el Sprint 4 como completado.
