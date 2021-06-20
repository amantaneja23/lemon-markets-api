import json

import flask
import flask_restful

from src.exception.bad_request_exception import BadRequestException
from src.service.orders_response import created_response, bad_request_response
from src.service.request_validator import validate_request

app = flask.Flask(__name__)
api = flask_restful.Api(app)

get_response = {
	'name': 'Aman Taneja',
	'id': '#Bulbasaur'
}


class Orders(flask_restful.Resource):
	@staticmethod
	def get():
		return json.dumps(get_response)

	@staticmethod
	def post():
		try:
			validate_request(flask.request)
			return created_response()
		except BadRequestException as e:
			return bad_request_response(e.validation_errors)


api.add_resource(Orders, '/orders')
