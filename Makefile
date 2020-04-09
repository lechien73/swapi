
install:
	pip3 install -r requirements.txt

build:
	python3 manage.py migrate
	python3 manage.py createsuperuser

load_data:
	python3 manage.py loaddata planets.json
	python3 manage.py loaddata people.json
	python3 manage.py loaddata species.json
	python3 manage.py loaddata transport.json
	python3 manage.py loaddata starships.json
	python3 manage.py loaddata vehicles.json
	python3 manage.py loaddata films.json

serve:
	python3 manage.py runserver

dump_data:
	python3 manage.py dumpdata resources.planet > resources/fixtures/planets.json --indent 4
	python3 manage.py dumpdata resources.people > resources/fixtures/people.json --indent 4
	python3 manage.py dumpdata resources.species > resources/fixtures/species.json --indent 4
	python3 manage.py dumpdata resources.starship > resources/fixtures/starships.json --indent 4
	python3 manage.py dumpdata resources.vehicle > resources/fixtures/vehicles.json --indent 4
	python3 manage.py dumpdata resources.transport > resources/fixtures/transport.json --indent 4
	python3 manage.py dumpdata resources.film > resources/fixtures/films.json --indent 4


drop_db:
	python3 manage.py flush

test:
	python3 manage.py test


clear_cache:
	python3 manage.py clear_cache
