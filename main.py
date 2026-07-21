"""
你的第一个 Kivy 手机 App
编译命令（本地测试）：python main.py
自动编译（云端）：git push → GitHub Actions → APK
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainScreen(BoxLayout):
    """主界面：输入名字，点击按钮显示问候语"""

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=30, spacing=15, **kwargs)

        # 标题
        self.title_label = Label(
            text='我的第一个 App',
            font_size=28,
            size_hint=(1, 0.2)
        )

        # 输入框
        self.name_input = TextInput(
            text='',
            hint_text='请输入你的名字',
            font_size=20,
            multiline=False,
            size_hint=(1, 0.15)
        )

        # 按钮
        self.greet_button = Button(
            text='点我打招呼',
            font_size=20,
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 1, 1)
        )
        self.greet_button.bind(on_press=self.on_greet)

        # 结果显示
        self.result_label = Label(
            text='欢迎！',
            font_size=24,
            size_hint=(1, 0.3)
        )

        # 组装界面
        self.add_widget(self.title_label)
        self.add_widget(self.name_input)
        self.add_widget(self.greet_button)
        self.add_widget(self.result_label)

    def on_greet(self, instance):
        name = self.name_input.text.strip()
        if name:
            self.result_label.text = f'你好，{name}！🎉'
        else:
            self.result_label.text = '你好，世界！🎉'


class MyApp(App):
    def build(self):
        self.title = '我的 Kivy App'
        return MainScreen()


if __name__ == '__main__':
    MyApp().run()
