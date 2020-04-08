from OOP.pant import Pants


class SalesPerson:

    def __init__(self, f_name, l_name, emp_id, salary, pant_sold=[], total_sale=0):
        self.first_name = f_name
        self.last_name = l_name
        self.employee_id = emp_id
        self.salary = salary
        self.pants_sold = pant_sold
        self.total_sales = total_sale

    def sell_pants(self, Pant):
        self.pants_sold.append(Pant)

    def display_sales(self, pant):
        print('color: {}, waist_size: {}, length: {}, price: {}'.format(pant.color, pant.waist_size, pant.length,
                                                                        pant.price))

    def calculate_sales(self):
        self.total_sales = 0
        for pant in self.pants_sold:
            self.total_sales += pant.price
        return self.total_sales

    def calculate_commission(self, percentage):
        return (self.total_sales * percentage)


if __name__ == "__main__":
    def check_results():
        pants_one = Pants('red', 35, 36, 15.12)
        pants_two = Pants('blue', 40, 38, 24.12)
        pants_three = Pants('tan', 28, 30, 8.12)

        salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

        assert salesperson.first_name == 'Amy'
        assert salesperson.last_name == 'Gonzalez'
        assert salesperson.employee_id == 2581923
        assert salesperson.salary == 40000
        assert salesperson.pants_sold == []
        assert salesperson.total_sales == 0

        salesperson.sell_pants(pants_one)
        salesperson.pants_sold[0] == pants_one.color

        salesperson.sell_pants(pants_two)
        salesperson.sell_pants(pants_three)

        assert len(salesperson.pants_sold) == 3
        assert round(salesperson.calculate_sales(), 2) == 47.36
        assert round(salesperson.calculate_commission(.1), 2) == 4.74

        print('Great job, you made it to the end of the code checks from salespaerson!')

check_results()
