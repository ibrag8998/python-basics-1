import requests
from bs4 import BeautifulSoup


def http_get(url):
    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        },
    )
    return response


def get_tag_text(parent_tag, tag_name, attrs):
    # TODO: Когда вызываем метод .find, подходящих результатов может не оказаться.
    #       Тогда возвращаемым значением будет None.
    #       Нужно как-то обрабатывать это исключение.
    return (
        parent_tag.find(tag_name, attrs=attrs)
        .text.replace("\u202f", " ")
        .replace("\xa0", " ")
    )


def parse_response(response):
    soup = BeautifulSoup(response.text, "html.parser")

    vacancy_tags = soup.find_all("div", attrs={"class": "vacancy-serp-item"})
    vacancies = []
    for vacancy_tag in vacancy_tags:
        title = get_tag_text(
            vacancy_tag, "a", {"data-qa": "vacancy-serp__vacancy-title"}
        )
        salary = get_tag_text(
            vacancy_tag, "span", {"data-qa": "vacancy-serp__vacancy-compensation"}
        )
        employer = get_tag_text(
            vacancy_tag, "a", {"data-qa": "vacancy-serp__vacancy-employer"}
        )
        region = get_tag_text(
            vacancy_tag, "div", {"data-qa": "vacancy-serp__vacancy-address"}
        )
        responsibility = get_tag_text(
            vacancy_tag,
            "div",
            {"data-qa": "vacancy-serp__vacancy_snippet_responsibility"},
        )
        requirement = get_tag_text(
            vacancy_tag,
            "div",
            {"data-qa": "vacancy-serp__vacancy_snippet_requirement"},
        )

        vacancy = {
            "title": title,
            "salary": salary,
            "employer": employer,
            "region": region,
            "responsibility": responsibility,
            "requirement": requirement,
        }

        vacancies.append(vacancy)

        print(vacancy)
        print()


cards = [
    {
        "title": "abc",
        "salary": "1000",
    },
    {
        "title": "qwe",
        "salary": "2000",
    },
]
