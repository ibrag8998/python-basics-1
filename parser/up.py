from parser.parse import http_get, parse_response

# url = input("Введите URL: ")
url = "https://makhachkala.hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&only_with_salary=true&text=python&clusters=true&ored_clusters=true&enable_snippets=true"

response = http_get(url)
soup = parse_response(response)
