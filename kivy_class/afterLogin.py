from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.card import MDCard
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.list import ThreeLineIconListItem
from querries import after_login_payload, subscriptions
from querries.message_database import get_msg_local_db, get_oneMsg_local_db
from kivy_class.message import MessageTextFm, MessageImageFm, MessagePlayAudio
from ast import literal_eval
from general_functions import functions
from rx import Observable
from rx.concurrency import ThreadPoolScheduler
import multiprocessing
import requests
import os
from database import base
from database.model_tickets import ModelTickets
from querries.tickets_database import load_tk_in_database
from querries.login_payload import upload_image
from querries.login_database import load_account_from_db, update_account
session = base.Session()



optimal_thread_count = multiprocessing.cpu_count() + 1
poo_scheduler = ThreadPoolScheduler(optimal_thread_count)

with open('./resource_files/language/spanish_after_login.json', 'r') as file:
    dict_l = literal_eval(file.read())

card_sub = dict_l['card_subs']


class CardSubscription(MDCard):
    def __init__(self, **kwargs):
        super(CardSubscription, self).__init__()
        self.title.text = kwargs.get('title')
        self.id = kwargs.get('id')


class ItemTickets(ThreeLineIconListItem):
    def __init__(self, after_login_class, **kwargs) -> object:
        super(ItemTickets, self).__init__()
        self.mainwid = after_login_class
        self.id = kwargs.get('id_tk')
        self.u_id = kwargs.get('id')
        self.text = kwargs.get('name')
        self.secondary_text = kwargs.get('last_msg')
        if kwargs.get('phone_num') is not None:
            self.tertiary_text = kwargs.get('phone_num')

        self.on_release = lambda: self.open_chat(self.id, self.u_id)


    def open_chat(self, id, u_id):
        if self.img_lef.source == './img_profile/default-image.png':
            id_tk = id
            dir_profile = './img_profile/' + id_tk + '.png'
            if os.path.isfile(dir_profile):
                self.img_lef.source = dir_profile
        self.mainwid.open_chat(u_id)
        print(self.mainwid.list_message.id)


def get_profile_img(payload):
    tk_id = payload['id_tk']
    try:
        response = requests.get(payload['url'])
        dir_profile = "./img_profile/" + tk_id + ".png"
        file = open(dir_profile, "wb")
        file.write(response.content)
        file.close()
    except:
        pass


def get_sub(data):
    if data['id_code'] != 0:
        id_sub = str(data['id_code']) + data['node2'] + data['node3'] + data['node4']
    else:
        id_sub = data['node2'] + data['node3'] + data['node4']
    return id_sub


class AfterLogin(MDBoxLayout):
    def __init__(self):
        super(AfterLogin, self).__init__()
        self.list_subscription = []
        self.layout = GridLayout(cols=1, spacing=20, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.file_manager = MDFileManager( exit_manager=self.exit_manager,
                                      select_path=self.select_path)
        path = '/'
        self.navDrawer.open_file.on_release = lambda: self.file_manager.show(path)

        self.data_account = load_account_from_db()


    def select_path(self, path):

        file_name = str(self.data_account.id) + ".png"
        dest_file = './img_account/'+file_name
        functions.copy(path, dest_file)
        upload_image('file_name', path)
        data = self.data_account
        data.avatar = dest_file
        update_account(data)
        self.navDrawer.avatar.source = path

        self.exit_manager()

    def exit_manager(self, *args):

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True

    def open_chat(self, id):
        self.screenManager.current = 'message'
        messages = get_msg_local_db(id)
        self.layout.clear_widgets()
        self.list_message.clear_widgets()
        for msg in messages:
            self.load_msg(msg)
        self.list_message.add_widget(self.layout)
        self.list_message.id = str(id)

    def back_subscriptions(self):
        self.screenManager.current = 'subscriptions'

    def callback(self, _id, data):
        print("callback")
        data = data['payload']['data']['getTK']
        data = literal_eval(data)
        id_tk = data['id_tk']
        id = data['id']
        data_sub = {'node': data}
        load_tk_in_database([data_sub])
        #self.set_msg_in_widget()

        if id_tk in self.ids:
            id_sub = get_sub(data)
            for i in self.ids[id_sub].list_tickets.children:
                if i.id == id_tk:
                    last_id_msg = data['last_id_msg']
                    last_msg = after_login_payload.getLastMsg(last_id_msg)
                    msg = functions.show_last_msg(last_msg, card_sub)
                    i.secondary_text = msg
                    break
            else:
                self.create_tk(data, sub="")

        else:
            self.create_tk(data, sub="")

    def set_msg_in_widget(self,id, id_msg):
        if self.list_message.id == id:
            message = get_oneMsg_local_db(id_msg)
            self.load_msg(message)

    def subscription_nodes(self, variables):
        id_code = variables['id_code']
        node_2 = variables['node2']
        node_3 = variables['node3']
        node_4 = variables['node4']

        variables = {'id_code': id_code, 'node_2': node_2, 'node_3': node_3, 'node_4': node_4}

        sub = subscriptions.subscriptions(self).getTK(variables)

    def load_drawer(self):
        if self.data_account is not None:
            if self.data_account.avatar:
                dir_profile_img = self.data_account.avatar
                self.navDrawer.avatar.source = dir_profile_img
            if self.data_account.name:
                person_name = self.data_account.name
                self.navDrawer.namePerson.text = person_name
            if self.data_account.idName:
                id_name = self.data_account.idName
                self.navDrawer.idName.text = id_name
            if self.data_account.email:
                email = self.data_account.email
                self.navDrawer.email.text = email




    def load_card_sub(self, account_name):
        subscriptions = after_login_payload.get_subscritions(account_name)
        for sub in subscriptions:
            subscription = sub['node']['source']
            self.list_subscription.append(subscription)
            self.scroll_view.cols = len(subscriptions)
            nodes = functions.get_nodes(subscription)

            after_login_payload.get_tickets(nodes)

            self.card_s = CardSubscription(title="  " + card_sub['title'] + subscription,
                                           id=subscription)

            self.scroll_view.add_widget(self.card_s)
            self.ids[subscription] = self.card_s
            tickets = session.query(ModelTickets).filter_by(id_code=str(nodes['id_code']), node2=nodes['node2'],
                                                            node3=nodes['node3'], node4=nodes['node4'])

            if tickets is not None:
                for tk in tickets:
                    data = {'id': tk.id, 'id_tk': tk.id_tk, 'name': tk.name,
                            'image': tk.image, 'last_id_msg': tk.last_id_msg,
                            'phone': tk.phone}

                    self.create_tk(data, subscription)

            self.subscription_nodes(nodes)

    def create_tk(self, data, sub):
        id = data['id']
        id_tk = data['id_tk']
        tk_name = data['name']
        last_id_msg = data['last_id_msg']
        phone = data['phone']
        last_msg = after_login_payload.getLastMsg(last_id_msg)
        msg = functions.show_last_msg(last_msg, card_sub)
        if sub == "":
            id_sub = get_sub(data)
        else:
            id_sub = sub
        item_tk = ItemTickets(self, id=id, id_tk=id_tk, name=tk_name, last_msg=msg, phone_num=phone)
        self.ids[id_sub].list_tickets.add_widget(item_tk)
        self.ids[id_tk] = item_tk
        image_url = data['image']
        dir_profile = "./img_profile/" + id_tk + ".png"
        save_profile = {'url': image_url, 'id_tk': id_tk}

        if os.path.isfile(dir_profile) and sub != "":
            item_tk.img_lef.source = dir_profile

        if not os.path.isfile(dir_profile):
            Observable.of(save_profile) \
                .map(lambda i: get_profile_img(i)) \
                .subscribe_on(poo_scheduler).subscribe()

        return item_tk

    def delete_tk(self, id_tk):
        for sub in self.list_subscription:
            if self.ids[id_tk] in self.ids[sub].list_tickets.children:
                self.ids[sub].list_tickets.remove_widget(self.ids[id_tk])
                break

    def load_msg(self, msg):
        if not msg.fromMe:
            orientation = 'left'

        else:
            orientation = 'right'

        if msg.type == "text":
            length = len(msg.text.split('\n'))

            if length > 1:
                line = 20 * length
            else:
                line = 0

            text = functions.format_text(msg.text)
            len_sentence = functions.count_lent_sentence(text)

            layoutAn = AnchorLayout(anchor_x=orientation, anchor_y='center', size_hint_y=None, height=50 + line)
            message = MessageTextFm(self, msg_text=text, size_hint_y=None, size_hint_x=None,
                                    width=85 + (8 * len_sentence),
                                    height=50 + line, orientation=orientation)

        if msg.type == "image":

            if msg.caption != "":
                caption = msg.caption
            else:
                caption = ""

            extension = functions.get_extension(msg.type)

            dir = "./media_file/" + msg.id + extension

            if not os.path.isfile(dir):
                dir = "file_not_exist"

            size_img = functions.get_resolution_img(msg.url)
            new_size = functions.get_height_img(size_img[0], size_img[1], 500)

            layoutAn = AnchorLayout(anchor_x=orientation, anchor_y='center', size_hint_y=None, height=new_size[1])

            message = MessageImageFm(self, size_hint_y=None,
                                     height=new_size[1], size_hint_x=None, width=new_size[0], orientation=orientation,
                                     source=dir, caption=caption, url=msg.url, id = msg.id)


            if msg.type == "audio":

                layoutAn = AnchorLayout(anchor_x=orientation, anchor_y='center', size_hint_y=None, height=150)
                message = MessagePlayAudio(self, size_hint_y=None,
                                         height=150, size_hint_x=None, width=450,
                                         orientation=orientation,
                                         source=dir, caption=caption, url=msg.url, id=msg.id)


        layoutAn.add_widget(message)
        self.layout.add_widget(layoutAn)