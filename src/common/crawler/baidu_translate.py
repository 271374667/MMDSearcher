import hashlib
import random
from functools import lru_cache

import loguru
import requests

from src.core.settings import settings


class BaiduTranslate:
    def __init__(self) -> None:
        self._app_id = settings.get(settings.BAIDU_TRANSLATE_APP_ID)
        self._secret_key = settings.get(settings.BAIDU_TRANSLATE_SECRET_KEY)

    @lru_cache
    def en2cn(self, content: str) -> str:
        return self._translate(content, 'en', 'zh')
        # return 'test'

    @lru_cache
    def cn2en(self, content: str) -> str:
        return self._translate(content, 'zh', 'en')

    @lru_cache
    def _translate(self, content: str, from_lang: str, to_lang: str) -> str:
        base_url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
        salt = str(random.randint(32768, 65536))
        sign = hashlib.md5((self._app_id + content + salt + self._secret_key).encode('utf-8')).hexdigest()
        params = {
                'q': content,
                'from': from_lang,
                'to': to_lang,
                'appid': self._app_id,
                'salt': salt,
                'sign': sign
                }
        response = requests.get(base_url, params=params)
        loguru.logger.debug(f"百度翻译返回结果: {response.json()}")
        return response.json()['trans_result'][0]['dst']


if __name__ == '__main__':
    baidu_translate = BaiduTranslate()
    print(baidu_translate.en2cn('test this line'))
    print(baidu_translate.en2cn('test this line'))
    print(baidu_translate.en2cn('test this line'))
