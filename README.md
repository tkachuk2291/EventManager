# EventManager

Event management REST API built with Django and Django REST Framework. JWT authentication, PostgreSQL, OpenAPI docs (Swagger UI / ReDoc).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tkachuk2291/EventManager.git
   cd EventManager
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a PostgreSQL database (PostgreSQL must be installed):

   ```bash
   createdb event_management-db
   ```

5. Create a `.env` file in the project root (see [.env-example](.env-example)):

   ```
   SECRET_KEY=secret_key
   DEBUG=True

   NAME=event_management-db
   USER=user_db
   HOST=localhost
   PORT=5432
   ```

6. Apply migrations and run the server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## API documentation

- Swagger UI: http://127.0.0.1:8000/api/schema/swagger-ui/
- ReDoc: http://127.0.0.1:8000/api/schema/redoc/

## API endpoints

### Users

- `POST /users/register/` — register a new user
- `GET /users/` — list users
- `POST /users/` — create a user
- `GET /users/<id>/` — get a user
- `PUT /users/<id>/` — update a user
- `DELETE /users/<id>/` — delete a user
- `POST /users/login/` — obtain JWT access and refresh tokens
- `POST /users/token/refresh/` — refresh the access token

### Events

- `GET /events/` — list events
- `POST /events/` — create an event
- `GET /events/<id>/` — get an event
- `PUT /events/<id>/` — update an event
- `DELETE /events/<id>/` — delete an event
- `POST /events/register/<id>/` — register a manager for an event

### Filtering

`GET /events/` accepts the query parameters `title`, `description`, `date` and `location` (case-insensitive partial match):

```
/events/?title=Test
/events/?location=Lviv
/events/?date=2024-05-09
```
