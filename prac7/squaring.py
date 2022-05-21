"""
CP1404 Prac7
Wang Anping
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class SquareNumberApp(App):

    def build(self):
        Window.size = (500, 300)
        self.title = "Make Ur Number^2"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def calculate_numbers(self, value):
        try:
            result = int(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Error"


SquareNumberApp().run()
