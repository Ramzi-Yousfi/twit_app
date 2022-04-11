from flask_restful import Api
from .resources import UserResource
api = Api()
api.add_resource(UserResource, '/api/users')