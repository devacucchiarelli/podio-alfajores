from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alfajores.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Alfajor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.String(200))
    imagen_url = db.Column(db.String(200))
    votos = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "marca": self.marca,
            "tipo": self.tipo,
            "descripcion": self.descripcion,
            "imagen_url": self.imagen_url,
            "votos": self.votos
        }

# Crear la base de datos si no existe
with app.app_context():
    db.create_all()

# Endpoints básicos
@app.route("/alfajores", methods=["GET"])
def get_alfajores():
    alfajores = Alfajor.query.order_by(Alfajor.votos.desc()).all()
    return jsonify([a.to_dict() for a in alfajores])

@app.route("/alfajores", methods=["POST"])
def add_alfajor():
    data = request.json
    nuevo = Alfajor(
        marca=data.get("marca"),
        tipo=data.get("tipo"),
        descripcion=data.get("descripcion"),
        imagen_url=data.get("imagen_url"),
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify(nuevo.to_dict()), 201

@app.route("/alfajores/<int:id>/votar", methods=["POST"])
def votar_alfajor(id):
    alfajor = Alfajor.query.get_or_404(id)
    alfajor.votos += 1
    db.session.commit()
    return jsonify(alfajor.to_dict())

# Actualizar un alfajor existente
@app.route("/alfajores/<int:id>", methods=["PUT"])
def update_alfajor(id):
    alfajor = Alfajor.query.get_or_404(id)
    data = request.get_json()

    alfajor.marca = data.get("marca", alfajor.marca)
    alfajor.tipo = data.get("tipo", alfajor.tipo)
    alfajor.descripcion = data.get("descripcion", alfajor.descripcion)
    alfajor.imagen_url = data.get("imagen_url", alfajor.imagen_url)

    db.session.commit()
    return jsonify(alfajor.to_dict())

# Eliminar un alfajor
@app.route("/alfajores/<int:id>", methods=["DELETE"])
def delete_alfajor(id):
    alfajor = Alfajor.query.get_or_404(id)
    db.session.delete(alfajor)
    db.session.commit()
    return jsonify({"message": f"Alfajor {id} eliminado con éxito"})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
