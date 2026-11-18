# Tareas del proyecto: E-commerce con FastAPI

En este proyecto van a ampliar la REST API. Hoy ya existe el CRUD de **productos**; deben agregar **categorías** y **órdenes**.

> Nuestra "base de datos" es el archivo `src/db/mock.json`. Cada tarea que cree datos nuevos debe guardarlos allí.

## Cómo está organizado el código

Cada recurso tiene tres archivos. Usen `products` como ejemplo:

| Carpeta | Qué contiene | Ejemplo |
|---|---|---|
| `src/routes/` | Los endpoints (las URLs) | `products.py` |
| `src/models/` | Leer y escribir en el `mock.json` | `product.py` |
| `src/schemas/` | Los datos que se piden y se devuelven | `product.py` |

Cada archivo de rutas nuevo se registra en `src/routes/__init__.py`.

---

## Tarea 1: CRUD de categorías

**Objetivo:** poder crear, ver, editar y eliminar categorías (por ejemplo: "Tecnología", "Alimentos", "Bebidas").

**Pasos:**
1. En `mock.json`, agregar la llave `"categories"` con 2 o 3 ejemplos (`id`, `name`, `description`).
2. Crear `schemas/category.py`, `models/category.py` y `routes/categories.py`.
3. Registrar el router en `src/routes/__init__.py`.

**Endpoints:**

| Método | Ruta | Qué hace |
|---|---|---|
| GET | `/categories` | Lista todas las categorías |
| GET | `/categories/{id}` | Muestra una categoría |
| POST | `/categories` | Crea una categoría |
| PUT | `/categories/{id}` | Edita una categoría |
| DELETE | `/categories/{id}` | Elimina una categoría |

**Listo cuando:** puedes probar los 5 endpoints en `/docs` de FastAPI y los cambios se ven en `mock.json`.

---

## Tarea 2: Relacionar productos con categorías

**Objetivo:** que cada producto pertenezca a una categoría.

**Pasos:**
1. En `mock.json`, agregar `"category_id"` a cada producto. Será una "clave foránea ficticia": un número que apunta al `id` de una categoría.
2. Actualizar los schemas de producto (`ProductBase`, `ProductRead`, `ProductUpdate`) para incluir `category_id`.
3. Ajusten **crear** y **editar** producto:
   - Si la categoría **no existe**, respondan con error `404` y un mensaje de error.
   - Si existe, guardar el producto normalmente.

**Listo cuando:** no se puede crear ni editar un producto con una categoría inventada.

---

## Tarea 3: Ver la categoría de un producto

**Objetivo:** consultar un producto y recibir también los datos de su categoría.

**Endpoint nuevo:**

| Método | Ruta | Qué hace |
|---|---|---|
| GET | `/products/{id}/category` | Devuelve la categoría del producto |

**Pista:** buscar el producto, tomar su `category_id` y con él buscar la categoría. Si el producto no existe, error `404`.

**Listo cuando:** `/products/1/category` devuelve la categoría correcta.

---

## Tarea 4: Órdenes de compra

**Objetivo:** que un cliente pueda comprar productos, y que el sistema revise que hay suficiente **stock** referente a las unidades disponibles.

**Datos de ejemplo** (ya están en `mock.json`):
- Cada producto tiene ahora un campo `"stock"`.
- Existe la llave `"orders"` con una orden de ejemplo:

```json
{
  "id": 1,
  "products": [
    { "product_id": 1, "quantity": 2 },
    { "product_id": 3, "quantity": 4 }
  ],
  "total": 1004.0
}
```

**Pasos:**
1. Creen `schemas/order.py`, `models/order.py` y `routes/orders.py`.
2. Registrar el router en `src/routes/__init__.py`.

**Endpoints:**

| Método | Ruta | Qué hace |
|---|---|---|
| GET | `/orders` | Lista todas las órdenes |
| GET | `/orders/{id}` | Muestra una orden |
| POST | `/orders` | Crea una orden |

**Validaciones al crear una orden** (si alguna falla, no se guarda nada):
- Cada producto debe existir y estar activo (`is_active`).
- La cantidad (`quantity`) debe ser mayor que 0.
- La cantidad pedida no puede superar el `stock` del producto. Ejemplo: si quedan 10 laptops y piden 15, responder con error `400` y un mensaje claro.

**Cuando la orden es válida:**
1. Calcular el `total` (precio × cantidad de cada producto, sumados).
2. Descuenten del `stock` de los productos las unidades compradas.
3. Guarden la orden con un `id` nuevo.

**Listo cuando:**
- Una orden válida se guarda con el total correcto y el stock baja.
- Una orden con demasiada cantidad devuelve error y el stock **no** cambia.

---

## Resumen

| # | Tarea | Dificultad |
|---|---|---|
| 1 | CRUD de categorías | Fácil |
| 2 | Productos con categoría | Media |
| 3 | Categoría de un producto | Fácil |
| 4 | Órdenes y validación de stock | Difícil |
