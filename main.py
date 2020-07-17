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
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.dropdown import DropDown


# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'bg3.jpg'
                   
            
            
    search: last_name
    
    orientation: "vertical"
    BoxLayout:
        height: "60dp"
        size_hint_y: None
        padding: 10
        pos: 0,300
        
        TextInput:
            id: last_name
            size_hint_x: 40
            multiline: False
            readonly: False
            foreground_color: [1, 1, 1, 1]
            background_color: (0,0,0,0.3)
                                    
            
        Button:
            text: "Search"
            size_hint_x: 25
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'settings'
                root.fetch_searchterm()


<SettingsScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'bg2.jpg'
            
    orientation: "vertical"
    
    BoxLayout: 
        padding: 10
        
        TextInput:
            id: outbox
            readonly: True
            
            
        Button: 
            text: "Go Back" 
            height: "60dp"
            background_color : 1, 1, 1, 1 
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'menu' 
        
<CustomDropDown>:

    Button:
        id: btn
        text: 'Press'
        on_release: dropdown.open(self)
        size_hint_y: None
        height: '48dp'

    DropDown:

        id: dropdown
        on_parent: self.dismiss()
        on_select: btn.text = '{}'.format(args[1])

        Button:
            text: 'First Item'
            size_hint_y: None
            height: '48dp'
            on_release: dropdown.select('First Item')

        Label:
            text: 'Second Item'
            size_hint_y: None
            height: '48dp'

        Button:
            text: 'Third Item'
            size_hint_y: None
            height: '48dp'
            on_release: dropdown.select('Third Item')
            
""")


#text: outbox.text = searchbox.text

class MenuScreen(Screen):
    #t = TextInput(font_size=150)
    search = ObjectProperty()
    searchterm = StringProperty('')
    
    def fetch_searchterm(self):
            self.searchterm = self.search.text
            print(self.searchterm)
    
    abc = "avengers"
    
    pass


class SettingsScreen(Screen):
    pass


#class CustomDropDown(DropDown): 
#    pass


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
#sm.add_widget(CustomDropDown(name='DropDown'))



class TestApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()