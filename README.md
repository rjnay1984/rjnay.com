# rjnay.com
My website built in wagtail cms and react.

## Get Started
1. [Activate virtual environment](https://docs.python.org/3/tutorial/venv.html)
2. Copy the env file: `cp web/settings/.env.example web/settings/.env`
3. Start docker: `docker-compose up`
4. Run database migrations: `docker-compose run web python manage.py migrate`
5. Create a superuser: `docker-compose run web python manage.py createsuperuser --username <USERNAME> --email <EMAIL>`
6. Visit `http://localhost:8000` to view wagtail site
7. To view the database, visit `http://localhost:8080`
