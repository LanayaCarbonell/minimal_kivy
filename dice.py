from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import random


class DiceApp(App):

    def build(self):
        return DiceRoller()


class DiceRoller(BoxLayout):
    val = StringProperty('1')

    def roll(self):
        self.val = str(random.randint(1, 6))

if __name__ == '__main__':
    DiceApp().run()
