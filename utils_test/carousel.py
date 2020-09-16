from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage


class CarouselApp(App):
    def build(self):
        carousel = Carousel(direction='left',)
        for i in range(10):
            src = "https://i.pinimg.com/736x/21/bb/76/21bb7620e7643af6aa6eec6409dddc57.jpg"
            image = AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)
        return carousel


CarouselApp().run()

