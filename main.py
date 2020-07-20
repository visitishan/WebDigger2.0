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
    
    RelativeLayout:
        size_hint_y: None
        padding: 10
        
        TextInput:
            id: last_name
            size_hint_x: 0.75
            size_hint_y: 0.4
            multiline: False
            readonly: False
            foreground_color: [1, 1, 1, 1]
            background_color: (0,0,0,0.3)
            pos_hint: {"x":0.005, "y":3}
            
                                    
            
        Button:
            text: "Search"
            size_hint_x: 0.25
            size_hint_y: 0.4
            pos_hint: {"right":0.995, "y":3}
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'settings'
                root.fetch_searchterm()
        
        
        CheckBox:
			id: rbutton1
			group: 'radio button'
			size_hint_x: 0.05
            pos_hint: {"x":0.02, "y":2.4}
            
        Label:
            size_hint_x: None
            text: "Video"
            pos_hint: {"x":0.05, "y":2.4}
            color: 0,0,0,1


		CheckBox:
			id: rbutton2
			group: 'radio button'
            size_hint_x: 0.05
            pos_hint: {"x":0.15, "y":2.4}
        Label:
            size_hint_x: None
            text: "Audio"
            pos_hint: {"x":0.17, "y":2.4}
            color: 0,0,0,1
        
        CheckBox:
			id: rbutton3
			group: 'radio button'
            size_hint_x: 0.05
            pos_hint: {"x":0.27, "y":2.4}
        Label:
            size_hint_x: None
            text: "Document"
            pos_hint: {"x":0.30, "y":2.4}
            color: 0,0,0,1
        
        CheckBox:
			id: rbutton4
			group: 'radio button'
            size_hint_x: 0.05
            pos_hint: {"x":0.40, "y":2.4}
        Label:
            size_hint_x: None
            text: "Software"
            pos_hint: {"x":0.42, "y":2.4}
            color: 0,0,0,1
        
        CheckBox:
			id: rbutton5
			group: 'radio button'
            size_hint_x: 0.05
            pos_hint: {"x":0.52, "y":2.4}
        Label:
            size_hint_x: None
            text: "Image"
            pos_hint: {"x":0.54, "y":2.4}
            color: 0,0,0,1

        


<SettingsScreen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'bg4.jpg'
            
    orientation: "vertical"
    
    RelativeLayout: 
        padding: 10
        
        TextInput:
            id: outbox
            readonly: True
            text: 'asdlf'
            size_hint_x: 0.8
            size_hint_y: 0.97
            pos_hint: {"x":0.005, "y":0}
            foreground_color: [1, 1, 1, 1]
            background_color: (0,0,0,0.3)
            
            
        Button: 
            text: "Go Back" 
            background_color : 1, 1, 1, 1 
            size_hint_x: 0.1
            size_hint_y: 0.4
            pos_hint: {"right":0.995, "y":0}
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'menu' 
        

            
""")

#height: "60dp"
#        size_hint_y: None
#        padding: 10
#        pos: 0,300
#        cols: 2
        
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



class RadioButton(Widget):
	# State labels
	slabel1 = StringProperty()
	slabel2 = StringProperty()

	def savedstate(self):
		# Here we can retrieve user saved radio button state if one exists
		# Assign optional label values
		self.slabel1 = 'On'
		self.slabel2 = 'Off'
		return ['down', 'normal']

	def switchstate1(self):
		# Switch radio button 1 on and process event trigger
		# Force 'down' state to avoid deselecting all radio buttons (Kivy thing)
		self.ids.rbutton1.state = 'down'
		# Update optional label values
		self.slabel1 = 'on'
		self.slabel2 = 'off'
		print(self.ids.rbutton1.state, self.ids.rbutton2.state)

	def switchstate2(self):
		# Switch radio button 2 on and process event trigger
		# Force 'down' state to avoid deselecting all radio buttons (Kivy thing)
		self.ids.rbutton2.state = 'down'
		# Update optional label values
		self.slabel1 = 'off'
		self.slabel2 = 'on'
		print(self.ids.rbutton1.state, self.ids.rbutton2.state)


#class CustomDropDown(DropDown): 
#    pass


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
#sm.add_widget(CustomDropDown(name='DropDown'))



class TestApp(App):
    def build(self):
        #print(self.)
        return sm

if __name__ == '__main__':
    TestApp().run()