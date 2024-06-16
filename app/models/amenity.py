from datetime import datetime
import uuid
from app.persistence.data_manager import DataManager

storage = DataManager()

class Amenity:
    """
    Represents an amenity in a property rental system.

    Attributes:
        id (str): The unique identifier of the amenity.
        name (str): The name of the amenity.
        created_at (datetime): The date and time when the amenity was created.
        updated_at (datetime): The date and time when the amenity was last updated.
    """

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Saves the current state of the amenity to the storage system.
        """
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def delete(self):
        """
        Deletes the amenity from the storage system.
        """
        storage.delete(self.id, 'Amenity')

    def to_dict(self):
        """
        Converts the amenity object to a dictionary representation.

        Returns:
            dict: A dictionary containing the amenity's attributes.
        """
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @staticmethod
    def get(amenity_id):
        """
        Retrieves an amenity object from the storage system based on its ID.

        Args:
            amenity_id (str): The ID of the amenity to retrieve.

        Returns:
            Amenity or None: The retrieved amenity object, or None if not found.
        """
        data = storage.get(amenity_id, 'Amenity')
        if data:
            amenity = Amenity(name=data['name'])
            amenity.id = data['id']
            amenity.created_at = datetime.fromisoformat(data['created_at'])
            amenity.updated_at = datetime.fromisoformat(data['updated_at'])
            return amenity
        return None

    @staticmethod
    def get_all():
        """
        Retrieves all amenity objects from the storage system.

        Returns:
            list: A list of Amenity objects.
        """
        data = storage.get_all('Amenity')
        amenities = []
        for item in data:
            amenity = Amenity(name=item['name'])
            amenity.id = item['id']
            amenity.created_at = datetime.fromisoformat(item['created_at'])
            amenity.updated_at = datetime.fromisoformat(item['updated_at'])
            amenities.append(amenity)
        return amenities
