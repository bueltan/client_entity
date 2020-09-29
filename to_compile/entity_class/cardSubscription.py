
"""DataSubscription """

from kivy.properties import StringProperty
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from database.base import Session
from database.model_tickets import ModelTickets
from entity_class.ItemTickets import itemTickets
from querries.tickets_payload import sync_tickets
from entity_class.build_data_tk import build_data_tk


class DataSubscription():
    session = Session()

    def __init__(self,*args ,**kwargs):
        self.data_tk = []
        self.data_sub = kwargs
        self.my_id = args[0]

        for i in self.data_sub['origen']:
            if i == 'entity':
                id_code = self.data_sub['origen']['entity']
                self.data_sub['id_code'] = id_code
            if i == 'whatsapp':
                id_code = self.data_sub['origen']['whatsapp']
                self.data_sub['id_code'] = id_code
            sync_tickets(self.data_sub,self.my_id)

        if len(self.data_sub['origen']) > 1:
            self.load_tk_in_sub()
        else :
            if id_code != '':
                self.load_tk_in_sub(id_code=id_code)
            else:
                self.load_tk_in_sub(id_user=self.my_id,id_code=id_code)

        Session.remove()

    def load_tk_in_sub(self, id_code=None, id_user=None):

        if id_user:
            tickets = self.session.query(ModelTickets)\
            .filter_by(id_tk=id_user)

        if id_code == None:
            tickets = self.session.query(ModelTickets)\
                .filter_by(node2=self.data_sub['node2'],
                           node3=self.data_sub['node3'], node4=self.data_sub['node4'])
        else:
            tickets = self.session.query(ModelTickets)\
                .filter_by(id_code=id_code, node2=self.data_sub['node2'],
                           node3=self.data_sub['node3'], node4=self.data_sub['node4'])

        self.mutation_data_tk(tickets)

    def mutation_data_tk(self, tickets):
        if tickets is not None:
            for tk in tickets:
                data = {'id': tk.id, 'id_tk': tk.id_tk, 'name': tk.name,
                        'image': tk.image, 'last_id_msg': tk.last_id_msg,
                        'phone': tk.phone, 'readed':tk.readed}
                self.data_tk.append(build_data_tk(data))
        else:
            self.data_tk.append(None)

        self.data_tk_sub = {'data_tks':self.data_tk,'data_sub':self.data_sub}


class CardSubscription(MDCard):
    """CardSubscription """
    def __init__(self, **kwargs):
        super(CardSubscription, self).__init__()
        self.title.font_style = "H6"
        self.titleSub.font_style = "Caption"
        self.data_tk = kwargs.get('data_tks')
        self.data_sub = kwargs.get('data_sub')
        self.title.text = self.data_sub['node2'] + \
                          self.data_sub['node3']+ self.data_sub['node4']
        self.set_list_data()

        for i in self.data_sub['origen']:
            if i == 'entity':
                self.origen.add_widget(MDIconButton(icon='graph', user_font_size="20sp"))
            if i == 'whatsapp':
                self.origen.add_widget(MDIconButton(icon='whatsapp', user_font_size="20sp"))


    def set_list_data(self, text="", search=False):
        if self.data_tk:
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

            def add_item_in_recycleView(data_tk):
                self.ids.rv.data.append(
                    {
                        "viewclass": data_tk['viewclass'],
                        "source_img": data_tk['source_img'],
                        "name_icon": data_tk['name_icon'],
                        "text": data_tk['text'],
                        "secondary_text": data_tk['secondary_text'],
                        "tertiary_text": data_tk['tertiary_text'],
                        "name": data_tk['name'],

                        # "on_release": lambda :edit_selected(id_tk=data_tk['id_tk'], new_text= data['id_tk'])

                    }
                )

            self.ids.rv.data = []

            for i, d in enumerate(self.data_tk):
                if search:
                    if (text).lower() in d['secondary_text'].lower() \
                            or text in d['text'].lower() or text in d['tertiary_text'].lower():
                        add_item_in_recycleView(self.data_tk[i])
                else:
                    add_item_in_recycleView(self.data_tk[i])


        #   self.subscription_nodes(nodes)



    """def subscription_nodes(self, variables):
        variables = {'id_code': variables['id_code'], 'node_2': variables['node2'],
                     'node_3': variables['node3'], 'node_4': variables['node4']}
        subscriptions.subscriptions(self).getTK(variables)
        """

