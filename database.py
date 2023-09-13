import sqlite3

def init_db():
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alumnos (
            legajo INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            edad INTEGER NOT NULL
        )
    ''')
 
def cargar_datos_de_ejemplo():
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    # Insertar datos de ejemplo
    cursor.execute("INSERT INTO alumnos (nombre, apellido, edad) VALUES (?, ?, ?)", ('Juan', 'Pérez', 25))
    cursor.execute("INSERT INTO alumnos (nombre, apellido, edad) VALUES (?, ?, ?)", ('María', 'González', 22))

    conn.commit()
    conn.close()


def get_alumnos():
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alumnos')
    alumnos = cursor.fetchall()
    conn.close()
    return [{'legajo': row[0], 'nombre': row[1], 'apellido': row[2], 'edad': row[3]} for row in alumnos]

def get_alumno_by_legajo(legajo):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alumnos WHERE legajo = ?', (legajo,))
    alumno = cursor.fetchone()
    conn.close()
    if alumno:
        return {'legajo': alumno[0], 'nombre': alumno[1], 'apellido': alumno[2], 'edad': alumno[3]}
    else:
        return None

def add_alumno(nombre, apellido, edad):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO alumnos (nombre, apellido, edad) VALUES (?, ?, ?)', (nombre, apellido, edad))
    conn.commit()
    legajo = cursor.lastrowid
    conn.close()
    return legajo

def update_alumno(legajo, nombre, apellido, edad):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE alumnos SET nombre = ?, apellido = ?, edad = ? WHERE legajo = ?', (nombre, apellido, edad, legajo))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    return rows_affected > 0

def delete_alumno(legajo):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM alumnos WHERE legajo = ?', (legajo,))
    conn.commit()
    rows_affected = cursor.rowcount
    conn.close()
    return rows_affected > 0
