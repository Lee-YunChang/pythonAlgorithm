class Car():

    tax = 1.0;

    def __init__(self, company, detail):
        self._company = company
        self._detail = detail

    def detail_info(self):
        print('Car Detail info : {} {}'.format(self._company, self._detail.get('price')))

    def get_none_tax_price(self):
        return 'None Tax price -> company : {}, price : {}'.format(self._company,self._detail.get('price'))

    def get_tax_price(self):
        return 'Tax price -> company : {}, price : {}'.format(self._company,self._detail.get('price') * Car.tax)

    @classmethod
    def tax_price(cls, tax):
        if tax <= 1:
            print("more than 1")
            return
        cls.tax = tax
        print('tax change')

car1 = Car('Genesis', {'color': 'black', 'price': 6000})
car2 = Car('KIA', {'color': 'white', 'price': 3000})

#세금 계산(클래스 메소드 미사용)
print(car1.get_none_tax_price())
Car.tax_price(1.2)
print(car1.get_tax_price())