import joblib
import pandas as pd
from flask import Flask

# Cargar el modelo
modelo = joblib.load("modelo.sav")

def titanic_sobrevivir(usuario):
    if usuario['sexo']==0:
        # Hombre
        simulacion = pd.DataFrame({
            'age': [usuario['edad']],
            'sex_female': [0],
            'sex_male': [1]
        })
    else:
        # Mujer
        simulacion = pd.DataFrame({
            'age': [usuario['edad']],
            'sex_female': [1],
            'sex_male': [0]
        })

    respuesta = modelo.predict(simulacion)[0]

    if respuesta==0:
        mensaje='No sobrevives'
    else:
        mensaje='Sobrevives!!!'

    return mensaje

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hola mundo!!!!</h1>"


@app.route("/<edad>/<sexo>")
def api_function(edad, sexo):
    usuario = {
    'edad': edad,
    'sexo': sexo
    }

    respuesta = titanic_sobrevivir(usuario)

    return {
        'datos_usuario' : usuario,
        'resultado': respuesta
    }

app.run()