# FastAPI CRUD Básico

CRUD básico desarrollado con FastAPI utilizando datos en memoria (lista de diccionarios).

## Funcionalidades
- Crear películas
- Listar todas las películas
- Obtener una película por ID
- Actualizar una película por ID
- Eliminar una película por ID

## Endpoints

### Obtener todas las películas
- **GET** `/movies_all`

### Crear una película
- **POST** `/movies/`
- Body (JSON):
```json
{
  "id": 4,
  "title": "Interstellar",
  "overview": "A team travels through a wormhole...",
  "year": 2014
}
