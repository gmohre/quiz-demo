#### Quiz Application

### Setup
- pip install -r requirements.txt
- python manage.py upgrade to run migrations
- python test-sql.py to run some API tests
- Run test suite - python test-sql.py
- python manage.py runserver to start a server on http://localhost:5000/
- API.md has API descriptions
### Workflow
- POST a Test object
- POST an Assessment object
- POST some Responses
- Client implements all test taking rules, API simply providing a store.
