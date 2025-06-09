from flask import Blueprint, request, jsonify
from models.users import User # importa la clase User del modelo

userBp = Blueprint('userBp', __name__) # crea las rutas de la API

# ruta para crear un usuario
@userBp.route('/users', methods=['POST'])
def createUser():
  try:
    data = request.get_json() # obtiene los datos del usuario desde el cuerpo de la solicitud
    print(data) # imprime los datos del usuario en la consola
    User.createUser(data) # llama al método createUser de la clase User para crear un nuevo usuario
    return jsonify({"message": "User created successfully"}), 201
  except Exception as e:
    return jsonify({"error": str(e)}), 400 # maneja errores y devuelve un mensaje de error
  
# ruta para obtener todos los usuarios
@userBp.route('/getAllUser', methods=['GET'])
def getAllUsers():
  try:
    user = User.getAllUser()
    return jsonify(user), 200 # devuelve una lista de todos los usuarios
  except Exception as e:
    return jsonify({"error": str(e)}), 400

