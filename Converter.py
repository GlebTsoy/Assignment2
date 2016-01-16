from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from datetime import datetime
from kivy.properties import NumericProperty
import web_utility


class Converter(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.today = datetime.now()
        self.currentDate = self.today.strftime('%Y/%m/%d')
        self.home_code = ''

    def build(self):
        self.root = Builder.load_file('converter.kv')
        return self.root

    def current_location(self, date_str):
        datetime.strptime(date_str, '%Y/%m/%d')
        dong = []
        with open('config.txt', encoding='utf8') as config:
            for line in config:
                dong.append(line.strip().split(','))
        for i in dong[1:]:
            if i[2] > date_str > i[1]:
                return i[0]

    def home_country(self):
        with open('config.txt', encoding='utf8') as countries:
            for line in countries:
                return line[0:]

    def countries(self):
        details = []
        with open("currency_details.txt", encoding='utf8') as currency_details:
            for line in currency_details:
                split_line = line.split(",")
                details.append(split_line[0])
        return details

    def home_currency_code(self):
        with open("currency_details.txt", encoding='utf8') as currency_details:
            for line in currency_details:
                split_line = line.split(",")
                if split_line[0] == self.root.ids.home.text:
                    self.home_code = split_line[1]



Config.set('graphics', 'width', 350)
Config.set('graphics', 'height', 700)

Converter().run()
