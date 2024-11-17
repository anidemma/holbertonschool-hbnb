import uuid
from datetime import datetime
from app.models.__init__ import BaseModel
import re
from flask_bcrypt import bcrypt


regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'


class User(BaseModel):
    def __init__(self, first_name, last_name, email, password):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = False
        self.places = []
        self._password = password

    def save(self):
        super().save()

    def update(self, data):
        super().update(data)

    def hash_password(self, password):
        #Hashes the password before storing it.
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    def verify_password(self, password):
        #Verifies if the provided password matches the hashed password.
        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def validate_request_data(data: dict):
        for key in data.keys():
            value = data[key]
            
            if key == 'first_name' or key == 'last_name':
                if not isinstance(value, str) and len(value) not in range(1, 51):
                    raise ValueError("String must be less than 50 chars and not empty.")
            
            elif key == 'email':
                if not re.match(regex, data["email"]):
                    raise ValueError("Email must follow standard email format.")
            
            elif key == 'id':
                if key not in data:
                    raise ValueError("ID is required.")
                try:
                    uuid_user = uuid.UUID(data[key], version=4)
                except ValueError:
                    raise ValueError("Invalid UUID format for ID.")
        return data