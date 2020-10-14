from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivymd.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from contact_class.funtions_contact import build_contact


class CustomThreeLineAvatarIconListItem(ThreeLineAvatarIconListItem):
    source_img = StringProperty()
    name_icon = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()


class NewContactEntity(BoxLayout):
     def __init__(self):
        super(NewContactEntity, self).__init__()

     def check_input(self):
        result = build_contact(self.data_input.text)
        print(result)

class Contacts(BoxLayout):
    def __init__(self):
        super(Contacts, self).__init__()
        data = []
        if data:
            instance_contact = ContactList(self)
        else:
            instance_contact = NewContact()

        self.orientation = 'vertical'
        self.carousel_contacts.add_widget(instance_contact)
        self.carousel_contacts.load_slide(instance_contact)

    def back_to_subscriptions(self):
        self.parent.parent.current = 'subscriptions'


class NewContact(BoxLayout):
    def __init__(self):
        super(NewContact, self).__init__()
        self.load_fields_entity()

    def load_fields_entity(self):
        self.container_newContact.clear_widgets()
        self.container_newContact.add_widget(NewContactEntity())

    def load_fields_wapp(self):
        self.container_newContact.clear_widgets()


class ContactList(BoxLayout):
    def __init__(self, mainwind):
        super(ContactList, self).__init__()
        self.mainwind = mainwind
        self.data_tk = []

    def open_new_contact(self):
        print("open_new_contact")
        create_new = True

        for i in self.mainwind.carousel_contacts.slides:
            if str(type(i)) == "<class 'contact_class.screen_contact.NewContact'>":
                print("go to screen new contacts")
                self.mainwind.carousel_contacts.load_slide(i)
                create_new = False
                break

        if create_new:
            instance_new_contact = NewContact()
            self.mainwind.carousel_contacts.add_widget(instance_new_contact)
            self.mainwind.carousel_contacts.load_slide(instance_new_contact)

    def set_list_contacts(self, text="", search=False):
        print("set_list_contacts")

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
                    if text.lower() in d['secondary_text'].lower() \
                            or text in d['text'].lower() or text in d['tertiary_text'].lower():
                        add_item_in_recycleView(self.data_tk[i])
                        print("hello")
                else:
                    add_item_in_recycleView(self.data_tk[i])
