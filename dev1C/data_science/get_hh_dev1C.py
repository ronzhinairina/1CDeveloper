import re
import requests
import json


class Vacancy:
    def __init__(self, name, description, key_skills, company, salary, area_name, published_at):
        self.name = name
        self.description = description
        self.key_skills = key_skills
        self.company = company
        self.salary = salary
        self.area_name = area_name
        self.published_at = published_at


def get_hh_dev1C():
    result = []
    request = requests.get(
        r"https://api.hh.ru/vacancies?text=1С&search_field=name&order_by=publication_time&per_page=10&page=1&date_from=2022-12-21T00:00:00&date_to=2022-12-22T12:00:00"
    )
    jsonText = request.text
    jsonData = json.loads(jsonText)
    items = jsonData['items']
    items.reverse()
    for i in items:
        request2 = requests.get(
            f"https://api.hh.ru/vacancies/{i['id']}"
        )
        jsonText2 = request2.text
        jsonData2 = json.loads(jsonText2)
        skills = ''
        for k in jsonData2['key_skills']:
            skills += f'{k["name"]}, '
        skills = skills[:-2]
        employer = i['employer']
        employer_name = employer['name']
        area = i['area']
        area_name = area['name']
        description = re.sub(r"<[^>]+>", "", jsonData2['description'], flags=re.S)
        salary = i['salary']
        if salary != None:
            if salary['from'] is None and salary['to'] is None:
                salary = f'{salary["currency"]}'
            elif salary['from'] is None:
                salary = f'{salary["to"]} {salary["currency"]}'
            elif salary['to'] is None:
                salary = f'{salary["from"]} {salary["currency"]}'
            else:
                sfrom = int(salary['from'])
                sto = int(salary['to'])
                salary = f'{(sfrom + sto) / 2} {salary["currency"]}'
        vacancy = Vacancy(i['name'], description, skills, employer_name, salary, area_name,
                          i['published_at'])
        result.append(vacancy)
    return result
