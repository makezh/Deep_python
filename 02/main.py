import json


def change_str(string: str):
    return string[::-1]


def parse_json(json_str: str,
               required_fields=None,
               keywords=None,
               keyword_callback=None):

    json_doc = json.loads(json_str)
    json_doc = {key: list(map(str, value.split()))
                for key, value in json_doc.items()}

    if (required_fields is None) \
            or (keyword_callback is None):
        return None

    triggers = 0  # количество найденных слов
    results = []

    for value in required_fields:
        if value in json_doc:
            for word in json_doc[value]:
                if word in keywords:
                    results.append(keyword_callback(word))
                    triggers += 1

    if triggers == 0:
        return None

    return results


if __name__ == '__main__':
    JSON_SOURCE = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    keys = ["key1", "key2"]
    values = ["Word1", "word3"]
    print(parse_json(JSON_SOURCE, keys, values, change_str))
