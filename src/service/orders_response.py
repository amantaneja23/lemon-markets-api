import json
from datetime import datetime
from http import HTTPStatus
from uuid import uuid4

import flask

from src.util.response_schema import response_schema

order_id = 'order_id'
created_at = 'created_at'
application_json = 'application/json'


def created_response():
	response_schema[order_id] = str(uuid4())
	response_schema[created_at] = str(datetime.now())
	return flask.Response(json.dumps(response_schema), status=HTTPStatus.CREATED, mimetype=application_json)


def bad_request_response(errors):
	response = dict()
	response['validation_errors'] = errors
	return flask.Response(json.dumps(response), status=HTTPStatus.BAD_REQUEST, mimetype=application_json)
