from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.snackbar import Snackbar

from register_class.register_payload import to_check, create_account


class Register(MDBoxLayout):
    def __init__(self, mainwid, **kwargs):
        super(Register, self).__init__()
        self.mainwid = mainwid
        self.user.bind(focus=self.on_focus)
        self.password.bind(focus=self.on_focus)
        self.second_password.bind(focus=self.on_focus)
        self.email.bind(focus=self.on_focus)

    def on_focus(self, instance, value):

        if value:
            pass
        else:
            if instance == self.user and self.user.text != '':
                self.check_name()
            if instance == self.password and self.password.text != '':
                self.check_pass1()
            if instance == self.second_password:
                self.check_pass2()
            if instance == self.email and self.email.text != '':
                self.check_email()

    def check_name(self):
        user = "." + self.user.text.lower()
        user_check = False
        if user.find(" ") > -1:
            Snackbar(text="Account name  without blanks", padding="20dp").show()
            user_check = False
            return user_check

        if len(user) < 5 or len(user) > 15:
            Snackbar(text=" Account name min 5, max: 15 ", padding="20dp").show()

            user_check = False
            return user_check

        if user == '':
            Snackbar(text="This field is required", padding="20dp").show()
            user_check = False
            return user_check

        exist = to_check(user, 'checkIdName', 'idName')


        if exist != None and user != '':
            Snackbar(text="Account name in use", padding="20dp").show()
            user_check = False
            return user_check

        if exist == None and len(user) >= 5:
            user_check = True
            return user_check

        return user_check

    def check_pass1(self):
        password = self.password.text
        pass1_check = False
        if (password != '' and len(password) >= 6) and len(password) <= 15:
            pass1_check = True
        else:
            pass1_check = False
        return pass1_check

    def check_pass2(self):
        passwordSecond = self.second_password.text
        if passwordSecond != self.password.text:
            Snackbar(text="password don't coincident", padding="20dp").show()
            pass2_check = False

            return pass2_check

        if ((passwordSecond != '' and len(passwordSecond) >= 6) and len(
                passwordSecond) <= 15) and passwordSecond == self.password.text:
            pass2_check = True
        else:
            pass2_check = False
        self.second_password.hint_text = "Repeat password"

        return pass2_check

    def check_email(self):

        email = self.email.text.lower()

        if email.find(" ") > -1:
            Snackbar(text="User name field without blanks", padding="20dp").show()
            email_check = False
            return email_check

        if email.find("@") == -1 or email.find(".") == -1:
            Snackbar(text="Use validate email", padding="20dp").show()
            email_check = False
            return email_check

        if email == '':
            Snackbar(text="The email field is required", padding="20dp").show()
            email_check = False
            return email_check

        exist = to_check(email, 'checkEmail', 'email')

        if exist is not None and exist is not False:
            Snackbar(text="this email is in use", padding="20dp").show()
            email_check = False
            return email_check

        if exist == None:
            self.email.helper_text = "Email"
            user_check = True
            return user_check

    def to_create_account(self):

        user = "." + self.user.text
        password = self.password.text
        email = self.email.text

        A = self.check_name()
        B = self.check_pass1()
        C = self.check_pass2()
        D = self.check_email()

        if A == True and B == True and C == True and D == True:
            id = create_account(user, password, email)

            if id != None:
                Snackbar(text="Account created, check you email for validate ", padding="20dp").show()
                return
        else:
            if A == False:
                Snackbar(text="Account name invalidate", padding="20dp").show()
                return
            if B == False or D == False:
                Snackbar(text="Password incorrect", padding="20dp").show()

                return

            if C == False:
                Snackbar(text="Email invalidate", padding="20dp").show()
                return

    def go_to_login(self):
        self.mainwid.goto_login()
