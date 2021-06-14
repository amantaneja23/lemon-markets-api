import datetime
import json
from uuid import UUID as valid_uuid

from src.api.rest_api import app

client = app.test_client()

request_schema = {
	'isin': 'amantaneja23',
	'limit_price': 23,
	'side': 'sell',
	'valid_until': 1623530303511,
	'quantity': 69
}


def test_valid_post_orders():
	return_code, response = post_orders_request(request_schema)
	print(str(response))
	assert return_code == 201
	assert response is not None
	assert response['status'] == 'ORDER_CREATED'
	assert valid_uuid(response['order_id'])
	assert valid_datetime(response['created_at'])


def test_invalid_isin_not_string():
	request_schema['isin'] = 'amantaneja'
	return_code, response = post_orders_request(request_schema)
	print(str(response))
	assert return_code == 400
	assert 'isin' in response['validation_errors']


def test_invalid_isin_short_string():
	request_schema['isin'] = 'amantaneja'
	return_code, response = post_orders_request(request_schema)
	print(str(response))
	assert return_code == 400
	assert 'isin' in response['validation_errors']


def test_invalid_isin_long_string():
	request_schema['isin'] = 'amantaneja2303'
	return_code, response = post_orders_request(request_schema)
	print(str(response))
	assert return_code == 400
	assert 'isin' in response['validation_errors']


def post_orders_request(request):
	response = client.post('orders', data=json.dumps(request), headers={'Content-Type': 'application/json'})
	return response.status_code, response.json


def valid_datetime(timestamp):
	assert datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
	return True
