from kivy.app import App
from cei2 import *

class QuestionsApp(App):
    def build(self):
        return QuestionsForm()

if __name__ == '__main__':
    QuestionsApp().run()
