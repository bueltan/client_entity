self.layout = GridLayout(cols=1, spacing=20, size_hint_y=None)
self.layout.bind(minimum_height=self.layout.setter('height'))

def sent_message(self):
    userId = self.account_id
    text = self.text_to_sent.text
    id_tk = currentTk.id_tk
    id = currentTk.id
    sub = functions.get_nodes(currentTk.sub)
    tickets = sub[0]
    tickets['idTk'] = id_tk
    tickets['id'] = id
    message = {'type': 'text', 'text': text}
    payload = {**tickets, **message, 'userId': userId}
    build_message.exec_query(payload)


def set_msg_in_widget(self, id, id_msg):
    if self.list_message.id == id:
        message = get_oneMsg_local_db(id_msg)
        self.load_msg(message)
