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

# ruta para obtener un usuario por ID
@userBp.route('/getUserid/<int:userID>', methods=['GET'])
def getUserById(userID):
  try:
      user = User.getUserById(userID) # obtiene un usuario por ID
      if user:
        return jsonify(user), 200 # devuelve el usuario encontrado
      return jsonify({"error": "User not found"}), 404 # maneja el caso en que no se encuentra el usuario
  except Exception as e:
      return jsonify({"error": str(e)}), 400

# ruta para eliminar usuario un usuario por ID
@userBp.route('/deleteUser/<int:userID>', methods=['DELETE'])
def deleteUser(userID):
  try:
    user = User.getUserById(userID) # busca el usuario por ID
    if user:
      User.deleteUserById(userID) # llama al método deleteUserById de la clase User
      return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"error": "User not found"}), 404 # maneja el caso en que no se encuentra el usuario
  except Exception as e:
    return jsonify({"error": str(e)}), 400
  
# ruta para actualizar un usuario por ID
@userBp.route('/updateUser/<int:userID>', methods=['PUT'])
def updateUser(userID):
  try:
    data = request.get_json() # obtiene los datos del usuario desde el cuerpo de la solicitud
    update = User.updateUser(userID, data)
    if update:
      return jsonify({"message": "User updated successfully"}), 200
    return jsonify({"error": "User not found"}), 404 # maneja el caso en que no se encuentra el usuario
  except Exception as e:
    return jsonify({"error": str(e)}), 400
