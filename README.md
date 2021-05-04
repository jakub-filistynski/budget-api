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
1. Setup .env:
 ```sh
$ cd .envs
$ mv .env.example .env
$ # Set SECRET_KEY in .env
 ```

2. Build project:
 ```sh
 $ docker-compose build
 ```

3. Run project: 
 ```sh
 $ docker-compose up
 ```

Open http://localhost:8000 to view it in the browser.

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
