from kivy.animation import Animation
from kivy.uix.image import Image
from kivymd.uix.boxlayout import MDBoxLayout
from querries.register_payload import get_id, create_account
from kivymd.uix.dialog import MDDialog


class check_ok(Image):
    def __init__(self, mainwid, **kwargs):
        super(check_ok, self).__init__()


class check_wrong(Image):
    def __init__(self, mainwid, **kwargs):
        super(check_wrong, self).__init__()


class MessagePopup():
    dialog = None

    def show_alert_dialog(self, text):
        if not self.dialog:
            self.dialog = MDDialog(
                text=text,
                radius=[20, 7, 20, 7]
            )

        self.dialog.open()


class Register(MDBoxLayout):
    def __init__(self, mainwid, **kwargs):
        super(Register, self).__init__()

        self.mainwid = mainwid

        self.user.bind(focus=self.on_focus)

        self.password.bind(focus=self.on_focus)

        self.second_password.bind(focus=self.on_focus)

        self.email.bind(focus=self.on_focus)

    def set_error_message(self, instance_textfield):
        instance_textfield.line_color_focus = 1, 0, 0, 1

    def set_not_error_message(self, instance_textfield):
        instance_textfield.line_color_focus = 0, 1, 0, 1

    def on_focus(self, instance, value):

        if value:
            pass
        else:
            if instance == self.user:
                self.check_name()
            if instance == self.password:
                self.check_pass1()
            if instance == self.second_password:
                self.check_pass2()
            if instance == self.email:
                self.check_email()

    def animateico(self, instance):
        anim = Animation(size=(35, 35), duration=.2)
        anim.start(instance)

    def check_name(self):
        user = "." + self.user.text.lower()
        id = get_id(user, 'checkName', 'name')
        self.wrong = check_wrong(self.mainwid)
        self.ok = check_ok(self.mainwid)
        # self.boxName.clear_widgets()
        user_check = False

        if user.find(" ") > -1:
            self.animateico(self.wrong)
            # self.boxName.add_widget(self.wrong)
            self.user.hint_text = "Ingrese nombre sin espacios"
            user_check = False
            return user_check

        if len(user) < 5 or len(user) > 15:
            self.animateico(self.wrong)
            # self.boxName.add_widget(self.wrong)
            self.user.hint_text = "Minimo 5 caracteres, maximo 15"
            user_check = False
            return user_check

        if user == '':
            self.animateico(self.wrong)
            # self.boxName.add_widget(self.wrong)
            self.user.hint_text = "Este campo es necesario"
            user_check = False

            return user_check

        if id == None and len(user) >= 5:
            self.animateico(self.ok)
            # self.boxName.add_widget(self.ok)
            self.user.hint_text = "Nombre de usuario"
            user_check = True
            return user_check

        if id != None and user != '':
            self.animateico(self.wrong)
            # self.boxName.add_widget(self.wrong)
            self.user.hint_text = "Nombre de usuario en uso"

            user_check = False

            return user_check

        return user_check

    def check_pass1(self):
        self.wrong = check_wrong(self.mainwid)
        self.ok = check_ok(self.mainwid)
        password = self.password.text
        # self.boxPassword.clear_widgets()

        pass1_check = False

        if (password != '' and len(password) >= 6) and len(password) <= 15:
            self.animateico(self.ok)
            # self.boxPassword.add_widget(self.ok)
            pass1_check = True
        else:
            self.animateico(self.wrong)
            # self.boxPassword.add_widget(self.wrong)

            pass1_check = False

        return pass1_check

    def check_pass2(self):
        self.wrong = check_wrong(self.mainwid)
        self.ok = check_ok(self.mainwid)

        passwordSecond = self.second_password.text
        # self.boxPasswordSecond.clear_widgets()

        pass2_check = False

        if passwordSecond != self.password.text:
            self.animateico(self.wrong)
            # self.boxPasswordSecond.add_widget(self.wrong)
            self.second_password.hint_text = "Las contraseñas no coinciden"

            pass2_check = False

            return pass2_check

        if ((passwordSecond != '' and len(passwordSecond) >= 6) and len(
                passwordSecond) <= 15) and passwordSecond == self.password.text:
            self.animateico(self.ok)
            # self.boxPasswordSecond.add_widget(self.ok)
            self.second_password.hint_text = "Contraseña"
            pass2_check = True
        else:
            self.animateico(self.wrong)
            # self.boxPasswordSecond.add_widget(self.wrong)
            self.second_password.hint_text = "Contraseña minimo 6 caracteres, maximo 15"

            pass2_check = False

        return pass2_check

        return pass2_check

    def check_email(self):

        email = self.email.text.lower()
        id = get_id(email, 'checkEmail', 'email')
        self.wrong = check_wrong(self.mainwid)
        self.ok = check_ok(self.mainwid)
        # self.boxEmail.clear_widgets()
        email_check = False

        if email.find(" ") > -1:
            self.animateico(self.wrong)
            # self.boxEmail.add_widget(self.wrong)
            self.email.hint_text = "Ingrese email sin espacios"
            email_check = False
            return email_check

        if email.find("@") == -1:
            self.animateico(self.wrong)
            # self.boxEmail.add_widget(self.wrong)
            self.email.hint_text = "Ingrese un email valido"
            email_check = False
            return email_check

        if email.find(".") == -1:
            self.animateico(self.wrong)
            # self.boxEmail.add_widget(self.wrong)
            self.email.hint_text = "Ingrese un email valido"
            email_check = False
            return email_check

        if email == '':
            self.animateico(self.wrong)
            # self.boxEmail.add_widget(self.wrong)
            self.email.hint_text = "Ingrese un email"
            email_check = False
            return email_check

        if id != None:
            self.animateico(self.wrong)
            # self.boxEmail.add_widget(self.wrong)
            self.email.hint_text = "Este email se encuentra registrado"
            email_check = False
            return email_check

        if id == None:
            self.animateico(self.ok)
            # self.boxEmail.add_widget(self.ok)
            self.email.hint_text = "Email"
            user_check = True
            return user_check

    def to_create_account(self):

        user = "." + self.user.text
        password = self.password.text
        email = self.email.text
        self.menssage = MessagePopup()

        A = self.check_name()

        B = self.check_pass1()

        C = self.check_pass2()

        D = self.check_email()

        if A == True and B == True and C == True and D == True:
            id = create_account(user, password, email)

            if id != None:
                self.menssage.show_alert_dialog('Cuenta creada correctamente')
                return
        else:
            if A == False:
                self.menssage.show_alert_dialog('Nombre de usuario invalido')
                return
            if B == False or D == False:
                self.menssage.show_alert_dialog('Contraseña invalida')

                return

            if C == False:
                self.menssage.show_alert_dialog('Email invalido')

                return

    def go_to_login(self):
        self.mainwid.goto_login()
