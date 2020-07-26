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

from kivy.uix.dropdown import DropDown 
# another way used to run kivy app  
#from kivy.base import runTouchApp 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner, SpinnerOption 



from digger import WebDigger
dg = WebDigger()


class MenuScreen(Screen):
    choice = StringProperty(' ')
    #CustomDropDown = CustomDropDown()
    def spinner_clicked(self, value): 
        print("Language selected is " + value)
        self.setChoice(value)

    def setChoice(self, fileType):
        #self.choice = fileType
        if fileType == "Video":
            self.choice = "1"
        elif fileType == "Audio":
            self.choice = "2"
        elif fileType == "Document":
            self.choice = "3"
        elif fileType == "Software":
            self.choice = "4"
        elif fileType == "Image":
            self.choice = "5"
         
        print("Button : ",self.choice)
        
    
    pass



class SettingsScreen(Screen):
    

    res = ListProperty()

    def fetch_searchterm(self, searchTerm, fileType):
        print(searchTerm,' ',fileType)
        urls = dg.startFunc(searchTerm, fileType)
        
        [self.res.append({
            'text': url, 
            'readonly': True, 
            'foreground_color': [1, 1, 1, 1], 
            'background_color': (0,0,0,0.3),
            'size_hint_x':0.8,
            }) for url in urls]
    pass


#class SpinnerOptions(SpinnerOption):
#    def __init__(self, **kwargs):
#        super(SpinnerOptions, self).__init__(**kwargs)
#        self.background_normal = ''
#        self.background_color = [0, 0, 1, 1]    # blue colour



class ScreenManagement(ScreenManager):
    pass

class TestApp(App):
    title = 'WebDigger'
    def build(self):
        return ScreenManagement()

if __name__ == '__main__':
    TestApp().run()