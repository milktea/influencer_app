define USAGE

Commands:
	init          Install Python dependencies with pipenv
	init-db       Setup database
	clean-db      Delete init db import
	serve         Run app in dev environment
	test          Run tests
endef

export USAGE
help:
	@echo "$$USAGE"

init:
	pip3 install --upgrade pip
	pip3 install -r influencer_app/requirements.txt

init-db:
	python manage.py migrate
	python manage.py import_teams_data influencer_app/data/teams.csv
	python manage.py import_campaigns_data influencer_app/data/campaigns.csv

clean-db:
	python manage.py clean_db_data

serve:
	python manage.py runserver

test:
	pytest -v
