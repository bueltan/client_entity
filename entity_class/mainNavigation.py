
""" mainNavigation """

from datetime import datetime
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from rx import Observable
import multiprocessing
from rx.concurrency import ThreadPoolScheduler
from kivymd.uix.navigationdrawer import NavigationLayout
from database import base
from entity_class.cardSubscription import DataSubscription, CardSubscription
from querries import sub_entity_payload
from ast import literal_eval
from general_functions import functions
from threading import current_thread
from path import dir_language
from new_contact.screen_contact import Contacts
from kivymd.uix.boxlayout import MDBoxLayout

session = base.Session()

with open(dir_language, 'r') as file:
    dict_l = literal_eval(file.read())

dictionary = dict_l['card_subs']

optimal_thread_count = multiprocessing.cpu_count()
poo_scheduler = ThreadPoolScheduler(optimal_thread_count)


class mainNavigation(NavigationLayout):
    dialog = None

    def __init__(self):
        super(mainNavigation, self).__init__()

    def show_screen_contacts(self):
        wid = Screen(name='screen_contact')
        wid.add_widget(Contacts())
        self._screen_manager.add_widget(wid)
        self._screen_manager.current = 'screen_contact'


    def get_subscription(self):
        subscriptions = sub_entity_payload.get_subscritions(self.account_name)
        list_sub = []

        def get_from_where(id_code, entity):
            if id_code == '' or entity:
                return 'entity'
            else: return 'whatsapp'
        origen = {}

        for sub in subscriptions:
            subscription = sub['node']['source']
            nodes_result = functions.get_nodes(subscription)
            nodes = nodes_result[0]
            if not list_sub :
                come_from = get_from_where(nodes['id_code'], nodes_result[1])
                origen[come_from] = nodes.pop('id_code')
                nodes['origen'] = origen
                list_sub.append(nodes)
            else :
                is_in_list_sub = False
                for j in list_sub:
                    if nodes['node2'] == j['node2'] and \
                       nodes['node3'] == j['node3'] and nodes['node4'] == j['node4']:
                       come_from = get_from_where(nodes['id_code'], nodes_result[1])
                       is_in_list_sub = True
                       j['origen'][come_from] = nodes['id_code']
                       break
                    else:
                        pass
                if not is_in_list_sub:
                    come_from = get_from_where(nodes['id_code'], nodes_result[1])
                    nodes['origen'] = {come_from: nodes.pop('id_code')}
                    list_sub.append(nodes)

        return list_sub

    def create_subscriptions(self, **kwargs):
        self.account_id = kwargs.get('account_id')
        self.account_name = kwargs.get('account_name')
        self.list_sub = self.get_subscription()
        self.data_subscriptions = []
        self.index = 0

        Observable.from_(self.list_sub) \
            .map(lambda i: DataSubscription(self.account_id, self.account_name, **i)) \
            .map(lambda e: self.data_subscriptions.append(e))\
            .subscribe_on(poo_scheduler)\
            .subscribe(on_next = lambda s: self.load_next(),
                       on_completed = lambda: print(datetime.now().time()))

    def load_next(self):
        self.event = Clock.schedule_once(self.build_card_subscription, -1)

    def build_card_subscription(self, dt):
        card_sub = CardSubscription(**self.data_subscriptions[self.index].data_tk_sub)
        self.container.add_widget(card_sub)
        self.index += 1








