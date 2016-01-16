from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from datetime import datetime
import web_utility


class Converter(App):
    def build(self):
        self.root = Builder.load_file('converter.kv')
        return self.root

    def current_date(self):
        today = datetime.now()
        currentDate = today.strftime('%Y/%m/%d')
        return currentDate

    def chosen_currency_code(self):
        with open("currency_details.txt", encoding='utf8') as currency_details:
            for line in currency_details:
                split_line = line.split(",")
                if split_line[0] == self.root.ids.spinner.text:
                    print(split_line[1])

    def home_currency_code(self):
        with open("currency_details.txt", encoding='utf8') as currency_details:
            for line in currency_details:
                split_line = line.split(",")
                if split_line[0] == self.root.ids.home.text:
                    print(split_line[1])

    def countries(self):
        details = []
        with open("currency_details.txt", encoding='utf8') as currency_details:
            for line in currency_details:
                split_line = line.split(",")
                details.append(split_line[0])
        return details

    def home_country(self):
        with open('config.txt', encoding='utf8') as countries:
            for line in countries:
                return line[0:]

    def convert(self, amount, home_currency_code, location_currency_code):
        url_string = "https://www.google.com/finance/converter?a={}&from={}&to={}".format(amount,
                                                                                          home_currency_code,
                                                                                          self.countries())
        result = web_utility.load_page(url_string)
        converted_amount = round(self.get_only_number(result[result.index('ld>'):result.index('</span>')]), 2)
        return converted_amount

    def get_only_number(self, given_string):
        return float(''.join(ele for ele in given_string if ele.isdigit() or ele == '.'))


Config.set('graphics', 'width', 350)
Config.set('graphics', 'height', 700)

Converter().run()
