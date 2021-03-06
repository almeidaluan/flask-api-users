# -*- coding: utf-8 -*-

# Third
# Importamos as classes API e Resource
from flask_restful import Api, Resource
from users.resources import SignUp

# Criamos uma classe que extende de Resource
class Index(Resource):
    # Definimos a operaçao get do protocolo http
    def get(self):
        # retornamos um simples dicionario que sera automaticamente
        # retornado em json pelo flask
        return {'hello': 'world by apps'}

# Instânciamos a API do FlaskRestful


api = Api()


def configure_api(app):

    # adicionamos na rota '/' a sua classe correspondente Index
    api.add_resource(Index, '/api')
    api.add_resource(SignUp, '/users')

    # inicializamos a api com as configurações do flask vinda por parâmetro
    api.init_app(app)
