## How to run

    python3 -m venv env
    source env/bin/activate

    pip install -r requirements.txt

Set environment variables:

    DATABASE_URL=...to a database named "postgres" with a user named "postgres"
    DB_PASSWORD=... this will be used to test connection using psycopg2 in the root url

run:

    python3 manage.py runserver