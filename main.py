# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 20:01:06 2020

@author: ishan.m.jain
"""

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

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'bg2.jpg'
                   
    
    orientation: "vertical"
    BoxLayout:
        height: "60dp"
        size_hint_y: None
        padding: 10
        pos: 0,300
        
        TextInput:
            size_hint_x: 40
            multiline: False
            readonly: False
            foreground_color: [1, 1, 1, 1]
            background_color: (0,0,0,0.3)
            
            
        Button:
            text: "Search"
            size_hint_x: 25

""")

#FloatLayout:
#        Button:
#            text: "LEARN"
#            font_size: '50sp'
#            pos: 60, 180
#            size_hint: .4, .4


class MenuScreen(Screen):
    pass


#class SettingsScreen(Screen):
#    pass


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(MenuScreen(name='menu'))
#sm.add_widget(SettingsScreen(name='settings'))



class TestApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()