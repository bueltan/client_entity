
from kivy.properties import StringProperty
from kivy.uix.image import AsyncImage
from kivymd.uix.list import ThreeLineAvatarIconListItem, ILeftBody


class AsyncImageLeftWidget(ILeftBody, AsyncImage):
    pass

class itemTickets(ThreeLineAvatarIconListItem):
    source_img = StringProperty()
    name_icon = StringProperty()
    secondary_text = StringProperty()
    tertiary_text = StringProperty()

"""
    on_release = lambda: open_chat(self.id, self.u_id, self.sub)

    def open_chat(self, id, u_id, sub):
        if self.img_lef.source == './img_profile/default-image.png':
            id_tk = id
            dir_profile = './img_profile/' + id_tk + '.png'
            if os.path.isfile(dir_profile):
                self.img_lef.source = dir_profile
        currentTk.id = u_id
        currentTk.id_tk = id
        currentTk.sub = sub
        self.mainwid.open_chat(u_id)

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


class currentTk:
    id, id_tk, sub = None, None, None

    def __init__(self, **kwargs):
        currentTk.id = kwargs.get('id')
        currentTk.id_tk = kwargs.get('id_tk')
        currentTk.sub = kwargs.get('sub')
"""