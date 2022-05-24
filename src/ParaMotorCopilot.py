# -*- coding: utf-8 -*-ç

"""
Paramotor Copilot v0.1
"""

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy_garden.mapview import MapView, MapMarker

class MainScreen(FloatLayout):
    
    def __init__(self, **kwargs):
        
        super(MainScreen, self).__init__(**kwargs)
        self.map = MapView(zoom=10, lat=34, lon=-4)
        marker1 = MapMarker(lon=50.6394, lat=3.057)   
        marker2 = MapMarker(lon=-33.867, lat=51.206)  
        self.map.add_marker(marker1)
        self.map.add_marker(marker2)
        self.add_widget(self.map)
        self.add_widget(Label(text='BETA version',color='red'))
        
class MyApp(App):

    def build(self):
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()