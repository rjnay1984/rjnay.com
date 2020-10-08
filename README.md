# rjnay.com
My website built in wagtail cms and react.

## Get Started
1. [Activate virtual environment](https://docs.python.org/3/tutorial/venv.html)
2. Start docker: `docker-compose up`
3. Run database migrations: `docker-compose run backend python manage.py migrate`
4. Initialize the database: `docker-compose run backend python manage.py loaddata data.json`
5. Visit `http://localhost:8000` to view wagtail site
6. To view the database, visit `http://localhost:8080`
