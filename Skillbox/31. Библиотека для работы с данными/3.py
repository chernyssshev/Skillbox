import requests
import json

url = 'https://www.breakingbadapi.com/api/deaths'


def main(url: str) -> None:
    my_req = requests.get(url)
    data = json.loads(my_req.text)
    max_death = 0
    for elem in data:
        if elem['number_of_deaths'] > max_death:
            max_death = elem['number_of_deaths']
    for elem in data:
        if elem['number_of_deaths'] == max_death:
            with open('max_death.json', 'w') as file:
                json.dump(elem, file, indent=4)
            with open('max_death.json', 'r') as file:
                data = json.load(file)
    for elem in data:
        print(elem, ':', data[elem])


if __name__ == '__main__':
    main(url)
