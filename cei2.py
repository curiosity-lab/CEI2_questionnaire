from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty
import xml.etree.ElementTree as ET
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.image import AsyncImage
from functools import partial
from kivy.storage.jsonstore import JsonStore


class AnswerButton(ToggleButton):
    question= ""
    answer = ""
    form= None
    def on_press(self, *args):
        super(AnswerButton,self).on_press(*args)
        self.form.answers[self.question] = self.answer

class QuestionsForm(BoxLayout):
    answers={}
    def __init__(self):
        super(QuestionsForm, self).__init__()
        with self.canvas.before:
            #Color(0, 1, 0, 1)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(source='back2.png')
            self.bind(size=self._update_rect, pos=self._update_rect)

        dict = {'q_in_page':[], 'qu_title': "", 'qu_description': "", 'ques': {},
                 'ans': {}, 'next_button': "", 'prev_button': ""}
        #f = open('try.py', 'r', encoding='utf-8')
        self.answers={}
        # txt = f.read()
        txt = "קרן"

        store = JsonStore('hello.json')
        self.add_widget(Label(text=txt[::-1], font_name="DejaVuSans.ttf"))
        self.add_widget(Label(text=store.get("questionnaire")["qu_title"][::-1], font_name="DejaVuSans.ttf"))
    #     tree = ET.fromstring(txt)
    #
    #     for child in tree:
    #         if child.tag in ['qu_title','qu_description','next_button','prev_button','questions']:
    #             dict[child.tag] = child.text[::-1]
    #             # print('qu_title',dict[child.tag])
    #         if child.tag in ['ques','ans']:
    #             dict[child.tag][child.attrib['name']]= child.text[::-1]
    #
    #     layout = GridLayout(cols=len(dict['ans'])+2, rows=len(dict['ques'])+1,row_default_height=25)
    #     layoutup = BoxLayout(orientation='vertical')
    #     layoutup.add_widget(Label(text=dict['qu_title'],font_size=30,font_name="DejaVuSans.ttf",halign='right',size_hint_y=0.2,color= [1, 0, 1, 1]))
    #     layoutup.add_widget(Label(text=dict['qu_description'],font_name="DejaVuSans.ttf",font_size=16,halign='right'))
    #
    #     q_counter=0
    #     for ques in dict['ques']:
    #         layout.add_widget(BoxLayout(size_hint_x=0.05))
    #         q_counter+=1
    #         if q_counter==1:
    #             for ans in dict['ans']:
    #                 print(ans)
    #                 layout.add_widget(Label(size_hint_x=0.1,text=dict['ans'][ans],font_name="DejaVuSans.ttf",halign='right'))
    #             layout.add_widget(Label(text=dict['questions'],font_name="DejaVuSans.ttf",halign='right',orientation='vertical'))
    #             layout.add_widget(BoxLayout(size_hint_x=0.1))
    #
    #         for ans in dict['ans']:
    #             ab = AnswerButton(size_hint_x=0.15,text="", group=str(q_counter),)
    #             ab.question = ques
    #             ab.answer = ans
    #             ab.form = self
    #             layout.add_widget(ab)
    #
    #         #CHECK ID AND KEEP THE CLICK VALUE
    #         layout.add_widget(Label(halign='right',text=dict['ques'][ques],font_name="DejaVuSans.ttf",orientation='vertical'))
    #
    #     layoutup.add_widget(layout)
    #     layoutup.add_widget(BoxLayout())
    #     layoutbuttons = BoxLayout(size_hint_y=0.2)
    #
    #     layoutbuttons.add_widget(Button(on_press=partial(print, self.answers),background_color= [1, 0, 1, 1],text=dict['next_button'],font_size=20,font_name="DejaVuSans.ttf",halign='right'))
    #     layoutbuttons.add_widget(BoxLayout(size_hint_x=0.2))
    #     layoutbuttons.add_widget(Button(background_color= [1, 0, 1, 1],text=dict['prev_button'],font_size=20,font_name="DejaVuSans.ttf",halign='right'))
    #
    #     layoutup.add_widget(layoutbuttons)
    #     self.add_widget(layoutup)
    #
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def prt(self, result, *args):
        print(result.id)

