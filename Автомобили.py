class automobile:   
    def __init__(self, brand, model, color, drive, body, engine, trans, year): 
        self.brand = brand
        self.model = model
        self.color = color
        self.drive = drive
        self.body = body
        self.engine = engine
        self.trans = trans
        self.year = year

    def __str__(self):
        return f"\nМарка автомобиля: {self.brand} \nМодель: {self.model} \nЦвет: {self.color} \nПривод: {self.year} \nТип кузова: {self.body} \nОбъем двигателя, л: {self.engine} \nКоробка передач: {self.trans} \nГод выпуска: {self.year}\n\n"

merc = automobile("Mercedes", "G AMG", "black", "Полный", "внедорожник", 4, "автомат", 2020)   # Создание объекта Mercedes
bmw = automobile("BMW", "M8", "violet", "Полный", "седан", 3.3, "автомат", 2023)   # Создание объекта BMW

cars = [merc, bmw]   # Объединение автомобилей в массив

print("\u0332".join(" Характеристики всех автомобилей:"))
for car in cars:
    print(car)

print()

filt_cars = list(filter(lambda car: car.engine < 4, cars))   # Фильтрация по объему двигателя

print("\u0332".join(" Автомобили с объемом двигателя меньше 4 л:"))
for car in filt_cars:
    print(car)

