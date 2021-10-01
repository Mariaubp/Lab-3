import requests


def paisesInfo() -> list:
    listadoPaises = []
    response = requests.get("https://api.covid19api.com/countries")
    if response.status_code == 200:
        for pais in response.json():
            listadoPaises.append(pais["Slug"])
    listadoPaises.sort()
    return listadoPaises