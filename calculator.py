from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class CalculatorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.num1_input = TextInput(hint_text="Enter first number", input_filter='float', multiline=False)
        self.layout.add_widget(self.num1_input)

        self.operator_spinner = Spinner(
            text='+',
            values=('+', '-', '*', '/'),
            size_hint=(1, None),
            height=44
        )
        self.layout.add_widget(self.operator_spinner)

        self.num2_input = TextInput(hint_text="Enter second number", input_filter='float', multiline=False)
        self.layout.add_widget(self.num2_input)

        calc_btn = Button(text="Calculate", size_hint=(1, None), height=50, on_press=self.calculate)
        self.layout.add_widget(calc_btn)

        self.result_label = Label(text="Result will appear here", size_hint=(1, None), height=44)
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate(self, instance):
        try:
            num1 = float(self.num1_input.text)
            num2 = float(self.num2_input.text)
            op = self.operator_spinner.text

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    self.show_error("Cannot divide by zero.")
                    return
            else:
                self.show_error("Invalid operator.")
                return

            self.result_label.text = f"Result: {result}"
        except ValueError:
            self.show_error("Please enter valid numbers.")

    def show_error(self, message):
        popup = Popup(title='Error',
                      content=Label(text=message),
                      size_hint=(0.8, 0.3))
        popup.open()

if __name__ == '__main__':
    CalculatorApp().run()

  
