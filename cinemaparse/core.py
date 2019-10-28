'''Cinema module'''
import requests
from bs4 import BeautifulSoup
class CinemaParser:
    '''Class CinemaInformations'''
    def __init__(self, city='msk'):
        '''Город'''
        self.city = city
        self.content = None
    def extract_raw_content(self):
        '''Инфрмация со страницы'''
        page = requests.get('https://msk.subscity.ru/')
        self.content = page.text
    def print_raw_content(self):
        '''Вывод информации со страницы'''
        beauty = BeautifulSoup(self.content)
        print(beauty.prettify())
MSK_PARSER = CinemaParser('spb')
MSK_PARSER.extract_raw_content()
MSK_PARSER.print_raw_content()
