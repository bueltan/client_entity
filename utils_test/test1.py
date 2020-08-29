from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import time

class MessagePlayAudio(MDBoxLayout):
    def __init__(self, theme, **kwargs):
        super(MessagePlayAudio, self).__init__()

        self.orientation = 'horizontal'
        self.padding = 10
        self.lenght  = 0
        self.stop = False
        self.flat = False
        file = 'Clip 4.ogg'
        """ containers """
        self.mainSliderBox = MDBoxLayout(orientation='vertical')
        self.playBox = AnchorLayout(anchor_x='center', anchor_y='center', size_hint = (.24, 1.22))
        self.sliderBox = AnchorLayout(anchor_x='center', anchor_y='center')
        self.labelStartBox = AnchorLayout(anchor_x='left', anchor_y='top')
        self.labelEndBox = AnchorLayout(anchor_x='right', anchor_y='top')
        self.labelBox = MDBoxLayout(orientation='horizontal', size_hint = (1, .3), padding = 5)
        """" widgets """
        self.playButton = MDIconButton(icon='play', user_font_size= "57sp", theme_text_color= "Custom", text_color= theme.primary_color, on_release=lambda x: self.play_sound() )
        self.labelStart = MDLabel(text=" 0:00")
        self.labelEnd = MDLabel(text="1:00", halign= "right" )
        self.slider = MDSlider(min=0, max=100)
        self.load_audio(file)
        self.slider.bind(value=self.on_value)

        self.labelStartBox.add_widget(self.labelStart)
        self.labelEndBox.add_widget(self.labelEnd)
        self.labelBox.add_widget(self.labelStartBox)
        self.labelBox.add_widget(self.labelEndBox)

        self.sliderBox.add_widget(self.slider)
        self.mainSliderBox.add_widget(self.sliderBox)
        self.mainSliderBox.add_widget(self.labelBox)
        self.playBox.add_widget(self.playButton)

        self.add_widget(self.playBox)
        self.add_widget(self.mainSliderBox)

    def load_audio(self, file):
        self.sound = SoundLoader.load(file)
        self.length = self.sound.length
        length_sec = self.length / 60
        length_sec = str(round(length_sec,2))
        length_sec = length_sec.replace(".", ":")
        print("Sound is %.3f seconds" % self.sound.length)
        self.labelEnd.text = (length_sec)

    def on_value(self, instance, percent):
        if not self.flat:
            print("on_value")
            position = self.length / 100 * percent
            self.playButton.icon = 'pause'
            self.show_position(percent)
            self.sound.stop()
            self.play(position)

    def show_position(self, percent):
        position = self.length / 100 * percent
        length_sec = position / 60
        length_sec = str(round(length_sec, 2))
        length_sec = length_sec.replace(".", ":")
        self.labelStart.text = length_sec

    def set_position(self):
        print("the sound is played")
        position = self.sound.get_pos()
        total = self.sound.length
        percent = position / total * 100
        self.show_position(percent)
        self.flat = True
        self.slider.value = percent
        self.flat = False
        if round(position,1) == round(total):
            print("fin sonido")
            self.flat = True
            self.slider.value = 100
            self.flat = False

            return False

        if self.stop:
            return False

    def play(self, seek):
        if seek != 0:
            self.sound.seek(seek)
        self.sound.play()
        self.audio = Clock.schedule_interval(lambda i: self.set_position(), 0.2)
        self.stop = False

    def play_sound(self):
        if self.playButton.icon == 'play':
            self.playButton.icon = 'pause'
            if self.sound:
                print("Sound found at %s" % self.sound.source)
                print("Sound is %.3f seconds" % self.sound.length)
                self.play(0)

        else:
            self.playButton.icon = 'play'
            self.sound.stop()
            self.stop = True
            print(self.sound.get_pos())


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"  # "Purple", "Red"

        self.theme_cls.primary_hue = "500"  # "500"
        return MessagePlayAudio(self.theme_cls)


if __name__ == "__main__":
    MainApp().run()