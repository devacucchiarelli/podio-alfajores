from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Configuración de la DB
db_config = {
    'host': 'db',
    'user': 'administrador',
    'password': 'Hola123456789',
    'database': 'alfajores_db'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

#  Listar todos los alfajores ordenados por votos
@app.route('/alfajores', methods=['GET'])
def listar_alfajores():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM alfajores ORDER BY votos DESC")
    alfajores = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(alfajores)

#  Agregar alfajor (público)
@app.route('/alfajores', methods=['POST'])
def agregar_alfajor():
    data = request.json or {}
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO alfajores (nombre, tipo, descripcion, imagen, votos)
        VALUES (%s, %s, %s, %s, 0)
        """,
        (
            data.get('nombre'),
            data.get('tipo'),
            data.get('descripcion'),
            data.get('imagen')
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Alfajor agregado con éxito"}), 201

#  Modificar un alfajor (solo admin)
@app.route('/alfajores/<int:id>', methods=['PUT'])
def modificar_alfajor(id):
    if request.headers.get("X-Admin") != "true":
        return jsonify({"error": "Solo el administrador puede modificar"}), 403

    data = request.json or {}
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE alfajores
        SET nombre = %s, tipo = %s, descripcion = %s, imagen = %s
        WHERE id = %s
        """,
        (
            data.get('nombre'),
            data.get('tipo'),
            data.get('descripcion'),
            data.get('imagen'),
            id
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Alfajor modificado con éxito"})

    # actualizar campos permitidos
    cursor.execute("""
        UPDATE alfajores
        SET marca = %s, tipo = %s, descripcion = %s, imagen_url = %s
        WHERE id = %s
    """, (
        data.get("marca"),
        data.get("tipo"),
        data.get("descripcion"),
        data.get("imagen_url"),
        id
    ))
    db.commit()

    return jsonify({"mensaje": "Alfajor modificado correctamente"})


#  Borrar alfajor (solo admin)
@app.route('/alfajores/<int:id>', methods=['DELETE'])
def borrar_alfajor(id):
    if request.headers.get("X-Admin") != "true":
        return jsonify({"error": "Solo el administrador puede borrar"}), 403

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alfajores WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Alfajor eliminado con éxito"})

#  Votar por un alfajor (público)
@app.route('/alfajores/<int:id>/votar', methods=['POST'])
def votar_alfajor(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE alfajores SET votos = votos + 1 WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Voto registrado"})
