# FastAPI Template

This template can be used to create a basic setup for a FastAPI based website.
Some technologies utilized include:

1. FastAPI for the backend
1. HTMX for front-end js library
1. Postgres for the database
1. Cloudbeaver to administer the database
1. UV for python package management and virtual environment management
1. Yoyo migrations for database migrations

## Prerequites

To get started, first ensure you have the following installed

1. [Docker](https://docs.docker.com/engine/install/)
1. [UV](https://docs.astral.sh/uv/guides/install-python/)

## Usuage

### Development

To run the application in development mode, run the following commands.

```bash
docker compose build
docker compose up db cloudbeaver
```

This will launch the postgres database and cloudbeaver on localhost:8978.

To set up cloud beaver for the first time, first create a username and password on the website.
Next set up a postgres connection with the following

host=db
database=application
username=admin
password=your_password

The database, username, and password should and can be changed on the docker-compose.yaml file, preferably using secret environment variables.
(Note: if you change the default database after running the first time, you must first remove the mounted volume prior to running the docker compose up command)

To run the fastAPI application, run

```bash
uv run fastapi dev src/main.py
```

### Production

To launch in production, run the following command

```bash
docker compose up
```
