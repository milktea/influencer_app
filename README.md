# Influencer App

- A platform to create and manage influencer marketing campaigns

## Setting up locally

### Stack

- Python 3.9.0
- Virtualenv
- Django
- Django Rest Framework
- PostgreSQL
- Pandas
- Mypy
- Pytest


### Cloning the repository
```
git clone https://github.com/milktea/influencer_app.git
```
Navigate to the app directory:
```
cd influencer_app
```

### Python Setup
You can optionally use pyenv to set your python version:
```
pyenv install 3.9.0
pyenv local 3.9.0
```
Double check if correct python version (3.9.x) is used by running, `python -V`. 
If not, try to run, `eval "$(pyenv init -)"`


Creating and activating virtualenv
```
virtualenv -p python3 venv
. venv/bin/activate source
```

### Prerequisites
To install the project with all the requirements, run:
```
make init
```

### Setting up the database
Modify the *sample.env* file to setup the environment variables, esp DB config, and rename to .env 
After modifying, export them by running:
```
source .env
```
(or you can upload this file in your IDE if supported)

Create *influencers* database:
```
psql -c "create database influencers"
```
Migrating and importing teams, hashtags and campaigns resources into the database:
```
make init-db
```
or
```
python manage.py migrate
python manage.py import_teams_data influencer_app/data/teams.csv
python manage.py import_campaigns_data influencer_app/data/campaigns.csv
```
If you want to delete the imported data later on, run:
```
make clean-db
```
### Running the app
To run the development server on localhost:8000:

Run the app:
```
python manage.py runserver
```
or
```
make serve
```
You should be able to access the application with this sample endpoint
http://localhost:8000/api/campaigns


### Running the tests
```
make test
```
or run the basic test suite with:

```
pytest
```
#### For specific tests:

##### pytest -v <TEST_FILE_PATH> -k <NAME_OF_TEST>
```
e.g
pytest -v campaigns/tests/test_serializers.py -k test_team_serializer
```

# Endpoints
    Get campaigns : /api/campaigns

### Documentation

This project was designed with the following concepts in mind.  

* Repository Pattern
    - Repository pattern is used to separate db queries.
      If we want to change the database, we will just need to modify queries inside the repo without having to touch other directories.
* Many to Many Relationship for Hashtag and Campaigns 
    - If hashtag search will be implemented in the future, it will be convenient.
* Services Repo:
    - Separated the import data inside services, e.g. if we want to add an endpoint to upload those data, 
      we can just right away use the services.
* Usage of an optional static type checker (mypy) for faster dev


### Built With

* [Django] - The web framework used

### Author

* milktea

For questions esp. regarding the project setup, feel free to message me @ sescatalan@gmail.com
