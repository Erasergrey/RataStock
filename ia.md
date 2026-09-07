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
