from flask import Blueprint, request
import ast
api_blueprint = Blueprint('api_bluenprint', __name__)

@api_blueprint.route('/', methods= ['POST'])
def distance():
    data = request.get_json()
    if not 'coordinate' in data:
        return 'Invalid  Request', 400
    with open('app/mkad_coordinates', 'r') as coordinates_file:
        coordinates = [ast.literal_eval(item) for item in list(coordinates_file)]
        if data.coordinate  in  coordinates:
            return {
                "Distance": "Same"
            }
            
    return 'Error', 500
