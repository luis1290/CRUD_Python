class User: # defininendo una clase User
  
  user = {}

  # agregar un usuario al diccionario de usuarios
  @classmethod
  def createUser(cls, userData):
    try:
      userID = userData["id"]
      cls.user[userID] = userData
    except Exception as e:
      print(f"Error creating user: {e}")

  # obtener un usuario del diccionario de usuarios
  @classmethod
  def getAllUser(cls):
    try:
      return list(cls.user.values()) # devuelve una lista de todos los usuarios
    except Exception as e:
      print(f"Error getting all users: {e}")
  
  