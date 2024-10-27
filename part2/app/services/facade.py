from app.persistence.repository import InMemoryRepository
from app.models.user import User


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