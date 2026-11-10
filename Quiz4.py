from pymongo import MongoClient

db = MongoClient("mongodb://localhost:27017")["tec"]["estudiantes"]
db.drop()

# CREATE: un expediente = un documento (historial con campos flexibles)
db.insert_many([
    {"carnet": "2024100001", "nombre": "Ana", "plan": 411,
     "cursos": ["CE2103", "CE1101"],
     "proyectos": [{"nombre": "Simulador", "tareas": [
         {"t": "Diseño", "ok": True}, {"t": "GC", "ok": False}]}],
     "historial": [{"curso": "CE1101", "nota": 92}]},
    {"carnet": "2023200045", "nombre": "Luis", "plan": 412, "especialidad": "Embebidos",
     "cursos": ["CE3201", "CE2103"],
     "proyectos": [{"nombre": "Driver SPI", "tareas": [{"t": "Driver", "ok": True}]}],
     "historial": [{"curso": "CE2101", "nota": 85, "laboratorio": 88}]},
])

# READ: por campo anidado
print(list(db.find({"cursos": "CE2103"}, {"_id": 0, "nombre": 1})))

# UPDATE: subtarea anidada y nueva calificación con otros campos
db.update_one({"carnet": "2024100001"},
              {"$set": {"proyectos.0.tareas.1.ok": True},
               "$push": {"historial": {"curso": "CE2103", "nota": 95, "rubrica": {"quices": 100}}}})

# AGGREGATE: promedio por plan
print(list(db.aggregate([{"$unwind": "$historial"},
                         {"$group": {"_id": "$plan", "promedio": {"$avg": "$historial.nota"}}}])))

# DELETE: retirar un curso
db.update_one({"carnet": "2023200045"}, {"$pull": {"cursos": "CE3201"}})
print(db.find_one({"carnet": "2023200045"}, {"_id": 0, "cursos": 1}))