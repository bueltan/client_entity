
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.carousel import Carousel
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivymd.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivymd.uix.textfield import MDTextField

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

    def __init__(self, data=None, new_contact=None, size=None):
        super(CarouselContacts, self).__init__()
        self.direction = 'left'
        self.add_widget(Content(data=data))


class Content(BoxLayout):
    def __init__(self, data):
        super(Content, self).__init__()
        self.data_tk = data

    def open_new_contact(self):
        create_new = True
        if self.parent:
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

                })

        self.ids.rv.data = []
        if self.data_tk:
            for i, d in enumerate(self.data_tk):
                if search:
                    if (text).lower() in d['secondary_text'].lower() \
                            or text in d['text'].lower() or text in d['tertiary_text'].lower():
                        add_item_in_recycleView(self.data_tk[i])
                else:
                    add_item_in_recycleView(self.data_tk[i])
