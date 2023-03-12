class Soda:

    def __init__(self, dob=None):
        self.dob = dob

    def show_my_drink(self):
        if self.dob:
            print(f'Газировка и {self.dob}')
        else:
            print('Обычная газировка')


gaz_1 = Soda('Ананас')
gaz_2 = Soda()

gaz_1.show_my_drink()
gaz_2.show_my_drink()



