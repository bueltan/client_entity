from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp


class createEntity(MDBoxLayout):
    def __init__(self, **kwargs):
        super(createEntity, self).__init__()

        self.orientation = 'vertical'
        self.toolbar = MDToolbar(title="Entities")
        self.mainBox = MDBoxLayout(size=self.size, orientation='horizontal')

        self.boxNewEntity = AnchorLayout(anchor_x='center', anchor_y='top', size_hint=(1, 1), )
        self.boxTextFieldEntity = MDBoxLayout(size_hint=(.7, .3), orientation='vertical')

        self.boxSecond = AnchorLayout(anchor_x='center', anchor_y='top', size_hint=(1, 1))
        self.label = MDLabel(text="create new entity", size_hint_y=None, height=20)

        self.nameEntityField = MDTextField()
        self.numberWsapp = MDTextField()
        self.boxTextFieldEntity.add_widget(self.label)
        self.boxTextFieldEntity.add_widget(self.entityField)
        self.boxTextFieldEntity.add_widget(self.nameEntityField)
        self.boxNewEntity.add_widget(self.boxTextFieldEntity)

        self.mainBox.add_widget(self.boxNewEntity)
        self.mainBox.add_widget(self.boxSecond)
        self.add_widget(self.toolbar)
        self.add_widget(self.mainBox)


class MainApp(MDApp):
    def build(self):
        self.load_kv('./kivy_file/wide_screen/createEtity.kv')
        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red"
        self.theme_cls.primary_hue = "500"  # "500"
        return createEntity()


if __name__ == "__main__":
    MainApp().run()
