import csv
import requests


class Vacancies():

    def __init__(self, emp_id, emp_name, vac_id, vac_name, area, date_of_publication, salary_from, url):
        """Инициализирует экземпляры класса"""
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.vac_id = vac_id
        self.vac_name = vac_name
        self.area = area
        self.date_of_publication = date_of_publication
        self.salary_from = salary_from
        self.url = url

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

    def get_vacancies(self):
        """Получает список всех вакансий как объектов класса Vacancies с сайта ХХ"""
        list_vac_obj = []
        url = 'https://api.hh.ru/vacancies'
        for page in range(5):
            payload = {"page": page, "per_page": 100}
            responce = requests.get(url, params=payload)
            data = responce.json()["items"]
            for item in data:
                vac_id = item["id"]
                vac_name = item["name"]
                try:
                    emp_id = item["employer"]["id"]
                except KeyError:
                    emp_id = 0
                emp_name = item["employer"]["name"]
                area = item["area"]["name"]
                date_of_publication = item["published_at"]
                try:
                    salary_from = int(item["salary"]["from"])
                except TypeError:
                    salary_from = 0
                vacancy = Vacancies(emp_id=emp_id,
                                    emp_name=emp_name,
                                    vac_id=vac_id,
                                    vac_name=vac_name,
                                    area=area,
                                    date_of_publication=date_of_publication,
                                    salary_from=salary_from,
                                    url=f'https://hh.ru/vacancy/{vac_id}')
                list_vac_obj.append(vacancy)
        return list_vac_obj


class VacanciesToCsvFile(HeadHunterAPI):

    def add_vacancy_to_file(self, data):
        """Записывает список всех вакансий как объектов класса Vacancies с сайта СД или ХХ в csv-файл"""
        with open('../vacancies_dir/vacancies.csv', mode="w", encoding='utf-8') as file:
            names = ["emp_id", "emp_name", "vac_id", "vac_name", "area", "date_of_publication", "salary_from", "url"]
            file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
            file_writer.writerows(data)

            # hh_api = HeadHunterAPI()
            # for obj_ in HeadHunterAPI.get_vacancies(hh_api):
            #     for att in dict_.items():
            #         file_writer.writerow(value)
            # # for i in HeadHunterAPI.get_vacancies(hh_api):
            # #     file_writer.writerow(i)

    def get_vacancies_from_file(self):
        """Получает построчно все вакансии из csv-файла"""
        with open('vacancies_dir.csv', mode="r", encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=",")
            return file_reader