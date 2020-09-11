from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDTextButton

KV = '''
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Example Tabs"

    MDTabs:
        id: tabs
        
       


<Tab>:
    list_tk:list_tk
    ScrollView:
        MDList:
            id: list_tk
            
'''


class Tab(BoxLayout, MDTabsBase):
     def __init__(self, text):
        super(Tab, self).__init__()
        self.text = text
        self.id = 'tab'
        for i in range(30):
            btn = MDTextButton(text="fdgkdfñlg")
            self.list_tk.add_widget(btn)
        print(self.size)

class Tab1(ScrollView, MDTabsBase):
     def __init__(self, text):
        super(Tab1, self).__init__()
        self.text = text
        self.id = 'tab1'
        label = MDLabel(text= text, id = 'label')
        self.add_widget(label)

class Example(MDApp):
    index = 0

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.add_tab()

    def get_tab_list(self):
        '''Prints a list of tab objects.'''
        print(self.root.ids.tabs.get_tab_list())

    def add_tab(self):
        self.index += 1
        tab1  = Tab1(text=f"{self.index} tab1")
        self.root.ids.tabs.add_widget(Tab(text=f"{self.index} tab"))
        self.root.ids.tabs.add_widget(tab1)
        self.root.ids['tab1'] = tab1

    def remove_tab(self):
        if self.index > 1:
            self.index -= 1
        self.root.ids.tabs.remove_widget(self.root.ids.tabs.get_tab_list()[0])

    def on_tab_switch(self, *args):
       print(args)

    def changeLabelTab1(self):
        self.root.ids['tab1'].children[0].text = "sdfsdf"




Example().run()