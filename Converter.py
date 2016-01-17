from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from datetime import datetime
from kivy.properties import NumericProperty
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
import web_utility


class Converter(App):
    home = StringProperty()
    selected_country = StringProperty()
    converted = NumericProperty(0)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.today = datetime.now()
        self.currentDate = self.today.strftime('%Y/%m/%d')


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


    def convert(self, amount):
        url_string = "https://www.google.com/finance/converter?a={}&from={}&to={}".format(amount, self.get_currency_code(self.selected_country), self.get_currency_code('Australia'))
        result = web_utility.load_page(url_string)
        converted_amount = round(self.get_only_number(result[result.index('ld>'):result.index('</span>')]), 2)
        self.converted = converted_amount

    def get_only_number(self, given_string):
        return float(''.join(ele for ele in given_string if ele.isdigit() or ele == '.'))

    def get_currency_code(self, country):
        with open("currency_details.txt", encoding='utf8') as currency_details:
            for line in currency_details:
                split_line = line.split(",")
                if split_line[0] == country:
                    return split_line[1]



Config.set('graphics', 'width', 350)
Config.set('graphics', 'height', 700)

Converter().run()
