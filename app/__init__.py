from flask import Blueprint
from flask_restplus import Api

from app.project.auth.auth_controller import api as auth_ns
from app.project.user.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='LMS FLASK RESTPLUS API WITH JWT',
          version='1.0',
          description='a LMS web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
