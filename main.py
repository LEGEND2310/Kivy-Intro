from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
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

TheLabApp().run()
