from datetime import datetime
import uuid
from app.persistence.data_manager import DataManager

storage = DataManager()

class Review:
    """
    Represents a review for a place.

    Attributes:
        id (str): The unique identifier of the review.
        user_id (str): The user ID associated with the review.
        place_id (str): The place ID associated with the review.
        rating (int): The rating given in the review.
        comment (str): The comment provided in the review.
        created_at (datetime): The timestamp when the review was created.
        updated_at (datetime): The timestamp when the review was last updated.
    """

    def __init__(self, user_id, place_id, rating, comment):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        Saves the review to the storage and updates the `updated_at` timestamp.
        """
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def delete(self):
        """
        Deletes the review from the storage.
        """
        storage.delete(self.id, 'Review')

    def to_dict(self):
        """
        Converts the review object to a dictionary.

        Returns:
            dict: A dictionary representation of the review object.
        """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': self.rating,
            'comment': self.comment,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @staticmethod
    def get(review_id):
        """
        Retrieves a review by its ID from the storage.

        Args:
            review_id (str): The ID of the review to retrieve.

        Returns:
            Review: The review object if found, None otherwise.
        """
        data = storage.get(review_id, 'Review')
        if data:
            review = Review(
                user_id=data['user_id'],
                place_id=data['place_id'],
                rating=data['rating'],
                comment=data['comment']
            )
            review.id = data['id']
            review.created_at = datetime.fromisoformat(data['created_at'])
            review.updated_at = datetime.fromisoformat(data['updated_at'])
            return review
        return None

    @staticmethod
    def get_all():
        """
        Retrieves all reviews from the storage.

        Returns:
            list: A list of review objects.
        """
        data = storage.get_all('Review')
        reviews = []
        for item in data:
            review = Review(
                user_id=item['user_id'],
                place_id=item['place_id'],
                rating=item['rating'],
                comment=item['comment']
            )
            review.id = item['id']
            review.created_at = datetime.fromisoformat(item['created_at'])
            review.updated_at = datetime.fromisoformat(item['updated_at'])
            reviews.append(review)
        return reviews
