# Technical Test - Event Management

This repository contains the solution to the Technical Test for the Backend Developer position. The test involves creating a Python API using Django Rest Framework for event registration and management.

## Objective

That I, Carlos Andres Moreno Alvarez, today, November 28, give a sample of my talent so that tomorrow, November 29, they tell me, you are hired; and thus be able to continue growing in life

## Configuration and Usage

Follow these steps to set up and use the API:

1. Clone this repository on your local machine:

   ```shell
   git clone (link)
   cd event_management
   ```
2. Configure .env with .envexample

3. Run
   ```shell
    $ sudo docker-compose -f local.yml build
    $ sudo docker-compose -f local.yml up
    ```
    or run with virtual env
    ```shell
        python -m venv env
        env\Scripts\activate
        (env) python manage.py runserver
    ```

## bd
 use you postgrests or run   
* docker build -t my-postgres-image .
* docker run -d --name my-postgres-container -p 5432:5432 my-postgres-image

### Migrations and load data

    $ docker-compose -f local.yml run --rm django python manage.py makemigrations
    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py loaddata event_fixture.json



## Contact
    If you have any questions or need support related to this technical test, feel free to contact:
* Name: Carlos Andres Moreno Alvarez
* Email: 5carlosmoreno2021@gmail.com