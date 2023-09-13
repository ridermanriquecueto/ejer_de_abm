from flask import Flask, request, jsonify
from database import init_db, get_alumnos, get_alumno_by_legajo, add_alumno, update_alumno, delete_alumno

app = Flask(__name__)
init_db()  # Inicializa la base de datos SQLite

# Ruta para obtener todos los alumnos
@app.route('/alumnos', methods=['GET'])
def obtener_alumnos():
    alumnos = get_alumnos()
    return jsonify(alumnos)

# Ruta para agregar un nuevo alumno
@app.route('/alumnos', methods=['POST'])
def agregar_alumno():
    data = request.json
    legajo = add_alumno(data['nombre'], data['apellido'], data['edad'])
    return jsonify({'legajo': legajo}), 201

# Ruta para obtener un alumno por su legajo
@app.route('/alumnos/<int:legajo>', methods=['GET'])
def obtener_alumno(legajo):
    alumno = get_alumno_by_legajo(legajo)
    if alumno:
        return jsonify(alumno)
    else:
        return jsonify({'error': 'Alumno no encontrado'}), 404

# Ruta para actualizar un alumno por su legajo
@app.route('/alumnos/<int:legajo>', methods=['PUT'])
def actualizar_alumno(legajo):
    data = request.json
    success = update_alumno(legajo, data['nombre'], data['apellido'], data['edad'])
    if success:
        return jsonify({'message': 'Alumno actualizado'}), 200
    else:
        return jsonify({'error': 'Alumno no encontrado'}), 404

# Ruta para eliminar un alumno por su legajo
@app.route('/alumnos/<int:legajo>', methods=['DELETE'])
def eliminar_alumno(legajo):
    success = delete_alumno(legajo)
    if success:
        return jsonify({'message': 'Alumno eliminado'}), 200
    else:
        return jsonify({'error': 'Alumno no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/alumnos', methods=['GET'])
def obtener_alumnos():
    print("Entrando en la función obtener_alumnos")
    alumnos = get_alumnos()
    print("Alumnos obtenidos:", alumnos)
    return jsonify(alumnos)


