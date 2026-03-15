from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class Root(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=24, spacing=16, **kwargs)
        self.label = Label(
            text="ONdas",
            font_size=32,
            bold=True,
        )
        self.status = Label(
            text="APK 빌드 준비 완료",
            font_size=18,
        )
        button = Button(
            text="눌러보기",
            size_hint=(1, None),
            height=56,
        )
        button.bind(on_press=self.on_press)

        self.add_widget(self.label)
        self.add_widget(self.status)
        self.add_widget(button)

    def on_press(self, *_args):
        self.status.text = "잘 눌렸어요"


class OndasApp(App):
    def build(self):
        self.title = "ONdas"
        return Root()


if __name__ == "__main__":
    OndasApp().run()
