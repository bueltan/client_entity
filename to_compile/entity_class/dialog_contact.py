from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.carousel import Carousel
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDIconButton
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFloatingActionButton
from kivymd.icon_definitions import md_icons
from kivy.properties import StringProperty
from kivymd.uix.textfield import MDTextField

KV = '''
#:import images_path kivymd.images_path


<CustomThreeLineAvatarIconListItem>:
    source_img : ""
    name_icon : ""
    ImageLeftWidget:
        source: root.source_img

    IconRightWidget:
        icon: root.name_icon
        on_release: print("hello")

<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)

<NewContact>:
    orientation: 'vertical'
    spacing: dp(5)
    size_hint: 1,1
    check_1:check_1
    check_2:check_2
    container_newContact:container_newContact
    BoxLayout:
        size_hint_Y:None
        height:35 
        orientation: 'horizontal'
        Check:
            id:check_1
            active: True
            pos_hint:{'center_y': 0.5} 
            on_state: if self.active : root.load_fields_entity()
        MDTextButton:
            pos_hint: {'center_x': .5, 'center_y': .5}
            text: "Entity contact"
            on_release: root.ids.check_1.active = True
        Check:
            id:check_2
            pos_hint:{'center_y': 0.5} 
            on_state: if self.active : root.load_fields_wapp()
        MDTextButton:
            pos_hint: {'center_x': .5, 'center_y': .5}
            text: "Whatsapp contact"
            on_release: root.ids.check_2.active = True
    BoxLayout:
        id:container_newContact
        size_hint_y: None
        height: root.height -35
        orientation:'vertical'

<Content>:
    orientation: 'vertical'
    spacing: dp(5)
    padding: dp(10)
    new_contact_btn:new_contact_btn
    search_box:search_box
    BoxLayout:
        id:search_box
        pos_hint:{'top': 1} 
        size_hint_y: None
        height: self.minimum_height
        MDIconButton:
            icon: 'magnify'
        MDTextField:
            id: search_field
            hint_text: 'Search contacts'
            on_text: root.set_list_md_icons(self.text, True)

    RelativeLayout:
        pos_hint:{'top': .9} 
        size_hint_y : None
        height: root.height - root.search_box.height
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
        MDFloatingActionButton:
            id: new_contact_btn
            pos: root.width /2 -25, 10
            icon:'plus'
            md_bg_color: self.theme_cls.primary_color
            on_release: root.open_new_contact()


FloatLayout:
    MDFlatButton:
        text: "CONTACTS"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release:app.show_dialog_contacts()

'''
class NewContact(BoxLayout):
    def __init__(self):
        super(NewContact, self).__init__()
        self.load_fields_entity()

    def load_fields_entity(self):
        self.container_newContact.clear_widgets()
        anchor_box = AnchorLayout(anchor_x='center', anchor_y='center')
        anchor_box_btn_add = AnchorLayout(anchor_x='center', anchor_y='center')
        anchor_box_btn_close = AnchorLayout(anchor_x='center', anchor_y='center')
        box_button = BoxLayout(orientation="vertical")

        anchor_box.add_widget(MDTextField(halign='center', hint_text='Account or entity', helper_text="hello",
                                          helper_text_mode="persistent"))
        anchor_box_btn_add.add_widget(MDRaisedButton(text="Add to contacts", on_release=lambda x: print("add")))
        anchor_box_btn_close.add_widget(MDIconButton(icon="close"))

        box_button.add_widget(anchor_box_btn_add)
        box_button.add_widget(anchor_box_btn_close)

        self.container_newContact.add_widget(anchor_box)
        self.container_newContact.add_widget(box_button)

    def load_fields_wapp(self):
        self.container_newContact.clear_widgets()


class CustomThreeLineAvatarIconListItem(ThreeLineAvatarIconListItem):
    source_img = StringProperty()
    name_icon = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()


class CarouselContacts(Carousel):

    def __init__(self, data=None, new_contact=None):
        super(CarouselContacts, self).__init__()
        self.direction = 'left'
        self.size_hint_y = None
        self.height = 500
        if data:
            self.add_widget(Content(data=data))


class Content(BoxLayout):

    def __init__(self, data):
        super(Content, self).__init__()
        self.data_tk = data

    def open_new_contact(self):
        create_new = True
        for i in self.parent.parent.slides:
            if str(type(i)) == "<class '__main__.NewContact'>":
                self.parent.parent.load_slide(i)
                create_new = False
                break
        if create_new:
            instance_new_contact = NewContact()
            self.parent.parent.add_widget(instance_new_contact)
            self.parent.parent.load_slide(instance_new_contact)

    def set_list_md_icons(self, text="", search=False):

        def find_index(list=self.ids.rv.data, name=None):
            if name:
                for i, j in enumerate(list):
                    a = (j['name'] == name)
                    if a:
                        return i

        def edit_selected(id_tk, new_text):
            i = find_index(name=id_tk)
            if self.ids.rv.data:
                self.ids.rv.data[i]['secondary_text'] = new_text
                self.ids.rv.refresh_from_data()

        def add_item_in_recycleView(data_tk=self.data_tk):
            self.ids.rv.data.append(
                {
                    "viewclass": data_tk['viewclass'],
                    "source_img": data_tk['source_img'],
                    "name_icon": data_tk['name_icon'],
                    "text": data_tk['text'],
                    "secondary_text": data_tk['secondary_text'],
                    "tertiary_text": data_tk['tertiary_text'],
                    "callback": lambda x: x,
                    "name": data_tk['name'],
                    # "on_release": lambda :edit_selected(id_tk=data_tk['id_tk'], new_text= data['id_tk'])

                }
            )

        self.ids.rv.data = []
        if self.data_tk:
            for i, d in enumerate(self.data_tk):
                if search:
                    if (text).lower() in d['secondary_text'].lower() \
                            or text in d['text'].lower() or text in d['tertiary_text'].lower():
                        add_item_in_recycleView(self.data_tk[i])
                else:
                    add_item_in_recycleView(self.data_tk[i])


class Example(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def noneDialog(self, *args):
        self.dialog = None

    def show_dialog_contacts(self):
        data = [{'name': "0101111101", 'viewclass': "CustomThreeLineAvatarIconListItem", 'text': "Denis",
                 'secondary_text': "hola ", 'name_icon': "cog", 'tertiary_text': "Entity", 'source_img': 'user-1.png'},
                {'name': "0101111101", 'viewclass': "CustomThreeLineAvatarIconListItem", 'text': "Denis",
                 'secondary_text': "hola ", 'name_icon': "cog", 'tertiary_text': "Entity", 'source_img': 'user-1.png'},
                {'name': "0101111101", 'viewclass': "CustomThreeLineAvatarIconListItem", 'text': "Denis",
                 'secondary_text': "hola ", 'name_icon': "cog", 'tertiary_text': "Entity", 'source_img': 'user-1.png'},
                {'name': "0101111101", 'viewclass': "CustomThreeLineAvatarIconListItem", 'text': "Denis",
                 'secondary_text': "hola ", 'name_icon': "cog", 'tertiary_text': "Entity", 'source_img': 'user-1.png'}]

        if not self.dialog:
            self.dialog = MDDialog(
                radius=[20, 7, 20, 7],
                title="Contacts",
                type="custom",
                content_cls=CarouselContacts(data),
                on_dismiss=self.noneDialog,

            )

            self.dialog.open()

    def dialog_close(self, *args):
        self.dialog.dismiss(force=True)
        self.dialog = None


Example().run()