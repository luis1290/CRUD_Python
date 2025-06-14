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

  # obtener un usuario por su ID
  @classmethod
  def getUserById(cls, userID):
    try:
      return cls.user.get(userID) # devuelve el usuario con el ID especificado o None si no existe
    except Exception as e:
      return print(f"Error getting user by ID: {e}")
  
  # eliminar un usuario por su ID
  @classmethod
  def deleteUserById(cls, userID):
    try:
      if userID in cls.user:
        cls.user.pop(userID)# elimina el usuario con el ID especificado
    except Exception as e:
      print(f"Error deleting user by ID: {e}")
  
  # actualizar un usuario por su ID
  @classmethod
  def updateUser(cls, userID, userData):
    try:
      if userID in cls.user:
        cls.user[userID].update(userData)
        return cls.user[userID]
      return print("User not found")
    except Exception as e:
      print(f"Error updating user: {e}")

  
    

  
  