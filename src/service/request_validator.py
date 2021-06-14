from cerberus import Validator

from src.exception.bad_request_exception import BadRequestException
from src.util.request_schema import request_schema

validator = Validator(request_schema)


def validate_request(raw_request):
	if raw_request.is_json:
		request = raw_request.get_json()
		validation = validator.validate(request)
		print('request: ' + str(request))
		print('validation: ' + str(validation))
		if not validation:
			print(validator.errors)
			raise BadRequestException(validator.errors)
	else:
		raise Exception('request-not-valid-json')
