setup:
	./manage.py migrate
	./manage.py loaddata sites/fixtures/initial.json
run:
	./manage.py runserver 0:8000
migrate:
	./manage.py migrate
collectstatic:
	./manage.py collectstatic --noinput
createsu:
	./manage.py createsuperuser
