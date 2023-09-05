import csv
from dataclasses import dataclass, astuple
from datetime import datetime
import requests


@dataclass
class Vacancies:

    emp_id: int
    emp_name: str
    vac_id: int
    vac_name: str
    area: str
    date_of_publication: datetime
    salary_from: int
    url: str

    def __iter__(self):
        """Итерирует экземпляры класса"""
        return iter([
            self.emp_id,
            self.emp_name,
            self.vac_id,
            self.vac_name,
            self.area,
            self.date_of_publication,
            self.salary_from,
            self.url
        ])


class HeadHunterAPI():


    def _get_vacancies(self, page: int = 0) -> list[dict]:
        """Получает список всех вакансий с сайта hh.ru"""
        payload = {"page": page, "per_page": 100, 'only_with_salary': True}
        url = 'https://api.hh.ru/vacancies'
        response = requests.get(url, params=payload)
        data = response.json()
        return data["items"]

    def get_vacancies(self):
        """Получает список всех вакансий как объектов класса Vacancies с сайта ХХ"""
        vacancies: list[Vacancies] = []
        for page in range(5):
            data = self._get_vacancies(page)
            for item in data:
                salary = item['salary']
                salary_from = salary.get('from', 0)

                vacancy = Vacancies(
                    emp_id=int(item["employer"].get('id', 0)),
                    emp_name=item["employer"]["name"],
                    vac_id=int(item["id"]),
                    vac_name=item["name"],
                    area=item["area"]["name"],
                    date_of_publication=datetime.fromisoformat(item["published_at"]),
                    salary_from=int(salary_from),
                    url=item['alternate_url']
                    )
                vacancies.append(vacancy)

        return vacancies



class VacanciesToCsvFile():

    def add_vacancy_to_file(self, data):
        """Записывает список всех вакансий как объектов класса Vacancies с сайта СД или ХХ в csv-файл"""
        with open('vacancies.csv', mode="w", encoding='utf-8') as file:
            names = ["emp_id", "emp_name", "vac_id", "vac_name", "area", "date_of_publication", "salary_from", "url"]
            file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
            for vacancy in data:
                file_writer.writerow(astuple(vacancy))


    def get_vacancies_from_file(self):
        """Получает построчно все вакансии из csv-файла"""
        vacancies: list[Vacancies] = []
        with open('vacancies.csv', mode="r", encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=",")
            for row in file_reader:
                vacancy = Vacancies(
                    emp_id=int(row[0]),
                    emp_name=row[1],
                    vac_id=int(row[2]),
                    vac_name=row[3],
                    area=row[4],
                    date_of_publication=datetime.fromisoformat(row[5]),
                    salary_from=int(row[6]),
                    url=row[7]
                )
                vacancies.append(vacancy)

            return vacancies


