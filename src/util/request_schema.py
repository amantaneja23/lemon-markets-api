import json

with open('src/util/request_schema.json', 'r') as request_schema_file:
	request_schema = json.load(request_schema_file)
