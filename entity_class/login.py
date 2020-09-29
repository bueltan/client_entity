from kivymd.uix.boxlayout import MDBoxLayout
from querries.login_payload import check_login
from kivymd.uix.dialog import MDDialog
from querries.login_database import save_account, load_account_from_db
from querries.login_payload import get_data_account


class MessagePopup():
    dialog = None

    def show_alert_dialog(self, text):
        if not self.dialog:
            self.dialog = MDDialog(
                text=text,
                radius=[20, 7, 20, 7]
            )

        self.dialog.open()


class Login(MDBoxLayout):
    def __init__(self, mainwid, **kwargs):
        super(Login, self).__init__()
        self.mainwid = mainwid
        self.title.font_style = "H3"
        self.keepOpen.on_release = lambda: self.change_ck()
        account = load_account_from_db()
        try:
            self.ck_keepOpen.active = account.keepOpen
        except:
            pass
        if self.ck_keepOpen.active == True:
            if account:
                self.user.text = account.idName.split(".")[1]
                self.password.text = account.password

    def change_ck(self):
        if self.ck_keepOpen.active == False:

            self.ck_keepOpen.active = True
        else:
            self.ck_keepOpen.active = False

    def go_in(self):
        # DELETE THIS DON'T FORGET
        connection = True

        user = "." + self.user.text
        user = user.lower()
        password = self.password.text
        id = check_login(user, password)
        if id:
            self.mainwid.goto_mainNavigation(account_name=user ,account_id = id)
            keepOpen = self.ck_keepOpen.active
            if connection:
                data = get_data_account(id)
                data['id'] = id
                data['keepOpen'] = keepOpen
                save_account(data)
        else:
            self.menssage = MessagePopup()
            self.menssage.show_alert_dialog('UserName or password is wrong')

    def go_to_register(self):
        self.mainwid.goto_register()
