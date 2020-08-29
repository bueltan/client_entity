from kivy.app import App
from os.path import sep, expanduser, isdir, dirname
import sys
from kivy_garden.filebrowser import FileBrowser


class TestApp(App):
    def build(self):
        if sys.platform == 'win':
            user_path = dirname(expanduser('~')) + sep + 'Documents'
        else:
            user_path = expanduser('~') + sep + 'Documents'
        browser = FileBrowser(select_string='Select',
                              favorites=[(user_path, 'Documents')],
                              filters=['*.png','*.jpg'])
        browser.bind(
                    on_success=self._fbrowser_success,
                    on_canceled=self._fbrowser_canceled
                    )
        return browser

    def _fbrowser_canceled(self, instance):
        print ('cancelled, Close self.')
        self.stop()

    def _fbrowser_success(self, instance):
        print (instance.selection)
        self.stop()





TestApp().run()

