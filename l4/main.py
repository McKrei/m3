import requests


url = 'http://85.209.89.152/handler/query_detail?query=%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82'

res = requests.get(url)

print(res.json())


with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(yoda, file, ensure_ascii=False, indent=1)
