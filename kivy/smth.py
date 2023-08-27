from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        btn = Button(text = "[b]Кнопка[/b]", markup=True)
        txt = Label(text = "[color=#254855]Лейбл[/color]", markup=True)
        btn.on_press = test
        layout = BoxLayout()
        layout.add_widget(txt)
        layout.add_widget(btn)


        return layout
    
def test():
    print('пр')

app = MyApp()
app.run()