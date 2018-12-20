from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.clock import Clock

import time

Window.size = (1000, 700)

class LoginScreen(Widget):
    def login(self, *args):
        fnama = self.ids.fnama_input
        fnama_text = fnama.text
        lnama = self.ids.lnama_input
        lnama_text = lnama.text
        no = self.ids.no_input
        no_text = no.text
        email = self.ids.email_input
        email_text = email.text
        password = self.ids.password_input
        password_text = password.text
        passwordk = self.ids.passwordk_input
        passwordk_text = passwordk.text
        if fnama_text == "Alfin" and lnama_text == "Niam" and no_text =="0877123123" and email_text == "alfin.anas@gmail.com" and password_text =="12345" and passwordk_text =="12345":
            label = self.ids.success
            label.text = "Berhasil Registrasi"
    
class LatihanApp(App):
    def build(self):
              return LoginScreen()


if __name__ == '__main__':
    LatihanApp().run()
