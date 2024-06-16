from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    """
    Interface for a persistence manager that handles saving, retrieving, updating, and deleting entities.
    """

    @abstractmethod
    def save(self, entity):
        """
        Save the given entity.

        Args:
            entity: The entity to be saved.
        """
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """
        Retrieve an entity by its ID and type.

        Args:
            entity_id: The ID of the entity.
            entity_type: The type of the entity.

        Returns:
            The retrieved entity.
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Update the given entity.

        Args:
            entity: The entity to be updated.
        """
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """
        Delete an entity by its ID and type.

        Args:
            entity_id: The ID of the entity.
            entity_type: The type of the entity.
        """
        pass

    @abstractmethod
    def get_all(self, entity_type):
        """
        Retrieve all entities of the given type.

        Args:
            entity_type: The type of the entities.

        Returns:
            A list of all entities of the given type.
        """
        pass
