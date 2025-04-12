class Soda:
    def __init__(self, additive = None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            print(f"Газировка и {self.additive}")
        else:
            print('Обычная газировка')


drink_y = Soda('Сахар')
drink_n = Soda()

drink_y.show_my_drink()
drink_n.show_my_drink()