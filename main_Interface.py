from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from entity_class.login import Login
from entity_class.register import Register
from entity_class.mainNavigation import mainNavigation

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
        self.load_kv('kivy_file/register.kv')
        self.load_kv('kivy_file/login.kv')
        self.load_kv('kivy_file/mainNavigation.kv')
        self.load_kv('kivy_file/messageFrame.kv')
        self.load_kv('kivy_file/cardSubscription.kv')
        self.theme_cls.primary_palette = "Green"  # "Purple", "Red"
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.theme_cls.primary_hue = "700"  # "500"
        return MainWid()

    def on_start(self):
        #self.fps_monitor_start()
        pass
    def on_stop(self):
        pass
    def on_pause(self):
        pass
    def on_resume(self):
        pass


if __name__ == "__main__":

    MainApp().run()
