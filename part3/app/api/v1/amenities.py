from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

@api.route('/')
class AmenityList(Resource):
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new amenity"""
        amenity_data = api.payload
        if not amenity_data:
            return {'message': 'Invalid input data'}, 400
        new_amenity = facade.create_amenity(amenity_data)
        return {
            'id': new_amenity.id,
            'name': new_amenity.name
        }, 201

    @api.response(200, 'List of amenities retrieved successfully')
    def get(self):
        """Retrieve a list of all amenities"""
        amenities_list = []
        for amenity in facade.get_all_amenities():
            amenities_list.append(
                {
                    'id': amenity.id,
                    'name': amenity.name
                }
            )
        return amenities_list

@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """Get amenity details by ID"""
        amenities_data = facade.get_amenity(amenity_id)
        
        if not amenities_data:
            return  {'message': 'Amenity not found'}, 404
        return {
            'id': amenities_data.id,
            'name': amenities_data.name
        }, 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """Update an amenity's information"""
        amenity_data = api.payload
        
        if not amenity_data:
             return {'message': 'Invalid input data'}, 400
         
        updated_amenities = facade.update_amenity(amenity_id, amenity_data)
        if not updated_amenities:
            return {'message': 'Amenity not found'}, 404
        return {
            'id': updated_amenities.id,
            'name': updated_amenities.name
        }