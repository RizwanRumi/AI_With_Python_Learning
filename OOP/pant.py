class Pants:

    def __init__(self, pant_color, pant_size, pant_length, pant_price):
        self.color = pant_color
        self.waist_size = pant_size
        self.length = pant_length
        self.price = pant_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)

'''
if __name__ == "__main__":
    def check_results():
        pants = Pants('red', 35, 36, 15.12)
        assert pants.color == 'red'
        assert pants.waist_size == 35
        assert pants.length == 36
        assert pants.price == 15.12

        pants.change_price(10) == 10
        assert pants.price == 10

        assert pants.discount(.1) == 9

        print('You made it to the end of the check. Nice job!')

check_results()
'''