from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

class Converter(App):
    def build(self):
        self.root = Builder.load_file('converter.kv')
        return self.root
Config.set('graphics', 'width', 350)
Config.set('graphics', 'height', 700)

Converter().run()