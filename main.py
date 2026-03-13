from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


KV = r'''
<CalculatorRoot>:
    orientation: "vertical"
    padding: dp(16)
    spacing: dp(12)

    Label:
        text: "온다스 / 온다스ETF 계산기"
        font_size: "20sp"
        size_hint_y: None
        height: self.texture_size[1] + dp(6)

    BoxLayout:
        orientation: "vertical"
        spacing: dp(8)

        Label:
            text: "온다스"
            bold: True
            size_hint_y: None
            height: self.texture_size[1] + dp(4)

        GridLayout:
            cols: 2
            row_default_height: dp(36)
            row_force_default: True
            spacing: dp(6)

            Label:
                text: "가격"
                halign: "left"
                valign: "middle"
                text_size: self.size
            TextInput:
                id: ondas_price
                text: root.ondas_price
                input_filter: "float"
                multiline: False
                on_text: root.on_input_change()

            Label:
                text: "고가"
                halign: "left"
                valign: "middle"
                text_size: self.size
            TextInput:
                id: ondas_high
                text: root.ondas_high
                input_filter: "float"
                multiline: False
                on_text: root.on_input_change()

            Label:
                text: "저가"
                halign: "left"
                valign: "middle"
                text_size: self.size
            TextInput:
                id: ondas_low
                text: root.ondas_low
                input_filter: "float"
                multiline: False
                on_text: root.on_input_change()

        GridLayout:
            cols: 2
            row_default_height: dp(30)
            row_force_default: True
            spacing: dp(6)

            Label:
                text: "비율(%) 고가"
                halign: "left"
                valign: "middle"
                text_size: self.size
            Label:
                text: root.ondas_ratio_high
                halign: "right"
                valign: "middle"
                text_size: self.size

            Label:
                text: "비율(%) 저가"
                halign: "left"
                valign: "middle"
                text_size: self.size
            Label:
                text: root.ondas_ratio_low
                halign: "right"
                valign: "middle"
                text_size: self.size

    BoxLayout:
        orientation: "vertical"
        spacing: dp(8)

        Label:
            text: "온다스ETF (2배)"
            bold: True
            size_hint_y: None
            height: self.texture_size[1] + dp(4)

        GridLayout:
            cols: 2
            row_default_height: dp(36)
            row_force_default: True
            spacing: dp(6)

            Label:
                text: "가격"
                halign: "left"
                valign: "middle"
                text_size: self.size
            TextInput:
                id: etf_price
                text: root.etf_price
                input_filter: "float"
                multiline: False
                on_text: root.on_input_change()

        GridLayout:
            cols: 2
            row_default_height: dp(30)
            row_force_default: True
            spacing: dp(6)

            Label:
                text: "비율(%) 고가"
                halign: "left"
                valign: "middle"
                text_size: self.size
            Label:
                text: root.etf_ratio_high
                halign: "right"
                valign: "middle"
                text_size: self.size

            Label:
                text: "비율(%) 저가"
                halign: "left"
                valign: "middle"
                text_size: self.size
            Label:
                text: root.etf_ratio_low
                halign: "right"
                valign: "middle"
                text_size: self.size

            Label:
                text: "고가"
                halign: "left"
                valign: "middle"
                text_size: self.size
            Label:
                text: root.etf_high
                halign: "right"
                valign: "middle"
                text_size: self.size

            Label:
                text: "저가"
                halign: "left"
                valign: "middle"
                text_size: self.size
            Label:
                text: root.etf_low
                halign: "right"
                valign: "middle"
                text_size: self.size

    Label:
        text: "입력값 변경 시 자동 계산됩니다."
        color: 0.35, 0.35, 0.35, 1
        font_size: "12sp"
        size_hint_y: None
        height: self.texture_size[1] + dp(6)
'''


class CalculatorRoot(BoxLayout):
    ondas_price = StringProperty("")
    ondas_high = StringProperty("")
    ondas_low = StringProperty("")

    ondas_ratio_high = StringProperty("-")
    ondas_ratio_low = StringProperty("-")

    etf_price = StringProperty("")
    etf_ratio_high = StringProperty("-")
    etf_ratio_low = StringProperty("-")
    etf_high = StringProperty("-")
    etf_low = StringProperty("-")

    def on_input_change(self):
        price = self._parse_float(self.ondas_price)
        high = self._parse_float(self.ondas_high)
        low = self._parse_float(self.ondas_low)
        etf_price = self._parse_float(self.etf_price)

        ratio_high = None
        ratio_low = None

        if price is not None and high is not None and price != 0:
            ratio_high = (high / price - 1) * 100
        if price is not None and low is not None and price != 0:
            ratio_low = (low / price - 1) * 100

        self.ondas_ratio_high = self._format(ratio_high)
        self.ondas_ratio_low = self._format(ratio_low)

        etf_ratio_high = ratio_high * 2 if ratio_high is not None else None
        etf_ratio_low = ratio_low * 2 if ratio_low is not None else None

        self.etf_ratio_high = self._format(etf_ratio_high)
        self.etf_ratio_low = self._format(etf_ratio_low)

        etf_high = None
        etf_low = None
        if etf_price is not None and etf_ratio_high is not None:
            etf_high = etf_price * (1 + etf_ratio_high / 100)
        if etf_price is not None and etf_ratio_low is not None:
            etf_low = etf_price * (1 + etf_ratio_low / 100)

        self.etf_high = self._format(etf_high)
        self.etf_low = self._format(etf_low)

    @staticmethod
    def _parse_float(value):
        value = (value or "").strip()
        if not value:
            return None
        try:
            return float(value)
        except ValueError:
            return None

    @staticmethod
    def _format(value):
        if value is None:
            return "-"
        return f"{value:.2f}"


class CalculatorApp(App):
    def build(self):
        Builder.load_string(KV)
        return CalculatorRoot()


if __name__ == "__main__":
    CalculatorApp().run()
