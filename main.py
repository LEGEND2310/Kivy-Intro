from kivy.app import App
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics import Color
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from  kivy.uix.widget import Widget

class WidgetsExample(GridLayout):
    enabled = BooleanProperty(False)
    my_text = StringProperty("0")
    text_input_str = StringProperty("Text Here")

    def on_button_click(self):
        if self.enabled:
            print("Button Clicked")
            self.my_text = str(int(self.my_text) + 1)
            
    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            widget.text = "Off"
            self.enabled = False
        else:
            widget.text = "On"
            self.enabled = True
        print("toggle state " + widget.state)

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))
    
    def on_slider_value(self, slider):
        print("Slider Value: " + str(int(slider.value)))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(100):
            b = Button(text = f"{i+1}", size_hint =(None, None), size= (dp(100),dp(100)))
            self.add_widget(b)
class GridLayoutExample(GridLayout):
    pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")

    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


class CanvasExample1(Widget):
    pass


class CanvasExample2(Widget):
    pass


class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points = (100, 100, 400, 500), width = 2)
            Color(0 , 1, 0)
            Line(circle = (100, 100, 100), width = 2)
            Line(rectangle = (700, 500, 150, 100), width = 2)
            self.rect = Rectangle(pos = (400, 400), size = (60,40))
    
    def on_button_a_click(self):
        x, y = self.rect.pos
        w,h = self.rect.size

        inc = dp(10)
        diff = self.width - (x+w)
        if(diff < inc):
            inc = diff
        
        x += inc
        self.rect.pos = (x, y)

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = 3
        self.vy = 4
        with self.canvas:
            self.ball = Ellipse(pos = (100,100), size = (self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        print("on size: " + str(self.width) + ", " + str(self.height)) 
        self.ball.pos = (self.center_x - self.ball_size/2, self.center_y - self.ball_size/2)

    def update(self, dt):
        # print("update")
        x, y = self.ball.pos

        if(x + self.ball_size >= self.width or x <= 0):
            self.vx *= -1
        if(y + self.ball_size >= self.height or y <= 0):
            self.vy *= -1

        self.ball.pos = (x + self.vx, y + self.vy)

class CanvasExample6(Widget):
    pass

class CanvasExample7(BoxLayout):
    pass

TheLabApp().run()
