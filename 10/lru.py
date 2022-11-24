import logging
import logging.config
import sys


LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "to_file": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
        "to_stdout": {
            "format": "[%(levelname)s] - %(message)s",
        },
    },
    "handlers": {
        "file_log": {
            "level": "INFO",
            "filename": "cache.log",
            "class": "logging.FileHandler",
            "formatter": "to_file",
        },
        "stdout_log": {
            "level": "DEBUG",
            'stream': 'ext://sys.stdout',
            "class": "logging.StreamHandler",
            "formatter": "to_stdout",
        },
    },
    "loggers": {
        "all": {
            "level": "DEBUG",
            "handlers": ["stdout_log", "file_log"],
        },
        "file": {
            "level": "INFO",
            "handlers": ["file_log"],
        },
        "stdout": {
            "level": "DEBUG",
            "handlers": ["stdout_log"],
        },
    },
}
logging.config.dictConfig(LOGGING_CONFIG)


class LRUCache:
    def __init__(self, limit=42, log_stdout=False):
        self.limit = limit
        self.cache = {}
        self.order_dict = {}
        self.order = 0

        if log_stdout:
            self.logger = logging.getLogger("all")
        else:
            self.logger = logging.getLogger("file")

        self.logger.debug("Инициализация + настройка логгера завершена.")

    def get(self, key):
        if key in self.cache:
            self.logger.info(f"Вызван get для существующего ключа - {key}")
            self.order_dict[key] = self.order
            self.order += 1
            self.logger.debug(f"Завершение get('{key}')")
            return self.cache[key]
        self.logger.warning(f"Вызван get для несуществующего ключа - {key}")
        self.logger.debug(f"Завершение get('{key}')")
        return None

    def set(self, key, value):
        if (
                len(self.cache) >= self.limit
                and
                key not in self.order_dict.keys()
        ):
            early_key = min(self.order_dict.keys(),
                            key=lambda k: self.order_dict[k])
            self.order_dict.pop(early_key)
            self.cache.pop(early_key)
            self.logger.warning(f"Переполнение! Удален ключ - {early_key}")

        elif key not in self.order_dict.keys():
            self.logger.info(f"Добавление! Новый ключ - {key}")
        else:
            self.logger.info(f"Изменение! Существующий ключ - {key}")

        self.order_dict[key] = self.order
        self.order += 1
        self.cache[key] = value
        self.logger.debug(f"Завершение set{key, value}")


def main():
    cache = LRUCache(2, True)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    cache.set("k1", "val11")
    cache.set("k3", "val3")

    print(cache.get("k1"))
    print(cache.get("k2"))


if __name__ == "__main__":
    main()
