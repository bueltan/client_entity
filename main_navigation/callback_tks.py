def callback(self, _id, data):
    data = data['payload']['data']['getTK']
    data = literal_eval(data)
    id_tk = data['id_tk']
    id = data['id']
    data_sub = {'node': data}
    load_tk_in_database([data_sub])
    # self.set_msg_in_widget()

    if id_tk in self.ids:
        id_sub = get_sub(data)
        for i in self.ids[id_sub].list_tickets.children:
            if i.id == id_tk:
                last_id_msg = data['last_id_msg']
                last_msg = after_login_payload.getLastMsg(last_id_msg)
                msg = functions.show_last_msg(last_msg, dictionary)
                i.secondary_text = msg
                break
        else:
            self.create_tk(data, sub=None)

    else:
        self.create_tk(data, sub=None)