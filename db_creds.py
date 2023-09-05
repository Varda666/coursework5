from pathlib import Path


DB_CREDS = {
    "host": "localhost",
    "port": 5432,
    "database": "postgres",
    "user": "postgres",
    "password": "Varda141190"
}

vacancies_csv_path = Path.cwd().joinpath('vacancies.csv')