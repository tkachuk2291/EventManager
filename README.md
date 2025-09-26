```markdown
# EventManager
 ```
## Installation
 ```
1. **Clone the repository:**
   ```
   git clone https://github.com/tkachuk2291/EventManager.git  
```bash
cd EventManager(if still not activate)
```

2. **Create and activate a virtual environment:**
   ```
   python3 -m venv venv  
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
   
   
3.1 Database Setup 

```
1. Make sure you have PostgreSQL installed on your computer.
2. open terminal and create new db for command
````
createdb event_management-db
 
4. **Configure environment variables:**

   Create a `.env` file in the project root with the following variables (example):
   
env_example or see file [.env-example](.env-example)
```
Django
----
SECRET_KEY=secret_key  
DEBUG=True  
----
Database
----
NAME=event_management-db
USER=user_db 
HOST=localhost  
PORT=5432**  
---
```

5. **Apply migrations:**

python manage.py migrate
```

6. **Run the development server:**
   ```
   python manage.py runserver
   ```

7. **API documentation (Swagger UI):**  
   [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)

---

## API Endpoints
```
### User Endpoints

- `POST /users/register/` — Register a new user.
- `GET /users/` — List all users.
- `POST /users/` — Create a new user.
- `GET /users/<int:pk>/` — Retrieve a user by ID.
- `PUT /users/<int:pk>/` — Update a user by ID.
- `DELETE /users/<int:pk>/` — Delete a user by ID.
- `POST /users/login/` — Obtain JWT access and refresh tokens.
- `POST /users/token/refresh/` — Refresh JWT access token.

### Event Endpoints

- `GET /events/` — List all events.
- `POST /events/` — Create a new event.
- `GET /events/<int:id>/` — Retrieve an event by ID.
- `PUT /events/<int:id>/` — Update an event by ID.
- `DELETE /events/<int:id>/` — Delete an event by ID.
- `POST /events/register/<int:id>/` — Register a manager for an event by ID.


###  Filtering & Search
   title , description , date ,location - fot this field can be filtering or search

Example:  
http://127.0.0.1:8000/events/?title=Test    
http://127.0.0.1:8000/events/?description=how  
http://127.0.0.1:8000/events/?description=204-05-09  
http://127.0.0.1:8000/events/?location=Lviv  




       