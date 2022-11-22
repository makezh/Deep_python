import asyncio
import sys
import time
import json
from collections import Counter
import aiohttp
import aiofiles
from bs4 import BeautifulSoup

FORMAT = 'utf-8'
END_QUE = '>END'

result = []


async def common_words(session: aiohttp.ClientSession,
                       que: asyncio.Queue,
                       count_words: int = 10):
    while True:
        url = await que.get()
        word_count = Counter()
        try:
            async with session.get(url) as response:
                resp_text = await response.text()
                soup = BeautifulSoup(resp_text, 'html.parser')
                all_words = soup.get_text(" ", strip=True).lower().split()

                for word in all_words:
                    cln_word = word.strip('.,?')
                    # не будем считать предлоги/союзы
                    if len(cln_word) > 3:
                        word_count[cln_word] += 1

                res_dict = {url: {words[0]: words[1] for words in
                                  word_count.most_common(count_words)}}
                result.append(res_dict)

                print(f"[INFO] Обработана ссылка {url}")
        finally:
            que.task_done()


async def gather_data(file: str, num_workers: int = 5):
    que = asyncio.Queue()
    async with aiofiles.open(file, 'r', encoding=FORMAT) as file_urls:
        async for line in file_urls:
            await que.put(line.strip())

    async with aiohttp.ClientSession() as session:
        workers = [
            asyncio.create_task(common_words(session, que))
            for _ in range(num_workers)
        ]

        await que.join()

        for worker in workers:
            worker.cancel()


def main():
    time_start = time.time()
    if len(sys.argv[1:]) == 2:
        filename, workers = sys.argv[1], int(sys.argv[2])
    else:
        filename, workers = "urls.txt", 1

    asyncio.run(gather_data(filename, workers))

    time_end = time.time()

    print(f"[TIME] {time_end - time_start} sec.")

    file_result = "parsing_result.json"

    with open(file_result, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    print(f"[FILE] The data is written to {file_result}")
    print("[END] bye 🖐")


if __name__ == "__main__":
    main()
