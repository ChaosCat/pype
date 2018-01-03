"""
Main Pype application program.
"""

# Imports
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

# Importing fonts
LabelBase.register(name='Noto', fn_regular='fonts/NotoSans-Light.ttf')
LabelBase.register(name='Noto Bold', fn_regular='fonts/NotoSans-Bold.ttf')


class LoginScreen(BoxLayout):

    """Application login screen
    """

    pass


class Title(Label):

    """Title label.
    """

    pass


class PypeApp(App):

    """Pype application class.

    Attributes:
        title (str): Window title.
    """

    def build(self):
        """Loads application widgets.

        Returns:
            LoginScreen: Login screen window.
        """

        self.title = 'Welcome to Pype'
        return LoginScreen()

# Running app
if __name__ == '__main__':
    PypeApp().run()
