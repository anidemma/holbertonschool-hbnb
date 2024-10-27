from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        User.validate_request_data(user_data)
        user = User(**user_data)
        self.user_repo.add(user)
        return user


    def get_user(self, user_id):
        return self.user_repo.get(user_id)


    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)


    def get_all_users(self):
        return list(self.user_repo.get_all())


    def update_user(self, user_id, user_data):
        User.validate_request_data(user_data)
        obj = self.get_user(user_id)
        if obj:
            obj.update(user_data)
        return obj


    def delete_user(self, user_id):
        user = self.user_repo.get(user_id)
        if user:
            self.user_repo.delete(user_id)
            return {"message": "User deleted successfully"}


    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return list(self.amenity_repo.get_all())

    def update_amenity(self, amenity_id, amenity_data):
        Amenity.validate_request_data(amenity_data)
        obj = self.get_amenity(amenity_id)
        if obj:
            obj.update(amenity_data)
        return obj

    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if place:
            if 'title' in place_data:
                place.title = place_data['title']
            if 'description' in place_data:
                place.description = place_data['description']
            if 'price' in place_data:
                place.price = place_data['price']
            if 'latitude' in place_data:
                place.latitude = place_data['latitude']
            if 'longitude' in place_data:
                place.longitude = place_data['longitude']
            if 'owner_id' in place_data:
                place.owner_id = place_data['owner_id']
            self.place_repo.update(place, place_data)
        return place