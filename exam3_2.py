class Lemonade:
    def __init__(self, additive='regular'):
        if isinstance(additive, str):
           self.__additive = additive

    def get_additive(self):
        return self.__additive

    def set_additive(self, additive):
        self.__additive = additive

    @property
    def drink_info(self):
        return f'This is {self.__additive} lemonade'

lemonade1 = Lemonade()
print(lemonade1.drink_info)

lemonade1.set_additive('raspberry')
print(lemonade1.drink_info)

lemonade2 = Lemonade('lemon')
print(lemonade2.drink_info)
