# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 20:01:06 2020

@author: ishan.m.jain
"""
#https://github.com/IgorRidanovic/kivy-radio-button/blob/master/radiobutton.kv


# -*- coding: cp1252 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty, ListProperty
from kivy.uix.dropdown import DropDown
from kivy.uix.recycleview import RecycleView

from digger import WebDigger
dg = WebDigger()


class MenuScreen(Screen):
    choice = StringProperty(' ')

    def setChoice(self, fileType):
        self.choice = fileType
        print("Button : ",self.choice)


class SettingsScreen(Screen):
    # results = ObjectProperty()
    # def __init__(self, **kwargs):
    # 	super(SettingsScreen, self).__init__(**kwargs)
    # 	self.rv.data = []

    res = ListProperty()

    def fetch_searchterm(self, searchTerm, fileType):
        print(searchTerm,' ',fileType)
        urls = dg.startFunc(searchTerm, fileType)
        # res_urls = str(urls)
        # res_urls = res_urls.replace(",",",\n")
        # self.results.text = res_urls
        # print(urls)
        [self.res.append({
            'text': url, 
            'readonly': True, 
            'foreground_color': [1, 1, 1, 1], 
            'background_color': (0,0,0,0.3),
            'size_hint_x':0.8,
            }) for url in urls]
        # print(self.res)
    pass


class RadioButton(Widget):
    pass

class ScreenManagement(ScreenManager):
    pass

class TestApp(App):
    def build(self):
        return ScreenManagement()

if __name__ == '__main__':
    TestApp().run()