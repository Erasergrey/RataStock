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

Sprints 1 y 2 completados.

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

Pendiente:

- CRUD propio;
- templates;
- login y logout propios;
- protección de vistas.
- pruebas finales.

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
