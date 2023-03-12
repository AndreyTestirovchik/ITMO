class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def s_rectangle(self):
        S = self.width * self.height
        print(f'Площадь = {S}')

    def p_rectangle(self):
        P = 2 * (self.width + self.height)
        print(f'Периметр = {P}')


rect_1 = Rectangle(8, 10)
rect_2 = Rectangle(6, 20)
rect_3 = Rectangle(15, 18)

rect_1.s_rectangle()
rect_1.p_rectangle()
rect_2.s_rectangle()
rect_2.p_rectangle()
rect_3.s_rectangle()
rect_3.p_rectangle()


class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        add = self.a + self.b
        print(f'Сумма: {add}')

    def multiplication(self):
        mult = self.a * self.b
        print(f'Умножение: {mult}')

    def division(self):
        if self.b == 0:
            print('На ноль делить нельзя')
        else:
            div = self.a / self.b
            print(f'Деление: {div}')

    def subtraction(self):
        sub = self.a - self.b
        print(f'Вычетание: {sub}')


numbers = Math(25, -5)

numbers.addition()
numbers.multiplication()
numbers.division()
numbers.subtraction()


class Button:

    type: str = 'Кнопка'

    def __init__(self, text, loc=' '):
        self.text = text
        self.loc = loc

    def clic(self):
        print(f'Клик по кнопке: {self.text}')


button_Text_Box = Button('Text Box')
button_Check_Box = Button('Check Box')
button_Radio_Button = Button('Radio Button')
button_Web_Tables = Button('Web Tables')
button_Buttons = Button('Buttons')
button_Links = Button('Links')
button_Broken_Links_Images = Button('Broken Links - Images')
button_Upload_and_Download = Button('Upload and Download')
button_Dynamic_Properties = Button('Dynamic Properties')


print(button_Text_Box.text)
button_Text_Box.clic()
print(button_Check_Box.text)
button_Check_Box.clic()
print(button_Radio_Button.text)
button_Radio_Button.clic()
print(button_Web_Tables.text)
button_Web_Tables.clic()
print(button_Buttons.text)
button_Buttons.clic()
print(button_Links.text)
button_Links.clic()
print(button_Broken_Links_Images.text)
button_Broken_Links_Images.clic()
print(button_Upload_and_Download.text)
button_Upload_and_Download.clic()
print(button_Dynamic_Properties.text)
button_Dynamic_Properties.clic()
