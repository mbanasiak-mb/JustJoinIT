import json

import numpy as np
import requests

# --------------------------------------------------------------------------------


def rectangular(x, h: float, v_min: float, v_max: float):
    return h if v_min <= x <= v_max else 0


def get_json(url: str):
    r = requests.get(url)
    c = r.content
    j = json.loads(c)
    return j


def get_salary_pl(data, employment: str) -> [float, float, str]:
    employment_types: list = data['employment_types']

    for employment_type in employment_types:
        type = employment_type['type']

        if type == employment:
            salary = employment_type["salary"]

            if salary is None:
                continue

            currency = salary['currency']
            if currency == "pln":
                experience_level: str = data['experience_level']
                salary_from: float = salary["from"]
                salary_to: float = salary["to"]
                return salary_from, salary_to, experience_level

    return 0, 0, ''


def url_category(category: str) -> str:
    return "" if category == 'all' else f"&categories[]={category}"


def get_data(employment: str, category: str):
    url = f"http://justjoin.it/api/offers/search?" + \
          f"&tab=with-salary" + \
          f"&employmentType={employment}" + \
          url_category(category)

    print("GETTING DATA : START")
    print(url)
    data = get_json(url)
    print("GETTING DATA : DONE")
    return data


def prepare_data(px, py, emp, cat):
    """
    :param emp: employment
    :param cat: category
    """

    global v_rectangular
    data = get_data(emp, cat)

    py_j = px * 0
    py_m = px * 0
    py_s = px * 0
    for d in data:
        v_min, v_max, seniority = get_salary_pl(d, emp)
        if v_min == v_max == 0:
            continue

        py = py + v_rectangular(px, 1, v_min, v_max)
        if seniority == 'junior':
            py_j = py_j + v_rectangular(px, 1, v_min, v_max)
        elif seniority == 'mid':
            py_m = py_m + v_rectangular(px, 1, v_min, v_max)
        elif seniority == 'senior':
            py_s = py_s + v_rectangular(px, 1, v_min, v_max)

    m = max(py)
    if m > 0:
        py = py / m
        py_j = py_j / m
        py_m = py_m / m
        py_s = py_s / m
    return px, py, py_j, py_m, py_s

# --------------------------------------------------------------------------------


v_rectangular = np.vectorize(rectangular)
