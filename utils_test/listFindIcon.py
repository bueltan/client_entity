from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import BoxLayout
from kivymd.icon_definitions import md_icons
from kivymd.app import MDApp

from kivymd.uix.list import ThreeLineAvatarIconListItem


Builder.load_string(
    '''
#:import images_path kivymd.images_path


<CustomThreeLineAvatarIconListItem>:
    source : ""
    ImageLeftWidget:
        source: root.source

     
    IconRightWidget:
        icon: "bell"
        theme_text_color:"Custom"
        text_color: [1,.8,0,1]
        on_release: print("hello")
   
        
<PreviousMDIcons>:

    BoxLayout:
        orientation: 'vertical'
        spacing: dp(10)
        padding: dp(20)

        BoxLayout:
            size_hint_y: None
            height: self.minimum_height

            MDIconButton:
                icon: 'magnify'
    
            MDTextField:
                id: search_field
                hint_text: 'Search icon'
                on_text: root.set_list_md_icons(self.text, True)

        RecycleView:
            id: rv
            key_viewclass: 'viewclass'
            key_size: 'height'

            RecycleBoxLayout:
                default_size: None, dp(90)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
'''
)


class CustomThreeLineAvatarIconListItem(ThreeLineAvatarIconListItem):
    source_img = StringProperty()
    name_icon = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()




class PreviousMDIcons(Screen):

    def set_list_md_icons(self, text="", search=False):

        def find_index(list = self.ids.rv.data, name=None ):
            if name :
                for i,j in enumerate(list):
                    a = (j['name'] == name)
                    if a:
                        return i

        def edit_selected(id_tk, new_text):
            i = find_index(name= id_tk)
            if self.ids.rv.data:
                self.ids.rv.data[i]['text'] = new_text
                self.ids.rv.refresh_from_data()

        def add_icon_item(name_icon):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomThreeLineAvatarIconListItem",
                    "source": 'user-1.png',
                    "text": name_icon,
                    "secondary_text": name_icon,
                    "tertiary_text": "go denis!",
                    "callback": lambda x: x,
                    "name": name_icon,
                    "on_release": lambda :edit_selected(id_tk=name_icon, new_text= name_icon + '- edited')
                }
            )


        self.ids.rv.data = []
        for name_icon in md_icons.keys():
            if search:
                if text in name_icon :
                    add_icon_item(name_icon)
            else:
                add_icon_item(name_icon)


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = PreviousMDIcons()

    def build(self):
        return self.screen

    def on_start(self):
        self.screen.set_list_md_icons()


MainApp().run()