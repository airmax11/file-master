from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from filesharer import Filesharer

import requests

Builder.load_file("frontend.kv")


class CameraScreen(Screen):

    def start(self):
        self.ids.camera.play = True

    def stop(self):
        pass

    def capture(self):
        pass


class ImageScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()