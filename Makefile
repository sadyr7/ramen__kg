migrate:
	python manage.py makemigrations
	python manage.py migrate

runserver:
    python3 manage.py bot
    python3 manage.py runserver