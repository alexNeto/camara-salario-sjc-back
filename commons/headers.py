from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Headers(Resource):
    @classmethod
    def get(self, header_type):
        if header_type == 'salarystuff':
            return salary_stuff()
        elif header_type == 'role':
            return role()
        elif header_type == 'cityname':
            return city_name()

def salary_stuff():
    linhas = ["Salário Base",
              "Plano de Carreira",
              "Gratificações",
              "Benefícios",
              "Abono",
              "Adiantamento Salarial",
              "Férias",
              "Décimo Terceiro",
              "Abatimento",
              "Descontos",
              "Salário Bruto",
              "Salário Líquido"]
    return {"salary_stuff": linhas}

def role():
    titulo = ["Nome do Servidor",
              "Cargo",
              "Salário Base",
              "Plano de Carreira",
              "Gratificações",
              "Benefícios",
              "Abono",
              "Adiantamento Salarial",
              "Férias",
              "Décimo Terceiro",
              "Abatimento",
              "Descontos",
              "Salário Bruto",
              "Salário Líquido"]
    return {"role": titulo}

def city_name():
    return {"city_name": "São José dos Campos"}
