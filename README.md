# Family budget API
## Description
The application allow to register new users. Each user can create a list of any number of budgets and share it with any number of users. 
The budget consists of income and expenses. They are grouped into categories.

## Technologies
* Python 3.9.4
* Django 3.1.8
* DRF
* PostgreSQL
* Pyenv, Poetry, Pre-commit
* Docker

## Instruction
Build project:
```sh
$ docker-compose build
```

Run project: 
```sh
$ docker-compose up
```

Load fixtures: 
```sh
$ docker-compose exec api bash
$ ./manage.py load_fixtures
```

# TODO:
## Budget:
* Share budget
* Retrieve budget
* Edit budget

## Finanse
* List finances
* Create finance
* Retrieve finance
* Edit finance
* Delete finance

# Auth
* Replace TokenAuthentication with something more secure for example JWT.
