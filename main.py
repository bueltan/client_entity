import os
import sys
from pathlib import Path
from kivy.loader import Loader

from kivy.core.window import Window
from kivymd import images_path
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from entity_class.login import Login
from entity_class.register import Register
from entity_class.mainNavigation import mainNavigation

os.environ["KIVY_PROFILE_LANG"] = "1"

if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["ENTITY_CLIENT_ROOT"] = sys._MEIPASS

else:
    sys.path.append(os.path.abspath(__file__).split("client_entity")[0])
    os.environ["ENTITY_CLIENT_ROOT"] = str(Path(__file__).parent)

os.environ["ENTITY_CLIENT_ASSETS"] = os.path.join(
    os.environ["ENTITY_CLIENT_ROOT"], f"assets{os.sep}"
)
Window.softinput_mode = "below_target"

class MainWid(ScreenManager):
    def __init__(self, **kwargs):
        super(MainWid, self).__init__()
        self.Login = Login(self)
        self.Register = Register(self)
        self.mainNavigation = mainNavigation()

        wid = Screen(name='loginScreen')
        wid.add_widget(self.Login)
        self.add_widget(wid)

        wid = Screen(name='RegisterScreen')
        wid.add_widget(self.Register)
        self.add_widget(wid)

        wid = Screen(name='mainNavigationScreen')
        wid.add_widget(self.mainNavigation)
        self.add_widget(wid)

        self.goto_login()

    def goto_login(self):
        self.current = 'loginScreen'

    def goto_register(self):
        self.current = 'RegisterScreen'

    def goto_mainNavigation(self, **kwargs):
        self.current = 'mainNavigationScreen'
        self.mainNavigation.create_subscriptions(**kwargs)
        #self.mainNavigation.load_drawer()


class MainApp(MDApp):
    def build(self):
        Window.size = 450, 700
        Loader.loading_image = f"{images_path}transparent.png"
        self.load_kv(f"{os.environ['ENTITY_CLIENT_ROOT']}/kivy_file/register.kv")
        self.load_kv(f"{os.environ['ENTITY_CLIENT_ROOT']}/kivy_file/login.kv")
        self.load_kv(f"{os.environ['ENTITY_CLIENT_ROOT']}/kivy_file/mainNavigation.kv")
        self.load_kv(f"{os.environ['ENTITY_CLIENT_ROOT']}/kivy_file/messageFrame.kv")
        self.load_kv(f"{os.environ['ENTITY_CLIENT_ROOT']}/kivy_file/cardSubscription.kv")

        self.theme_cls.primary_palette = "Green"  # "Purple", "Red"
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.theme_cls.primary_hue = "700"  # "500"
        return MainWid()

    def on_start(self):
        #self.fps_monitor_start()
        return True

    def on_stop(self):
        return True

    def on_pause(self):
        return True

    def on_resume(self):
        return True


if __name__ == "__main__":

    MainApp().run()
