from flask import Blueprint, make_response, Flask, request
from json_response import buildJsonResponse
from db_model import *
from json import loads
from datetime import datetime

read_queries = Blueprint('read_queries', __name__)

# {name: "", description:"", location: [latitude, longitude] }
def addTagProcessor(tag):
    tag['datetime'] = datetime.now() 
    addTag(tag)
    return {'errno':0}

QUERY_MAP = {'tags': {'add':{'processor': addTagProcessor, 'schema':''}}}

@read_queries.route('/tags/<method>', methods=['POST'])
def processTagsQueries(method):
    # Check query
    if method not in QUERY_MAP['tags'].keys():
        return buildJsonResponse({'errno':1}) 
    # Parse json
    data = loads(request.get_data())
    if type(data) is not dict:
        return buildJsonResponse({'errno':1})
    # Check schema
    # Call processor
    processor = QUERY_MAP['tags'][method]['processor']
    result = processor(data)
    # Return json
    return buildJsonResponse(result)

