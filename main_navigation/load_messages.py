
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
                                 source=dir, caption=caption, url=msg.url, id=msg.id)
        if msg.type == "audio":
            layoutAn = AnchorLayout(anchor_x=orientation, anchor_y='center', size_hint_y=None, height=150)
            message = MessagePlayAudio(self, size_hint_y=None,
                                       height=150, size_hint_x=None, width=450,
                                       orientation=orientation,
                                       source=dir, caption=caption, url=msg.url, id=msg.id)
    layoutAn.add_widget(message)
    self.layout.add_widget(layoutAn)
