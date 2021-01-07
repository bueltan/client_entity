
""" mainNavigation """

from datetime import datetime
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from rx import Observable
import multiprocessing
from rx.concurrency import ThreadPoolScheduler
from kivymd.uix.navigationdrawer import NavigationLayout
from database import base
from main_navigation.cardSubscription import DataSubscription, CardSubscription
from querries import sub_entity_payload
from ast import literal_eval
from general_functions import functions
from threading import current_thread
from path import dir_language
from contact_class.screen_contact import Contacts
from kivymd.uix.boxlayout import MDBoxLayout

session = base.Session()

with open(dir_language, 'r') as file:
    dict_l = literal_eval(file.read())

dictionary = dict_l['card_subs']

optimal_thread_count = multiprocessing.cpu_count()
poo_scheduler = ThreadPoolScheduler(optimal_thread_count)

class mainNavigation(NavigationLayout):
    def __init__(self):
        super(mainNavigation, self).__init__()

    def show_screen_contacts(self):
        if self._screen_manager.has_screen('screen_contact') is False:
            wid = Screen(name='screen_contact')
            print("is not in screen manager")
            screen_contact = Contacts()
            wid.add_widget(screen_contact)
            self._screen_manager.add_widget(wid)

        self._screen_manager.current = 'screen_contact'

    def get_subscriptions(self):
        list_sub = []
        subscriptions = sub_entity_payload.get_subscritions(self.account_name)
        for sub in subscriptions:
            subscription = sub['node']['source']
            nodes_result = functions.get_nodes(subscription)
            nodes_result['origen'] = 'entity'
            list_sub.append(nodes_result)
        return list_sub

    def create_list_tks(self, **kwargs):
        self.list_sub = self.get_subscriptions()
        self.data_subscriptions = []
        self.index = 0
        Observable.from_(self.list_sub) \
            .map(lambda i: DataSubscription(kwargs.get('account_id'), kwargs.get('account_name'), **i)) \
            .map(lambda e: self.data_subscriptions.append(e))\
            .subscribe_on(poo_scheduler).subscribe(on_next=lambda s: self.load_next(),
                       on_completed=lambda: print(datetime.now().time()), on_error=lambda e: print(e))

    def load_next(self):
        self.event = Clock.schedule_once(self.build_card_subscription, -1)

    def build_card_subscription(self, dt):
        card_sub = CardSubscription(**self.data_subscriptions[self.index].data_tk_sub)
        self.container.add_widget(card_sub)
        self.index += 1








