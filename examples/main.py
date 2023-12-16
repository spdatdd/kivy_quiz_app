from kivy.uix.widget import Widget
from kivy.app import App
from kivy.metrics import dp
from kivy.graphics import *

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))

class ExerciseApp(App):
    pass

ExerciseApp().run()