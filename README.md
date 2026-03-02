# Equipment Management API

FastAPI CRUD API para gestión de equipos industriales.

## Features
- CRUD completo (Create, Read, Update, Delete)
- Validación con Pydantic
- Error handling (404)

## Tech Stack
- Python 3.10+
- FastAPI
- Pydantic

## Installation
```bash
pip install fastapi uvicorn
```

## Usage
```bash
uvicorn main:app --reload
```

API estará disponible en: http://127.0.0.1:8000

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome message |
| GET | /equipments | List all equipments |
| POST | /equipments | Create new equipment |
| GET | /equipments/{id} | Get specific equipment |
| PUT | /equipments/{id} | Update equipment |
| DELETE | /equipments/{id} | Delete equipment |

## Example Request

POST /equipments
```json
{
  "name": "Compresor de Aire Principal",
  "type": "Pneumatic",
  "location": "Planta Baja - Sector A",
  "status": "operational"
}
```

## Example Response
```json
{
  "equipments": [
    {
      "id": 456,
      "name": "Compresor de Aire Principal",
      "type": "Pneumatic",
      "location": "Planta Baja - Sector A",
      "status": "operational"
    }
  ]
}
```