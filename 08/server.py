import asyncio
from collections import Counter
import requests
import aiohttp
import json
from bs4 import BeautifulSoup


def common_words(url: str, count_words: int):
    word_count = Counter()
    try:
        request = requests.get(url, timeout=3)
    except (requests.ConnectionError,
            requests.exceptions.MissingSchema,
            requests.exceptions.ReadTimeout):
        res_json = json.dumps({url: 'error'}, ensure_ascii=False)
    else:
        soup = BeautifulSoup(request.text, 'html.parser')
        all_words = soup.get_text(" ", strip=True).lower().split()

        for word in all_words:
            cln_word = word.strip('.,?')
            # не будем считать предлоги/союзы
            if len(cln_word) > 3:
                word_count[cln_word] += 1

        res_dict = {url: {words[0]: words[1] for words in word_count.most_common(count_words)}}
        res_json = json.dumps(res_dict, ensure_ascii=False)

    return res_json


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text())

asyncio.run(main())