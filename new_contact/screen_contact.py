from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivymd.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from .payload_contact import check_if_exist


class CustomThreeLineAvatarIconListItem(ThreeLineAvatarIconListItem):
    source_img = StringProperty()
    name_icon = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()


class newContactEntity(BoxLayout):
     def __init__(self):
        super(newContactEntity, self).__init__()

     def check_and_get(self):
        data = self.data_input.text
        data_contact = False
        if data:
            if data[0] == '@' and len(data) >= 6 :
                """ the data is entity, check for nodes"""
                data_contact = check_if_exist(data)
                print(" the data is entity, check for nodes")
            else:
                if data[0] != '.' and len(data) >= 5:
                    print(data.find("@") )
                    if data.find("@") != -1 and data.find(".") != 1 and data.find("#") == -1:
                        """ the data is email get account """
                        #data_contact = chek_for_email
                        print(" the data is email get account ")
                    elif data.find("@") == -1 and data.find(".") == -1:
                        """ the data is account name but without "." """
                        # atach "." and data_contact = get_account
                        print(" the data is account name but without ")
                    else:
                        print(" the data is not correct")
                        data_contact = False

                elif data.find("@") == -1 and len(data) >= 6:
                    #data_contact = get_account
                    print(" the data is account name ")
                else:
                    print(" the data is not correct ")
                    data_contact = False
        else:
            print("the data is enty")


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
        self.container_newContact.add_widget(newContactEntity())

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
            if str(type(i)) == "<class 'new_contact.screen_contact.NewContact'>":
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
