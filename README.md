# Quiz #4 - NoSQL: Expedientes académicos con MongoDB

## Escenario
La Escuela de Ingeniería en Computadores necesita gestionar expedientes
académicos. Cada estudiante:
- se matricula en varios cursos,
- tiene proyectos con subtareas,
- posee un historial de calificaciones cuya estructura varía según el
  plan de estudio o la especialidad.

## Tipo de base de datos: Documentos (MongoDB)
Se eligió porque:
1. **Un expediente = un documento.** Cursos, proyectos y tareas van anidados,
   por lo que se lee todo en una sola consulta, sin joins.
2. **Esquema flexible.** El historial de un plan puede tener campos distintos
   a otro (rúbricas, laboratorio, componentes) sin alterar tablas.
3. **Consultas sobre datos anidados.** `cursos.codigo`, `proyectos.tareas.completada`.
4. **Agregaciones.** Progreso de proyectos y promedio por plan con `$aggregate`.

## Modelo (colección `estudiantes`)
{ carnet, nombre, plan_estudio, especialidad,
  cursos: [ {codigo, estado, ...} ],
  proyectos: [ {nombre, tareas: [ {titulo, completada} ]} ],
  historial: [ {curso, nota, ...campos variables} ] }

## Operaciones implementadas
Crear (insert_many), consultar por campos anidados, actualizar subtareas
(array_filters), agregar calificaciones ($push), agregaciones y eliminar
cursos ($pull).

## Ejecución
1. `docker run -d -p 27017:27017 mongo`
2. `pip install -r requirements.txt`
3. `python main.py`

## Autores
Nombre 1, Nombre 2
