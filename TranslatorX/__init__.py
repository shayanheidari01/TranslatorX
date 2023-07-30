from user_agent import generate_user_agent
import urllib.parse
import httpx
import html
import re


__version__ = '1.0'
__author__ = 'Shayan Heidari'


class AsyncTranslator:
    def __init__(self, base_url: str = None) -> None:
        self.base_url = base_url or 'https://translate.google.com'
        self.__client = httpx.AsyncClient(base_url=self.base_url)

    async def Translate(self, text: str, to_lang: str = 'auto', from_lang: str = 'auto') -> str:
        '''
        Translates a text from one language to another using the Google Translate API.

        Args:
            text (str): The text to translate.
            to_lang (str, optional): The language to translate the text to. Defaults to "auto".
            from_lang (str, optional): The language of the text to translate. Defaults to "auto".

        Returns:
            str: The translated text.
        '''
        link = f'/m?tl={to_lang}&sl={from_lang}&q={urllib.parse.quote(text)}'
        response = await self.__client.get(link, headers={'User-Agent': generate_user_agent()})

        if response.status_code == 200:
            result = re.findall(r'(?s)class="(?:t0|result-container)">(.*?)<', response.text)
            return None if len(result) == 0 else html.unescape(result[0])
        else:
            return None


class Translator:
    def __init__(self, base_url: str = None) -> None:
        self.base_url = base_url or 'https://translate.google.com'
        self.__client = httpx.Client(base_url=self.base_url)

    def Translate(self, text: str, to_lang: str = 'auto', from_lang: str = 'auto') -> str:
        '''
        Translates a text from one language to another using the Google Translate API.

        Args:
            text (str): The text to translate.
            to_lang (str, optional): The language to translate the text to. Defaults to "auto".
            from_lang (str, optional): The language of the text to translate. Defaults to "auto".

        Returns:
            str: The translated text.
        '''
        response = self.__client.get(url=f'/m?tl={to_lang}&sl={from_lang}&q={urllib.parse.quote(text)}',
                                     headers={'User-Agent': generate_user_agent()})

        if response.status_code == 200:
            result = re.findall(r'(?s)class="(?:t0|result-container)">(.*?)<', response.text)
            return None if len(result) == 0 else html.unescape(result[0])
        else:
            return None