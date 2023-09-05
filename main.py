import vacancies_dir.vacancies
import table_dir.table
import db_manager_dir.db_manager



hh_api = vacancies_dir.vacancies.HeadHunterAPI()
data = hh_api.get_vacancies()
vac_to_csv = vacancies_dir.vacancies.VacanciesToCsvFile()
vac_to_csv.add_vacancy_to_file(data)
tab_creator = table_dir.table.TableCreator()
tab_creator.create_table()
tab_creator.insert_data()
db_manager = db_manager_dir.db_manager.DBManager()
data1 = db_manager.connect_with_db(db_manager.get_companies_and_vacancies_count())
print('Сортировка компаний по количеству вакансий')
for row in data1:
    print(f'Компания {row[2]} - {row[0]}, количество вакансий {row[1]}')

data2 = db_manager_dir.db_manager.DBManager.connect_with_db(db_manager,
                                                    db_manager_dir.db_manager.DBManager.get_all_vacancies(db_manager))
print('Все доступные вакансии')
for row in data2:
    print(f'Компания {row[0]}, вакансия {row[1]}, зарплата от {row[2]}, ссылка {row[3]}')

data3 = db_manager_dir.db_manager.DBManager.connect_with_db(db_manager,
                                                    db_manager_dir.db_manager.DBManager.get_avg_salary(db_manager))
for row in data3:
    print(f'Средняя зарплата по всем вакансиям {int(row[0])} рублей')

data4 = db_manager_dir.db_manager.DBManager.connect_with_db(db_manager,
                                                    db_manager_dir.db_manager.DBManager.get_vacancies_with_higher_salary(db_manager))
print('Выборка вакансий с зарплатой выше среднего значения 368839 руб.')
for row in data4:
    print(f'Компания {row[1]} - {row[0]}, зарплата от {row[2]}')

print('Введите слово для поиска по названию вакансии')
keyword = input()
data5 = db_manager_dir.db_manager.DBManager.get_vacancies_with_keyword(db_manager, keyword)
print('Выборка вакансий спо ключевому слову keyword')
for row in data5:
    print(f'Компания {row[1]} - {row[0]}, зарплата от {row[2]}')
