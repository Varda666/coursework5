import csv
import psycopg2


class TableCreator:

    def create_table(self):
        """Создает таблицу в БД postgres"""
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="Varda141190") as conn:
            with conn.cursor() as cur:
                create_table_employers_and_vacs = """CREATE TABLE IF NOT EXISTS employers_and_vacs
                (emp_id int,
                emp_name varchar(100) NOT NULL,
                vac_id int PRIMARY KEY,
                vac_name varchar(100) NOT NULL,
                area varchar(100),
                date_of_publication varchar(100),
                salary_from int,
                url varchar(100));
                """
                cur.execute(create_table_employers_and_vacs)

    def insert_data(self):
        """Заполняет таблицу в БД postgres данными о вакансиях и компаниях из csv-файла"""
        with psycopg2.connect(host="localhost", database="postgres", user="postgres", password="Varda141190") as conn:
            with conn.cursor() as cur:
                postgres_insert_query_employers_and_vacs = """ INSERT INTO employers_and_vacs VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
                with open('../vacancies_dir/vacancies.csv', mode="r", encoding='utf-8') as file:
                    file_reader = csv.reader(file, delimiter=",")
                    for row in file_reader:
                        record_to_insert_employers_and_vacs = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                        cur.execute(postgres_insert_query_employers_and_vacs, record_to_insert_employers_and_vacs)