import psycopg2
from db_creds import DB_CREDS


class DBManager:

    def connect_with_db(self, postgres_req_employers_and_vacs):
        """Подключается к базе данных"""
        with psycopg2.connect(**DB_CREDS) as conn:
            with conn.cursor() as cur:
                cur.execute(postgres_req_employers_and_vacs)
                rows = cur.fetchall()
                return rows


    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        postgres_req_employers_and_vacs = """SELECT emp_id, COUNT(*), emp_name
        FROM employers_and_vacs
        GROUP BY emp_id, emp_name
        ORDER BY COUNT(*) DESC"""
        return postgres_req_employers_and_vacs

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию"""
        postgres_req_employers_and_vacs = """SELECT emp_name, vac_name, salary_from, url
        FROM employers_and_vacs
        GROUP BY emp_name, vac_name, salary_from, url
        ORDER BY emp_name"""
        return postgres_req_employers_and_vacs

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""
        postgres_req_employers_and_vacs = """SELECT AVG(salary_from)
        FROM employers_and_vacs"""
        return postgres_req_employers_and_vacs

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        postgres_req_employers_and_vacs = """SELECT emp_id, emp_name, salary_from
        FROM employers_and_vacs
        WHERE salary_from > 368839
        GROUP BY emp_id, emp_name, salary_from"""
        return postgres_req_employers_and_vacs

    def get_vacancies_with_keyword(self, keyword):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python"""
        with psycopg2.connect(**DB_CREDS) as conn:
            with conn.cursor() as cur:
                postgres_req_employers_and_vacs = f"""SELECT * FROM employers_and_vacs 
                WHERE vac_name LIKE '%{keyword}%'"""
                cur.execute(postgres_req_employers_and_vacs, keyword)
                rows = cur.fetchall()
                return rows
