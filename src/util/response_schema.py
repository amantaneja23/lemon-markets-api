import json

with open('src/util/response_schema.json', 'r') as response_schema_file:
	response_schema = json.load(response_schema_file)
