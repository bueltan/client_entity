self.file_manager = MDFileManager(exit_manager=self.exit_manager,
                                  select_path=self.select_path)
self.navDrawer.open_file.on_release = lambda: self.file_manager.show('/')
self.data_account = load_account_from_db()


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


def select_path(self, path):
    file_name = str(self.data_account.id) + ".png"
    dest_file = './img_account/' + file_name
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