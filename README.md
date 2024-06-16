# HOLBERTONSCHOOL-HBNB


## DESCRIPTION
This is the repository for our project at [Holberton School](https://www.holbertonschool.fr/).
The project involves creating `HBNB`, a platform for managing vacation rentals, including a backend API for handling bookings, users, and listings. This project was completed as part of the curriculum over a period of two weeks by a team of three people.


## TABLE OF CONTENTS
- [OVERVIEW](#overview)
- [FEATURES](#features)
- [API ENDPOINTS](#api-endpoints)
  - [User Management](#user-management)
  - [Listing Management](#listing-management)
  - [Booking Management](#booking-management)
- [INSTALLATION AND RUNNING](#installation-and-running)
- [EXAMPLES](#api-request-examples)
  - [User Management](#api-request-examples)
  - [Listing Management](#api-request-examples)
  - [Booking Management](#api-request-examples)
- [PROJECT FILES DESCRIPTION](#project-files-description)
- [AUTHORS](#authors)
- [LICENSE](#license)


## OVERVIEW
`HBNB` is a custom platform designed for managing vacation rentals. It features a backend API developed in Python with Flask, which supports CRUD operations for users, listings, and bookings. The project includes robust error handling and efficient data management.


## FEATURES
`HBNB` provides:
- **User Management**: Registration, login, and profile management.
- **Listing Management**: Creation, updating, deletion, and viewing of rental listings.
- **Booking Management**: Management of bookings including creation, cancellation, and viewing of reservations.


## INSTALLATION AND RUNNING

1. Clone the repository:

    ```sh
    git clone https://github.com/jmsjrz/holbertonschool-hbnb.git
    ```

2. Navigate to the project directory:

    ```sh
    cd holbertonschool-hbnb
    ```

3. Build the Docker image and start the containers with Docker Compose:

    ```sh
    docker-compose up --build
    ```

4. Once the containers are running, you can access the application at [http://0.0.0.0:5000](http://0.0.0.0:5000) in your web browser.


## CONFIGURATION AND DEPENDENCIES

| Software/Framework     | Version       | Description                                     |
|------------------------|---------------|-------------------------------------------------|
| Flask                  | 2.0.2         | Micro web framework for Python                  |
| Flask-RESTful          | -             | Extension for building REST APIs with Flask     |
| Flask-SQLAlchemy       | -             | Flask extension for SQLAlchemy integration     |
| pytest                 | 6.2.4         | Framework for running Python tests             |
| Flask-RESTx            | 0.5.1         | Extension for adding swagger to Flask APIs     |
| Gunicorn               | 20.1.0        | Python WSGI HTTP Server for Unix               |
| Werkzeug               | 2.0.2         | WSGI utility library for Python                |
| Docker                 | 26.1.3        | Containerization platform                      |
| Ubuntu                 | 22.04 LTS     | Linux distribution                             |


## API ENDPOINTS

### User Management
- **Register**: `POST /api/v1/users`
- **Login**: `POST /api/v1/auth/login`
- **Profile**: `GET /api/v1/users/<user_id>`

### Listing Management
- **Create Listing**: `POST /api/v1/listings`
- **Update Listing**: `PUT /api/v1/listings/<listing_id>`
- **Delete Listing**: `DELETE /api/v1/listings/<listing_id>`
- **View Listings**: `GET /api/v1/listings`

### Booking Management
- **Create Booking**: `POST /api/v1/bookings`
- **Cancel Booking**: `DELETE /api/v1/bookings/<booking_id>`
- **View Bookings**: `GET /api/v1/bookings`


## API REQUEST EXAMPLES

| Operation                  | Endpoint                                     | Description                            | Example CURL Command                                                                                     |
|----------------------------|----------------------------------------------|----------------------------------------|----------------------------------------------------------------------------------------------------------|
| **User Management**        |                                              |                                        |                                                                                                          |
| Create a user              | POST /api/v1/users/                          | Create a new user                      | `curl -X POST http://0.0.0.0:5000/api/v1/users/ -H "Content-Type: application/json" -d '{"email": "test@example.com","first_name": "John","last_name": "Doe","password": "password123"}'` |
| Get all users              | GET /api/v1/users/                           | Retrieve all users                     | `curl -X GET http://0.0.0.0:5000/api/v1/users/ -H "accept: application/json"`                             |
| Get a user by ID           | GET /api/v1/users/<user_id>                  | Retrieve a specific user by ID          | `curl -X GET http://0.0.0.0:5000/api/v1/users/<user_id> -H "accept: application/json"`                    |
| Update a user              | PUT /api/v1/users/<user_id>                  | Update a user's information            | `curl -X PUT http://0.0.0.0:5000/api/v1/users/<user_id> -H "Content-Type: application/json" -d '{"first_name": "John","last_name": "DoeUpdated","password": "newpassword123"}'` |
| Delete a user              | DELETE /api/v1/users/<user_id>               | Delete a user                          | `curl -X DELETE http://0.0.0.0:5000/api/v1/users/<user_id>`                                                |
| **Listing Management**     |                                              |                                        |                                                                                                          |
| Create a place             | POST /api/v1/places/                         | Create a new place                     | `curl -X POST http://0.0.0.0:5000/api/v1/places/ -H "Content-Type: application/json" -d '{"name": "Charming Cottage","description": "A lovely cottage in the countryside","address": "123 Country Lane","city_id": "<city_id>","latitude": 45.123,"longitude": -123.456,"host_id": "<user_id>","number_of_rooms": 3,"number_of_bathrooms": 2,"price_per_night": 120,"max_guests": 5,"amenity_ids": ["<amenity_id1>", "<amenity_id2>"]}'` |
| Get all places             | GET /api/v1/places/                          | Retrieve all places                    | `curl -X GET http://0.0.0.0:5000/api/v1/places/ -H "accept: application/json"`                            |
| Get a place by ID          | GET /api/v1/places/<place_id>                | Retrieve a specific place by ID         | `curl -X GET http://0.0.0.0:5000/api/v1/places/<place_id> -H "accept: application/json"`                   |
| Update a place             | PUT /api/v1/places/<place_id>                | Update a place's information           | `curl -X PUT http://0.0.0.0:5000/api/v1/places/<place_id> -H "Content-Type: application/json" -d '{"name": "Charming Cottage Updated","description": "A newly renovated lovely cottage in the countryside"}'` |
| Delete a place             | DELETE /api/v1/places/<place_id>             | Delete a place                         | `curl -X DELETE http://0.0.0.0:5000/api/v1/places/<place_id>`                                              |
| **Review Management**      |                                              |                                        |                                                                                                          |
| Create a review for a place| POST /api/v1/places/<place_id>/reviews       | Add a review for a specific place      | `curl -X POST http://0.0.0.0:5000/api/v1/places/<place_id>/reviews -H "Content-Type: application/json" -d '{"user_id": "<user_id>","rating": 5,"comment": "Amazing place! Highly recommend."}'` |
| Get all reviews for a place| GET /api/v1/places/<place_id>/reviews        | Retrieve all reviews for a specific place | `curl -X GET http://0.0.0.0:5000/api/v1/places/<place_id>/reviews -H "accept: application/json"`           |
| Get all reviews by a user  | GET /api/v1/users/<user_id>/reviews          | Retrieve all reviews written by a specific user | `curl -X GET http://0.0.0.0:5000/api/v1/users/<user_id>/reviews -H "accept: application/json"`             |
| Get a review by ID         | GET /api/v1/reviews/<review_id>              | Retrieve a specific review by ID       | `curl -X GET http://0.0.0.0:5000/api/v1/reviews/<review_id> -H "accept: application/json"`                  |
| Update a review            | PUT /api/v1/reviews/<review_id>              | Update a review                        | `curl -X PUT http://0.0.0.0:5000/api/v1/reviews/<review_id> -H "Content-Type: application/json" -d '{"rating": 4,"comment": "Great place, but a bit noisy."}'` |
| Delete a review            | DELETE /api/v1/reviews/<review_id>           | Delete a review                        | `curl -X DELETE http://0.0.0.0:5000/api/v1/reviews/<review_id>`                                            |
| **Amenity Management**     |                                              |                                        |                                                                                                          |
| Create an amenity          | POST /api/v1/amenities/                      | Create a new amenity                   | `curl -X POST http://0.0.0.0:5000/api/v1/amenities/ -H "Content-Type: application/json" -d '{"name": "WiFi"}'` |
| Get all amenities          | GET /api/v1/amenities/                       | Retrieve all amenities                 | `curl -X GET http://0.0.0.0:5000/api/v1/amenities/ -H "accept: application/json"`                         |
| Get an amenity by ID       | GET /api/v1/amenities/<amenity_id>           | Retrieve a specific amenity by ID       | `curl -X GET http://0.0.0.0:5000/api/v1/amenities/<amenity_id> -H "accept: application/json"`              |
| Update an amenity          | PUT /api/v1/amenities/<amenity_id>           | Update an amenity                      | `curl -X PUT http://0.0.0.0:5000/api/v1/amenities/<amenity_id> -H "Content-Type: application/json" -d '{"name": "High-Speed WiFi"}'` |
| Delete an amenity          | DELETE /api/v1/amenities/<amenity_id>        | Delete an amenity                      | `curl -X DELETE http://0.0.0.0:5000/api/v1/amenities/<amenity_id>`                                        |
| **City Management**        |                                              |                                        |                                                                                                          |
| Create a city              | POST /api/v1/cities/                         | Create a new city                      | `curl -X POST http://0.0.0.0:5000/api/v1/cities/ -H "Content-Type: application/json" -d '{"name": "New City","country_code": "<country_code>"}'` |
| Get all cities             | GET /api/v1/cities/                          | Retrieve all cities                    | `curl -X GET http://0.0.0.0:5000/api/v1/cities/ -H "accept: application/json"`                            |
| Get a city by ID           | GET /api/v1/cities/<city_id>                 | Retrieve a specific city by ID         | `curl -X GET http://0.0.0.0:5000/api/v1/cities/<city_id> -H "accept: application/json"`                    |
| Update a city              | PUT /api/v1/cities/<city_id>                 | Update a city                          | `curl -X PUT http://0.0.0.0:5000/api/v1/cities/<city_id> -H "Content-Type: application/json" -d '{"name": "Updated City Name"}'` |
| Delete a city              | DELETE /api/v1/cities/<city_id>              | Delete a city                          | `curl -X DELETE http://0.0.0.0:5000/api/v1/cities/<city_id>`                                               |
| **Country Management**     |                                              |                                        |                                                                                                          |
| Get all countries          | GET /api/v1/countries/                       | Retrieve all countries                 | `curl -X GET http://0.0.0.0:5000/api/v1/countries/ -H "accept: application/json"`                         |
| Get a country by code      | GET /api/v1/countries/<country_code>         | Retrieve a specific
| Get all cities of a country| GET /api/v1/countries/<country_code>/cities  | Retrieve all cities of a specific country | `curl -X GET http://0.0.0.0:5000/api/v1/countries/<country_code>/cities -H "accept: application/json"`    |


## RUN THE TESTS

To run the unit tests using Docker Compose:

```bash
docker-compose run --rm web sh -c "python3 -m unittest discover -s tests -v"
```
To run the unit tests without Docker, ensure you have Python 3.10 installed and follow these steps:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the tests:
   ```bash
   python3 -m unittest discover -s tests -v
   ```

## DIAGRAM CLASS UML OVERVIEW

![Diagram Class UML](https://i.imgur.com/zK4tojr.png)


## PROJECT FILES DESCRIPTION

The project files are organized as follows:

- **`app/`**: Contains the main application files.
  - `api/`: API endpoints for user, place, review, amenity, city, and country management.
  - `models/`: Defines models for users, places, reviews, amenities, cities, and countries.
  - `persistence/`: Handles database interactions and queries.
- **`tests/`**: Unit tests for API endpoints and models.
- **.gitignore**: Specifies files and directories to be ignored by Git, such as temporary files and dependencies.
- **docker-compose.yml**: Docker Compose configuration file for container orchestration.
- **Dockerfile**: Dockerfile for building the Docker image of the application.
- **requirements.txt**: Lists all Python dependencies required by the application.
- **README.md**: Project documentation file containing an overview, API endpoints, installation instructions, and examples.
- **LICENSE**: Licensing information for the project.


## AUTHORS
• **Guillaume SELLIER**
[@Guillom8769](https://github.com/Guillom8769)

• **James JAROSZ**
[@jmsjrz](https://github.com/jmsjrz)

• **Khadija ABDELMALEK**
[@khadmalek](https://github.com/khadmalek)

## LICENSE
Copyright © <26/04/2024> • **James JAROSZ** & **Guillaume SELLIER** & **Khadija ABDELMALEK**
For more informations, consult the `LICENSE` file.
