import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

# set app size

Window.size = (500, 700)

# diseño
Builder.load_file('calc.kv')


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    # Funcion de los botones
    def button_press(self, button):
        # variable auxiliar
        prior = self.ids.calc_input.text
        # test errores
        if 'ERROR' in prior:
            prior = ''

        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    # funcion borrar
    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    # positivo y negativo
    def pos_neg(self):
        prior = self.ids.calc_input.text
        if '-' in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    # funcion decimal
    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split('+')

        if '+' in prior and '.' not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif '.' in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

    # funciones operatorias
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'

    # funcion igual
    def equals(self):
        prior = self.ids.calc_input.text
        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except Exception:
            self.ids.calc_input.text = 'ERROR'
        # adicion
        """if '+' in prior:
            num_list = prior.split('+')
            answer = 0.0
            for number in num_list:
                answer = answer + float(number)

            self.ids.calc_input.text = str(answer)
"""


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()
