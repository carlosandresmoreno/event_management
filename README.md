``` d88888b db    db d88888b d8b   db d888888b      .88b  d88.  .d8b.  d8b   db  .d8b.   d888b  d88888b d8888b. 
88'     88    88 88'     888o  88 `~~88~~'      88'YbdP`88 d8' `8b 888o  88 d8' `8b 88' Y8b 88'     88  `8D 
88ooooo Y8    8P 88ooooo 88V8o 88    88         88  88  88 88ooo88 88V8o 88 88ooo88 88      88ooooo 88oobY' 
88~~~~~ `8b  d8' 88~~~~~ 88 V8o88    88         88  88  88 88~~~88 88 V8o88 88~~~88 88  ooo 88~~~~~ 88`8b   
88.      `8bd8'  88.     88  V888    88         88  88  88 88   88 88  V888 88   88 88. ~8~ 88.     88 `88. 
Y88888P    YP    Y88888P VP   V8P    YP         YP  YP  YP YP   YP VP   V8P YP   YP  Y888P  Y88888P 88   YD 
                                                                                                               
```

---

<p align="center"> Event Manager with the CRUD for a test
    <br> 
</p>

## 📝 Table of Contents

- [About](#🧐-about)
- [Getting Started](#🏁-getting-started)
   - [Prerequisites](#prerequisites)
   - [Installing](#installing)
   - [Running the tests](#🔧-running-the-tests)
   - [Coding style tests](#coding-style-tests)
- [Usage](#🎈-usage)
- [Built Using](#⛏️-built-using)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#✍️-authors)
- [Acknowledgments](#🎉-acknowledgements)

      

## 🧐 About

This repository contains the solution to the Technical Test for the Backend Developer position. The test involves creating a Python API using Django Rest Framework for event registration and management.


## 🏁 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [Deployment](#🚀-deployment) for notes on how to deploy the project on a live system.

### Prerequisites

Define the enviroment variables:

- DB_NAME
- DB_USER
- DB_PASSWD
- DB_HOST
- DB_PORT


### Installing whith docker

    $ sudo docker-compose -f local.yml build
    $ sudo docker-compose -f local.yml up

### Installing whith entorn
1. create enviorment, activate the environment and activate variables

      ```bash
      python -m venv venv
      ```

      ```bash
      source venv/bin/activate
      ```

      ```bash
      .env.ps1  
      ```

2. install dependences

      ```bash
      python -m pip install -r requirements.txt 
    
    ```
3. Database with docker



4. Run:

   ```bash
   python manage.py runserver
   ```

5. Run with docker (Optional)
   ```bash
   	docker-compose -f local.yml build
 		docker-compose -f local.yml up
   ```



### Migrations and load data

 use you postgrests or run   
* docker build -t my-postgres-image .
* docker run -d --name my-postgres-container -p 5432:5432 my-postgres-image
* or execute"docker run --name mi-postgresql -e POSTGRES_DB="${DB_NAME}" -e POSTGRES_USER="${DB_USER}" -e POSTGRES_PASSWORD="${DB_PASSWD}" -p "${DB_PORT}:5432" -d postgres:13
"

    $ docker-compose -f local.yml run --rm django python manage.py makemigrations
    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py loaddata event_fixture.json


### 🔧 Running the tests

without test

### Coding style tests

1. install requirements development

   ```bash
   python -m pip install requirements-dev.txt
   ```

2. ejecute formatter black: black is a tool that allows you to identify errors and format your Python code at the same time.

   ```bash
   black app/
   ```

3. ejecute flake8: flake8 is a Python library that includes PyFlakes, Pycodestyle and Ned Batchelder's McCabe script. It is a great toolkit for checking your code base against coding style (PEP8), programming errors such as "library imported but unused", "Undefined name" and code that is not indented.

   ```bash
   flake8 app/
   ```

## 🎈 Usage

   All documentation regarding how to consume this rest service is inside the endpoint. Once the service is up, in the main path you add "docs" here you will see all the documentation for each endpoint.

   {ip}:{port}/swagger


## ⛏️ Built Using

- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" title="Python" alt="Python" height="30px"/> - Language
- <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1NFdQkKQJZ81ncbWWIib6CJZtb27fDP5NBpj11_iT6zRMLx-xrnHuM4ydXIawLbDRN3E&usqp=CAU" title="Django" alt="Django" height="30px"/> - Framework
- <img src="https://iconos8.es/icon/38561/postgresql" title="Redis" alt="Postgres" height="30px"/>- Data base

## ✍️ Authors

- @carlosandresmoreno - Developer


## 🎉 Acknowledgements

- Hat tip to anyone whose code was used