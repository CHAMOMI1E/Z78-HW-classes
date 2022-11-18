# 1
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        if v <= self.capacity:
            MoneyBox.add(self, v)
        else:
            print("Нет места в копилке для данного числа монет")

    # True, если можно добавить v монет, False иначе
    def add(self, v):
        self.capacity -= v
        print(f"Монетка добавлена в копилку. Осталось места для {self.capacity} монеток")
    # положить v монет в копилку


mb = MoneyBox(int(input("Введите максимальную вместимость копилки: ")))  # mb - Money Box
while True:
    mb.can_add(int(input("Введите чило монет которое вы хотите положить в копилку: ")))
