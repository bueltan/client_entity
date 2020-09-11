from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_class.login import Login
from kivy_class.register import Register
from kivy_class.afterLogin import AfterLogin


class MainWid(ScreenManager):
    def __init__(self, **kwargs):
        super(MainWid, self).__init__()
        self.Login = Login(self)
        self.Register = Register(self)
        self.After_login = AfterLogin()

        wid = Screen(name='loginScreen')
        wid.add_widget(self.Login)
        self.add_widget(wid)

        wid = Screen(name='RegisterScreen')
        wid.add_widget(self.Register)
        self.add_widget(wid)

        wid = Screen(name='after_login_screen')
        wid.add_widget(self.After_login)
        self.add_widget(wid)

        self.goto_register()
        self.goto_login()

    def goto_login(self):
        self.current = 'loginScreen'

    def goto_register(self):
        self.current = 'RegisterScreen'

    def goto_after_login(self, **kwargs):
        print("goto_after_login")
        self.current = 'after_login_screen'

        self.After_login.load_card_sub(**kwargs)
        self.After_login.load_drawer()


class MainApp(MDApp):
    def build(self):
        self.load_kv('kivy_file/wide_screen/register.kv')
        self.load_kv('kivy_file/wide_screen/login.kv')
        self.load_kv('kivy_file/wide_screen/afterLogin.kv')
        self.load_kv('kivy_file/wide_screen/message.kv')
        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red"
        self.theme_cls.theme_style = "Light"  # "Light"
        self.theme_cls.primary_hue = "500"  # "500"
        return MainWid()


if __name__ == "__main__":
    MainApp().run()
