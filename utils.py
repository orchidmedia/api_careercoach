import json
import re

# RECOMMEND JOBS
REGEX_TITLES_RECOMMEND = r'\d+\.\s([^:]+):'
##CARRER CHALLENGES
REGEX_TITLES_CHALLENGES_CARRIER = r'\d+\.\s*(.*?):'
REGEX_ITEMS_CHALLENGES_CARRIER = r'- [^\n]*'


def extract_recommend(response: str):
    titles = re.findall(REGEX_TITLES_RECOMMEND, response)
    body = []
    for title in range(0, len(titles)):
        response = response[response.find(titles[title]):]
        description = response[response.find(':') + 1:response.find('\n\n')]
        body.append({
            "title": titles[title],
            "description": description.strip()
        })
    return body


def extract_carrer_path_challenges(response):
    body = []
    response = json.loads(response)

    for key in response:
        body.append({
            "title": key,
            "description": response[key]
        })
    # Buscar los títulos en el texto
    return body


def extract_data_3(response: str):
    # Define regular expressions for titles, subtitles, and content
    title_pattern = r'[A-Za-z].*?\:'
    titles = re.findall(title_pattern, response, re.MULTILINE)
    print(titles)
    titles = titles[1:]
    description = r'([A-Z][^.]*\.)'
    body = []

    for i, title in enumerate(titles):
        # print(title)

        response = response[response.find(title):]
        descriptions = re.findall(description, response, re.MULTILINE)

        body.append({
            "title": title,
            "description": descriptions
        })
    body.reverse()
    descriptions_already_exists = []
    for item in body:
        if len(descriptions_already_exists) == 0:
            descriptions_already_exists.extend(item['description'])
            continue
        item['description'] = list(filter(lambda x: x not in descriptions_already_exists, item['description']))
        descriptions_already_exists.extend(item['description'])
    body = list(filter(lambda x: len(x['description']) > 0, body))
    body.reverse()
    print('body', body)
    return body


def extract_data_2(response: str):
    # Define regular expressions for titles, subtitles, and content
    title_pattern = r'[A-Z].*?\:'
    titles = re.findall(title_pattern, response, re.MULTILINE)
    print(titles)
    titles = titles[1:]
    description = r'^-\s(.*?;)'
    body = []

    for i, title in enumerate(titles):
        # print(title)

        response = response[response.find(title):]
        descriptions = re.findall(description, response, re.MULTILINE)

        body.append({
            "title": title,
            "description": descriptions
        })
    body.reverse()
    descriptions_already_exists = []
    for item in body:
        if len(descriptions_already_exists) == 0:
            descriptions_already_exists.extend(item['description'])
            continue
        item['description'] = list(filter(lambda x: x not in descriptions_already_exists, item['description']))
        descriptions_already_exists.extend(item['description'])
    body = list(filter(lambda x: len(x['description']) > 0, body))
    body.reverse()
    print('body', body)
    return body


def extract_data(response: str):
    # Define regular expressions for titles, subtitles, and content
    title_pattern = r'\n- (.*?):'
    titles = re.findall(title_pattern, response, re.MULTILINE)
    titles = titles[1:]
    if len(titles) == 0:
        return extract(response)
    description = r'^\d+\.\s(.*?\.)$'
    body = []

    for i, title in enumerate(titles):
        # print(title)

        response = response[response.find(title):]
        descriptions = re.findall(description, response, re.MULTILINE)

        body.append({
            "title": title,
            "description": descriptions
        })
    body.reverse()
    descriptions_already_exists = []
    for item in body:
        if len(descriptions_already_exists) == 0:
            descriptions_already_exists.extend(item['description'])
            continue
        item['description'] = list(filter(lambda x: x not in descriptions_already_exists, item['description']))
        descriptions_already_exists.extend(item['description'])
    body = list(filter(lambda x: len(x['description']) > 0, body))
    body.reverse()
    print('body', body)
    return body


def extract_titles(response: str):
    title_pattern = r'^- .*?:$'
    titles = re.findall(title_pattern, response, re.MULTILINE)
    titles = titles[1:]
    # titles=list(map(lambda x: x.replace('\n',''),titles))
    description = r'- (.*?\.)'
    body = []
    print('here', titles)
    for i, title in enumerate(titles):
        # print(title)

        response = response[response.find(title):]
        descriptions = re.findall(description, response, re.MULTILINE)
        body.append({
            "title": title,
            "description": descriptions
        })
    body.reverse()
    descriptions_already_exists = []
    for item in body:
        if len(descriptions_already_exists) == 0:
            descriptions_already_exists.extend(item['description'])
            continue
        item['description'] = list(filter(lambda x: x not in descriptions_already_exists, item['description']))
        descriptions_already_exists.extend(item['description'])
    body = list(filter(lambda x: len(x['description']) > 0, body))
    body.reverse()
    print(body)
    return body


def extract(response: str):
    # Define regular expressions for titles, subtitles, and content
    title_pattern = r'[A-Z\s]+:'
    titles = re.findall(title_pattern, response, re.MULTILINE)
    titles = titles[1:]
    # titles=list(map(lambda x: x.replace('\n',''),titles))
    description = r'^-\s(.*?)\n'
    body = []
    print('here', titles)
    for i, title in enumerate(titles):
        print('titles', title)

        response = response[response.find(title):]
        descriptions = re.findall(description, response, re.MULTILINE)

        body.append({
            "title": title,
            "description": descriptions
        })
    body.reverse()
    descriptions_already_exists = []
    for item in body:
        if len(descriptions_already_exists) == 0:
            descriptions_already_exists.extend(item['description'])
            continue
        item['description'] = list(filter(lambda x: x not in descriptions_already_exists, item['description']))
        descriptions_already_exists.extend(item['description'])
    body = list(filter(lambda x: len(x['description']) > 0, body))
    body.reverse()
    print(body)
    return body
