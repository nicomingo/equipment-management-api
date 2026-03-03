from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

class Equipment(BaseModel):
    name: str
    type: str
    location: str
    status: str

equipments = [
  {
    "name": "Compresor de Aire Principal",
    "type": "Pneumatic",
    "location": "Planta Baja - Sector A",
    "status": "operational"
  },
  {
    "name": "Motor Trifásico de Inducción 50HP",
    "type": "Electrical",
    "location": "Sala de Máquinas 2",
    "status": "needs_maintenance"
  },
  {
    "name": "Bomba Centrífuga de Alta Presión",
    "type": "Hydraulic",
    "location": "Planta de Tratamiento",
    "status": "operational"
  },
  {
    "name": "Transformador de Distribución 500kVA",
    "type": "Electrical",
    "location": "Subestación Principal",
    "status": "operational"
  },
  {
    "name": "Generador Diésel de Respaldo",
    "type": "Electromechanical",
    "location": "Subsuelo - Generación",
    "status": "offline"
  }
]

def assign_IDs(equipments):
    IDs = []
    for item in equipments:
        true_or_false = True

        if "id" in item:
            IDs.append(item["id"])
        else:
            while true_or_false:
                item["id"] = random.randint(1, 1000)
                if item["id"] in IDs:
                    continue
                else:
                    true_or_false = False
    return equipments

def equipment_with_specific_ID(equipments, id):
    for item in equipments:
        if item["id"] == id:
            return item

def update_equipment(equipments, update, id):
    for item in equipments:
        if item["id"] == id:
            update["id"] = id
            item.update(update)
            return item

equipments = assign_IDs(equipments)

@app.get("/")
def root():
    return {"message": "Esta es la pagina de bienvenida"}

@app.get("/equipments")
def list_equipments():
    return {"equipments": equipments}

@app.post("/equipments", status_code=status.HTTP_201_CREATED)
def new_equipment(post: Equipment):
    equipments.append(post.model_dump())
    equipments_with_IDs = assign_IDs(equipments)
    return {"equipments": equipments_with_IDs}

@app.get("/equipments/{id}")
def get_specific_equipment(id: int):
        equipment = equipment_with_specific_ID(equipments, id)
        if equipment is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El equipo solicitado no existe en el inventario" )
        return {"equipment": equipment}

@app.put("/equipments/{id}")
def update_equipment_information(id: int, update: Equipment):
    updated_equipment = update_equipment(equipments, update.model_dump(), id)
    if updated_equipment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El equipo solicitado no existe en el inventario")
    return{"updated information": updated_equipment}

@app.delete("/equipments/{id}")
def delete_equipment(id: int):
    equipment_to_delete = equipment_with_specific_ID(equipments, id)
    if equipment_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El equipo solicitado no existe en el inventario")
    equipments.remove(equipment_to_delete)
    return {"equipments": equipments}
    
