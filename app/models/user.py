import uuid
from datetime import datetime
from app.persistence.data_manager import DataManager

storage = DataManager()

class User:
    """
    Represents a user in the system.

    Attributes:
        id (str): The unique identifier of the user.
        email (str): The email address of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        password (str): The password of the user.
        created_at (datetime): The timestamp when the user was created.
        updated_at (datetime): The timestamp when the user was last updated.
    """

    def __init__(self, email, first_name, last_name, password=None):
        self.id = str(uuid.uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Saves the user to the storage.

        Raises:
            ValueError: If the email already exists.
        """
        if not self.is_email_unique():
            raise ValueError("Email already exists.")
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def delete(self):
        """
        Deletes the user from the storage.
        """
        storage.delete(self.id, 'User')

    def to_dict(self):
        """
        Converts the user object to a dictionary.

        Returns:
            dict: A dictionary representation of the user object.
        """
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def is_email_unique(self):
        """
        Checks if the email is unique among all users.

        Returns:
            bool: True if the email is unique, False otherwise.
        """
        users = User.get_all()
        for user in users:
            if user.email == self.email and user.id != self.id:
                return False
        return True

    @staticmethod
    def get(user_id):
        """
        Retrieves a user by their ID.

        Args:
            user_id (str): The ID of the user to retrieve.

        Returns:
            User: The user object if found, None otherwise.
        """
        data = storage.get(user_id, 'User')
        if data:
            user = User(
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password=data.get('password')
            )
            user.id = data['id']
            user.created_at = datetime.fromisoformat(data['created_at'])
            user.updated_at = datetime.fromisoformat(data['updated_at'])
            return user
        return None

    @staticmethod
    def get_all():
        """
        Retrieves all users.

        Returns:
            list: A list of user objects.
        """
        data = storage.get_all('User')
        users = []
        for item in data:
            user = User(
                email=item['email'],
                first_name=item['first_name'],
                last_name=item['last_name'],
                password=item.get('password')
            )
            user.id = item['id']
            user.created_at = datetime.fromisoformat(item['created_at'])
            user.updated_at = datetime.fromisoformat(item['updated_at'])
            users.append(user)
        return users
