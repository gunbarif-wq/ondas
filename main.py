from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout


KV = r"""
<CardLabel@Label>:
    color: 0.08, 0.08, 0.1, 1
    font_size: "14sp"

<ValueField@TextInput>:
    multiline: False
    input_filter: "float"
    padding: [dp(12), dp(12)]
    background_normal: ""
    background_active: ""
    background_color: 1, 1, 1, 1
    foreground_color: 0.1, 0.1, 0.1, 1
    cursor_color: 0.1, 0.1, 0.1, 1
    size_hint_y: None
    height: dp(44)
    halign: "left"
    valign: "middle"

<ResultPill@Label>:
    size_hint_y: None
    height: dp(34)
    text_size: self.size
    halign: "center"
    valign: "middle"
    color: 1, 1, 1, 1
    canvas.before:
        Color:
            rgba: 0.16, 0.35, 0.62, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(16)]

<AppRoot>:
    orientation: "vertical"
    padding: dp(18)
    spacing: dp(16)
    canvas.before:
        Color:
            rgba: 0.96, 0.97, 0.99, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: "vertical"
        size_hint_y: None
        height: self.minimum_height
        spacing: dp(6)

        Label:
            text: "Ondas"
            font_size: "26sp"
            bold: True
            color: 0.08, 0.12, 0.2, 1
            size_hint_y: None
            height: self.texture_size[1] + dp(6)

        Label:
            text: "Android investment helper"
            font_size: "13sp"
            color: 0.4, 0.45, 0.55, 1
            size_hint_y: None
            height: self.texture_size[1] + dp(2)

    BoxLayout:
        orientation: "vertical"
        spacing: dp(12)
        size_hint_y: None
        height: self.minimum_height
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [dp(18)]

        BoxLayout:
            orientation: "vertical"
            padding: dp(16)
            spacing: dp(10)
            size_hint_y: None
            height: self.minimum_height

            CardLabel:
                text: "Base Price"
            ValueField:
                id: base_price
                text: root.base_price
                on_text: root.on_input_change()

            CardLabel:
                text: "Target High"
            ValueField:
                id: target_high
                text: root.target_high
                on_text: root.on_input_change()

            CardLabel:
                text: "Target Low"
            ValueField:
                id: target_low
                text: root.target_low
                on_text: root.on_input_change()

    BoxLayout:
        orientation: "horizontal"
        spacing: dp(12)
        size_hint_y: None
        height: dp(44)

        ResultPill:
            text: root.high_ratio
        ResultPill:
            text: root.low_ratio

    BoxLayout:
        orientation: "vertical"
        spacing: dp(12)
        size_hint_y: None
        height: self.minimum_height
        canvas.before:
            Color:
                rgba: 1, 1, 1, 1
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [dp(18)]

        BoxLayout:
            orientation: "vertical"
            padding: dp(16)
            spacing: dp(10)
            size_hint_y: None
            height: self.minimum_height

            CardLabel:
                text: "ETF Price (2x)"
            ValueField:
                id: etf_price
                text: root.etf_price
                on_text: root.on_input_change()

            CardLabel:
                text: "ETF Target High"
            ResultPill:
                text: root.etf_high
            CardLabel:
                text: "ETF Target Low"
            ResultPill:
                text: root.etf_low

    Label:
        text: "Values update instantly as you type."
        font_size: "12sp"
        color: 0.4, 0.45, 0.55, 1
        size_hint_y: None
        height: self.texture_size[1] + dp(4)
"""


class AppRoot(BoxLayout):
    base_price = StringProperty("")
    target_high = StringProperty("")
    target_low = StringProperty("")
    etf_price = StringProperty("")

    high_ratio = StringProperty("High +0.00%")
    low_ratio = StringProperty("Low +0.00%")
    etf_high = StringProperty("0.00")
    etf_low = StringProperty("0.00")

    def on_input_change(self):
        base = self._parse_float(self.base_price)
        high = self._parse_float(self.target_high)
        low = self._parse_float(self.target_low)
        etf = self._parse_float(self.etf_price)

        high_ratio = self._ratio(base, high)
        low_ratio = self._ratio(base, low)

        self.high_ratio = self._ratio_label("High", high_ratio)
        self.low_ratio = self._ratio_label("Low", low_ratio)

        etf_high = self._apply_ratio(etf, high_ratio)
        etf_low = self._apply_ratio(etf, low_ratio)

        self.etf_high = self._format_number(etf_high)
        self.etf_low = self._format_number(etf_low)

    @staticmethod
    def _parse_float(value):
        if not value:
            return None
        try:
            return float(value.strip())
        except ValueError:
            return None

    @staticmethod
    def _ratio(base, target):
        if base is None or target is None or base == 0:
            return None
        return (target / base - 1) * 100

    @staticmethod
    def _apply_ratio(price, ratio):
        if price is None or ratio is None:
            return None
        return price * (1 + ratio / 100)

    @staticmethod
    def _ratio_label(label, ratio):
        if ratio is None:
            return f"{label} --"
        sign = "+" if ratio >= 0 else ""
        return f"{label} {sign}{ratio:.2f}%"

    @staticmethod
    def _format_number(value):
        if value is None:
            return "--"
        return f"{value:,.2f}"


class OndasApp(App):
    def build(self):
        Builder.load_string(KV)
        return AppRoot()


if __name__ == "__main__":
    OndasApp().run()
