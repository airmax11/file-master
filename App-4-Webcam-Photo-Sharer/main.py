import time

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from filesharer import Filesharer
from kivy.core.clipboard import Clipboard
import webbrowser


Builder.load_file("frontend.kv")


class CameraScreen(Screen):

    def start(self):
        self.ids.camera.play = True
        self.ids.camera.texture = self.ids.camera._camera.texture
        self.ids.camera.opacity = 1

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera.texture = None
        self.ids.camera.opacity = 0

    def capture(self):
        current_time = time.strftime("%Y%m%d-%H%M%S")
        self.filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = "image_screen"
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    MESSAGE = "Create a Link First"

    def create_link(self):
        filepath = App.get_running_app().root.ids.first_screen.filepath
        filesharer = Filesharer(filepath=filepath)
        self.url = filesharer.share()
        self.ids.link_text.text = self.url
        print(self.url)

    def clipboard_copy(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link_text.text = self.MESSAGE

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link_text.text = self.MESSAGE

    def return_to_widget(self):
        self.manager.current = "first_screen"
        self.ids.link_text.text = ''


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()