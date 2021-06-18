import datetime
import json
from uuid import UUID as valid_uuid

from src.api.rest_api import app

client = app.test_client()

request_schema = {
	'isin': 'amantaneja23',
	'limit_price': 23.03,
	'side': 'sell',
	'valid_until': 1623530303511,
	'quantity': 69
}
# copy() because it is a flat dict, no need for deepcopy()


def test_valid_post_orders():
	request = request_schema.copy()
	return_code, response = post_orders_request(request)
	print(str(response))
	assert return_code == 201
	assert response is not None
	assert response['status'] == 'ORDER_CREATED'
	assert valid_uuid(response['order_id'])
	assert valid_datetime(response['created_at'])


def test_invalid_isin_not_string():
	request = request_schema.copy()
	request['isin'] = False
	return_code, response = post_orders_request(request)
	print(str(response))
	assert return_code == 400
	assert 'isin' in response['validation_errors']


def test_invalid_isin_short_string():
	request = request_schema.copy()
	request['isin'] = 'amantaneja'
	return_code, response = post_orders_request(request)
	print(str(response))
	assert return_code == 400
	assert 'isin' in response['validation_errors']


def test_invalid_isin_long_string():
	request = request_schema.copy()
	request['isin'] = 'amantaneja2303'
	return_code, response = post_orders_request(request)
	print(str(response))
	assert return_code == 400
	assert 'isin' in response['validation_errors']


def test_invalid_limit_price_not_float():
	request = request_schema.copy()
	request['limit_price'] = "float"
	return_code, response = post_orders_request(request)
	print(str(response))
	assert return_code == 400
	assert 'limit_price' in response['validation_errors']


def test_invalid_limit_price_negative_float():
	request = request_schema.copy()
	request['limit_price'] = -23.03
	return_code, response = post_orders_request(request)
	print(str(response))
	assert return_code == 400
	assert 'limit_price' in response['validation_errors']


def test_invalid_side_not_string():
	request = request_schema.copy()
	request['side'] = 0
	return_code, response = post_orders_request(request)
	print(str(response))
	assert return_code == 400
	assert 'side' in response['validation_errors']


def test_invalid_side_not_valid():
	request = request_schema.copy()
	request['side'] = "gamble"
	return_code, response = post_orders_request(request)
	print(str(response))
	assert return_code == 400
	assert 'side' in response['validation_errors']


def test_invalid_valid_until_not_integer():
	request = request_schema.copy()
	request['valid_until'] = "integer"
	return_code, response = post_orders_request(request)
	print(str(response))
	assert return_code == 400
	assert 'valid_until' in response['validation_errors']


def test_invalid_valid_until_negative_integer():
	request = request_schema.copy()
	request['valid_until'] = -420
	return_code, response = post_orders_request(request)
	print(str(response))
	assert return_code == 400
	assert 'valid_until' in response['validation_errors']


def test_invalid_quantity_not_integer():
	request = request_schema.copy()
	request['valid_until'] = "long"
	return_code, response = post_orders_request(request)
	print(str(response))
	assert return_code == 400
	assert 'valid_until' in response['validation_errors']


def test_invalid_quantity_negative_integer():
	request = request_schema.copy()
	request['quantity'] = -69
	return_code, response = post_orders_request(request)
	print(str(response))
	assert return_code == 400
	assert 'quantity' in response['validation_errors']


def post_orders_request(request):
	response = client.post('orders', data=json.dumps(request), headers={'Content-Type': 'application/json'})
	return response.status_code, response.json


def valid_datetime(timestamp):
	assert datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
	return True
