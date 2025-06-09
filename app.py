from flask import Flask # importa Flask 


from controllers.userContreller import userBp # importa el blueprint de usuarios

app = Flask(__name__) # crea una instancia de la aplicación Flask
app.register_blueprint(userBp) # registra el blueprint de usuarios en la aplicación

if __name__ == '__main__': # verifica si este archivo es el principal
    app.run(debug=True) # ejecuta la aplicación en modo de depuración